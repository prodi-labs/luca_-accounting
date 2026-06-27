# Luca accounting

Skills in `.claude/skills/` automate bookkeeping tasks (e.g. `process-invoice`).
Skills only **propose** bookings — never post to a live accounting system unless
the user confirms. When something is unclear, ask instead of guessing.

Full test-harness docs: `README.md`.

## Running on Windows

This repo is developed on Windows. Use Windows paths and commands.

**Setup (once):**

```powershell
py -3.13 -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements.txt
claude auth login
```

If `claude` fails in PowerShell, use `claude.cmd` instead (execution-policy
block on `claude.ps1`).

**Run the test harness:**

```powershell
.venv\Scripts\python.exe main.py
```

**Run invoice scripts** (load, validate, list) — always use the venv Python:

```powershell
.venv\Scripts\python.exe scripts/load_invoice.py <path>
.venv\Scripts\python.exe scripts/validate_booking.py <invoice> <booking>
```

Do **not** use `.venv/bin/python`; that path is Unix-only and does not exist here.

Scratch copies and booking JSON go in `tests/.work/` (cleared each run).
Test invoices and embedded answers live in `tests/invoices/`.
