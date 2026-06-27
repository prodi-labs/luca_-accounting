# Account-specific VAT rules

Purpose: use this file for VAT rules that depend on a specific MAR account. Keep the available Odoo VAT codes in `VAT_codes_odoo.md`; keep the general account classification rules in `MAR_booking_agent_en.md`; put account-specific VAT preferences and exceptions here.

The agent should apply these rules only after selecting a likely MAR account. Invoice facts always override defaults. If the invoice context conflicts with the default rule, mark the transaction for review.

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
| `616680` | Restaurant expenses | Services | Usually `21% S`, but VAT deduction may be restricted or unavailable | Review | Review | Limited/non-deductible VAT may apply | Any restaurant/catering invoice | Always flag VAT attention unless dossier has explicit rule. |
| `612600` | Fuel for company cars | Goods/service depending on invoice | Review | Review | Review | Passenger car VAT limitation often applies | Any passenger car fuel/charging cost | Needs vehicle and deduction context. |
| `612602` | Car expenses per vehicle | Goods/services depending on invoice | Review or limited deduction code such as `21% G D50` where applicable | Review | Review | Depends on vehicle and file settings | Any car expense without known vehicle rule | Use configured vehicle deduction percentage. |
| `610101` | Business address costs | Mixed: services/goods/real estate | Depends on invoice line | Review | Review | Business-use percentage may apply | Home office, mixed-use address, utilities, rent | Do not invent professional-use percentage. |
| `623020` | Meal vouchers | Personnel-related service | Usually review | Review | Review | Depends on payroll/benefit treatment | Missing payroll/voucher details | Often better handled from payroll or voucher provider rules. |
| `657100` | Bank charges | Financial/bank fees | Usually `21% S` only if VAT is charged; otherwise review/no VAT depending document | Review | Review | Depends on document | Bank fees without invoice VAT detail | Use invoice VAT facts; bank transactions alone may be insufficient. |

## Recommended maintenance rule

When adding a new rule:

1. Add the MAR account code and exact account name.
2. Define whether the account normally concerns merchandise (`M`), services (`S`), miscellaneous goods (`G`), or investment goods (`IG`).
3. Add the default domestic, EU and extra-EU Odoo VAT code families.
4. Add deduction limitations only when they are account- or dossier-specific.
5. Add review triggers for anything the agent must not decide automatically.

