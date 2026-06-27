# MAR knowledge base for automated bookkeeping

Source file: `MAR.xlsx`

Purpose: this document explains when a bookkeeping agent should select each Belgian MAR account. The wording is intentionally written as decision rules: first choose the most specific account, avoid catch-all accounts when a better account exists, and request additional context when the invoice, supplier or description is not clear enough.

## General decision rules

- Book a purchase on the account that reflects the economic nature of the cost, not only the supplier name.
- Distinguish direct costs for a customer, job or project from general operating costs. Direct costs usually belong in class 60; overhead usually belongs in class 61.
- Distinguish expenses from fixed assets. Goods or works that are used durably or increase the value of an asset should generally be capitalised instead of expensed immediately.
- Use car expense accounts only when the cost is linked to a vehicle. For passenger cars, VAT deduction and income tax deductibility must be assessed separately.
- Use director/manager accounts only for remuneration, benefits in kind, social security contributions and allowances for company directors/managers. Employee costs belong under 62/623.
- Use profit appropriation accounts only at year-end closing or after approval of the profit allocation. Do not use them for ordinary purchase invoices.
- When a document is not clear enough, mark the booking as `to be reviewed` instead of forcing a guessed account.

## 600000 Raw materials purchases

**Use when:** the business purchases goods that are physically or economically processed into an end product or service.

**Do not use for:** goods purchased for resale without processing, or materials purchased directly for a customer job or site. Those will usually be booked on `604000`.

**Agent rules:** choose this account only when the description points to production, processing or manufacturing. For ordinary purchases for resale or installation at the customer, `604000` is more likely.

## 603000 General subcontracting

**Use when:** an external party performs work that is directly part of a specific customer job, site, delivery or project.

**Examples:** self-employed subcontractors working on a site, hired execution work for an event, machinery or containers rented specifically for one customer job.

**Do not use for:** structural rental of machinery or materials that remain permanently available to the business. Use `610200` instead. Consultants supporting the internal organisation without a direct link to a customer job belong on `612300`.

**Agent rules:** if the cost should be included in the margin of a specific job, book it on `603000`. If the cost is general support or overhead, choose a class 61 account.

## 604000 Purchases of goods for resale

**Use when:** goods or materials are purchased to be resold, used in a customer job or left with the customer after completion.

**Examples:** materials for a site, products for resale, parts installed in a customer project.

**Do not use for:** subcontracting (`603000`), ancillary purchase costs such as transport and import costs (`607000`), or inventory movements (`609400`).

**Agent rules:** this is the default account for goods included in the sales margin. Do not create subaccounts unless there is a clear practical, analytical or tax reason. If one supplier delivers both goods and services, use invoice lines or descriptions to distinguish `603000` from `604000`.

**VAT:** in the travel sector or under a margin scheme, VAT on direct costs may be non-deductible. For intra-Community purchases or imports, determine the correct VAT code separately.

## 607000 Ancillary purchase costs

**Use when:** costs are directly linked to purchasing, importing, transporting, delivering or shipping goods for resale.

**Examples:** FedEx, DHL, DPD, PostNL, Bpost, import formalities, transport of goods to the business or from the business to the customer.

**Do not use for:** ordinary postage without a link to goods for resale. Use `611000` or another office/administrative account instead.

**Agent rules:** logistics costs from parcel and transport partners may be grouped here, even if the invoice contains both incoming and outgoing shipments. For imports from outside the EU, the invoice should ideally be linked to the import and customs document.

**VAT:** import VAT is deductible if the business has deduction rights and the import documents are available. If imports are frequent, an ET14000 permit may be relevant, but that is not an automatic booking rule.

## 609400 Inventory changes for goods for resale

**Use when:** inventory of goods for resale is adjusted periodically based on an inventory count.

**Do not use for:** ordinary purchase invoices or sales invoices.

**Agent rules:** book inventory changes only on the basis of a reliable inventory list provided by the client. Use this account to reverse the existing inventory and recognise the new inventory against `340000`.

## 610101 [street] [no.], [postcode] [city], [0.0%]

