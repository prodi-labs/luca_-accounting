"""Chat controller: LLM-powered accounting assistant REPL.

Luca answers accounting questions in natural language and can book invoices,
explain booking decisions, and display financial reports — all in the terminal.
"""

import json
import re
import textwrap
from collections import defaultdict
from pathlib import Path

from claude_agent_sdk import (
    AssistantMessage,
    ClaudeAgentOptions,
    ResultMessage,
    TextBlock,
    create_sdk_mcp_server,
    query,
    tool,
)

from model import InvoiceModel, lib

# ── ANSI helpers ─────────────────────────────────────────────────────────────
_B  = "\033[1m"
_D  = "\033[2m"
_R  = "\033[0m"
_G  = "\033[92m"
_Y  = "\033[93m"
_C  = "\033[96m"


def _render_table(table_lines: list[str]) -> list[str]:
    """Render a markdown table block as a styled terminal table with box-drawing characters."""
    # Parse rows; detect the separator row (|---|---|) to identify the header
    raw_rows: list[list[str]] = []
    header_idx: int | None = None

    for line in table_lines:
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if all(re.match(r"^:?-+:?$", c) for c in cells if c):
            if raw_rows:
                header_idx = len(raw_rows) - 1
        else:
            raw_rows.append(cells)

    if not raw_rows:
        return table_lines

    num_cols = max(len(r) for r in raw_rows)
    rows = [r + [""] * (num_cols - len(r)) for r in raw_rows]

    # Column widths: natural width capped so the table stays readable
    WRAP_AT = 42
    col_widths = [
        min(max(len(r[c]) for r in rows), WRAP_AT)
        for c in range(num_cols)
    ]

    def _wrap(text: str, width: int) -> list[str]:
        return textwrap.wrap(text, width) or [""]

    def _row_lines(row: list[str], is_hdr: bool) -> list[str]:
        wrapped = [_wrap(row[c], col_widths[c]) for c in range(num_cols)]
        n = max(len(w) for w in wrapped)
        lines = []
        for li in range(n):
            parts = []
            for c in range(num_cols):
                txt = wrapped[c][li] if li < len(wrapped[c]) else ""
                if is_hdr:
                    parts.append(f" {_B}{_C}{txt:<{col_widths[c]}}{_R} ")
                elif c == 0:
                    parts.append(f" {_Y}{txt:<{col_widths[c]}}{_R} ")
                else:
                    parts.append(f" {txt:<{col_widths[c]}} ")
            lines.append("  │" + "│".join(parts) + "│")
        return lines

    def _div(l: str = "├", m: str = "┼", r: str = "┤") -> str:
        return "  " + l + m.join("─" * (w + 2) for w in col_widths) + r

    out = [_div("┌", "┬", "┐")]
    for i, row in enumerate(rows):
        is_hdr = i == header_idx
        out.extend(_row_lines(row, is_hdr))
        if i < len(rows) - 1:
            out.append(_div("├", "┼", "┤") if not is_hdr else _div("╞", "╪", "╡"))
    out.append(_div("└", "┴", "┘"))
    return out


def _render(text: str) -> str:
    """Convert common markdown to ANSI codes for terminal display."""
    out: list[str] = []
    lines = text.split("\n")
    i = 0
    while i < len(lines):
        line = lines[i]

        # Collect and render a table block (consecutive lines starting with |)
        if line.strip().startswith("|"):
            block: list[str] = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                block.append(lines[i])
                i += 1
            out.extend(_render_table(block))
            continue

        # Block: headers
        if m := re.match(r"^(#{1,3}) (.+)", line):
            depth = len(m.group(1))
            content = m.group(2)
            if depth == 1:
                line = f"{_B}{_C}{content}{_R}"
            elif depth == 2:
                line = f"{_B}{content}{_R}"
            else:
                line = f"{_B}{_D}{content}{_R}"
        # Block: bullet points (- or *)
        elif re.match(r"^(\s*)[-*] ", line):
            line = re.sub(r"^(\s*)[-*] ", lambda m: m.group(1) + "  • ", line)

        # Inline: bold **text**
        line = re.sub(r"\*\*(.+?)\*\*", f"{_B}\\1{_R}", line)
        # Inline: code `text`
        line = re.sub(r"`([^`\n]+)`", f"{_Y}\\1{_R}", line)

        out.append(line)
        i += 1
    return "\n".join(out)


def _sym(currency: str) -> str:
    return {"EUR": "€", "USD": "$", "GBP": "£"}.get(currency, currency + " ")


def _fmt(amount: float, currency: str = "") -> str:
    return f"{_sym(currency)}{amount:,.2f}"


