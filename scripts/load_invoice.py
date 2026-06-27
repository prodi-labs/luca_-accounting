#!/usr/bin/env python3
"""Load and validate one invoice, ready for booking.

Usage:
    .venv/bin/python scripts/load_invoice.py <path-to-invoice.json>

On success: prints the invoice as JSON with the test answer removed, exit 0.
This is the clean, validated data the model should book from.

On failure: prints {"error": "..."} as JSON and exits 1. The message says
what is wrong with the file (not found, not JSON, or a missing field). The
caller — including the model running the process-invoice skill — should read
that message and decide what to do (flag it, stop, ask a human), rather than
guess at a malformed invoice.
"""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import invoice_lib as lib  # noqa: E402


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print(json.dumps({"error": "usage: load_invoice.py <path-to-invoice.json>"}))
        return 2
    try:
        invoice = lib.load_invoice(argv[1])
    except lib.InvoiceError as exc:
        print(json.dumps({"error": str(exc)}))
        return 1
    print(json.dumps(invoice, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