**Use when:** costs relate to a specific address used for business purposes.

**Examples:** rent, electricity, heating, water, maintenance, repairs, fit-out, municipal tax, provincial tax, property tax, fire insurance and waste collection for that address.

**Do not use for:** rental deposits (`288000`), major investment works or structural value-increasing renovations. Rent expenses that must be tracked for MLH270 belong on `610130`.

**Agent rules:** create a separate account per address and include the business-use percentage in the account name. Apply VAT deduction and expense deduction according to the business-use percentage. For mixed use or home office costs, the agent must not invent a percentage: request the calculation or use the configured percentage.

## 610130 Rent expenses MLH270

**Use when:** paid rent must be tracked for form MLH270 in the personal income tax or corporate income tax return.

**Do not use for:** B2B rent invoiced by another company when MLH270 reporting is not required. Such rent usually remains on the address account.

**Agent rules:** use this account for rent paid to individuals or directors/managers when MLH270 reporting is required. If rent is paid to two beneficiaries, both beneficiaries must be included in the tax follow-up.

## 610200 Rental expenses for installations, machinery and equipment

**Use when:** the business rents machinery, installations, materials or equipment for structural use.

**Examples:** forklift, scaffolding, copier, CNC machine, water dispenser, bicycle leasing, short-term vehicle rental, car-sharing.

**Do not use for:** rental of materials used exclusively for one site or customer job. Use `603000` instead.

**Agent rules:** for lease, renting or rental contracts, the agent should flag the interest component for reclassification to financial expenses at year-end. Passenger cars require VAT limitation and income tax deductibility checks.

## 610700 Maintenance and repairs of installations, machinery and equipment

**Use when:** costs are incurred to repair or keep existing machinery, installations or equipment operational.

**Do not use for:** improvements or extensions that substantially increase the value, capacity or useful life of an asset. Those belong in fixed assets.

**Agent rules:** words such as repair, maintenance, service, replacement part and service contract point to `610700`, unless the invoice clearly relates to a vehicle, building or software.

## 611000 Office supplies and printing

**Use when:** the purchase relates to general office supplies, printing, stationery or small administrative materials.

**Examples:** paper, folders, pens, printed matter, envelopes, postage stamps without a link to goods for resale, small office items.

**Do not use for:** marketing materials (`616610`), durable office equipment that must be capitalised, or shipping of goods for resale (`607000`).

**Agent rules:** this is the default account for small office and administrative consumables.

## 611001 Canteen expenses

**Use when:** the business purchases drinks, snacks or consumables for internal use by employees, directors/managers or visitors.

**Examples:** coffee, tea, water, milk, sugar, soft drinks, biscuits, fruit, small canteen supplies.

**Do not use for:** restaurant visits (`616680`), business gifts or hospitality with a commercial purpose (`616500`), or goods intended for resale.

**Agent rules:** if an invoice from a supermarket contains both canteen goods and other purchases, split the invoice lines where possible.

## 611200 Small equipment

**Use when:** small equipment is purchased and is not durable enough or material enough to be capitalised.

**Examples:** small accessories, simple devices, cables, adapters and other low-value tools.

**Do not use for:** tools and work clothing (`611210`), sector-specific consumables (`611220`) or equipment that must be capitalised under the file's policy.

**Agent rules:** when uncertain between expense and fixed asset, check value, useful life and the client's capitalisation policy.

## 611210 Tools and work clothing

**Use when:** the purchase relates to tools or professional clothing required to perform the work.

**Examples:** hand tools, safety glasses, safety shoes, helmet, professional workwear.

**Do not use for:** ordinary non-specific clothing (`616681`) or large machinery/installations that must be capitalised.

**Agent rules:** clothing qualifies as work clothing only if it is specific to the profession or clearly cannot be used as ordinary private clothing.

## 611220 [sector-specific] materials

**Use when:** consumable materials are purchased that are specific to the client's activity and are not resold as goods.

**Examples:** medical consumables, salon materials, cleaning products for a cleaning business, technical consumables.

**Do not use for:** goods that remain with the customer or are recharged as goods for resale (`604000`).

