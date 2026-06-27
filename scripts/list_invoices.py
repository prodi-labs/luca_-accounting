#!/usr/bin/env python3
"""List the invoices in a directory as JSON.

Usage:
    .venv/bin/python scripts/list_invoices.py [invoices-dir]

Defaults to tests/invoices/. Prints a JSON array, one object per invoice, with
its id, vendor, total, currency, and whether it is testable — enough to show a
menu without booking anything. Files that can't be read are skipped with a note
on stderr so one bad file doesn't sink the whole list.
"""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import invoice_lib as lib  # noqa: E402

DEFAULT_DIR = Path(__file__).resolve().parent.parent / "tests" / "invoices"


def main(argv: list[str]) -> int:
    invoices_dir = Path(argv[1]) if len(argv) > 1 else DEFAULT_DIR
    summaries = []
    for path in sorted(invoices_dir.glob("*.json")):
        try:
            summaries.append(lib.summarize(path))
        except lib.InvoiceError as exc:
            print(f"skipping {path.name}: {exc}", file=sys.stderr)
    print(json.dumps(summaries, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
