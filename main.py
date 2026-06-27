#!/usr/bin/env python3
"""Test harness for the invoice-booking skill.

Each invoice in tests/invoices/ carries its own correct answer (an
`expected` block) plus a `testable` flag. The harness books a *sanitized*
copy of the invoice — with the answer removed — through the `process-invoice`
skill, then compares the skill's booking against the embedded answer and
reports which invoices booked correctly. It never touches a live accounting
system.

This file is just the entry point and lives at the repo root. The actual
work lives in src/, split MVC-style:
    src/model.py       — books sanitized copies and checks them (data + skill).
    src/view/          — prints the run to the terminal (the CLI front end).
    src/controller.py  — drives the loop, wiring model and view together.

Usage:
    python main.py    # show a menu: test one invoice, or test all

Auth: reuses your Claude Code login — no API key needed. Make sure the
`claude` command works in this terminal first.
"""

import asyncio
import sys
from pathlib import Path

# The harness modules live in src/; put it on the import path so they
# can import each other by their plain names (model, view, controller).
sys.path.insert(0, str(Path(__file__).parent / "src"))

from controller import BookingController  # noqa: E402
from model import InvoiceModel  # noqa: E402
from view import CliView  # noqa: E402


def main() -> None:
    controller = BookingController(InvoiceModel(), CliView())
    asyncio.run(controller.run())


if __name__ == "__main__":
    main()
