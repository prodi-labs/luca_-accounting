#!/usr/bin/env python3
"""Full invoice report: all invoices joined with their booking status.

Usage:
    .venv/bin/python scripts/invoice_report.py [invoices-dir] [work-dir]

    invoices-dir  defaults to tests/invoices/
    work-dir      defaults to tests/.work/

Prints a JSON object with the complete P&L dataset:

  generated_at          ISO timestamp.
  summary.total_invoices  total number of invoice files.
  summary.booked          number with a booking file.
  summary.unbooked        number without a booking file yet.
  summary.by_currency     pre-tax subtotals per currency for booked invoices,
                          and total-including-tax for unbooked ones.
  booked[]              one entry per booked invoice with per-line detail:
                          invoice_id, vendor, date, currency,
                          total_including_tax, subtotal_excluding_tax,
                          lines[]{description, amount, account_code,
                                  account_name, vat_code}
  unbooked[]            one entry per unbooked invoice:
                          invoice_id, vendor, date, currency,
                          total_including_tax

The agent uses this output to build P&L reports, spending breakdowns,
and other financial summaries — it never needs to read invoice files
directly.
"""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import invoice_lib as lib  # noqa: E402

REPO = Path(__file__).resolve().parent.parent
DEFAULT_INVOICES = REPO / "tests" / "invoices"
DEFAULT_WORK = REPO / "tests" / ".work"


def main(argv: list[str]) -> int:
    invoices_dir = Path(argv[1]) if len(argv) > 1 else DEFAULT_INVOICES
    work_dir = Path(argv[2]) if len(argv) > 2 else DEFAULT_WORK

    if not invoices_dir.exists():
        print(json.dumps({"error": f"invoices directory not found: {invoices_dir}"}))
        return 1

    work_dir.mkdir(parents=True, exist_ok=True)
    data = lib.report_data(invoices_dir, work_dir)
    print(json.dumps(data, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