**Agent rules:** use this account only when the material is consumed internally while providing services. If it is part of the sales margin, use `604000`.

## 612050 Administrative services

**Use when:** external administrative support is purchased.

**Examples:** secretarial services, administrative outsourcing, file administration, document processing, virtual assistant services.

**Do not use for:** bookkeepers/accountants (`615200`), lawyers/notaries/auditors (`615300`) or consultants with an advisory assignment (`612300`).

**Agent rules:** choose this account when the service is mainly administrative and execution-oriented.

## 612060 Legal publications and statutory obligations

**Use when:** costs arise from legal formalities, publications or mandatory registrations.

**Examples:** Belgian Official Gazette publication, Crossroads Bank formalities, UBO formalities, court registry fees, filing fees, mandatory certificates or registrations.

**Do not use for:** fees of the professional handling the formality. Those belong on `615200` or `615300`.

**Agent rules:** if the invoice contains both a professional fee and publication costs, split the lines where possible.

## 612070 Training

**Use when:** costs relate to training, study days, seminars, courses or education for a director/manager or employee.

**Examples:** training course, study day, webinar, course fee, exam fee, professional literature clearly linked to a training.

**Do not use for:** general consulting (`612300`) or ordinary subscriptions/software (`612100` or `616200`, depending on nature).

**Agent rules:** training is normally a business expense when it is linked to the activity or professional knowledge. Flag training without a clear business link for review.

## 612100 IT services

**Use when:** the invoice relates to IT services or software-related support.

**Examples:** website maintenance, IT support, software implementation, hosting with technical services, systems consultancy, configuration.

**Do not use for:** telecom and internet subscriptions (`616200`), ordinary office hardware that must be capitalised, or general consultants (`612300`).

**Agent rules:** SaaS and IT services can be booked here unless the file uses a separate software or subscriptions account. Large development projects may be fixed assets.

## 612300 Consultant fees

**Use when:** external consultants provide substantive advice or support to the business.

**Examples:** management advice, HR advice, marketing advice, strategic advice, operational support.

**Do not use for:** subcontractors working directly on a customer job (`603000`) or regulated professional fees such as bookkeeper, lawyer, notary or auditor (`615200`/`615300`).

**Agent rules:** if the service improves or supports the internal organisation, choose `612300`. If it belongs in the cost price of a specific customer job, choose `603000`.

## 612600 Fuel for company cars

**Use when:** fuel or charging costs relate to company cars.

**Examples:** petrol, diesel, LPG, CNG, electric charging, charge card invoices.

**Do not use for:** fuel for machinery or site equipment without a vehicle nature, unless the file tracks those as vehicle costs.

**Agent rules:** link the cost to the correct car if accounts are tracked per vehicle. Passenger cars require VAT limitation and income tax deductibility based on vehicle data.

## 612601 Parking, car wash and tolls

**Use when:** costs are directly related to parking, car wash, tolls, tunnels, ferries or road vignettes for company cars.

**Do not use for:** general travel and accommodation costs without a vehicle link (`616700`).

**Agent rules:** link to the correct vehicle where possible. Parking at a restaurant or event remains a car cost if the invoice is specifically for parking.

## 612602 Car expenses [make] | [1AAA000] | [0.0%]

**Use when:** costs relate to a specific company car.

**Examples:** maintenance, repairs, tyres, insurance, technical inspection, roadside assistance, rental/lease components if the file tracks them per car.

**Do not use for:** fuel (`612600`) or parking/tolls/car wash (`612601`) when separate accounts exist.

**Agent rules:** the account name should include make, licence plate and deduction percentage. For a new car or missing licence plate, request review.

## 613200 Business risk insurance

**Use when:** insurance premiums cover business risks.

**Examples:** public liability, professional liability, fire insurance for business premises, legal expenses insurance, cyber insurance, machinery breakdown insurance.

**Do not use for:** car insurance if tracked per vehicle (`612602`) or director/manager pension insurances (`613210`, `613220`).

**Agent rules:** choose this account for general business insurance policies.

