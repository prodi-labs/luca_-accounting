"""Report server: serves HTML reports over HTTP in a background thread.

Starts automatically when the program launches. Reports are generated fresh
on every request so they always reflect the latest bookings.

Routes:
    GET /        →  P&L report (same as /reports/pl)
    GET /reports/pl  →  Profit & Loss report built from booked invoices
"""

import sys
import threading
from collections import defaultdict
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

from model import InvoiceModel, SCRIPTS

sys.path.insert(0, str(SCRIPTS))
import invoice_lib as lib  # noqa: E402


class ReportServer:
    def __init__(self, model: InvoiceModel, port: int = 8765) -> None:
        self.model = model
        self.port = port
        self._server: ThreadingHTTPServer | None = None

    def start(self) -> int:
        """Start the server in a daemon thread. Returns the port it bound to."""
        handler = _make_handler(self.model)
        for port in range(self.port, self.port + 10):
            try:
                self._server = ThreadingHTTPServer(("127.0.0.1", port), handler)
                break
            except OSError:
                continue
        else:
            raise RuntimeError(f"No free port found in range {self.port}–{self.port + 9}")  # noqa: RUF001

        self.port = port
        thread = threading.Thread(target=self._server.serve_forever, daemon=True)
        thread.start()
        return self.port


# ---------------------------------------------------------------------------
# Report data
# ---------------------------------------------------------------------------

def _pl_data(model: InvoiceModel) -> dict:
    """Fetch P&L data via invoice_lib — the single source of truth."""
    model.work.mkdir(parents=True, exist_ok=True)
    return lib.report_data(model.invoices, model.work)


# ---------------------------------------------------------------------------
# HTML generation
# ---------------------------------------------------------------------------

_CSS = """
* { box-sizing: border-box; margin: 0; padding: 0; }
body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
       font-size: 14px; color: #1a1a1a; background: #f5f5f5; }
.wrap { max-width: 900px; margin: 0 auto; padding: 32px 24px 64px; }
h1 { font-size: 22px; font-weight: 600; margin-bottom: 4px; }
.meta { color: #666; font-size: 12px; margin-bottom: 32px; }
.meta a { color: #666; }
h2 { font-size: 15px; font-weight: 600; margin: 32px 0 12px; color: #333; }
h3 { font-size: 13px; font-weight: 600; margin: 20px 0 8px; color: #555;
     text-transform: uppercase; letter-spacing: .04em; }
table { width: 100%; border-collapse: collapse; background: #fff;
        border-radius: 6px; overflow: hidden;
        box-shadow: 0 1px 3px rgba(0,0,0,.08); }
th { background: #f0f0f0; font-weight: 600; font-size: 12px;
     text-transform: uppercase; letter-spacing: .04em; color: #555; }
th, td { padding: 9px 14px; text-align: left; border-bottom: 1px solid #eee; }
td.num, th.num { text-align: right; font-variant-numeric: tabular-nums; }
tr:last-child td { border-bottom: none; }
tr.subtotal td { font-weight: 600; background: #fafafa; }
tr.total td { font-weight: 700; background: #f0f0f0; border-top: 2px solid #ddd; }
.empty { color: #999; font-style: italic; padding: 16px 0; }
.badge { display: inline-block; padding: 2px 7px; border-radius: 3px;
         font-size: 11px; font-weight: 600; }
.badge-ok { background: #e6f4ea; color: #1e7e34; }
.badge-pending { background: #fff3cd; color: #856404; }
.refresh { float: right; font-size: 12px; color: #888; text-decoration: none;
           border: 1px solid #ddd; padding: 3px 10px; border-radius: 4px;
           background: #fff; }
.refresh:hover { background: #f0f0f0; }
"""

def _fmt(amount: float, currency: str) -> str:
    symbol = {"EUR": "€", "USD": "$", "GBP": "£"}.get(currency, currency + " ")
    return f"{symbol}{amount:,.2f}"