def _print_report(data: dict) -> None:
    summary  = data["summary"]
    booked   = data["booked"]
    unbooked = data["unbooked"]

    print(
        f"\n{_B}{_C}  P&L Report{_R}  "
        f"{_D}{data['generated_at'].replace('T', ' ')}{_R}"
    )
    print(
        f"  {_B}{summary['booked']}{_R} booked  ·  "
        f"{_Y}{summary['unbooked']}{_R} pending  ·  "
        f"{summary['total_invoices']} total\n"
    )

    # Aggregate: currency → account_code → {name, total}
    by_cur: dict = defaultdict(lambda: defaultdict(lambda: {"name": "", "total": 0.0}))
    for entry in booked:
        cur = entry["currency"]
        for ln in entry["lines"]:
            acc = ln["account_code"]
            by_cur[cur][acc]["name"]   = ln["account_name"]
            by_cur[cur][acc]["total"] += ln["amount"] or 0.0

    if booked:
        for cur in sorted(by_cur):
            accounts = by_cur[cur]
            grand = sum(v["total"] for v in accounts.values())
            print(f"  {_B}Expenses — {cur}{_R}")
            print(f"  {_D}  {'Account':<10}  {'Name':<34}  {'Amount':>14}{_R}")
            print(f"    {'─'*10}  {'─'*34}  {'─'*14}")
            for acc in sorted(accounts):
                v = accounts[acc]
                print(
                    f"    {_Y}{acc:<10}{_R}  {v['name']:<34}  "
                    f"{_G}{_fmt(v['total'], cur):>14}{_R}"
                )
            print(f"    {'─'*10}  {'─'*34}  {'─'*14}")
            print(f"    {_B}{'Total':<10}  {'':34}  {_fmt(grand, cur):>14}{_R}\n")
    else:
        print(f"  {_D}No booked invoices yet.{_R}\n")

    if unbooked:
        print(f"  {_B}Pending — not yet booked{_R}")
        print(f"  {_D}  {'Date':<12}  {'Invoice':<14}  {'Vendor':<30}  {'Amount':>14}{_R}")
        print(f"    {'─'*12}  {'─'*14}  {'─'*30}  {'─'*14}")
        for inv in sorted(unbooked, key=lambda i: i["date"]):
            total = inv["total_including_tax"]
            amt_str = _fmt(total, inv["currency"]) if total is not None else "—"
            print(
                f"    {inv['date']:<12}  {inv['invoice_id']:<14}  "
                f"{inv['vendor']:<30}  {_Y}{amt_str:>14}{_R}"
            )
        print()


# ── System prompt ─────────────────────────────────────────────────────────────

SYSTEM_PROMPT = """\
You are Luca, an accounting assistant. You help book invoices and answer
questions about the company's financial position.

Tools available:
- list_invoices: all invoices with booking status (booked/unbooked), vendor
  (supplier), customer (buyer the invoice is addressed to), amount, currency.
- book_invoice: book one invoice by invoice_id.
- show_report: print a P&L report to the terminal. Call this when the user
  asks to see the P&L, expenses, or a financial report.
- get_booking_detail: return the invoice content and its booking for one
  invoice_id. Use this when the user asks why an invoice was booked a
  certain way.

Invoice structure:
- vendor: the supplier who issued the invoice (accounts payable side).
- customer: the company the invoice is addressed to (the buyer — usually
  Beetech or a variant of that name).
- Both fields are always available from list_invoices.

Accounting guidelines:
- When the user asks "which clients" or "which customers", they mean the
  customer field — who these invoices were billed to.
- To find invoices for a specific customer or vendor, call list_invoices and
  filter by the relevant field.
- For batch booking ("book all unbooked", "book all invoices from vendor X"),
  call list_invoices first, then call book_invoice for each qualifying one.
- To explain a booking, call get_booking_detail. Describe which account code
  was chosen, why it fits the line item description, and what the VAT code
  means.
- Answer concisely. Use accounting terms: vendor, customer, account code,
  VAT code, booking, line item.
- If a booking seems wrong or you are uncertain, say so rather than guess.
"""


# ── Controller ────────────────────────────────────────────────────────────────

