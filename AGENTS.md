# Accounting automation skills

This repo holds **skills** that help automate our bookkeeping work.
A skill is a set of written instructions, in plain English, that tells
the agent how to do one specific accounting task — for example, categorizing
a transaction, preparing an invoice, or checking a VAT number.

## Repository layout

- `.cursor/skills/` — one folder per skill. Each folder has a `SKILL.md` file
  that describes the task and how to do it.
- `README.md` — a plain-language guide on how to read, use, and add skills.
- `.cursor/skills/categorize-transaction/` — a worked example to copy from.

## Agent behavior

- When the user asks for an accounting task, check `.cursor/skills/` for a
  skill that matches and follow it.
- Skills only **propose** bookings. Never enter anything into an external
  accounting system unless a skill explicitly says to and the user
  confirms.
- When a transaction or document is unclear, ask the user instead of
  guessing. Accuracy matters more than speed here.
- Keep all instructions in skills written in plain, non-technical language.
  The people writing and reading them are accountants, not programmers.

## Adding a new skill

To add a skill, copy the `.cursor/skills/categorize-transaction/` folder,
rename it, and rewrite the `SKILL.md` for the new task. The README explains
each part. No coding is required.
