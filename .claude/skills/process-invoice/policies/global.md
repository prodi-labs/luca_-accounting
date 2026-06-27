# Global accounting policy

These rules apply to **every** invoice, unless a vendor file or the invoice's
own note overrides them. The accountant (Arno) owns this file — edit it in
plain language; no code changes are needed for the agent to pick up a change.

## Default accounts

If no vendor file gives a more specific account, fall back to these by the kind
of spend:

- Software, SaaS, online subscriptions → **6200 — Software & subscriptions**
- Restaurants, cafes, food delivery → **6300 — Meals & entertainment**
- Flights, hotels, trains, taxis → **6400 — Travel**
- Phone, internet, electricity → **6500 — Utilities**
- Bank and card fees → **6600 — Bank charges**
- Anything else → leave the account blank and flag for review.

## Tax codes

- A supplier inside the EU but in a different country from us, with no VAT
  charged on the invoice → **VAT-RC-EU** (reverse charge).
- A domestic supplier charging VAT → **VAT-STD** (standard rate).
- A supplier outside the EU → **VAT-NONEU**.
- If the invoice shows a VAT amount that doesn't match any of the above, flag
  it rather than guessing.

## When to always flag

- The total is over 1,000 and there is no vendor file for the supplier.
- The currency is not EUR.
- The invoice is missing a date, a total, or any line item.