## 613210 IPT group insurance

**Use when:** the invoice or premium relates to an individual pension commitment (IPT/EIP) or group insurance.

**Do not use for:** VAPZ premiums (`613220`) or ordinary social security contributions (`618100`).

**Agent rules:** check beneficiary, policyholder and deductibility conditions. For a director/manager, this is usually linked to remuneration and the 80% rule. Flag large or one-off premiums.

## 613220 VAPZ premiums

**Use when:** premiums for the Belgian supplementary pension for self-employed persons (VAPZ/PLCI) are paid through the business or processed in the bookkeeping.

**Do not use for:** IPT/group insurance (`613210`) or social security contributions (`618100`).

**Agent rules:** VAPZ is person-specific. Check whether the premium is booked in the correct entity and for the correct person.

## 615200 Fees of bookkeepers and accountants

**Use when:** the invoice comes from a bookkeeper, accountant, tax adviser or certified accountant for accounting or tax services.

**Examples:** monthly bookkeeping, annual accounts, tax return, advice by an accountant.

**Do not use for:** lawyers, notaries and auditors (`615300`).

**Agent rules:** publication or filing costs on the same invoice may need to be split to `612060`.

## 615300 Fees of auditors, lawyers and notaries

**Use when:** fees relate to legal, notarial or audit services.

**Examples:** lawyer, notary, statutory auditor, deed costs, legal proceedings.

**Do not use for:** bookkeepers/accountants (`615200`) or general consultants (`612300`).

**Agent rules:** notarial costs may partly be fixed assets, taxes, registration duties or fees. For acquisitions of real estate or shares, always split or request review.

## 615400 Copyright fees and royalties

**Use when:** compensation relates to the transfer or licensing of copyright.

**Do not use for:** ordinary fees, wages or services without a separate transfer/licence of rights.

**Agent rules:** use only when the document clearly mentions copyright/royalties or when the file has an approved copyright structure. Check contract, service/rights split, withholding tax and tax qualification.

## 616200 Telephone and internet expenses

**Use when:** costs relate to telephone, mobile subscription, internet, data connections or telecom bundles.

**Do not use for:** IT services or software implementation (`612100`) and devices that should be booked as fixed assets or small equipment.

**Agent rules:** for mixed private/business use, apply the configured business-use percentage. Devices included on telecom invoices must be assessed separately.

## 616500 Hospitality costs and business gifts

**Use when:** costs are incurred to receive customers, suppliers or business relations, or to give a business gift.

**Examples:** flowers for a client, business gift, reception, small courtesy gift, hospitality drinks for visitors.

**Do not use for:** internal canteen expenses (`611001`) or restaurant expenses (`616680`).

**Agent rules:** flag business gifts for income tax and VAT deduction limitations. Split mixed invoices where possible.

## 616610 Marketing materials

**Use when:** costs relate to promotional material or advertising.

**Examples:** flyers, banners, stickers, advertisements, marketing print, promotional material.

**Do not use for:** general office printing (`611000`) or trade fair participation (`616620`).

**Agent rules:** if the purpose is commercial visibility or promotion, choose `616610`.

## 616620 Trade fairs and exhibitions

**Use when:** costs relate to participation in trade fairs, exhibitions or professional events.

**Examples:** stand rental, fair registration, stand construction, fair-specific materials.

**Do not use for:** ordinary training (`612070`) or marketing materials unrelated to a fair (`616610`).

**Agent rules:** fair-related costs may be grouped here when they relate to the same event.

## 616651 Professional association fees

**Use when:** membership fees or contributions are paid to professional associations, sector organisations or recognised professional institutes.

**Do not use for:** training (`612070`) or donations/sponsorship (`616660` or `616500`, depending on nature).

**Agent rules:** words such as membership fee, contribution, professional association, order, institute or sector federation point to this account.

## 616660 Deductible donations

**Use when:** the business makes a donation to a recognised institution for which tax deduction may be available.

**Do not use for:** sponsorship with advertising consideration (`616610`) or business gifts (`616500`).

