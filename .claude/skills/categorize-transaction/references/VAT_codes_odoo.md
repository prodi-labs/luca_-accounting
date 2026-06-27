# Odoo VAT codes for Belgian bookkeeping

Source file: `BTW (account.tax)(1).xlsx`

Purpose: this reference lists the available Odoo VAT codes and explains how a bookkeeping agent should interpret them. The exact value in `Odoo VAT code` must be preserved when returning a suggested VAT code, because it is the value used in Odoo.

## How the agent should use this file

1. First classify the transaction and MAR account using `MAR_booking_agent_en.md`.
2. Then choose the VAT code using this reference and the invoice facts: supplier country, customer VAT number, VAT rate shown on the document, goods/services/investment nature, reverse charge text, import/export clues, and deduction limitations.
3. Do not infer a VAT code from the MAR account alone when the invoice gives conflicting facts.
4. If the invoice lacks VAT details or the transaction has mixed/private use, return `needs_review: true`.
5. For purchase invoices, distinguish:
   - merchandise / goods for resale (`M`)
   - services (`S`)
   - miscellaneous goods (`G`)
   - investment goods (`IG`)
6. For EU or non-EU suppliers, check whether the supply is goods, services, or investment goods before choosing an `EU` or `EX` code.
7. For limited deduction codes such as `D35`, `D50`, `D75`, or `D85`, use them only when the account rule, document context, or dossier rule explicitly supports the deduction limitation.

## Data quality notes

- `6% S` has original description `12% BTW (Services/diensten)` in the source file; likely typo, preserved in the raw description.
- Some `Reeks` sequence values are duplicated in the source file; preserve `BTW naam` as the unique practical identifier.

## Sales VAT codes

| Reeks | Odoo VAT code | Rate | Scope | Regime | Deduction | Invoice label | Description |
|---:|---|---:|---|---|---|---|---|
| 10 | `21%` | 21% |  | Domestic / standard | Normal deduction, unless limited by account or document context | 21% | 21% VAT on sales |
| 11 | `12%` | 12% |  | Domestic / standard | Normal deduction, unless limited by account or document context | 12% | 12% VAT on sales |
| 12 | `6%` | 6% |  | Domestic / standard | Normal deduction, unless limited by account or document context | 6% | 6% VAT on sales |
| 13 | `0%` | 0% |  | Domestic / standard | Normal deduction, unless limited by account or document context | 0% | 0% VAT on sales |
| 14 | `0% Cocont` | 0% |  | Co-contracting | Normal deduction, unless limited by account or document context | 0% | 0% co-contracting |
| 15 | `0% EU S` | 0% | Services | Intra-Community | Normal deduction, unless limited by account or document context | 0% | 0% intra-Community (Services/diensten) |
| 16 | `0% EU M` | 0% | Goods | Intra-Community | Normal deduction, unless limited by account or document context | 0% | 0% intra-Community (Goods/all goods) |
| 17 | `0% EU T` | 0% | Services | Intra-Community | Normal deduction, unless limited by account or document context | 0% | 0% intra-Community (Triangular) |
| 18 | `0% EX` | 0% |  | Intra-Community | Normal deduction, unless limited by account or document context | 0% | 0% extra-Community (outside EU) |

## Purchase VAT codes

