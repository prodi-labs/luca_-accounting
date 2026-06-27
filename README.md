# Luca — invoice assistant

Ask questions about your invoices and book them, in plain language.

## Setup

Requires Python 3.10+ and an active Claude Code login (`claude --version` to check).

```sh
python3.13 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
```

## Run

```sh
.venv/bin/python main.py
```

A menu asks whether you want the chat interface or the test harness.

**Chat** — ask questions in plain language:

```
> how many invoices do I have
> list all invoices
> what is my biggest invoice
> how much did we spend in total
> book invoice Notion
> book all my invoices
```

**Test** — checks whether the skill books invoices correctly against embedded expected answers. Only invoices marked `"testable": true` with an `invoice_lines` block appear in the test menu.

Invoices live in `tests/invoices/`. Booking writes a JSON file to `tests/.work/`.