class ChatController:
    def __init__(self, model: InvoiceModel) -> None:
        self.model = model
        self._session_id: str | None = None
        self._mcp_server = self._build_mcp_server()

    def _build_mcp_server(self):
        model = self.model

        @tool(
            "list_invoices",
            "List all invoices with booking status, vendor, amount, currency.",
            {},
        )
        async def list_invoices(args):
            invoices = model.list_invoices()
            rows = [
                {
                    "invoice_id": inv.invoice_id,
                    "vendor":     inv.vendor_name,
                    "customer":   inv.customer_name,
                    "amount":     inv.total_amount,
                    "currency":   inv.currency,
                    "booked":     model.booking_path(inv.path).exists(),
                }
                for inv in invoices
            ]
            return {"content": [{"type": "text", "text": json.dumps(rows, indent=2)}]}

        @tool(
            "book_invoice",
            "Book an invoice using the accounting skill. Pass the exact invoice_id.",
            {"invoice_id": str},
        )
        async def book_invoice(args):
            invoice_id = args["invoice_id"]
            invoices = model.list_invoices()
            inv = next(
                (i for i in invoices if i.invoice_id.lower() == invoice_id.lower()),
                None,
            )
            if inv is None:
                return {"content": [{"type": "text", "text": f"Invoice '{invoice_id}' not found."}]}

            model.work.mkdir(parents=True, exist_ok=True)
            booking = model.booking_path(inv.path)

            print(
                f"\n  {_C}Booking {inv.invoice_id}{_R} "
                f"({_D}{inv.vendor_name}{_R})...",
                flush=True,
            )
            async for kind, line in model.run_skill(inv.path, booking):
                if kind == "tool":
                    print(f"  {_D}→ {line}{_R}", flush=True)
                else:
                    print(f"  {line}", flush=True)

            result = model.read_result(booking)
            if result.status == "no-booking":
                text = f"No booking produced for {invoice_id}."
            elif result.flags:
                text = f"Flagged: {'; '.join(result.flags)}"
            else:
                lines_str = ", ".join(
                    f"{ln.account_code} / {ln.vat_code}" for ln in result.lines
                )
                text = f"Booked {invoice_id}: {lines_str}"

            print(flush=True)
            return {"content": [{"type": "text", "text": text}]}

        @tool(
            "show_report",
            "Print a P&L report to the terminal.",
            {},
        )
        async def show_report(args):
            model.work.mkdir(parents=True, exist_ok=True)
            data = lib.report_data(model.invoices, model.work)
            _print_report(data)
            s = data["summary"]
            lines = [f"{s['booked']} invoices booked, {s['unbooked']} pending."]
            for cur, vals in s["by_currency"].items():
                subtotal = vals.get("booked_subtotal", 0.0)
                lines.append(f"  {cur} booked subtotal (excl. VAT): {_fmt(subtotal, cur)}")
            return {"content": [{"type": "text", "text": "\n".join(lines)}]}

        @tool(
            "get_booking_detail",
            "Return the invoice and its booking for one invoice_id, to explain the booking.",
            {"invoice_id": str},
        )
        async def get_booking_detail(args):
            invoice_id = args["invoice_id"]
            invoices = model.list_invoices()
            inv = next(
                (i for i in invoices if i.invoice_id.lower() == invoice_id.lower()),
                None,
            )
            if inv is None:
                return {"content": [{"type": "text", "text": f"Invoice '{invoice_id}' not found."}]}

            invoice_data = json.loads(Path(inv.path).read_text())
            booking_path = model.booking_path(inv.path)
            detail = {
                "invoice_id": inv.invoice_id,
                "vendor":     inv.vendor_name,
                "date":       invoice_data.get("document", {}).get("issue_date", ""),
                "line_items": invoice_data.get("line_items", []),
                "amounts":    invoice_data.get("amounts", {}),
                "booking":    json.loads(booking_path.read_text()) if booking_path.exists() else None,
            }
            return {"content": [{"type": "text", "text": json.dumps(detail, indent=2)}]}

        return create_sdk_mcp_server(
            "invoices",
            tools=[list_invoices, book_invoice, show_report, get_booking_detail],
        )

    def _options(self) -> ClaudeAgentOptions:
        opts = ClaudeAgentOptions(
            cwd=str(self.model.repo),
            model=self.model.model,
            system_prompt=SYSTEM_PROMPT,
            mcp_servers={"invoices": self._mcp_server},
            tools=[],
            allowed_tools=["list_invoices", "book_invoice", "show_report", "get_booking_detail"],
            permission_mode="bypassPermissions",
            setting_sources=["project"],
        )
        if self._session_id:
            opts.resume = self._session_id
        return opts

    async def run(self) -> None:
        print("Ask anything about your invoices. Type 'quit' to exit.\n")
        while True:
            try:
                user_input = input("> ").strip()
            except (EOFError, KeyboardInterrupt):
                print("\nBye.")
                return
            if not user_input:
                continue
            if user_input.lower() in ("quit", "exit", "q", "bye"):
                print("Bye.")
                return
            print()
            async for message in query(prompt=user_input, options=self._options()):
                if isinstance(message, AssistantMessage):
                    for block in message.content:
                        if isinstance(block, TextBlock) and block.text.strip():
                            print(_render(block.text.strip()))
                elif isinstance(message, ResultMessage):
                    if message.session_id:
                        self._session_id = message.session_id
            print()
