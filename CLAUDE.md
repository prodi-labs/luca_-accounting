# Project: Accounting automation skills

This repo holds **skills** that help automate our bookkeeping work.
A skill is a set of written instructions, in plain English, that tells
Claude how to do one specific accounting task — for example, categorizing
a transaction, preparing an invoice, or checking a VAT number.

## How this repo is organized

- `.claude/skills/` — one folder per skill. Each folder has a `SKILL.md`
  file that describes the task and how to do it. (Claude Code looks for
  skills in this exact location.)
- `.claude/skills/process-invoice/vendors/` — one markdown file per vendor,
  holding that vendor's accounting rules. Owned by the accountant.
- `.claude/skills/process-invoice/policies/global.md` — rules that apply to
  every invoice.
- `tests/invoices/` — the test invoices. Each one marked `"testable": true`
  carries its own correct answer in its `invoice_lines` block (per line: the
  `account_code`, `account_name`, and `vat_code`), which the booking is
  validated against.
- `tests/.work/` — scratch copies of invoices with the answer removed, plus the
  booking JSON the skill writes (never the originals). Cleared at the start of
  each run.
- `scripts/` — the deterministic Python tools, run by both the skill and the
  harness so they share one code path: `load_invoice.py` (load + structure
  check, answer stripped), `list_invoices.py`, `validate_booking.py` (judge a
  booking against the answer), and `invoice_lib.py` (the shared logic). The
  idea: scripts do everything deterministic; the model only does inference
  (which account, which VAT code). Run them with `.venv/bin/python`.
- `main.py` — the entry point you run, at the repo root. It's a test harness:
  it books a sanitized copy of each invoice and checks it against the answer.
- `src/` — the harness code (`model.py`, `view/`, `controller.py`).
  Run the whole thing with `python main.py`.
- `README.md` — a plain-language guide on how to read, use, and add skills.
- `.claude/skills/categorize-transaction/` — a worked example to copy from.

## How to behave in this repo

- When the user asks for an accounting task, check `.claude/skills/` for a
  skill that matches and follow it.
- Skills only **propose** bookings. Never enter anything into an external
  accounting system unless a skill explicitly says to and the user
  confirms.
- When a transaction or document is unclear, ask the user instead of
  guessing. Accuracy matters more than speed here.
- Keep all instructions in skills written in plain, non-technical language.
  The people writing and reading them are accountants, not programmers.

## Adding a new skill

To add a skill, copy the `.claude/skills/categorize-transaction/` folder,
rename it, and rewrite the `SKILL.md` for the new task. The README explains
each part. No coding is required.
