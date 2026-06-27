"""CLI view: prints the test run to the terminal.

This is the only layer that prints. It is handed plain data by the
controller (`InvoiceSummary`s, `CheckResult`s) and decides how to display
it, so the formatting can change here without touching the test logic.
"""

from model import CheckResult, InvoiceSummary


class CliView:
    """Renders a test run as plain text on stdout."""

    def menu(self, summaries: list[InvoiceSummary]) -> str | int | None:
        """Show the testable invoices as a menu and ask the user to pick.

        Returns:
          * "all"          — test every invoice,
          * an int index   — test that one invoice (0-based into summaries),
          * None           — quit without testing.
        """
        print("\nTestable invoices in tests/invoices/:\n")
        width = len(str(len(summaries)))
        for i, s in enumerate(summaries, start=1):
            total = "—" if s.total_amount is None else f"{s.total_amount:,.2f}"
            print(
                f"  {i:>{width}}) {s.invoice_id:<16} {s.vendor_name:<24} "
                f"{total:>12} {s.currency:<4}"
            )
        print("\n  A) Test all")
        print("  Q) Quit")

        while True:
            try:
                choice = input(f"\nSelect an invoice [1-{len(summaries)}/A/Q]: ").strip()
            except (EOFError, KeyboardInterrupt):
                print()
                return None
            if choice.lower() in ("q", ""):
                return None
            if choice.lower() == "a":
                return "all"
            if choice.isdigit() and 1 <= int(choice) <= len(summaries):
                return int(choice) - 1
            print("  ! not a valid choice, try again")

    def no_testable(self) -> None:
        print("No testable invoices in tests/invoices/.")
        print("Mark an invoice with \"testable\": true and an \"expected\" block.")

    def start_run(self, count: int) -> None:
        word = "invoice" if count == 1 else "invoices"
        print(f"\nTesting {count} {word} (the answer is hidden from the model)...")

    def testing_header(self, invoice_id: str) -> None:
        print(f"\n=== Testing {invoice_id} ===")

    def agent_line(self, text: str) -> None:
        print(f"  {text}")

    def tool_line(self, text: str) -> None:
        """Print a tool the agent just called, so every call shows in the console."""
        print(f"  → {text}")

    # Labels for each check status, shown in the left column of the report.
    _CHECK_LABELS = {
        "pass": "PASS",
        "fail": "FAIL",
        "untested": "----",
        "no-booking": "FAIL",
    }

    def report(self, checks: list[CheckResult]) -> None:
        """Print the pass/fail report for a test run."""
        print("\nResults (booking vs each invoice's expected answer):\n")
        for c in checks:
            label = self._CHECK_LABELS.get(c.status, "????")
            if c.status == "pass":
                detail = ", ".join(
                    f"{ln.account_code} / {ln.vat_code}" for ln in c.result.lines
                )
            elif c.status == "fail":
                detail = "; ".join(c.diffs)
            elif c.status == "no-booking":
                detail = "the model wrote no booking"
            else:  # untested
                detail = "no expected answer in the invoice"
            print(f"  {label}  {c.invoice_id:<16} {detail}")

        passed = sum(1 for c in checks if c.status == "pass")
        failed = sum(1 for c in checks if c.status in ("fail", "no-booking"))
        untested = sum(1 for c in checks if c.status == "untested")
        parts = [f"{passed} passed", f"{failed} failed"]
        if untested:
            parts.append(f"{untested} untested")
        print(f"\nResult: {', '.join(parts)}.")
