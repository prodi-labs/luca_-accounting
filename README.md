# How to test the invoice-booking skill

This program checks whether the `process-invoice` skill books invoices
correctly. Each test invoice carries its own correct answer. The program
shows the skill a copy of the invoice **with the answer hidden**, lets it
book it, and then compares what it produced against the correct answer. It
never posts anything to a live accounting system.

## One-time setup

1. **Log in to Claude Code** (the program reuses this login — no API key
   needed). Check it works:

   ```sh
   claude --version
   ```

2. **Create the environment and install dependencies** (needs Python 3.10+):

   ```sh
   python3.13 -m venv .venv
   .venv/bin/python -m pip install -r requirements.txt
   ```

## Run it

Start the program with no extra words:

```sh
.venv/bin/python main.py
```

It shows a menu of the testable invoices in `tests/invoices/`. Type a number
to test just that one invoice, `A` to test all of them, or `Q` to quit.

## How a test invoice is set up

The correct answer lives inside each invoice, in its `invoice_lines` block.
Mark the invoice with `"testable": true` and give each line the account and
VAT code it should book to:

```json
{
  "document": { "document_number": "INV-2026-0042", "issue_date": "2026-06-15" },
  "supplier": { "legal_name": "Adobe Inc.", "country": "IE" },
  "amounts": { "currency": "EUR", "total_including_tax": 599.88 },
  "tax": { "reverse_charge": true, "tax_lines": [ ... ] },
  "line_items": [
    { "description": "Creative Cloud All Apps - Annual plan", "amount": 599.88 }
  ],
  "testable": true,
  "invoice_lines": [
    {
      "description": "Creative Cloud All Apps - Annual plan",
      "account_code": "6200",
      "account_name": "Software & subscriptions",
      "vat_code": "VAT-RC-EU"
    }
  ]
}
```

Only invoices marked `testable` appear in the menu. The `invoice_lines` block
is the answer: for each line, the program checks the booked `account_code` and
`vat_code` against it. There is one entry per line item, in the same order.

## What happens during a test

The deterministic steps are done by small Python scripts in `scripts/`, which
the model also calls — so the program and the model run the exact same code.
For each invoice, the program:

1. Writes a **sanitized copy** into `tests/.work/` — the same invoice but
   with `testable`, `invoice_lines`, and any old `booking` removed, so the
   skill can't see the answer.
2. Runs the `process-invoice` skill on that copy. The skill loads the invoice
   with `scripts/load_invoice.py` (which checks the structure and would return
   an error for a malformed file), does the accounting decisions, and writes a
   structured **booking JSON** to `tests/.work/<name>.booking.json`.
3. Runs `scripts/validate_booking.py` to compare that booking, line by line,
   against the invoice's own `invoice_lines` — a deterministic verdict.

Your real invoices in `tests/invoices/` are never changed — only the copies
in `tests/.work/` are written to, and they are cleared at the start of every
run. The report looks like:

```
Results (booking vs each invoice's expected answer):

  PASS  INV-2026-0042    6200 / VAT-RC-EU
  FAIL  INV-2026-0099    account: expected 6300, got 6200
  ----  INV-2026-0100    no expected answer in the invoice

Result: 1 passed, 1 failed, 1 untested.
```

Use this whenever you change the skill, the policies, or the vendor rules,
to make sure bookings still come out right. Each test books an invoice for
real (it calls the model), so testing all of them costs one booking each.

## How the program is laid out

You don't need to read the code to use the program, but if you're curious,
the work is split into a few plain parts:

- `main.py` — the starting point you actually run (at the repo root).
- `scripts/` — the deterministic tools, shared by the program and the model:
  - `load_invoice.py` — load + structure-check one invoice (answer removed).
  - `list_invoices.py` — list the invoices as JSON (for the menu).
  - `validate_booking.py` — judge a booking JSON against the answer.
  - `invoice_lib.py` — the shared logic the three scripts wrap.
- `src/model.py` — runs the scripts and the model, and ties the run together.
- `src/view/` — the menu, the report, and everything you see on screen.
- `src/controller.py` — ties the two together and runs the loop.
- `tests/invoices/` — the test invoices, each with its embedded answer.
- `tests/.work/` — scratch copies and booking JSON the skill writes (cleared
  each run).
- `.claude/skills/process-invoice/{policies,vendors}/` — the accounting
  rules the accountant owns, next to the skill that uses them.
