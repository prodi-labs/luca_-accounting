"""Model: invoice data and the test-booking operation.

This layer ties the deterministic invoice scripts (in `scripts/`) to the
model run. The split is deliberate: anything a computer should decide —
reading a file, checking its structure, hiding the answer, judging a
booking — lives in `scripts/invoice_lib.py` and its CLI wrappers; the model
is left to do the *inference* (which account, which VAT code).

It exposes:

  * `list_invoices`  — summarize every invoice for the selection menu.
  * `prepare_copy`   — write a sanitized copy (answer removed) for the model.
  * `booking_path`   — where the model's booking JSON for a copy should land.
  * `run_skill`      — run the process-invoice skill over one copy,
                       yielding the agent's text as it streams.
  * `read_result`    — read the booking JSON the skill wrote.
  * `check`          — run the validation script over a booking.

The skill never sees the answer: it books a *sanitized copy* (see
`prepare_copy`), produces a structured booking JSON, and the deterministic
`validate_booking.py` script — not the model — decides whether it is right.
Nothing here touches a live accounting system.
"""

import json
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import AsyncIterator

from claude_agent_sdk import (
    AssistantMessage,
    ClaudeAgentOptions,
    ResultMessage,
    TextBlock,
    ToolUseBlock,
    query,
)

# This file lives in src/; the project root (which holds .claude/, scripts/
# and CLAUDE.md) is one level up. The root is what we hand the agent as its
# cwd, so it can find the skills and run the scripts — keep it pointing here.
REPO = Path(__file__).parent.parent.resolve()
SCRIPTS = REPO / "scripts"
INVOICES = REPO / "tests" / "invoices"
WORK = REPO / "tests" / ".work"        # scratch: sanitized copies + booking JSON
MODEL = "claude-opus-4-8"

# Reuse the exact deterministic logic the CLI scripts (and the agent) use, so
# the harness and the agent can never drift apart.
sys.path.insert(0, str(SCRIPTS))
import invoice_lib as lib  # noqa: E402


@dataclass
class InvoiceSummary:
    """A one-line view of an invoice, for the selection menu."""

    path: Path
    invoice_id: str
    vendor_name: str
    customer_name: str
    total_amount: float | None
    currency: str
    testable: bool


@dataclass
class BookingLine:
    """One booked line: where a single invoice line should land."""

    account_code: str | None = None
    account_name: str | None = None
    vat_code: str | None = None


@dataclass
class BookingResult:
    """The structured booking JSON the skill wrote."""

    rel: str                       # booking path, relative to the repo
    status: str                    # "booked", "flagged", or "no-booking"
    lines: list[BookingLine] = field(default_factory=list)
    rule_cited: str | None = None
    scope: str | None = None
    confidence: str | None = None
    flags: list[str] = field(default_factory=list)


@dataclass
class CheckResult:
    """How one booking compared to the invoice's embedded expected answer."""

    rel: str                       # invoice path, relative to the repo
    invoice_id: str
    status: str                    # "pass", "fail", "untested", or "no-booking"
    result: "BookingResult | None" = None
    diffs: list[str] = field(default_factory=list)