def _pl_html(model: InvoiceModel) -> str:
    data = _pl_data(model)
    booked = data["booked"]
    unbooked = data["unbooked"]
    summary = data["summary"]
    generated_at = data["generated_at"].replace("T", " ")

    # Flatten booked entries into per-line rows for the tables
    # Group by currency → account_code for the summary table
    by_currency: dict[str, dict[str, dict]] = defaultdict(
        lambda: defaultdict(lambda: {"account_name": "", "total": 0.0})
    )
    detail_rows = []
    for entry in booked:
        cur = entry["currency"]
        for ln in entry["lines"]:
            amt = ln["amount"] or 0.0
            acc = ln["account_code"]
            by_currency[cur][acc]["account_name"] = ln["account_name"]
            by_currency[cur][acc]["total"] += amt
            detail_rows.append({
                "date": entry["date"],
                "invoice_id": entry["invoice_id"],
                "vendor": entry["vendor"],
                "account_code": acc,
                "amount": amt,
                "currency": cur,
            })

    parts = [f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta http-equiv="refresh" content="30">
<title>P&amp;L — Luca</title>
<style>{_CSS}</style>
</head>
<body>
<div class="wrap">
<a class="refresh" href="/">↻ Refresh</a>
<h1>Profit &amp; Loss</h1>
<p class="meta">Generated {generated_at} &nbsp;·&nbsp;
  {summary['booked']} of {summary['total_invoices']} invoices booked</p>
"""]

    if not booked:
        parts.append('<p class="empty">No booked invoices yet. '
                     'Book some in the chat interface to see the report.</p>')
    else:
        for currency in sorted(by_currency):
            accounts = by_currency[currency]
            grand_total = sum(v["total"] for v in accounts.values())
            parts.append(f"<h2>Expenses — {currency}</h2>\n<table>")
            parts.append(
                "<thead><tr><th>Account code</th><th>Account name</th>"
                "<th class='num'>Amount</th></tr></thead><tbody>"
            )
            for acc in sorted(accounts):
                v = accounts[acc]
                parts.append(
                    f"<tr><td>{acc}</td><td>{v['account_name']}</td>"
                    f"<td class='num'>{_fmt(v['total'], currency)}</td></tr>"
                )
            parts.append(
                f"<tr class='total'><td colspan='2'>Total expenses</td>"
                f"<td class='num'>{_fmt(grand_total, currency)}</td></tr>"
            )
            parts.append("</tbody></table>")

        parts.append("<h2>Booked invoices</h2><table>")
        parts.append(
            "<thead><tr><th>Date</th><th>Invoice</th><th>Vendor</th>"
            "<th>Account</th><th class='num'>Amount</th><th>Currency</th>"
            "</tr></thead><tbody>"
        )
        for row in sorted(detail_rows, key=lambda r: (r["date"], r["invoice_id"])):
            parts.append(
                f"<tr><td>{row['date']}</td><td>{row['invoice_id']}</td>"
                f"<td>{row['vendor']}</td><td>{row['account_code']}</td>"
                f"<td class='num'>{row['amount']:,.2f}</td><td>{row['currency']}</td></tr>"
            )
        parts.append("</tbody></table>")

    if unbooked:
        parts.append("<h2>Pending — not yet booked</h2><table>")
        parts.append(
            "<thead><tr><th>Date</th><th>Invoice</th><th>Vendor</th>"
            "<th class='num'>Amount</th><th>Currency</th></tr></thead><tbody>"
        )
        for inv in sorted(unbooked, key=lambda i: i["date"]):
            amt = f"{inv['total_including_tax']:,.2f}" if inv["total_including_tax"] is not None else "—"
            parts.append(
                f"<tr><td>{inv['date']}</td><td>{inv['invoice_id']}</td>"
                f"<td>{inv['vendor']}</td>"
                f"<td class='num'>{amt}</td><td>{inv['currency']}</td></tr>"
            )
        parts.append("</tbody></table>")

    parts.append("</div></body></html>")
    return "\n".join(parts)


# ---------------------------------------------------------------------------
# HTTP handler
# ---------------------------------------------------------------------------

def _make_handler(model: InvoiceModel):
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self) -> None:
            path = self.path.split("?")[0].rstrip("/") or "/"
            if path in ("/", "/reports/pl"):
                html = _pl_html(model)
                body = html.encode("utf-8")
                self.send_response(200)
                self.send_header("Content-Type", "text/html; charset=utf-8")
                self.send_header("Content-Length", str(len(body)))
                self.end_headers()
                self.wfile.write(body)
            else:
                self.send_response(404)
                self.end_headers()

        def log_message(self, *args) -> None:
            pass  # suppress request logs — they'd clutter the terminal

    return Handler
