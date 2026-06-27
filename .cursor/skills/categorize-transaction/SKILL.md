---
name: categorize-transaction
description: >-
  Decides which bookkeeping category and account a bank or card transaction
  belongs to. Use when someone pastes a transaction description and amount
  and asks how it should be booked or categorized.
---

# Categorize a transaction

Example skill — copy this folder and rewrite the instructions for new tasks.
See the README for a walkthrough.

## Instructions

1. Read the transaction description and amount.

2. Match it to a category using this list:
   - Anything from Google, Microsoft, Adobe, Notion, Zoom, or similar →
     **Software & subscriptions** (account 6200).
   - Restaurants, cafes, food delivery → **Meals & entertainment**
     (account 6300).
   - Flights, hotels, trains, taxis, Uber → **Travel** (account 6400).
   - Phone, internet, electricity → **Utilities** (account 6500).
   - Bank fees, card fees → **Bank charges** (account 6600).
   - Anything you are not sure about → leave the category blank and flag
     it for review.

3. Flag the transaction for human review if any of these is true:
   - The amount is over 1,000.
   - You are not confident which category fits.
   - It looks like it could belong to more than one category.

## Output format

Reply with a short table:

| Description | Amount | Category | Account | Needs review? |
|-------------|--------|----------|---------|---------------|

Then add one sentence explaining why you chose that category, so it can be
double-checked.

## Guardrails

- Only suggest how to book a transaction. Never enter anything into the
  accounting system.
- If the transaction is unclear, stop and ask instead of guessing.