| Reeks | Odoo VAT code | Rate | Scope | Regime | Deduction | Invoice label | Description |
|---:|---|---:|---|---|---|---|---|
| 19 | `21% M` | 21% | Goods | Domestic / standard | Normal deduction, unless limited by account or document context | 21% | 21% VAT on merchandise / goods for resale |
| 20 | `12% M` | 12% | Goods | Domestic / standard | Normal deduction, unless limited by account or document context | 12% | 12% VAT on merchandise / goods for resale |
| 21 | `6% M` | 6% | Goods | Domestic / standard | Normal deduction, unless limited by account or document context | 6% | 6% VAT on merchandise / goods for resale |
| 22 | `0% M` | 0% | Goods | Domestic / standard | Normal deduction, unless limited by account or document context | 0% | 0% VAT on merchandise / goods for resale |
| 23 | `21% S` | 21% | Services | Domestic / standard | Normal deduction, unless limited by account or document context | 21% | 21% VAT on services |
| 24 | `21% G` | 21% | Goods | Domestic / standard | Normal deduction, unless limited by account or document context | 21% | 21% VAT on goods / miscellaneous goods |
| 25 | `12% S` | 12% | Services | Domestic / standard | Normal deduction, unless limited by account or document context | 12% | 12% VAT on services |
| 26 | `12% G` | 12% | Goods | Domestic / standard | Normal deduction, unless limited by account or document context | 12% | 12% VAT on goods / miscellaneous goods |
| 27 | `6% S` | 6% | Services | Domestic / standard | Normal deduction, unless limited by account or document context | 6% | 12% VAT on services |
| 28 | `6% G` | 6% | Goods | Domestic / standard | Normal deduction, unless limited by account or document context | 6% | 6% VAT on goods / miscellaneous goods |
| 29 | `0% S` | 0% | Services | Domestic / standard | Normal deduction, unless limited by account or document context | 0% | 0% VAT on services |
| 30 | `0% G` | 0% | Goods | Domestic / standard | Normal deduction, unless limited by account or document context | 0% | 0% VAT on goods / miscellaneous goods |
| 31 | `21% IG` | 21% | Investment goods | Domestic / standard | Normal deduction, unless limited by account or document context | 21% | 21% VAT on investment goods |
| 32 | `12% IG` | 12% | Investment goods | Domestic / standard | Normal deduction, unless limited by account or document context | 12% | 12% VAT on investment goods |
| 33 | `6% IG` | 6% | Investment goods | Domestic / standard | Normal deduction, unless limited by account or document context | 6% | 6% VAT on investment goods |
| 34 | `0% IG` | 0% |  | Domestic / standard | Normal deduction, unless limited by account or document context | 0% | 0% VAT on investment goods |
| 35 | `21% M.Cocont` | 21% | Goods | Co-contracting | Normal deduction, unless limited by account or document context | 21% | 21% BTW co-contracting (Merchandise/handelsgoederen) |
| 36 | `12% M.Cocont` | 12% | Goods | Co-contracting | Normal deduction, unless limited by account or document context | 12% | 12% BTW co-contracting (Merchandise/handelsgoederen) |
| 37 | `6% M.Cocont` | 6% | Goods | Co-contracting | Normal deduction, unless limited by account or document context | 6% | 6% BTW co-contracting (Merchandise/handelsgoederen) |
| 38 | `0% M.Cocont` | 0% | Goods | Co-contracting | Normal deduction, unless limited by account or document context | 0% | 0% BTW co-contracting (Merchandise/handelsgoederen) |
| 39 | `21% S.Cocont` | 21% | Services | Co-contracting | Normal deduction, unless limited by account or document context | 21% | 21% BTW co-contracting (Services/diensten) |
| 40 | `12% S.Cocont` | 12% | Services | Co-contracting | Normal deduction, unless limited by account or document context | 12% | 12% BTW co-contracting (Services/diensten) |
| 41 | `6% S.Cocont` | 6% | Services | Co-contracting | Normal deduction, unless limited by account or document context | 6% | 6% BTW co-contracting (Services/diensten) |
| 42 | `0% S.Cocont` | 0% | Services | Co-contracting | Normal deduction, unless limited by account or document context | 0% | 0% BTW co-contracting (Services/diensten) |
| 43 | `21% IG.Cocont` | 21% | Investment goods | Co-contracting | Normal deduction, unless limited by account or document context | 21% | 21% BTW co-contracting (Investment Goods/investeringsgoederen) |
| 44 | `12% IG.Cocont` | 12% | Investment goods | Co-contracting | Normal deduction, unless limited by account or document context | 12% | 12% BTW co-contracting (Investment Goods/investeringsgoederen) |
| 45 | `6% IG.Cocont` | 6% | Investment goods | Co-contracting | Normal deduction, unless limited by account or document context | 6% | 6% BTW co-contracting (Investment Goods/investeringsgoederen) |
| 46 | `0% IG.Cocont` | 0% | Investment goods | Co-contracting | Normal deduction, unless limited by account or document context | 0% | 0% BTW co-contracting (Investment Goods/investeringsgoederen) |
| 47 | `21% G D50` | 21% | Goods | Domestic / standard | 50% deductible | 21% | 21% VAT on goods / miscellaneous goods with 50% deduction |
| 48 | `21% G D35` | 21% | Services | Domestic / standard | 35% deductible | 21% | 21% VAT on goods / miscellaneous goods with 35% deduction |
| 49 | `21% IG D35` | 21% | Investment goods | Domestic / standard | 35% deductible | 21% | 21% BTW (Investment goods/investeringsgoederen) with 35% deduction |
| 50 | `21% S D85` | 21% | Services | Domestic / standard | 85% deductible | 21% | 21% VAT on services with 85% deduction |
| 50 | `21% S D75` | 21% | Services | Domestic / standard | 75% deductible | 21% | 21% VAT on services with 75% deduction |
| 51 | `21% EU M` | 21% | Goods | Intra-Community | Normal deduction, unless limited by account or document context | 21% | 21% BTW intra-Community (Merchandise/handelsgoederen) |
| 52 | `12% EU M` | 12% | Goods | Intra-Community | Normal deduction, unless limited by account or document context | 12% | 12% BTW intra-Community (Merchandise/handelsgoederen) |
| 53 | `6% EU M` | 6% | Goods | Intra-Community | Normal deduction, unless limited by account or document context | 6% | 6% intra-Community (Merchandise/handelsgoederen) |
| 54 | `0% EU M` | 0% | Goods | Intra-Community | Normal deduction, unless limited by account or document context | 0% | 0% intra-Community (Merchandise/handelsgoederen) |
| 55 | `21% EU S` | 21% | Services | Intra-Community | Normal deduction, unless limited by account or document context | 21% | 21% intra-Community (Services/diensten) |
| 56 | `12% EU S` | 12% | Services | Intra-Community | Normal deduction, unless limited by account or document context | 12% | 12% intra-Community (Services/diensten) |
| 57 | `6% EU S` | 6% | Services | Intra-Community | Normal deduction, unless limited by account or document context | 6% | 6% intra-Community (Services/diensten) |
| 57 | `0% EU S` | 0% | Services | Intra-Community | Normal deduction, unless limited by account or document context | 0% | 0% intra-Community (Services/diensten) |
| 57 | `21% EU G` | 21% | Goods | Intra-Community | Normal deduction, unless limited by account or document context | 21% | 21% intra-Community (Goods/diverse goederen) |
| 57 | `12% EU G` | 12% | Goods | Intra-Community | Normal deduction, unless limited by account or document context | 12% | 12% intra-Community (Goods/diverse goederen) |
| 57 | `6% EU G` | 6% | Goods | Intra-Community | Normal deduction, unless limited by account or document context | 6% | 6% intra-Community (Goods/diverse goederen) |
| 57 | `0% EU G` | 0% | Goods | Intra-Community | Normal deduction, unless limited by account or document context | 0% | 0% intra-Community (Goods/diverse goederen) |
| 57 | `21% EU IG` | 21% | Investment goods | Intra-Community | Normal deduction, unless limited by account or document context | 21% | 21% intra-Community (Investment Goods/investeringsgoederen) |
| 57 | `12% EU IG` | 12% | Investment goods | Intra-Community | Normal deduction, unless limited by account or document context | 12% | 12% intra-Community (Investment Goods/investeringsgoederen) |
| 57 | `6% EU IG` | 6% | Investment goods | Intra-Community | Normal deduction, unless limited by account or document context | 6% | 6% intra-Community (Investment Goods/investeringsgoederen) |
| 57 | `0% EU IG` | 0% | Investment goods | Intra-Community | Normal deduction, unless limited by account or document context | 0% | 0% intra-Community (Investment Goods/investeringsgoederen) |
| 57 | `21% EX M` | 21% | Goods | Intra-Community | Normal deduction, unless limited by account or document context | 21% | 21% extra-Community (Merchandise/handelsgoederen)(outside EU) |
| 57 | `12% EX M` | 12% | Goods | Intra-Community | Normal deduction, unless limited by account or document context | 12% | 12% extra-Community (Merchandise/handelsgoederen)(outside EU) |
| 57 | `6% EX M` | 6% | Goods | Intra-Community | Normal deduction, unless limited by account or document context | 6% | 6% extra-Community (Merchandise/handelsgoederen)(outside EU) |
| 57 | `0% EX M` | 0% | Goods | Intra-Community | Normal deduction, unless limited by account or document context | 0% | 0% extra-Community (Merchandise/handelsgoederen)(outside EU) |
| 57 | `21% EX S` | 21% | Services | Intra-Community | Normal deduction, unless limited by account or document context | 21% | 21% extra-Community (Services/diensten)(outside EU) |
| 57 | `12% EX S` | 12% | Services | Intra-Community | Normal deduction, unless limited by account or document context | 12% | 12% extra-Community (Services/diensten)(outside EU) |
| 57 | `6% EX S` | 6% | Services | Intra-Community | Normal deduction, unless limited by account or document context | 6% | 6% extra-Community (Services/diensten)(outside EU) |
| 57 | `0% EX S` | 0% | Services | Intra-Community | Normal deduction, unless limited by account or document context | 0% | 0% extra-Community (Services/diensten)(outside EU) |
| 57 | `21% EX IG` | 21% | Investment goods | Intra-Community | Normal deduction, unless limited by account or document context | 21% | 21% extra-Community (Investment Goods/investeringsgoederen)(outside EU) |
| 57 | `12% EX IG` | 12% | Investment goods | Intra-Community | Normal deduction, unless limited by account or document context | 12% | 12% extra-Community (Investment Goods/investeringsgoederen)(outside EU) |
| 57 | `6% EX IG` | 6% | Investment goods | Intra-Community | Normal deduction, unless limited by account or document context | 6% | 6% extra-Community (Investment Goods/investeringsgoederen)(outside EU) |
| 57 | `0% EX IG` | 0% | Investment goods | Intra-Community | Normal deduction, unless limited by account or document context | 0% | 0% extra-Community (Investment Goods/investeringsgoederen)(outside EU) |
| 58 | `21% EU G D35 already in Belgium` | 21% | Goods | Intra-Community | Normal deduction, unless limited by account or document context | 21% | 21% BTW intra-Community 35% deductionbaar (goederen reeds in België) |