class InvoiceModel:
    """Books sanitized invoice copies and checks them with the scripts."""

    def __init__(self, repo: Path = REPO, model: str = MODEL) -> None:
        self.repo = repo
        self.invoices = repo / "tests" / "invoices"
        self.work = repo / "tests" / ".work"
        self.model = model

    def list_invoices(self) -> list[InvoiceSummary]:
        """Summarize every invoice in tests/invoices/, for the menu."""
        return [
            InvoiceSummary(
                path=Path(s["path"]).resolve(),
                invoice_id=s["invoice_id"],
                vendor_name=s["vendor_name"],
                customer_name=s["customer_name"],
                total_amount=s["total_amount"],
                currency=s["currency"],
                testable=s["testable"],
            )
            for s in lib.list_invoices(self.invoices)
        ]

    def clear_work(self) -> None:
        """Empty the scratch dir so each run books fresh sanitized copies."""
        if self.work.exists():
            for f in self.work.glob("*.json"):
                f.unlink()
        self.work.mkdir(parents=True, exist_ok=True)

    def prepare_copy(self, path: Path) -> Path:
        """Write a sanitized copy of one invoice for the model to book.

        Strips the answer fields so the skill can't see the correct
        accounts/VAT codes, then writes the copy under tests/.work/ and returns
        its path. Structure is *not* checked here on purpose — the skill's own
        `load_invoice.py` call does that, so a malformed invoice reaches the
        model and exercises its error handling. The source invoice is untouched.
        """
        data = lib.load_raw(path)
        sanitized = lib.sanitize(data)
        self.work.mkdir(parents=True, exist_ok=True)
        copy = self.work / path.name
        copy.write_text(json.dumps(sanitized, indent=2) + "\n")
        return copy

    def booking_path(self, copy: Path) -> Path:
        """Where the model should write its booking JSON for a given copy."""
        return self.work / f"{copy.stem}.booking.json"

    def _options(self) -> ClaudeAgentOptions:
        return ClaudeAgentOptions(
            cwd=str(self.repo),
            model=self.model,
            setting_sources=["project"],    # load CLAUDE.md + .claude/skills
            # Bash lets the agent run the invoice scripts; Write lets it save
            # its booking JSON.
            allowed_tools=["Read", "Write", "Edit", "Glob", "Grep", "Bash"],
            permission_mode="acceptEdits",  # write the booking back unattended
        )

    async def run_skill(self, copy: Path, booking: Path) -> AsyncIterator[tuple[str, str]]:
        """Run the process-invoice skill over one sanitized copy.

        Tells the agent to load the invoice with the script, do the inference,
        and write its booking as JSON to `booking`. Yields `(kind, text)` pairs
        as the turn streams, so the view can show progress live:

          * ("text", ...)  — a line of the agent's reply,
          * ("tool", ...)  — a tool the agent just called (its name + a short
                             summary of what it ran on), so every tool call is
                             visible in the console.
        """
        copy_rel = copy.relative_to(self.repo)
        booking_rel = booking.relative_to(self.repo)
        prompt = (
            f"Use the process-invoice skill to book the invoice.\n"
            f"1. Load and validate it by running: "
            f"`.venv/bin/python scripts/load_invoice.py {copy_rel}`. If it "
            f"prints an error, follow the skill's guidance for a bad invoice.\n"
            f"2. Apply the vendor and global rules to decide the booking.\n"
            f"3. Write your booking as a single JSON object to {booking_rel}, "
            f"following the booking schema in the skill."
        )

        async for message in query(prompt=prompt, options=self._options()):
            if isinstance(message, AssistantMessage):
                for block in message.content:
                    if isinstance(block, TextBlock) and block.text.strip():
                        yield ("text", block.text.strip())
                    elif isinstance(block, ToolUseBlock):
                        yield ("tool", self._tool_summary(block))
            elif isinstance(message, ResultMessage):
                pass  # turn finished

    @staticmethod
    def _tool_summary(block: ToolUseBlock) -> str:
        """A one-line "name: what it ran on" summary of a tool call.

        Picks the most telling argument for the common tools (the command for
        Bash, the file for Read/Write/Edit, the pattern for Grep/Glob) so the
        console shows what each call actually did, not just the tool name.
        """
        args = block.input or {}
        detail = (
            args.get("command")
            or args.get("file_path")
            or args.get("pattern")
            or args.get("path")
            or ""
        )
        detail = " ".join(str(detail).split())
        if len(detail) > 100:
            detail = detail[:97] + "..."
        return f"{block.name}: {detail}" if detail else block.name

    def read_result(self, booking: Path) -> BookingResult:
        """Read the structured booking JSON the skill wrote (for display)."""
        rel = str(booking.relative_to(self.repo))
        if not booking.exists():
            return BookingResult(rel=rel, status="no-booking")
        try:
            b = json.loads(booking.read_text())
        except json.JSONDecodeError:
            return BookingResult(rel=rel, status="no-booking")
        lines = [
            BookingLine(
                account_code=ln.get("account_code"),
                account_name=ln.get("account_name"),
                vat_code=ln.get("vat_code"),
            )
            for ln in (b.get("lines") or [])
            if isinstance(ln, dict)
        ]
        flags = b.get("flags") or []
        if flags:
            status = "flagged"
        elif lines:
            status = "booked"
        else:
            status = "no-booking"
        return BookingResult(
            rel=rel,
            status=status,
            lines=lines,
            rule_cited=b.get("rule_cited"),
            scope=b.get("scope"),
            confidence=b.get("confidence"),
            flags=flags,
        )

    def check(self, invoice: Path, booking: Path) -> CheckResult:
        """Run validate_booking.py over a booking and read back its verdict.

        The script reads the original invoice (which still holds the answer) and
        the model's booking JSON, and decides the outcome deterministically. We
        also read the booking ourselves, purely so the report can show what was
        booked on a pass.
        """
        data = lib.load_raw(invoice)
        invoice_id = lib.invoice_id(data, invoice.stem)
        result = self.read_result(booking)
        verdict = self._run_validator(invoice, booking)

        status = verdict.get("status", "fail")
        diffs = list(verdict.get("diffs", [])) + list(verdict.get("problems", []))
        if status == "invalid":   # malformed booking JSON counts as a failure
            status = "fail"
        return CheckResult(
            rel=result.rel, invoice_id=invoice_id, status=status, result=result, diffs=diffs
        )

    def _run_validator(self, invoice: Path, booking: Path) -> dict:
        """Call validate_booking.py and parse its JSON verdict."""
        proc = subprocess.run(
            [sys.executable, str(SCRIPTS / "validate_booking.py"), str(invoice), str(booking)],
            capture_output=True,
            text=True,
        )
        try:
            return json.loads(proc.stdout)
        except json.JSONDecodeError:
            detail = proc.stderr.strip() or proc.stdout.strip() or "no output"
            return {"status": "fail", "diffs": [f"validator error: {detail}"], "problems": []}
