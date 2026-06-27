"""Fill account_code, account_name, and vat_code on invoice_lines in skeleton invoices."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "invoices" / "skeleton_invoices"

EU_COUNTRIES = {
    "AT", "BE", "BG", "HR", "CY", "CZ", "DK", "EE", "FI", "FR", "DE", "GR", "HU",
    "IE", "IT", "LV", "LT", "LU", "MT", "NL", "PL", "PT", "RO", "SK", "SI", "ES", "SE",
}

ACCOUNTS = {
    "612100": "IT services",
    "612050": "Administrative services",
    "612070": "Training",
    "618110": "Meal vouchers for director/manager",
    "615200": "Fees of bookkeepers and accountants",
    "616200": "Telephone and internet expenses",
    "616680": "Restaurant expenses",
    "616700": "Travel and accommodation expenses",
    "612600": "Fuel for company cars",
    "657100": "Bank charges",
    "604000": "Purchases of goods for resale",
    "607000": "Ancillary purchase costs",
    "611200": "Small equipment",
    "611000": "Office supplies and printing",
    "610700": "Maintenance and repairs of installations, machinery and equipment",
    "617000": "Temporary agency workers",
    "610101": "Business address costs",
    "613200": "Business risk insurance",
    "640000": "Business taxes",
    "611220": "Sector-specific materials",
}


def vat_code(
    *,
    country: str | None,
    reverse_charge: bool,
    vat_rate: float | None,
    scope: str,
) -> str:
    country = (country or "BE").upper()

    if country == "BE":
        if vat_rate in (21, 21.0):
            return f"21% {scope}"
        if vat_rate in (12, 12.0):
            return f"12% {scope}"
        if vat_rate in (6, 6.0):
            return f"6% {scope}"
        if vat_rate in (0, 0.0):
            return f"0% {scope}"
        if vat_rate is None:
            return ""
        return f"{int(vat_rate)}% {scope}" if float(vat_rate).is_integer() else f"{vat_rate}% {scope}"

    if reverse_charge or vat_rate in (0, 0.0, None):
        if country in EU_COUNTRIES:
            return f"21% EU {scope}"
        return f"21% EX {scope}"

    if vat_rate in (21, 21.0):
        return f"21% {scope}"
    if vat_rate in (12, 12.0):
        return f"12% {scope}"
    if vat_rate in (6, 6.0):
        return f"6% {scope}"
    return f"0% {scope}"


IT_SUPPLIERS = (
    "google", "notion", "github", "openai", "groq", "eleven labs", "livekit",
    "twilio", "combell", "microsoft", "stripe", "anthropic",
)


def line_booking(description: str, supplier: str, doc: dict) -> tuple[str, str]:
    desc = description.lower()
    supplier_l = (supplier or "").lower()
    doc_type = (doc.get("document") or {}).get("document_type", "")

    if any(name in supplier_l for name in IT_SUPPLIERS):
        return "612100", ACCOUNTS["612100"]
    if any(k in desc for k in ("smartwatch", "apple tv", "charger", "usb-c", "recupel", "environmental contribution", "auvibel")):
        return "611200", ACCOUNTS["611200"]
    if any(name in supplier_l for name in ("proximus", "telenet")):
        return "616200", ACCOUNTS["616200"]
    if any(k in desc for k in ("bundle klik", "telephony", "mobile subscription", "mobile data", "business flex", "business mobile", "proximus", "telenet")):
        return "616200", ACCOUNTS["616200"]
    if any(k in desc for k in ("subscription", "plan monthly", "per seat", "chatgpt", "workspace", "copilot", "api usage", "token")):
        return "612100", ACCOUNTS["612100"]
    if desc.strip() == "ship":
        return "612100", ACCOUNTS["612100"]

    if any(k in desc for k in ("accounting", "bookkeeping", "bookkeeper", "boekhouder")):
        return "615200", ACCOUNTS["615200"]
    if any(k in desc for k in ("monthly forfait", "debit card cost", "payment fee", "bank")) or "beobank" in supplier_l:
        return "657100", ACCOUNTS["657100"]
    if any(k in desc for k in ("wages and salaries", "dimona", "start-up cost", "administration costs")) and "interim" in supplier_l:
        return "617000", ACCOUNTS["617000"]
    if "travel costs" in desc and "interim" in supplier_l:
        return "617000", ACCOUNTS["617000"]
    if any(k in desc for k in ("municipal tax", "gemeentebelasting", "general municipal tax")):
        return "640000", ACCOUNTS["640000"]
    if any(k in desc for k in ("insurance excess", "franchise cost")):
        return "613200", ACCOUNTS["613200"]
    if "monizze" in supplier_l:
        if any(k in desc for k in ("meal voucher", "vouchers issued")):
            return "618110", ACCOUNTS["618110"]
        if any(k in desc for k in ("service cost", "recurrent service")):
            return "612050", ACCOUNTS["612050"]
    if "itaa" in supplier_l or "itaa registration" in desc:
        return "612070", ACCOUNTS["612070"]
    if any(k in desc for k in ("ticket", "train")) or doc_type == "travel_ticket_receipt":
        return "616700", ACCOUNTS["616700"]
    if any(k in desc for k in ("diesel", "adblue", "fuel", "petrol")):
        return "612600", ACCOUNTS["612600"]
    if any(k in desc for k in ("gauf", "mista", "gambas", "sepia", "negroni", "carolus", "spa 0.5")):
        return "616680", ACCOUNTS["616680"]
    if any(k in supplier_l for k in ("lire", "restaurant")):
        return "616680", ACCOUNTS["616680"]
    if any(k in desc for k in ("residual waste", "roll container", "waste", "emptying")):
        return "610101", ACCOUNTS["610101"]
    if "shipping" in desc or "service / shipping" in desc:
        return "607000", ACCOUNTS["607000"]
    if any(k in desc for k in ("toner", "cartridge")):
        return "611000", ACCOUNTS["611000"]
    if any(k in desc for k in ("window handle", "fixing screw", "sobinco")):
        return "610700", ACCOUNTS["610700"]
    if any(k in desc for k in ("kabel", "stopcontact", "o-ring", "transistor", "phoenix contact")):
        return "611220", ACCOUNTS["611220"]
    if any(k in desc for k in ("administrative and support", "administrative services")):
        return "612050", ACCOUNTS["612050"]
    if any(k in desc for k in (
        "google workspace", "notion", "github", "openai", "groq", "eleven labs", "livekit",
        "api", "copilot", "token", "subscription", "starter (per subscription)", "ship",
        "backup", "microsoft 365", "developer_early_access", "hosting",
    )):
        return "612100", ACCOUNTS["612100"]
    if "twilio" in supplier_l:
        return "612100", ACCOUNTS["612100"]
    if "combell" in supplier_l:
        return "612100", ACCOUNTS["612100"]
    return "604000", ACCOUNTS["604000"]


def line_scope(account_code: str, description: str) -> str:
    desc = description.lower()
    if account_code in {"604000"}:
        return "M"
    if account_code in {"607000", "611200", "611000", "611220", "610700", "612600"}:
        return "G"
    return "S"


def apply_to_invoice_lines(doc: dict) -> bool:
    supplier = (doc.get("supplier") or {}).get("legal_name") or ""
    country = (doc.get("supplier") or {}).get("country")
    reverse_charge = (doc.get("tax") or {}).get("reverse_charge", False)
    changed = False

    for line in doc.get("invoice_lines") or []:
        desc = line.get("description") or ""
        account_code, account_name = line_booking(desc, supplier, doc)
        scope = line_scope(account_code, desc)
        code = vat_code(
            country=country,
            reverse_charge=reverse_charge,
            vat_rate=line.get("vat_rate"),
            scope=scope,
        )
        if account_code == "640000":
            code = ""
        if account_code == "616680" and line.get("vat_rate") in (12, 12.0):
            code = "12% ND"
        if account_code == "616680" and line.get("vat_rate") in (21, 21.0):
            code = "21% ND"
        if account_code == "616680" and line.get("vat_rate") in (6, 6.0):
            code = "6% ND"
        if account_code == "616700" and line.get("vat_rate") is None:
            code = "6% S"
        if account_code == "612070":
            code = "0% S"
        if account_code == "618110":
            code = "0% S"
        if account_code == "612100" and country and country.upper() != "BE":
            if country.upper() in EU_COUNTRIES:
                code = "21% EU S"
            else:
                code = "21% EX S"
        if account_code == "612100" and reverse_charge and country and country.upper() == "BE":
            code = "21% S"

        new_values = {
            "account_code": account_code,
            "account_name": account_name,
            "vat_code": code,
        }
        for key, value in new_values.items():
            if line.get(key) != value:
                line[key] = value
                changed = True
    return changed


def process_file(path: Path) -> bool:
    if path.name in {"summary.json"}:
        return False

    with path.open(encoding="utf-8") as f:
        data = json.load(f)

    changed = False
    if isinstance(data, dict) and "documents" in data:
        for doc in data["documents"]:
            if apply_to_invoice_lines(doc):
                changed = True
    elif isinstance(data, dict) and "invoice_lines" in data:
        changed = apply_to_invoice_lines(data)
    elif isinstance(data, list):
        return False

    if changed:
        with path.open("w", encoding="utf-8", newline="\n") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
            f.write("\n")
    return changed


def main() -> None:
    files = sorted(ROOT.rglob("*.json"))
    updated = 0
    for path in files:
        if process_file(path):
            updated += 1
            print(f"updated: {path.relative_to(ROOT)}")
    print(f"Done. Updated {updated} of {len(files)} files.")


if __name__ == "__main__":
    main()