**Agent rules:** request or check the tax certificate. Without a certificate or recognised institution, the cost may need different or non-deductible treatment.

## 616680 Restaurant expenses

**Use when:** restaurant, catering or meal costs have a business purpose.

**Examples:** business lunch, dinner with a client, catering for a meeting, restaurant while travelling for business.

**Do not use for:** internal canteen expenses (`611001`) or meal vouchers (`623020`/`618110`).

**Agent rules:** restaurant expenses are often only partly deductible and VAT is often not deductible. Record participants or business purpose where possible.

## 616681 Non-specific business clothing

**Use when:** clothing is purchased for business use but can also be worn as ordinary private clothing.

**Do not use for:** genuine workwear or safety clothing (`611210`).

**Agent rules:** these costs are usually tax-sensitive or non-deductible. Flag for review unless the file has a clear policy.

## 616682 Other non-deductible expenses

**Use when:** a cost must be recorded in the accounts but is not tax-deductible and no more specific non-deductible account exists.

**Examples:** private expenses borne by the company, tax-disallowed costs without their own account, non-business expenses.

**Do not use for:** fines (`644000`) or restaurant/car expenses with their own deduction limitation.

**Agent rules:** use this account carefully. If a cost is clearly private, also assess whether it should be processed through current account, benefit in kind or recovery.

## 616700 Travel and accommodation expenses

**Use when:** costs relate to business travel and accommodation without a specific car-cost nature.

**Examples:** hotel, train, flight, taxi, public transport, lodging, travel allowance if processed through an expense claim.

**Do not use for:** parking/tolls/car wash (`612601`), restaurant expenses (`616680`) or commuting/personnel costs if tracked separately.

**Agent rules:** check business purpose, destination and any private component. Foreign trips with a mixed purpose must be flagged.

## 617000 Temporary agency workers

**Use when:** invoices from temporary employment agencies relate to temporary workers.

**Do not use for:** ordinary payroll (`620000`) or subcontractors (`603000`).

**Agent rules:** invoices from Randstad, Adecco, Manpower and similar suppliers usually point to this account.

## 618000 Director/manager remuneration

**Use when:** remuneration, salary or compensation of company directors/managers is booked.

**Do not use for:** employee wages (`620000`) or board fees outside the ordinary remuneration structure (`618300`).

**Agent rules:** use mostly based on payroll entries, payroll provider documents or year-end entries. Do not use for ordinary supplier invoices.

## 618001 Benefit in kind - rent reclassification

**Use when:** a benefit or remuneration component is booked as a result of rent reclassification for a director/manager.

**Do not use for:** ordinary rent expenses (`610101`/`610130`) or other benefits in kind (`618002`).

**Agent rules:** use only for a tax correction or payroll processing. Requires review of rent, cadastral income, business use and the reclassification calculation.

## 618002 Other benefits in kind

**Use when:** other benefits in kind for directors/managers are booked.

**Examples:** housing, utilities, telephone, internet, laptop, other assets made available.

**Do not use for:** passenger car benefit in kind (`618003`) or recovery of benefit in kind (`618010`).

**Agent rules:** use only for payroll processing, tax forms or year-end entries. Link to the underlying cost where possible.

## 618003 Benefit in kind - passenger car

**Use when:** the benefit in kind for a director/manager's passenger car is booked.

**Do not use for:** car expenses themselves (`612600`, `612601`, `612602`) or other benefits in kind (`618002`).

**Agent rules:** use based on the benefit-in-kind calculation or payroll processing. Requires vehicle data such as catalogue value, CO2, fuel type, age and period of use.

## 618010 Recovery of director/manager benefit in kind

**Use when:** a director/manager pays a contribution or a benefit in kind is recovered.

**Do not use for:** ordinary remuneration or expense bookings.

**Agent rules:** book only the recovery or personal contribution that reduces or corrects the benefit in kind. Check the link with the payroll tax form.

## 618100 Paid social security contributions

**Use when:** social security contributions of self-employed directors/managers are paid or booked.

**Do not use for:** employer social security contributions for employees (`621000`) or VAPZ premiums (`613220`).

