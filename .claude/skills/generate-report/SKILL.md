---
name: generate-report
description: >-
  Generates financial reports from booked invoices. Use when the user asks
  for a P&L, a spending breakdown, a summary of invoices, or any other
  financial report.
---

# Generate a report

## Step 1 — Get the data

Call the `show_report` tool to print a formatted P&L to the terminal, or call
`list_invoices` for raw invoice data to answer specific questions.

For any question that needs amounts or account details (totals per vendor,
totals per account, etc.), call `show_report` first so the full P&L is visible,
then answer from the data it returns.

## Step 2 — Build the report

Common reports and how to handle them:

**P&L summary** — call `show_report`. It prints a table of expenses grouped by
account code and currency, plus a pending invoice list.

**Spending by vendor** — call `list_invoices`, filter to booked ones, group by
vendor, sum amounts. Present as a simple list in the chat.

**Unbooked invoices** — call `list_invoices`, filter to `booked=false`. List
vendor, invoice_id, amount, and date.

**Explain a specific booking** — call `get_booking_detail` for the invoice_id.
Describe the account code chosen, why it matches the line item description,
and what the VAT code means.

## Step 3 — Present results

Always include:
- How many invoices are booked vs. still pending.
- Totals per currency (never mix currencies in a single sum).
- The date range covered (earliest to latest date in the data).

Reply in plain text in the chat. Keep it concise — the colored table from
`show_report` already shows the detail; your reply should summarize or
highlight what the user asked about.

## Guardrails

- Use only data from the tools. Do not read invoice or booking files directly.
- Never enter anything into an accounting system.
- If many invoices are unbooked, say so clearly — a partial P&L can be
  misleading.
- Do not invent or estimate numbers. If an amount is missing, say "unknown".