## Machine-readable compact list

```json
[
  {
    "sequence": 10,
    "odoo_tax_name": "21%",
    "rate": 21,
    "description_original": "21% BTW op verkopen",
    "description_en": "21% VAT on sales",
    "tax_type": "Sales",
    "scope": "",
    "regime": "Domestic / standard",
    "deduction": "Normal deduction, unless limited by account or document context",
    "invoice_label": "21%"
  },
  {
    "sequence": 11,
    "odoo_tax_name": "12%",
    "rate": 12,
    "description_original": "12% BTW op verkopen",
    "description_en": "12% VAT on sales",
    "tax_type": "Sales",
    "scope": "",
    "regime": "Domestic / standard",
    "deduction": "Normal deduction, unless limited by account or document context",
    "invoice_label": "12%"
  },
  {
    "sequence": 12,
    "odoo_tax_name": "6%",
    "rate": 6,
    "description_original": "6% BTW op verkopen",
    "description_en": "6% VAT on sales",
    "tax_type": "Sales",
    "scope": "",
    "regime": "Domestic / standard",
    "deduction": "Normal deduction, unless limited by account or document context",
    "invoice_label": "6%"
  },
  {
    "sequence": 13,
    "odoo_tax_name": "0%",
    "rate": 0,
    "description_original": "0% BTW op verkopen",
    "description_en": "0% VAT on sales",
    "tax_type": "Sales",
    "scope": "",
    "regime": "Domestic / standard",
    "deduction": "Normal deduction, unless limited by account or document context",
    "invoice_label": "0%"
  },
  {
    "sequence": 14,
    "odoo_tax_name": "0% Cocont",
    "rate": 0,
    "description_original": "0% Co-contracting",
    "description_en": "0% co-contracting",
    "tax_type": "Sales",
    "scope": "",
    "regime": "Co-contracting",
    "deduction": "Normal deduction, unless limited by account or document context",
    "invoice_label": "0%"
  },
  {
    "sequence": 15,
    "odoo_tax_name": "0% EU S",
    "rate": 0,
    "description_original": "0% Intra-Community (Services/diensten)",
    "description_en": "0% intra-Community (Services/diensten)",
    "tax_type": "Sales",
    "scope": "Services",
    "regime": "Intra-Community",
    "deduction": "Normal deduction, unless limited by account or document context",
    "invoice_label": "0%"
  },
  {
    "sequence": 16,
    "odoo_tax_name": "0% EU M",
    "rate": 0,
    "description_original": "0% Intra-Community (Goods/Alle goederen)",
    "description_en": "0% intra-Community (Goods/all goods)",
    "tax_type": "Sales",
    "scope": "Goods",
    "regime": "Intra-Community",
    "deduction": "Normal deduction, unless limited by account or document context",
    "invoice_label": "0%"
  },
  {
    "sequence": 17,
    "odoo_tax_name": "0% EU T",
    "rate": 0,
    "description_original": "0% Intra-Community (Triangular)",
    "description_en": "0% intra-Community (Triangular)",
    "tax_type": "Sales",
    "scope": "Services",
    "regime": "Intra-Community",
    "deduction": "Normal deduction, unless limited by account or document context",
    "invoice_label": "0%"
  },
  {
    "sequence": 18,
    "odoo_tax_name": "0% EX",
    "rate": 0,
    "description_original": "0% Extra-Community (buiten EU)",
    "description_en": "0% extra-Community (outside EU)",
    "tax_type": "Sales",
    "scope": "",
    "regime": "Intra-Community",
    "deduction": "Normal deduction, unless limited by account or document context",
    "invoice_label": "0%"
  },
  {
    "sequence": 19,
    "odoo_tax_name": "21% M",
    "rate": 21,
    "description_original": "21% BTW (Merchandise/handelsgoederen)",
    "description_en": "21% VAT on merchandise / goods for resale",
    "tax_type": "Purchase",
    "scope": "Goods",
    "regime": "Domestic / standard",
    "deduction": "Normal deduction, unless limited by account or document context",
    "invoice_label": "21%"
  },
  {
    "sequence": 20,
    "odoo_tax_name": "12% M",
    "rate": 12,
    "description_original": "12% BTW (Merchandise/handelsgoederen)",
    "description_en": "12% VAT on merchandise / goods for resale",
    "tax_type": "Purchase",
    "scope": "Goods",
    "regime": "Domestic / standard",
    "deduction": "Normal deduction, unless limited by account or document context",
    "invoice_label": "12%"
  },
  {
    "sequence": 21,
    "odoo_tax_name": "6% M",
    "rate": 6,
    "description_original": "6% BTW (Merchandise/handelsgoederen)",
    "description_en": "6% VAT on merchandise / goods for resale",
    "tax_type": "Purchase",
    "scope": "Goods",
    "regime": "Domestic / standard",
    "deduction": "Normal deduction, unless limited by account or document context",
    "invoice_label": "6%"
  },
  {
    "sequence": 22,
    "odoo_tax_name": "0% M",
    "rate": 0,
    "description_original": "0% BTW (Merchandise/handelsgoederen)",
    "description_en": "0% VAT on merchandise / goods for resale",
    "tax_type": "Purchase",
    "scope": "Goods",
    "regime": "Domestic / standard",
    "deduction": "Normal deduction, unless limited by account or document context",
    "invoice_label": "0%"
  },
  {
    "sequence": 23,
    "odoo_tax_name": "21% S",
    "rate": 21,
    "description_original": "21% BTW (Services/diensten)",
    "description_en": "21% VAT on services",
    "tax_type": "Purchase",
    "scope": "Services",
    "regime": "Domestic / standard",
    "deduction": "Normal deduction, unless limited by account or document context",
    "invoice_label": "21%"
  },
  {
    "sequence": 24,
    "odoo_tax_name": "21% G",
    "rate": 21,
    "description_original": "21% BTW (Goods/diverse goederen)",
    "description_en": "21% VAT on goods / miscellaneous goods",
    "tax_type": "Purchase",
    "scope": "Goods",
    "regime": "Domestic / standard",
    "deduction": "Normal deduction, unless limited by account or document context",
    "invoice_label": "21%"
  },
  {
    "sequence": 25,
    "odoo_tax_name": "12% S",
    "rate": 12,
    "description_original": "12% BTW (Services/diensten)",
    "description_en": "12% VAT on services",
    "tax_type": "Purchase",
    "scope": "Services",
    "regime": "Domestic / standard",
    "deduction": "Normal deduction, unless limited by account or document context",
    "invoice_label": "12%"
  },
  {
    "sequence": 26,
    "odoo_tax_name": "12% G",
    "rate": 12,
    "description_original": "12% BTW (Goods/diverse goederen)",
    "description_en": "12% VAT on goods / miscellaneous goods",
    "tax_type": "Purchase",
    "scope": "Goods",
    "regime": "Domestic / standard",
    "deduction": "Normal deduction, unless limited by account or document context",
    "invoice_label": "12%"
  },
  {
    "sequence": 27,
    "odoo_tax_name": "6% S",
    "rate": 6,
    "description_original": "12% BTW (Services/diensten)",
    "description_en": "12% VAT on services",
    "tax_type": "Purchase",
    "scope": "Services",
    "regime": "Domestic / standard",
    "deduction": "Normal deduction, unless limited by account or document context",
    "invoice_label": "6%"
  },
  {
    "sequence": 28,
    "odoo_tax_name": "6% G",
    "rate": 6,
    "description_original": "6% BTW (Goods/diverse goederen)",
    "description_en": "6% VAT on goods / miscellaneous goods",
    "tax_type": "Purchase",
    "scope": "Goods",
    "regime": "Domestic / standard",
    "deduction": "Normal deduction, unless limited by account or document context",
    "invoice_label": "6%"
  },
  {
    "sequence": 29,
    "odoo_tax_name": "0% S",
    "rate": 0,
    "description_original": "0% BTW (Services/diensten)",
    "description_en": "0% VAT on services",
    "tax_type": "Purchase",
    "scope": "Services",
    "regime": "Domestic / standard",
    "deduction": "Normal deduction, unless limited by account or document context",
    "invoice_label": "0%"
  },
  {
    "sequence": 30,
    "odoo_tax_name": "0% G",
    "rate": 0,
    "description_original": "0% BTW (Goods/diverse goederen)",
    "description_en": "0% VAT on goods / miscellaneous goods",
    "tax_type": "Purchase",
    "scope": "Goods",
    "regime": "Domestic / standard",
    "deduction": "Normal deduction, unless limited by account or document context",
    "invoice_label": "0%"
  },
  {
    "sequence": 31,
    "odoo_tax_name": "21% IG",
    "rate": 21,
    "description_original": "21% BTW (Investment Goods/investeringsgoederen)",
    "description_en": "21% VAT on investment goods",
    "tax_type": "Purchase",
    "scope": "Investment goods",
    "regime": "Domestic / standard",
    "deduction": "Normal deduction, unless limited by account or document context",
    "invoice_label": "21%"
  },
  {
    "sequence": 32,
    "odoo_tax_name": "12% IG",
    "rate": 12,
    "description_original": "12% BTW (Investment Goods/investeringsgoederen)",
    "description_en": "12% VAT on investment goods",
    "tax_type": "Purchase",
    "scope": "Investment goods",
    "regime": "Domestic / standard",
    "deduction": "Normal deduction, unless limited by account or document context",
    "invoice_label": "12%"
  },
  {
    "sequence": 33,
    "odoo_tax_name": "6% IG",
    "rate": 6,
    "description_original": "6% BTW (Investment Goods/investeringsgoederen)",
    "description_en": "6% VAT on investment goods",
    "tax_type": "Purchase",
    "scope": "Investment goods",
    "regime": "Domestic / standard",
    "deduction": "Normal deduction, unless limited by account or document context",
    "invoice_label": "6%"
  },
  {
    "sequence": 34,
    "odoo_tax_name": "0% IG",
    "rate": 0,
    "description_original": "0% BTW (Investment Goods/investeringsgoederen)",
    "description_en": "0% VAT on investment goods",
    "tax_type": "Purchase",
    "scope": "",
    "regime": "Domestic / standard",
    "deduction": "Normal deduction, unless limited by account or document context",
    "invoice_label": "0%"
  },
  {
    "sequence": 35,
    "odoo_tax_name": "21% M.Cocont",
    "rate": 21,
    "description_original": "21% BTW Co-contracting (Merchandise/handelsgoederen)",
    "description_en": "21% BTW co-contracting (Merchandise/handelsgoederen)",
    "tax_type": "Purchase",
    "scope": "Goods",
    "regime": "Co-contracting",
    "deduction": "Normal deduction, unless limited by account or document context",
    "invoice_label": "21%"
  },
  {
    "sequence": 36,
    "odoo_tax_name": "12% M.Cocont",
    "rate": 12,
    "description_original": "12% BTW Co-contracting (Merchandise/handelsgoederen)",
    "description_en": "12% BTW co-contracting (Merchandise/handelsgoederen)",
    "tax_type": "Purchase",
    "scope": "Goods",
    "regime": "Co-contracting",
    "deduction": "Normal deduction, unless limited by account or document context",
    "invoice_label": "12%"
  },
  {
    "sequence": 37,
    "odoo_tax_name": "6% M.Cocont",
    "rate": 6,
    "description_original": "6% BTW Co-contracting (Merchandise/handelsgoederen)",
    "description_en": "6% BTW co-contracting (Merchandise/handelsgoederen)",
    "tax_type": "Purchase",
    "scope": "Goods",
    "regime": "Co-contracting",
    "deduction": "Normal deduction, unless limited by account or document context",
    "invoice_label": "6%"
  },
  {
    "sequence": 38,
    "odoo_tax_name": "0% M.Cocont",
    "rate": 0,
    "description_original": "0% BTW Co-contracting (Merchandise/handelsgoederen)",
    "description_en": "0% BTW co-contracting (Merchandise/handelsgoederen)",
    "tax_type": "Purchase",
    "scope": "Goods",
    "regime": "Co-contracting",
    "deduction": "Normal deduction, unless limited by account or document context",
    "invoice_label": "0%"
  },
  {
    "sequence": 39,
    "odoo_tax_name": "21% S.Cocont",
    "rate": 21,
    "description_original": "21% BTW Co-contracting (Services/diensten)",
    "description_en": "21% BTW co-contracting (Services/diensten)",
    "tax_type": "Purchase",
    "scope": "Services",
    "regime": "Co-contracting",
    "deduction": "Normal deduction, unless limited by account or document context",
    "invoice_label": "21%"
  },
  {
    "sequence": 40,
    "odoo_tax_name": "12% S.Cocont",
    "rate": 12,
    "description_original": "12% BTW Co-contracting (Services/diensten)",
    "description_en": "12% BTW co-contracting (Services/diensten)",
    "tax_type": "Purchase",
    "scope": "Services",
    "regime": "Co-contracting",
    "deduction": "Normal deduction, unless limited by account or document context",
    "invoice_label": "12%"
  },
  {
    "sequence": 41,
    "odoo_tax_name": "6% S.Cocont",
    "rate": 6,
    "description_original": "6% BTW Co-contracting (Services/diensten)",
    "description_en": "6% BTW co-contracting (Services/diensten)",
    "tax_type": "Purchase",
    "scope": "Services",
    "regime": "Co-contracting",
    "deduction": "Normal deduction, unless limited by account or document context",
    "invoice_label": "6%"
  },
  {
    "sequence": 42,
    "odoo_tax_name": "0% S.Cocont",
    "rate": 0,
    "description_original": "0% BTW Co-contracting (Services/diensten)",
    "description_en": "0% BTW co-contracting (Services/diensten)",
    "tax_type": "Purchase",
    "scope": "Services",
    "regime": "Co-contracting",
    "deduction": "Normal deduction, unless limited by account or document context",
    "invoice_label": "0%"
  },
  {
    "sequence": 43,
    "odoo_tax_name": "21% IG.Cocont",
    "rate": 21,
    "description_original": "21% BTW Co-contracting (Investment Goods/investeringsgoederen)",
    "description_en": "21% BTW co-contracting (Investment Goods/investeringsgoederen)",
    "tax_type": "Purchase",
    "scope": "Investment goods",
    "regime": "Co-contracting",
    "deduction": "Normal deduction, unless limited by account or document context",
    "invoice_label": "21%"
  },
  {
    "sequence": 44,
    "odoo_tax_name": "12% IG.Cocont",
    "rate": 12,
    "description_original": "12% BTW Co-contracting (Investment Goods/investeringsgoederen)",
    "description_en": "12% BTW co-contracting (Investment Goods/investeringsgoederen)",
    "tax_type": "Purchase",
    "scope": "Investment goods",
    "regime": "Co-contracting",
    "deduction": "Normal deduction, unless limited by account or document context",
    "invoice_label": "12%"
  },
  {
    "sequence": 45,
    "odoo_tax_name": "6% IG.Cocont",
    "rate": 6,
    "description_original": "6% BTW Co-contracting (Investment Goods/investeringsgoederen)",
    "description_en": "6% BTW co-contracting (Investment Goods/investeringsgoederen)",
    "tax_type": "Purchase",
    "scope": "Investment goods",
    "regime": "Co-contracting",
    "deduction": "Normal deduction, unless limited by account or document context",
    "invoice_label": "6%"
  },
  {
    "sequence": 46,
    "odoo_tax_name": "0% IG.Cocont",
    "rate": 0,
    "description_original": "0% BTW Co-contracting (Investment Goods/investeringsgoederen)",
    "description_en": "0% BTW co-contracting (Investment Goods/investeringsgoederen)",
    "tax_type": "Purchase",
    "scope": "Investment goods",
    "regime": "Co-contracting",
    "deduction": "Normal deduction, unless limited by account or document context",
    "invoice_label": "0%"
  },
  {
    "sequence": 47,
    "odoo_tax_name": "21% G D50",
    "rate": 21,
    "description_original": "21% BTW (Goods/diverse goederen) met 50% aftrek",
    "description_en": "21% VAT on goods / miscellaneous goods with 50% deduction",
    "tax_type": "Purchase",
    "scope": "Goods",
    "regime": "Domestic / standard",
    "deduction": "50% deductible",
    "invoice_label": "21%"
  },
  {
    "sequence": 48,
    "odoo_tax_name": "21% G D35",
    "rate": 21,
    "description_original": "21% BTW (Goods/diverse goederen) met 35% aftrek",
    "description_en": "21% VAT on goods / miscellaneous goods with 35% deduction",
    "tax_type": "Purchase",
    "scope": "Services",
    "regime": "Domestic / standard",
    "deduction": "35% deductible",
    "invoice_label": "21%"
  },
  {
    "sequence": 49,
    "odoo_tax_name": "21% IG D35",
    "rate": 21,
    "description_original": "21% BTW (Investment goods/investeringsgoederen) met 35% aftrek",
    "description_en": "21% BTW (Investment goods/investeringsgoederen) with 35% deduction",
    "tax_type": "Purchase",
    "scope": "Investment goods",
    "regime": "Domestic / standard",
    "deduction": "35% deductible",
    "invoice_label": "21%"
  },
  {
    "sequence": 50,
    "odoo_tax_name": "21% S D85",
    "rate": 21,
    "description_original": "21% BTW (Services/diensten) met 85% aftrek",
    "description_en": "21% VAT on services with 85% deduction",
    "tax_type": "Purchase",
    "scope": "Services",
    "regime": "Domestic / standard",
    "deduction": "85% deductible",
    "invoice_label": "21%"
  },
  {
    "sequence": 50,
    "odoo_tax_name": "21% S D75",
    "rate": 21,
    "description_original": "21% BTW (Services/diensten) met 75% aftrek",
    "description_en": "21% VAT on services with 75% deduction",
    "tax_type": "Purchase",
    "scope": "Services",
    "regime": "Domestic / standard",
    "deduction": "75% deductible",
    "invoice_label": "21%"
  },
  {
    "sequence": 51,
    "odoo_tax_name": "21% EU M",
    "rate": 21,
    "description_original": "21% BTW Intra-Community (Merchandise/handelsgoederen)",
    "description_en": "21% BTW intra-Community (Merchandise/handelsgoederen)",
    "tax_type": "Purchase",
    "scope": "Goods",
    "regime": "Intra-Community",
    "deduction": "Normal deduction, unless limited by account or document context",
    "invoice_label": "21%"
  },
  {
    "sequence": 52,
    "odoo_tax_name": "12% EU M",
    "rate": 12,
    "description_original": "12% BTW Intra-Community (Merchandise/handelsgoederen)",
    "description_en": "12% BTW intra-Community (Merchandise/handelsgoederen)",
    "tax_type": "Purchase",
    "scope": "Goods",
    "regime": "Intra-Community",
    "deduction": "Normal deduction, unless limited by account or document context",
    "invoice_label": "12%"
  },
  {
    "sequence": 53,
    "odoo_tax_name": "6% EU M",
    "rate": 6,
    "description_original": "6% Intra-Community (Merchandise/handelsgoederen)",
    "description_en": "6% intra-Community (Merchandise/handelsgoederen)",
    "tax_type": "Purchase",
    "scope": "Goods",
    "regime": "Intra-Community",
    "deduction": "Normal deduction, unless limited by account or document context",
    "invoice_label": "6%"
  },
  {
    "sequence": 54,
    "odoo_tax_name": "0% EU M",
    "rate": 0,
    "description_original": "0% Intra-Community (Merchandise/handelsgoederen)",
    "description_en": "0% intra-Community (Merchandise/handelsgoederen)",
    "tax_type": "Purchase",
    "scope": "Goods",
    "regime": "Intra-Community",
    "deduction": "Normal deduction, unless limited by account or document context",
    "invoice_label": "0%"
  },
  {
    "sequence": 55,
    "odoo_tax_name": "21% EU S",
    "rate": 21,
    "description_original": "21% Intra-Community (Services/diensten)",
    "description_en": "21% intra-Community (Services/diensten)",
    "tax_type": "Purchase",
    "scope": "Services",
    "regime": "Intra-Community",
    "deduction": "Normal deduction, unless limited by account or document context",
    "invoice_label": "21%"
  },
  {
    "sequence": 56,
    "odoo_tax_name": "12% EU S",
    "rate": 12,
    "description_original": "12% Intra-Community (Services/diensten)",
    "description_en": "12% intra-Community (Services/diensten)",
    "tax_type": "Purchase",
    "scope": "Services",
    "regime": "Intra-Community",
    "deduction": "Normal deduction, unless limited by account or document context",
    "invoice_label": "12%"
  },
  {
    "sequence": 57,
    "odoo_tax_name": "6% EU S",
    "rate": 6,
    "description_original": "6% Intra-Community (Services/diensten)",
    "description_en": "6% intra-Community (Services/diensten)",
    "tax_type": "Purchase",
    "scope": "Services",
    "regime": "Intra-Community",
    "deduction": "Normal deduction, unless limited by account or document context",
    "invoice_label": "6%"
  },
  {
    "sequence": 57,
    "odoo_tax_name": "0% EU S",
    "rate": 0,
    "description_original": "0% Intra-Community (Services/diensten)",
    "description_en": "0% intra-Community (Services/diensten)",
    "tax_type": "Purchase",
    "scope": "Services",
    "regime": "Intra-Community",
    "deduction": "Normal deduction, unless limited by account or document context",
    "invoice_label": "0%"
  },
  {
    "sequence": 57,
    "odoo_tax_name": "21% EU G",
    "rate": 21,
    "description_original": "21% Intra-Community (Goods/diverse goederen)",
    "description_en": "21% intra-Community (Goods/diverse goederen)",
    "tax_type": "Purchase",
    "scope": "Goods",
    "regime": "Intra-Community",
    "deduction": "Normal deduction, unless limited by account or document context",
    "invoice_label": "21%"
  },
  {
    "sequence": 57,
    "odoo_tax_name": "12% EU G",
    "rate": 12,
    "description_original": "12% Intra-Community (Goods/diverse goederen)",
    "description_en": "12% intra-Community (Goods/diverse goederen)",
    "tax_type": "Purchase",
    "scope": "Goods",
    "regime": "Intra-Community",
    "deduction": "Normal deduction, unless limited by account or document context",
    "invoice_label": "12%"
  },
  {
    "sequence": 57,
    "odoo_tax_name": "6% EU G",
    "rate": 6,
    "description_original": "6% Intra-Community (Goods/diverse goederen)",
    "description_en": "6% intra-Community (Goods/diverse goederen)",
    "tax_type": "Purchase",
    "scope": "Goods",
    "regime": "Intra-Community",
    "deduction": "Normal deduction, unless limited by account or document context",
    "invoice_label": "6%"
  },
  {
    "sequence": 57,
    "odoo_tax_name": "0% EU G",
    "rate": 0,
    "description_original": "0% Intra-Community (Goods/diverse goederen)",
    "description_en": "0% intra-Community (Goods/diverse goederen)",
    "tax_type": "Purchase",
    "scope": "Goods",
    "regime": "Intra-Community",
    "deduction": "Normal deduction, unless limited by account or document context",
    "invoice_label": "0%"
  },
  {
    "sequence": 57,
    "odoo_tax_name": "21% EU IG",
    "rate": 21,
    "description_original": "21% Intra-Community (Investment Goods/investeringsgoederen)",
    "description_en": "21% intra-Community (Investment Goods/investeringsgoederen)",
    "tax_type": "Purchase",
    "scope": "Investment goods",
    "regime": "Intra-Community",
    "deduction": "Normal deduction, unless limited by account or document context",
    "invoice_label": "21%"
  },
  {
    "sequence": 57,
    "odoo_tax_name": "12% EU IG",
    "rate": 12,
    "description_original": "12% Intra-Community (Investment Goods/investeringsgoederen)",
    "description_en": "12% intra-Community (Investment Goods/investeringsgoederen)",
    "tax_type": "Purchase",
    "scope": "Investment goods",
    "regime": "Intra-Community",
    "deduction": "Normal deduction, unless limited by account or document context",
    "invoice_label": "12%"
  },
  {
    "sequence": 57,
    "odoo_tax_name": "6% EU IG",
    "rate": 6,
    "description_original": "6% Intra-Community (Investment Goods/investeringsgoederen)",
    "description_en": "6% intra-Community (Investment Goods/investeringsgoederen)",
    "tax_type": "Purchase",
    "scope": "Investment goods",
    "regime": "Intra-Community",
    "deduction": "Normal deduction, unless limited by account or document context",
    "invoice_label": "6%"
  },
  {
    "sequence": 57,
    "odoo_tax_name": "0% EU IG",
    "rate": 0,
    "description_original": "0% Intra-Community (Investment Goods/investeringsgoederen)",
    "description_en": "0% intra-Community (Investment Goods/investeringsgoederen)",
    "tax_type": "Purchase",
    "scope": "Investment goods",
    "regime": "Intra-Community",
    "deduction": "Normal deduction, unless limited by account or document context",
    "invoice_label": "0%"
  },
  {
    "sequence": 57,
    "odoo_tax_name": "21% EX M",
    "rate": 21,
    "description_original": "21% Extra-Community (Merchandise/handelsgoederen)(buiten EU)",
    "description_en": "21% extra-Community (Merchandise/handelsgoederen)(outside EU)",
    "tax_type": "Purchase",
    "scope": "Goods",
    "regime": "Intra-Community",
    "deduction": "Normal deduction, unless limited by account or document context",
    "invoice_label": "21%"
  },
  {
    "sequence": 57,
    "odoo_tax_name": "12% EX M",
    "rate": 12,
    "description_original": "12% Extra-Community (Merchandise/handelsgoederen)(buiten EU)",
    "description_en": "12% extra-Community (Merchandise/handelsgoederen)(outside EU)",
    "tax_type": "Purchase",
    "scope": "Goods",
    "regime": "Intra-Community",
    "deduction": "Normal deduction, unless limited by account or document context",
    "invoice_label": "12%"
  },
  {
    "sequence": 57,
    "odoo_tax_name": "6% EX M",
    "rate": 6,
    "description_original": "6% Extra-Community (Merchandise/handelsgoederen)(buiten EU)",
    "description_en": "6% extra-Community (Merchandise/handelsgoederen)(outside EU)",
    "tax_type": "Purchase",
    "scope": "Goods",
    "regime": "Intra-Community",
    "deduction": "Normal deduction, unless limited by account or document context",
    "invoice_label": "6%"
  },
  {
    "sequence": 57,
    "odoo_tax_name": "0% EX M",
    "rate": 0,
    "description_original": "0% Extra-Community (Merchandise/handelsgoederen)(buiten EU)",
    "description_en": "0% extra-Community (Merchandise/handelsgoederen)(outside EU)",
    "tax_type": "Purchase",
    "scope": "Goods",
    "regime": "Intra-Community",
    "deduction": "Normal deduction, unless limited by account or document context",
    "invoice_label": "0%"
  },
  {
    "sequence": 57,
    "odoo_tax_name": "21% EX S",
    "rate": 21,
    "description_original": "21% Extra-Community (Services/diensten)(buiten EU)",
    "description_en": "21% extra-Community (Services/diensten)(outside EU)",
    "tax_type": "Purchase",
    "scope": "Services",
    "regime": "Intra-Community",
    "deduction": "Normal deduction, unless limited by account or document context",
    "invoice_label": "21%"
  },
  {
    "sequence": 57,
    "odoo_tax_name": "12% EX S",
    "rate": 12,
    "description_original": "12% Extra-Community (Services/diensten)(buiten EU)",
    "description_en": "12% extra-Community (Services/diensten)(outside EU)",
    "tax_type": "Purchase",
    "scope": "Services",
    "regime": "Intra-Community",
    "deduction": "Normal deduction, unless limited by account or document context",
    "invoice_label": "12%"
  },
  {
    "sequence": 57,
    "odoo_tax_name": "6% EX S",
    "rate": 6,
    "description_original": "6% Extra-Community (Services/diensten)(buiten EU)",
    "description_en": "6% extra-Community (Services/diensten)(outside EU)",
    "tax_type": "Purchase",
    "scope": "Services",
    "regime": "Intra-Community",
    "deduction": "Normal deduction, unless limited by account or document context",
    "invoice_label": "6%"
  },
  {
    "sequence": 57,
    "odoo_tax_name": "0% EX S",
    "rate": 0,
    "description_original": "0% Extra-Community (Services/diensten)(buiten EU)",
    "description_en": "0% extra-Community (Services/diensten)(outside EU)",
    "tax_type": "Purchase",
    "scope": "Services",
    "regime": "Intra-Community",
    "deduction": "Normal deduction, unless limited by account or document context",
    "invoice_label": "0%"
  },
  {
    "sequence": 57,
    "odoo_tax_name": "21% EX IG",
    "rate": 21,
    "description_original": "21% Extra-Community (Investment Goods/investeringsgoederen)(buiten EU)",
    "description_en": "21% extra-Community (Investment Goods/investeringsgoederen)(outside EU)",
    "tax_type": "Purchase",
    "scope": "Investment goods",
    "regime": "Intra-Community",
    "deduction": "Normal deduction, unless limited by account or document context",
    "invoice_label": "21%"
  },
  {
    "sequence": 57,
    "odoo_tax_name": "12% EX IG",
    "rate": 12,
    "description_original": "12% Extra-Community (Investment Goods/investeringsgoederen)(buiten EU)",
    "description_en": "12% extra-Community (Investment Goods/investeringsgoederen)(outside EU)",
    "tax_type": "Purchase",
    "scope": "Investment goods",
    "regime": "Intra-Community",
    "deduction": "Normal deduction, unless limited by account or document context",
    "invoice_label": "12%"
  },
  {
    "sequence": 57,
    "odoo_tax_name": "6% EX IG",
    "rate": 6,
    "description_original": "6% Extra-Community (Investment Goods/investeringsgoederen)(buiten EU)",
    "description_en": "6% extra-Community (Investment Goods/investeringsgoederen)(outside EU)",
    "tax_type": "Purchase",
    "scope": "Investment goods",
    "regime": "Intra-Community",
    "deduction": "Normal deduction, unless limited by account or document context",
    "invoice_label": "6%"
  },
  {
    "sequence": 57,
    "odoo_tax_name": "0% EX IG",
    "rate": 0,
    "description_original": "0% Extra-Community (Investment Goods/investeringsgoederen)(buiten EU)",
    "description_en": "0% extra-Community (Investment Goods/investeringsgoederen)(outside EU)",
    "tax_type": "Purchase",
    "scope": "Investment goods",
    "regime": "Intra-Community",
    "deduction": "Normal deduction, unless limited by account or document context",
    "invoice_label": "0%"
  },
  {
    "sequence": 58,
    "odoo_tax_name": "21% EU G D35 already in Belgium",
    "rate": 21,
    "description_original": "21% BTW Intra-Community 35% aftrekbaar (goederen reeds in België)",
    "description_en": "21% BTW intra-Community 35% deductionbaar (goederen reeds in België)",
    "tax_type": "Purchase",
    "scope": "Goods",
    "regime": "Intra-Community",
    "deduction": "Normal deduction, unless limited by account or document context",
    "invoice_label": "21%"
  }
]
```