**Agent rules:** invoices from a social insurance fund for a director/manager usually point to this account. Check whether the contribution should be paid by the company or privately.

## 618101 KEW expense allowance

**Use when:** a flat-rate or actual expense allowance to a director/manager is booked.

**Do not use for:** reimbursement of specific invoices that should be booked directly on expense accounts.

**Agent rules:** use only when there is a policy or tax basis, such as serious standards or an allowance reported on the tax form. Do not automatically use this account for every payment to a director/manager.

## 618110 Meal vouchers for director/manager

**Use when:** the employer cost of meal vouchers for directors/managers is booked.

**Do not use for:** employee meal vouchers (`623020`) or recovery/personal contribution (`618111`).

**Agent rules:** check number of vouchers, employer contribution, personal contribution and possible overlap with other meal allowances.

## 618111 Recovery of director/manager meal voucher contribution

**Use when:** the director/manager's personal contribution for meal vouchers is recovered.

**Do not use for:** the employer cost itself (`618110`).

**Agent rules:** use as contra-entry or correction to the director/manager meal voucher cost.

## 618120 Eco vouchers for director/manager

**Use when:** eco vouchers for directors/managers are booked.

**Do not use for:** employee eco vouchers if those are separately tracked under personnel costs.

**Agent rules:** check tax conditions and maximum amounts. Use based on payroll provider documents or voucher supplier invoices.

## 618130 Warrant plan for director/manager

**Use when:** costs or benefits from a warrant plan for directors/managers are booked.

**Do not use for:** ordinary remuneration, bonuses or employee warrants without a director/manager context.

**Agent rules:** use only when an explicit warrant plan or payroll processing exists. Flag for review because of tax and social security sensitivity.

## 618190 Director/manager remuneration regularisation

**Use when:** corrections or regularisations of director/manager remuneration are booked.

**Do not use for:** ordinary periodic remuneration (`618000`) when it can be booked correctly.

**Agent rules:** use for closing entries, correction entries or rework of payroll/tax forms. Add a clear description.

## 618300 Board fees

**Use when:** fees are paid to directors for a board mandate, attendance fees or similar services.

**Do not use for:** ordinary director/manager remuneration (`618000`) or fees of external consultants (`612300`).

**Agent rules:** check the director's VAT status, reporting obligation and any withholding. Do not use for invoices without a board mandate.

## 620000 Wages and salaries

**Use when:** gross wages and salaries of employees are booked.

**Do not use for:** director/manager remuneration (`618000`) or temporary agency invoices (`617000`).

**Agent rules:** use based on payroll journals or payroll provider documents. Ordinary supplier invoices do not belong here.

## 620001 Recovery of personnel costs

**Use when:** personnel costs are recharged, recovered or corrected.

**Do not use for:** ordinary payroll booking (`620000`) or invoiced revenue that should be recorded as turnover.

**Agent rules:** use for reimbursements by third parties, recovery of benefits or corrections to personnel costs. Check whether a negative expense or revenue account is more appropriate under the file's policy.

## 621000 Employer social security contributions

**Use when:** employer social security contributions on employee wages are booked.

**Do not use for:** social security contributions of self-employed directors/managers (`618100`).

**Agent rules:** use based on payroll journals or payroll provider documents.

## 623000 Other personnel costs

**Use when:** personnel-related costs do not belong on wages, social security or a more specific personnel account.

**Examples:** occupational health service, commuting reimbursements if not tracked elsewhere, personnel insurance, work-related employee costs, team building with a personnel nature.

**Do not use for:** meal vouchers (`623020`) or costs for directors/managers (`618xxx`).

**Agent rules:** check that the cost relates to employees and not to directors/managers, customers or general operations.

## 623020 Meal vouchers

**Use when:** meal vouchers for employees are booked.

**Do not use for:** meal vouchers for directors/managers (`618110`) or director/manager personal contribution (`618111`).

**Agent rules:** split employer contribution and employee contribution according to payroll processing or the voucher supplier invoice. Check maximum amounts and number of vouchers.

## 631000 Inventory impairment

