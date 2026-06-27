---
name: categorize-transaction
description: >-
  Decides which bookkeeping category and account a bank or card transaction
  belongs to. Use whenever someone pastes a transaction (description and
  amount) and asks how it should be booked or categorized.
---

# Categorize a transaction

This is an EXAMPLE skill. It exists to show what a skill looks like so you
can copy it and write your own. See the README in the main folder for a
walkthrough. To make a real skill, copy this folder, give it a new name,
and rewrite the parts below.

## When to use this

Use this skill when someone gives you a transaction — a short description
and an amount — and wants to know the right category and account for it.

## What to do

1. Look at the description and the amount.

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

## How to answer

Reply with a short table:

| Description | Amount | Category | Account | Needs review? |
|-------------|--------|----------|---------|---------------|

Then add one sentence explaining why you chose that category, so it can be
double-checked.

## Important

- This skill only suggests how to book a transaction. It never enters
  anything into the accounting system.
- If the transaction is unclear, stop and ask instead of guessing.
