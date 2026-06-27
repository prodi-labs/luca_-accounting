---
name: process-invoice
description: >-
  Loads an invoice file, decides the correct MAR account and VAT code for each
  line, writes a booking JSON, and validates it. Use when given a path to an
  invoice JSON file to process.
---

# Process an invoice

## Step 1 — Load and validate the invoice

Run this command, replacing `<path>` with the invoice file path:

```
.venv/bin/python scripts/load_invoice.py <path>
```

The script loads the file, checks its structure, and strips the embedded test
answer so you never see it.

**If the output contains `"error"`: stop immediately.** Report the error message
to the user and do not continue. A malformed invoice must not be booked.

If the script succeeds, use its JSON output as your invoice data for all
remaining steps. Do not read the raw invoice file yourself.

## Step 2 — Read the reference files

Read these three files before making any booking decision. Read them every time
— do not rely on memory from a previous run.

1. `.claude/skills/categorize-transaction/references/MAR_booking_agent_en.md`
   — Belgian MAR account codes and when to use each one.

2. `.claude/skills/categorize-transaction/references/VAT_codes_odoo.md`
   — Available Odoo VAT codes and how to choose between them.

3. `.claude/skills/categorize-transaction/references/account_vat_rules.md`
   — Account-specific VAT rules and exceptions that override the general rules.

Do not read any other files. Do not glob for policies, vendors, or rules folders
— they do not exist.

## Step 3 — Decide the booking

For each line item in the invoice:

1. Choose the MAR account code and name using `MAR_booking_agent_en.md`.
   - Pick the most specific account that fits the economic nature of the cost.
   - If genuinely uncertain, stop and ask the user rather than guessing.

2. Choose the VAT code using `VAT_codes_odoo.md` and `account_vat_rules.md`.
   - The VAT code must match exactly — correct capitalisation and spacing.
   - Base it on: supplier country, VAT rate shown on the invoice,
     goods/services/investment nature, and any reverse-charge text.
   - If the invoice lacks VAT detail or the case is ambiguous, flag it for
     review instead of guessing.

## Step 4 — Write the booking file

Write the booking to:

```
tests/.work/<invoice-stem>.booking.json
```

where `<invoice-stem>` is the filename of the invoice without `.json`
(e.g. invoice at `tests/invoices/batch_foo__INV-001.json` →
booking at `tests/.work/batch_foo__INV-001.booking.json`).

The booking must follow this exact structure:

```json
{
  "lines": [
    {
      "account_code": "612100",
      "account_name": "IT services",
      "vat_code": "21% S"
    }
  ]
}
```

One entry in `lines` per invoice line item. `account_code` and `vat_code` are
required. `account_name` is a human-readable label — include it for clarity.

## Step 5 — Validate the booking

Run:

```
.venv/bin/python scripts/validate_booking.py <invoice-path> <booking-path>
```

Read the JSON output:

- `"status": "pass"` — booking is correct. Report success to the user.
- `"status": "fail"` — booking is wrong. Show the user the `diffs` list and
  explain your reasoning so the mistake can be understood.
- `"status": "invalid"` — the booking JSON is malformed. Fix the structure
  (see `problems` list) and validate again.
- `"status": "untested"` — the invoice has no embedded answer. The booking
  has been written but cannot be automatically checked; tell the user.
- `"status": "no-booking"` — the booking file was not written. Check step 4.

## Guardrails

- Never enter anything into an accounting system. This skill only proposes a
  booking.
- If any step is unclear or the invoice is ambiguous, ask the user instead of
  guessing. Accuracy matters more than speed.
- Do not read `scripts/load_invoice.py`, `scripts/validate_booking.py`, or
  `scripts/invoice_lib.py` — you do not need to understand their implementation.
