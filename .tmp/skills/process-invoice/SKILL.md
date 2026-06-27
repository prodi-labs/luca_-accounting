---
name: process-invoice
description: >-
  Books one parsed invoice end-to-end: loads the invoice JSON with the loader
  script, identifies the vendor, applies the matching rules, and writes a
  structured booking JSON (the chart-of-accounts account and VAT code per line).
  Use whenever someone asks to book, categorize, or process an invoice file.
---

# Process an invoice

This skill books a single invoice that has already been parsed into a JSON
file. It walks four fixed stations in order. It does **not** decide its own
steps — it always follows the same four, every time.

The accounting decisions live in markdown that the accountant owns. These
folders sit **next to this skill file**, inside its own folder
(`.claude/skills/process-invoice/`):

- `.claude/skills/process-invoice/policies/global.md` — rules that apply to
  every invoice.
- `.claude/skills/process-invoice/vendors/<name>.md` — rules for one specific
  vendor.
- The invoice's own `notes` field, **if it has one** — a one-off instruction
  for just this invoice.

**Precedence, when two rules disagree:** the invoice's own note (if present)
wins over the vendor file, and the vendor file wins over the global policy.
Always say which rule you used.

## What to do

Work the four stations in order for the one invoice you were given. The
deterministic parts — loading the file and checking its structure — are done
by small scripts in `scripts/`, so you can trust their output and focus on the
accounting decisions. Run the scripts with the project's `.venv` interpreter
from the repo root (it has the right Python version).

### Station 1 — Load the invoice

Load the invoice by **running the loader script**, not by reading the file
yourself:

```sh
.venv/bin/python scripts/load_invoice.py <path-to-invoice.json>
```

- On success it prints the invoice as JSON (the answer, if any, already
  removed). Work from that output.
- On failure it prints `{"error": "..."}` and exits non-zero. The message says
  what is wrong (missing field, not valid JSON, and so on). **Do not guess at a
  broken invoice** — record a flag that quotes the error and stop (see "Writing
  the booking").

The loaded invoice is laid out in named sections:

- `supplier.legal_name` — who billed us (the vendor).
- `document.issue_date` — the invoice date.
- `amounts.total_including_tax` and `amounts.currency` — the total and currency.
- `tax` — the VAT actually charged (`reverse_charge`, plus a `tax_lines` list).
- `line_items` — the things billed; one entry per line, each with a
  `description`, `amount`, and `tax_rate`. **This is what you book** — one
  booked line per line item, in the same order.

### Station 2 — Identify the vendor

Look in this skill's `vendors/` folder for a file whose `match:` list contains
the supplier's legal name (matching is case-insensitive and ignores small
differences like "Inc." vs "Inc"). If you find exactly one match, use it. If
you find none, or more than one, flag it for review and stop.

### Station 3 — Decide account and tax

Read the matched vendor file and `.claude/skills/process-invoice/policies/global.md`.
For **each line item**, produce:

- the **account** (`account_code` number + `account_name`) that line should be
  booked to, and
- the **VAT code** (`vat_code`) that applies.

Most invoices book every line to the same account and VAT code; only split them
when the line items clearly belong to different categories.

Apply the precedence rule above. Write down the single rule that decided the
values (the file path), so the booking can be double-checked.

If the vendor file and global policy together don't give you a confident
answer, flag it rather than guessing.

### Station 4 — Reconcile (sanity check)

Before writing anything, check the booking against the vendor file's stated
expectations:

- Is the total roughly in the usual range for this vendor? If the vendor file
  gives a typical amount and this invoice is far above it, flag it.
- Does the tax code make sense for the amounts shown?

If a check fails, add a specific flag (e.g. "amount 3x the usual for this
vendor") but still record your best-guess booking.

## Writing the booking

Your output is a **single structured JSON object** — the booking. Write it with
the `Write` tool to the path you were told to use (the caller gives you one;
otherwise save it next to the invoice as `<name>.booking.json`). Do not edit the
invoice file itself.

The object has exactly these keys. The `lines` list has **one entry per line
item**, in the same order as `line_items`:

```json
{
  "lines": [
    {
      "account_code": "6200",
      "account_name": "Software & subscriptions",
      "vat_code": "VAT-RC-EU"
    }
  ],
  "rule_cited": ".claude/skills/process-invoice/vendors/adobe.md",
  "scope": "vendor",
  "confidence": "high",
  "flags": [],
  "booked_at": "2026-06-27",
  "booked_by": "agent"
}
```

- Each entry in `lines` carries the `account_code`, `account_name`, and
  `vat_code` for the matching line item. Keep them in the same order as
  `line_items`, one entry per line item.
- `scope` is one of `invoice`, `vendor`, or `global` — whichever rule decided
  the accounts/VAT.
- `confidence` is `high`, `medium`, or `low`.
- `flags` is a list of short, specific strings. An empty list means the invoice
  booked cleanly with no human review needed. If you had to stop (a bad invoice,
  no vendor match), still write the object with an empty `lines` list and the
  reason in `flags`.
- Write nothing but this JSON object to the booking file — a separate script
  reads it to validate the booking, so it must parse cleanly.

## Important

- This skill only **proposes** a booking, as a JSON object. It never posts
  anything to a live accounting system, and it never edits the invoice file.
- When in doubt, flag and stop — accuracy matters more than speed.