**Use when:** inventory must be written down because of obsolescence, damage, lower market value or unsaleability.

**Do not use for:** ordinary inventory changes (`609400`) or impairment of trade receivables (`633000`).

**Agent rules:** book only based on inventory, valuation decision or year-end review.

## 633000 Impairment of trade receivables

**Use when:** a trade receivable is likely not to be collected in full and an impairment is required.

**Do not use for:** final loss on realisation or payment differences without doubtful-debt character.

**Agent rules:** use for doubtful debtors, bankruptcy, disputes or long-overdue invoices. Requires support per customer/invoice.

## 640000 Business taxes

**Use when:** taxes, levies or duties are business expenses and do not directly relate to the profit/result.

**Examples:** municipal tax, provincial tax, environmental tax, road tax if not booked through a car expense account, patrimony tax, non-profit-based levies.

**Do not use for:** corporate income tax or personal income tax on business profit (`670000`), withholding tax on movable income (`670001`) or fines (`644000`).

**Agent rules:** if the assessment or invoice is a tax on activity, ownership, establishment or use, choose `640000`. If the tax is calculated on profit/result, choose `670000`.

## 644000 Fines

**Use when:** the business pays a fine, administrative penalty, tax increase or late-payment interest with a punitive character.

**Examples:** traffic fine, tax fine, social security fine, administrative penalty, late-filing penalty.

**Do not use for:** ordinary default interest on loans or suppliers without punitive character (`650610` or `659000`) and ordinary taxes (`640000`/`670000`).

**Agent rules:** fines are often tax non-deductible. Mark for review as a disallowed expense.

## 650610 Interest on leasing, loans and renting

**Use when:** interest on loans, leasing, renting or financing is booked.

**Do not use for:** principal repayments, rent/lease costs without an interest component (`610200`) or bank charges (`657100`).

**Agent rules:** split principal and interest. If a leasing invoice does not show a clear split, flag for review or use the repayment schedule.

## 654000 Unfavourable exchange differences

**Use when:** a foreign exchange difference is unfavourable to the business.

**Examples:** payment to a foreign supplier is higher than the booked liability, collection from a foreign customer is lower than the booked receivable, foreign currency revaluation with a loss.

**Do not use for:** bank charges (`657100`) or ordinary payment differences in EUR (`658000`).

**Agent rules:** use only when the difference arises from exchange rates. Record currency, original booking and payment date where available.

## 657100 Bank charges

**Use when:** fees are charged by banks, payment platforms or card processors.

**Examples:** bank subscription, transaction fees, card fees, Bancontact/Stripe/PayPal fees, bank file charges.

**Do not use for:** interest (`650610`) or payment differences (`658000`).

**Agent rules:** payment provider fees belong here, even when deducted from payouts. Split revenue and costs if the payout is net.

## 658000 Payment differences in your disadvantage

**Use when:** a small payment or reconciliation difference is unfavourable to the business and is not caused by exchange rates.

**Examples:** rounding difference, small shortfall in customer payment, small difference between invoice and payment.

**Do not use for:** exchange differences (`654000`), bank charges (`657100`) or significant commercial discounts/credit notes.

**Agent rules:** use only for small differences. Large differences must be investigated and not automatically written off.

## 659000 Other financial expenses

**Use when:** a financial expense does not fit interest, exchange differences, bank charges or payment differences.

**Examples:** guarantee costs, financing file charges, financial management costs, other financial charges.

**Do not use for:** ordinary operating expenses or more specific financial accounts.

**Agent rules:** use as a residual account within financial expenses. For recurring specific costs, a separate account may be preferable.

## 660000 Exceptional expenses

**Use when:** expenses are exceptional or non-recurring and do not arise from normal business activity.

**Examples:** loss event, exceptional restructuring cost, non-recurring loss, exceptional correction.

**Do not use for:** ordinary operating expenses that happen to be large. Use the normal expense account instead.

**Agent rules:** do not use automatically. Requires clear motivation or closing instruction.

## 663000 Loss on realisation

**Use when:** an asset is sold or taken out of use at a loss compared with its book value.

