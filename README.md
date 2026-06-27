# Accounting skills — how to use this repo

This repo is our shared place for building **skills** that automate parts of
our bookkeeping. You don't need to be technical to use it. This guide
explains what a skill is, how to run one, and how to add your own.

## What is a skill?

A skill is a folder with a written set of instructions for one task. When
you ask the agent to do that task, it reads the instructions and follows them.
Think of it as a recipe card: clear steps that produce a consistent result
every time, no matter who asks.

Each skill lives in its own folder inside `.cursor/skills/` and contains one
file called `SKILL.md`.

## What's in this repo

```
.
├── AGENTS.md                         ← background the agent reads automatically
├── README.md                         ← this guide
└── .cursor/skills/
    └── categorize-transaction/       ← example skill, copy this to start
        └── SKILL.md
```

## How to use a skill

1. Open this folder in Cursor.
2. Ask in plain language, e.g.
   *"Categorize this transaction: ADOBE INC, 59.99"*.
3. The agent finds the matching skill and follows it. You'll get a consistent,
   explained answer.

You don't have to name the skill — the agent picks the right one based on the
`description` line at the top of each `SKILL.md`. That's why a good
description matters (see below).

## Anatomy of a SKILL.md file

Open `.cursor/skills/categorize-transaction/SKILL.md` and you'll see two parts.

**1. The header (between the `---` lines).** This tells the agent when to use
the skill:

```
---
name: categorize-transaction
description: >-
  Decides which bookkeeping category and account a bank or card transaction
  belongs to. Use when someone pastes a transaction description and amount
  and asks how it should be booked or categorized.
---
```

- `name` — a short label, lowercase with dashes, same as the folder name.
- `description` — the most important line. Describe *what the skill does*
  and *when to use it*, in third person. The agent reads this to decide
  whether to use the skill, so be specific about the trigger ("Use when
  someone...").

**2. The body (everything below).** Plain-English instructions: steps to
follow, how to format the answer, and guardrails. Write it the way you'd
explain the task to a new colleague.

## How to add a new skill

No coding needed. Just:

1. **Copy** the `.cursor/skills/categorize-transaction/` folder.
2. **Rename** the new folder to match the task, e.g.
   `.cursor/skills/prepare-sales-invoice/`.
3. **Open** the `SKILL.md` inside and rewrite it:
   - Change `name` to match the new folder name.
   - Write a clear `description` (what it does + when to use it).
   - Replace the steps with the actual steps for the new task.
4. **Save.** That's it — the skill is ready to use.

### Tips for writing good skills

- One skill = one task. If a skill is doing two things, split it in two.
- Be specific in the steps. "Book travel to account 6400" is better than
  "book it correctly".
- Say what the skill should **not** do (e.g. "never post to the accounting
  system, only suggest").
- Tell the agent to **ask** when something is unclear instead of guessing.
- Test it: ask the agent to run the task with a real example and check the
  result, then adjust the wording.

## Ideas for skills to build next

- Prepare a sales invoice from an order.
- Match incoming payments to open invoices.
- Check a supplier's VAT/tax number format.
- Flag duplicate or suspicious transactions.
- Summarize the month's expenses by category.

Add one folder per idea and we'll refine them together.
