#!/usr/bin/env python3
"""Validate the model's booking against an invoice's embedded answer.

Usage:
    .venv/bin/python scripts/validate_booking.py <invoice.json> <booking.json>

  * <invoice.json> is the original invoice (it still holds the answer, in its
    `invoice_lines` block).
  * <booking.json> is the structured booking the model produced.

This is the deterministic judge: the model does the inference and writes a
booking; this script decides, by fixed rules, whether that booking is right.
It prints a JSON result and always exits 0 (the verdict is in the JSON, not the
exit code):

    {"status": "...", "diffs": [...], "problems": [...]}

  status:
    pass        booking matches the answer
    fail        booking is well-formed but wrong (see diffs)
    invalid     booking JSON is missing/malformed (see problems)
    no-booking  no booking file was written
    untested    the invoice isn't marked testable — nothing to check against
"""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import invoice_lib as lib  # noqa: E402


def _result(status: str, diffs: list | None = None, problems: list | None = None) -> int:
    print(json.dumps({"status": status, "diffs": diffs or [], "problems": problems or []}, indent=2))
    return 0


def main(argv: list[str]) -> int:
    if len(argv) != 3:
        print(json.dumps({"error": "usage: validate_booking.py <invoice.json> <booking.json>"}))
        return 2

    invoice_path, booking_path = argv[1], argv[2]
    try:
        invoice = lib.load_raw(invoice_path)
    except lib.InvoiceError as exc:
        print(json.dumps({"error": str(exc)}))
        return 2

    expected = lib.expected_lines(invoice)
    if expected is None:
        return _result("untested")

    bp = Path(booking_path)
    if not bp.exists():
        return _result("no-booking", problems=["booking file not found"])
    try:
        booking = json.loads(bp.read_text())
    except json.JSONDecodeError as exc:
        return _result("invalid", problems=[f"booking is not valid JSON: {exc}"])

    problems = lib.validate_booking_structure(booking)
    if problems:
        return _result("invalid", problems=problems)

    verdict = lib.compare_booking(booking, expected)
    return _result(verdict["status"], diffs=verdict["diffs"])


if __name__ == "__main__":
    sys.exit(main(sys.argv))