**Examples:** sale of machinery below book value, sale of vehicle below book value, disposal with remaining book value.

**Do not use for:** ordinary sales costs, depreciation or inventory/receivable impairments.

**Agent rules:** use only on realisation or disposal of assets. Requires comparison between selling price and net book value.

## 670000 Income taxes

**Use when:** corporate income tax, personal income tax on business profit or other profit-based taxes are booked.

**Do not use for:** business taxes not based on profit (`640000`), withholding tax on movable income (`670001`) or tax prepayments (`670002`).

**Agent rules:** use for tax calculations, tax assessments or closing entries for taxes on profit.

## 670001 Withholding tax on movable income

**Use when:** withholding tax on movable income is booked as a tax expense.

**Examples:** withholding tax on dividends, interest or copyright income, depending on the role of the business.

**Do not use for:** payroll withholding tax or ordinary corporate income tax (`670000`).

**Agent rules:** determine whether the business is debtor, withholding agent or recipient. For dividends, link with profit appropriation and withholding tax return.

## 670002 Tax prepayments

**Use when:** tax prepayments are booked or offset.

**Do not use for:** final tax expense without prepayment character (`670000`).

**Agent rules:** use for corporate income tax/personal income tax prepayments according to due dates. At year-end, prepayments must be offset against estimated or final tax.

## 670003 Tax regularisations

**Use when:** corrections, supplements or reversals of taxes from previous periods are booked.

**Examples:** additional assessment for a previous year, correction of tax provision, refund or additional payment after assessment.

**Do not use for:** normal tax expense of the current financial year (`670000`).

**Agent rules:** use when the document refers to regularisation, supplement, revision or previous assessment years.

## 680000 Transfer to deferred taxes

**Use when:** deferred taxes are booked according to closing or valuation rules.

**Do not use for:** ordinary corporate income tax or tax prepayments.

**Agent rules:** only use for closing entries prepared by an accountant or tax adviser. Do not use based on ordinary invoices or tax assessments.

## 690000 Loss carried forward from previous financial year

**Use when:** the loss from the previous financial year is included in the profit appropriation.

**Do not use for:** current-year loss or ordinary expenses.

**Agent rules:** only use in profit appropriation/year-end closing. Requires approved annual accounts or closing statement.

## 691001 Additions to capital

**Use when:** profit is allocated to capital or contribution according to a shareholders' decision or the articles of association.

**Do not use for:** ordinary capital contributions by shareholders or bank movements without profit appropriation.

**Agent rules:** only use in profit appropriation. Requires a resolution or clear closing instruction.

## 692100 Additions to other reserves

**Use when:** profit is added to other reserves.

**Do not use for:** liquidation reserve (`692101`) or profit to be carried forward (`693000`).

**Agent rules:** only use in profit appropriation. Check the general meeting resolution.

## 692101 Additions to liquidation reserve

**Use when:** profit is allocated to a liquidation reserve.

**Do not use for:** ordinary other reserves (`692100`) or dividends (`694000`).

**Agent rules:** only use in profit appropriation with an explicit choice for a liquidation reserve. Check conditions, tax rate and separate assessment.

## 693000 Profit to be carried forward

**Use when:** profit of the financial year is carried forward to the next financial year.

**Do not use for:** actual dividend distribution (`694000`) or addition to reserves (`692100`/`692101`).

**Agent rules:** use in profit appropriation according to the approved allocation.

## 693100 Result to be carried forward

**Use when:** the result is generally carried forward according to the closing structure of the file.

**Do not use for:** a specific allocation that better fits `693000`, `690000`, `692100`, `692101` or `694000`.

**Agent rules:** use only if the file uses this account as a general carry-forward account. Otherwise choose the more specific profit appropriation account.

## 694000 Dividends

**Use when:** profit is distributed or allocated as a dividend.

**Do not use for:** ordinary supplier payments, board fees or payroll.

**Agent rules:** only use in profit appropriation, interim dividend or intermediate dividend based on a valid decision. Check withholding tax, available distributable reserves and company-law distribution tests where applicable.

