# Account-specific VAT rules

Purpose: use this file for VAT rules that depend on a specific MAR account. Keep the available Odoo VAT codes in `VAT_codes_odoo.md`; keep the general account classification rules in `MAR_booking_agent_en.md`; put account-specific VAT preferences and exceptions here.

The agent should apply these rules only after selecting a likely MAR account. Invoice facts always override defaults. If the invoice context conflicts with the default rule, mark the transaction for review.

## Non-deductible VAT codes (`ND`)

Use `21% ND`, `12% ND`, or `6% ND` (matching the rate on the document) when VAT on the document **cannot be deducted**.

**Use `ND` when the document is a ticket or receipt, not a VAT-compliant invoice**, for example:

- missing supplier VAT number
- payment-terminal or ticket slip without full invoice details
- gas-station, parking, car-wash, or restaurant/catering tickets

**Exception — train tickets (NMBS/SNCB and similar):** even without a full VAT invoice, the **6% VAT is recoverable**. Book the travel cost on `616700` with **`6% S`**, not `6% ND`. The ticket price is VAT-inclusive (e.g. €1.06 total = €1.00 cost + €0.06 recoverable VAT).

**Also use `ND`** when the expense type normally excludes VAT deduction even on a compliant invoice (restaurant/catering, parking, car wash).

Use normal purchase codes (`21% G`, `21% S`, `21% EU S`, etc.) only when the document is a **full VAT invoice** that supports deduction. Digital service receipts with supplier VAT number, customer details, and reverse charge are not tickets — book with the usual EU/EX codes.

Do not use an `ND` code when a normal or limited-deduction code applies and the document supports deduction.

## How to fill this file

Use one row per MAR account or account pattern. Keep the Odoo VAT code names exact.

| MAR account | Account name | Default VAT scope | Domestic purchase VAT codes | EU purchase VAT codes | Extra-EU purchase VAT codes | Deduction limitation | Review triggers | Notes |
|---|---|---|---|---|---|---|---|---|
| `604000` | Purchases of goods for resale | Merchandise / goods for resale | `21% M`, `12% M`, `6% M`, `0% M` | `21% EU M`, `12% EU M`, `6% EU M`, `0% EU M` | `21% EX M`, `12% EX M`, `6% EX M`, `0% EX M` | Usually normal deduction | Supplier sells both goods and services; import/customs document missing; margin scheme | Use `M` because this account is part of goods-for-resale margin. |
| `607000` | Ancillary purchase costs | Usually linked to goods | Usually `21% G` or same family as underlying purchase if file policy requires | Usually review | Usually review | Normal unless import/customs/VAT document says otherwise | Import VAT, customs, logistics invoice linked to non-EU goods | Shipping/logistics can require careful VAT treatment. |
| `612100` | IT services | Services | `21% S`, `12% S`, `6% S`, `0% S` | `21% EU S`, `12% EU S`, `6% EU S`, `0% EU S` | `21% EX S`, `12% EX S`, `6% EX S`, `0% EX S` | Usually normal deduction | SaaS supplier outside Belgium; reverse charge text missing; hardware included | Typical for SaaS, API usage, hosting and IT support. |
| `615200` | Fees of bookkeepers and accountants | Services | `21% S` | `21% EU S` if EU service supplier and reverse charge applies | `21% EX S` if non-EU service supplier and reverse charge/import service logic applies | Usually normal deduction | Public filing costs mixed with professional fees | Split legal/publication costs if needed. |
| `615300` | Fees of auditors, lawyers and notaries | Services, but often mixed | `21% S` | Review | Review | Depends on underlying transaction | Real estate purchase, registration duties, notary split, non-deductible items | Notary invoices often need splitting. |
| `616200` | Telephone and internet expenses | Services | `21% S` | `21% EU S` | `21% EX S` | Apply business-use percentage if mixed/private use | Device included, private use, mixed subscription | Do not invent business-use percentage. |
| `616680` | Restaurant expenses | Services | `21% ND`, `12% ND`, or `6% ND` (match invoice rate) | Review | Review | VAT usually non-deductible | Any restaurant/catering invoice or ticket | Use `ND` on tickets and receipts; normal codes only on a compliant VAT invoice. |
| `612601` | Parking, car wash and tolls | Goods/services depending on invoice | `21% ND`, `12% ND`, or `6% ND` (match invoice rate) | Review | Review | VAT usually non-deductible on tickets/receipts | Parking ticket, car wash receipt, toll slip | Ticket-style documents → `ND`; normal codes only on a compliant VAT invoice. |
| `612600` | Fuel for company cars | Goods/service depending on invoice | `21% ND`, `12% ND`, or `6% ND` on gas-station tickets/receipts; `21% G` (or limited-deduction code) on compliant fuel invoices | Review | Review | Passenger car VAT limitation often applies | Gas-station ticket/receipt; fuel invoice without vehicle context | Ticket or receipt at a petrol station → `ND`; full VAT invoice from fuel card provider → normal/limited code per vehicle rules. |
| `612602` | Car expenses per vehicle | Goods/services depending on invoice | Review, limited deduction code such as `21% G D50`, or `21% ND`/`12% ND`/`6% ND` on non-compliant tickets | Review | Review | Depends on vehicle and file settings | Any car expense without known vehicle rule | Use configured vehicle deduction percentage; use `ND` for ticket-style documents. |
| `616700` | Travel and accommodation expenses | Services | **`6% S` on train tickets** (recoverable without full invoice); `21% ND`/`12% ND`/`6% ND` on other ticket-style travel where VAT is not deductible; normal codes on compliant travel invoices | Review | Review | Train 6% is recoverable | NMBS/SNCB train ticket; other travel ticket/receipt | Train tickets → `6% S`; other non-compliant travel tickets → `ND`. |
| `612050` | Administrative services | Services | `21% S`, `12% S`, `6% S`, `0% S` | Review | Review | Usually normal deduction | Meal-voucher provider admin fees (e.g. Monizze service charge) | Voucher administration/platform fees are services, not the voucher value itself. |
| `612070` | Training | Services | `21% S` or `0% S` if supplier is VAT-exempt | Review | Review | Normal deduction unless exempt | Registration from VAT-exempt professional body (e.g. ITAA) | VAT-exempt organisations → `0% S`. |
| `618110` | Meal vouchers for director/manager | Personnel-related | `0% S` on voucher face value | Review | Review | No VAT on voucher value | Monizze or other meal-voucher orders for directors/managers | Split provider service fees to `612050` with `21% S`. |
| `610101` | Business address costs | Mixed: services/goods/real estate | Depends on invoice line | Review | Review | Business-use percentage may apply | Home office, mixed-use address, utilities, rent | Do not invent professional-use percentage. |
| `623020` | Meal vouchers | Personnel-related service | Usually review | Review | Review | Depends on payroll/benefit treatment | Employee meal vouchers (not directors) | Director/manager vouchers → `618110`. Provider fees → `612050`. |
| `657100` | Bank charges | Financial/bank fees | Usually `21% S` only if VAT is charged; otherwise review/no VAT depending document | Review | Review | Depends on document | Bank fees without invoice VAT detail | Use invoice VAT facts; bank transactions alone may be insufficient. |

## Recommended maintenance rule

When adding a new rule:

1. Add the MAR account code and exact account name.
2. Define whether the account normally concerns merchandise (`M`), services (`S`), miscellaneous goods (`G`), or investment goods (`IG`).
3. Add the default domestic, EU and extra-EU Odoo VAT code families.
4. Add deduction limitations only when they are account- or dossier-specific.
5. Add review triggers for anything the agent must not decide automatically.

