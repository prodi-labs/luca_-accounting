"""Deterministic invoice logic, shared by the CLI scripts and the harness.

This module holds the *non-inference* parts of the workflow — the things a
computer should decide, not the model:

  * reading an invoice file and checking its structure is well-formed,
  * stripping the embedded test answer before the model ever sees it,
  * summarizing invoices for the menu,
  * validating the model's booking JSON and comparing it to the answer.

The thin CLI wrappers in this folder (`load_invoice.py`, `list_invoices.py`,
`validate_booking.py`) just call into here, so the agent and the test harness
run the exact same code. Nothing here calls a model or touches a live
accounting system. Keep it standard-library only — it needs Python 3.10+
(it uses modern type-hint syntax), which is the project's `.venv` interpreter.
"""

import json
from pathlib import Path
from typing import Any

# Fields that hold the answer or a prior run; stripped before the model sees a
# copy, so it can never read the expected accounts/VAT codes. The per-line
# answer lives in `invoice_lines`; `expected` is the older single-block form.
ANSWER_FIELDS = ("testable", "invoice_lines", "expected", "booking")

# The keys the model must fill in for each booked line.
BOOKING_LINE_KEYS = ("account_code", "account_name", "vat_code")


class InvoiceError(Exception):
    """A file is missing, isn't valid JSON, or isn't a structurally valid invoice."""


def _dig(data: Any, *keys: str, default: Any = None) -> Any:
    """Walk a chain of dict keys, returning `default` if any step is missing."""
    for key in keys:
        if not isinstance(data, dict):
            return default
        data = data.get(key)
        if data is None:
            return default
    return data


def _norm(value: Any) -> str:
    """Normalize an account or VAT code for comparison.

    Case-insensitive, with surrounding and repeated inner whitespace collapsed,
    so "21% G" and "21%  g" count as equal but genuinely different codes still
    differ.
    """
    return " ".join(str(value if value is not None else "").split()).upper()


def invoice_id(data: dict, fallback: str) -> str:
    """The invoice's human id — its document number, or a fallback (filename)."""
    return _dig(data, "document", "document_number") or fallback


def load_raw(path: str | Path) -> dict:
    """Read and JSON-parse an invoice file. Raises InvoiceError on any problem."""
    p = Path(path)
    if not p.exists():
        raise InvoiceError(f"file not found: {p}")
    try:
        return json.loads(p.read_text())
    except json.JSONDecodeError as exc:
        raise InvoiceError(f"not valid JSON: {exc}") from exc


def validate_structure(data: Any) -> list[str]:
    """Return a list of structural problems with an invoice (empty == valid).

    Checks only the parts the booking depends on — a supplier, a date, a total
    and currency, and at least one line item with a description and amount.
    """
    if not isinstance(data, dict):
        return ["top level is not a JSON object"]

    problems: list[str] = []
    if not _dig(data, "document", "document_number"):
        problems.append("missing document.document_number")
    if not _dig(data, "document", "issue_date"):
        problems.append("missing document.issue_date")
    if not _dig(data, "supplier", "legal_name"):
        problems.append("missing supplier.legal_name")
    if _dig(data, "amounts", "total_including_tax") is None:
        problems.append("missing amounts.total_including_tax")
    if not _dig(data, "amounts", "currency"):
        problems.append("missing amounts.currency")

    items = data.get("line_items")
    if not isinstance(items, list) or not items:
        problems.append("line_items must be a non-empty list")
    else:
        for i, item in enumerate(items):
            if not isinstance(item, dict):
                problems.append(f"line_items[{i}] is not an object")
                continue
            if not item.get("description"):
                problems.append(f"line_items[{i}] missing description")
            if item.get("amount") is None:
                problems.append(f"line_items[{i}] missing amount")
    return problems


def sanitize(data: dict) -> dict:
    """Drop the answer fields so the model never sees the expected booking."""
    return {k: v for k, v in data.items() if k not in ANSWER_FIELDS}


def load_invoice(path: str | Path) -> dict:
    """Load, validate, and return the bookable (answer-stripped) invoice.

    Raises InvoiceError — with a message the caller can show or act on — if the
    file is missing, isn't JSON, or fails the structure check.
    """
    data = load_raw(path)
    problems = validate_structure(data)
    if problems:
        raise InvoiceError("invalid invoice structure: " + "; ".join(problems))
    return sanitize(data)


def summarize(path: str | Path) -> dict:
    """A one-line view of an invoice, for the selection menu."""
    data = load_raw(path)
    p = Path(path)
    return {
        "path": str(p),
        "invoice_id": invoice_id(data, p.stem),
        "vendor_name": _dig(data, "supplier", "legal_name", default="?"),
        "total_amount": _dig(data, "amounts", "total_including_tax"),
        "currency": _dig(data, "amounts", "currency", default=""),
        "testable": bool(data.get("testable")),
    }


def list_invoices(invoices_dir: str | Path) -> list[dict]:
    """Summarize every *.json invoice in a directory, sorted by name."""
    return [summarize(p) for p in sorted(Path(invoices_dir).glob("*.json"))]


def expected_lines(data: dict) -> list | None:
    """A testable invoice's embedded answer (its `invoice_lines`), or None."""
    if not data.get("testable"):
        return None
    return data.get("invoice_lines")


def validate_booking_structure(booking: Any) -> list[str]:
    """Return a list of problems with the model's booking JSON (empty == valid)."""
    if not isinstance(booking, dict):
        return ["booking is not a JSON object"]

    problems: list[str] = []
    lines = booking.get("lines")
    if not isinstance(lines, list) or not lines:
        problems.append("booking.lines must be a non-empty list")
    else:
        for i, line in enumerate(lines):
            if not isinstance(line, dict):
                problems.append(f"lines[{i}] is not an object")
                continue
            for key in ("account_code", "vat_code"):
                if not line.get(key):
                    problems.append(f"lines[{i}] missing {key}")
    return problems


def compare_booking(booking: dict, expected: list[dict]) -> dict:
    """Compare a booking against the expected invoice_lines, line by line.

    Returns {"status": "pass"|"fail", "diffs": [...]}. Each booked line is
    matched, in order, against the expected line: `account_code` and `vat_code`
    must agree (the `account_name` is just a label that follows from the code,
    so it isn't asserted on its own).
    """
    diffs: list[str] = []
    lines = booking.get("lines") or []
    if len(lines) != len(expected):
        diffs.append(f"line count: expected {len(expected)}, got {len(lines)}")

    for i, exp in enumerate(expected):
        got = lines[i] if i < len(lines) else None
        if got is None:
            diffs.append(f"line {i + 1}: no booking written")
            continue
        if _norm(exp.get("account_code")) != _norm(got.get("account_code")):
            diffs.append(
                f"line {i + 1} account: expected {exp.get('account_code')}, "
                f"got {got.get('account_code')}"
            )
        if _norm(exp.get("vat_code")) != _norm(got.get("vat_code")):
            diffs.append(
                f"line {i + 1} vat: expected {exp.get('vat_code')}, "
                f"got {got.get('vat_code')}"
            )

    return {"status": "fail" if diffs else "pass", "diffs": diffs}
