"""Controller: drives the test loop.

It owns the flow of a run — show the testable invoices, let the user pick
one or all, then for each: book a sanitized copy through the skill, check
the result against the invoice's embedded answer, and hand everything to
the view to display. It holds no formatting and no file logic; those live
in the view and the model.
"""

from pathlib import Path

from model import InvoiceModel
from view import CliView


class BookingController:
    def __init__(self, model: InvoiceModel, view: CliView) -> None:
        self.model = model
        self.view = view

    async def run(self) -> None:
        """Show the testable invoices, let the user pick one or all, run."""
        testable = [s for s in self.model.list_invoices() if s.testable]
        if not testable:
            self.view.no_testable()
            return
        choice = self.view.menu(testable)
        if choice is None:
            return
        if choice == "all":
            await self._run_tests([s.path for s in testable])
        else:
            await self._run_tests([testable[choice].path])

    async def _run_tests(self, paths: list[Path]) -> None:
        """Book a sanitized copy of each invoice and check it against truth."""
        self.model.clear_work()
        self.view.start_run(len(paths))
        checks = []
        for path in paths:
            self.view.testing_header(path.stem)
            copy = self.model.prepare_copy(path)
            booking = self.model.booking_path(copy)
            async for kind, text in self.model.run_skill(copy, booking):
                if kind == "tool":
                    self.view.tool_line(text)
                else:
                    self.view.agent_line(text)
            check = self.model.check(path, booking)
            checks.append(check)
        self.view.report(checks)
