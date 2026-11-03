# Case 04 — Circle USDC Freezing Workflow (Aug 2022)

<!-- mapping: case_id=04 case_name="Circle USDC freezing workflow" year=2022 paradigm=VASP mechanism_primary=Screening mechanism_secondary=KYT lifecycle_primary=Ex-Ante lifecycle_secondary=None confidence=High overlap=false -->

## Summary

Circle Internet Financial is the U.S.-regulated issuer of USDC; its ERC-20 contract exposes a `blacklist(address)` administrative function described as: once an address is blacklisted, it can "no longer receive USDC and all of the USDC controlled by that address is blocked and cannot be transferred on-chain" (`data/evidence/04_circle_usdc_freeze/circle_allaire_tornado_cash_response.txt`). On 8 August 2022, within hours of the OFAC Tornado Cash designation (`data/evidence/04_circle_usdc_freeze/ofac_tornado_cash_aug2022.txt`), Circle CEO Jeremy Allaire publicly confirmed: "Circle complied with these sanctions and blocked the addresses on our platform, cutting off USDC access from Circle accounts to and from the Tornado Cash sanctioned addresses" (`circle_allaire_tornado_cash_response.txt`). Approximately 75,000–81,000 USDC was frozen across the 44 sanctioned addresses (same file). Allaire framed the operational basis as: "On Monday, August 8, the systems we have in place to comply with applicable law, and government regulations worked. Centre, the consortium behind USDC, followed the US Treasury sanctions against Tornado Cash and blocked the related addresses" (same file). Circle's stated policy is that "USDC will not be frozen without a court order" (or equivalent sanctions order; same file), making the workflow a canonical example of compliant-stablecoin Ex-Ante controls implemented through a centralized administrative key.

## Taxonomy 1 — Regulatory Paradigm

**Virtual Asset Regulation (Centralized).** Although the freeze executes on a public blockchain, the policy actor is a centralized licensed issuer (Circle / Centre) responding to traditional OFAC sanctions orders (`circle_allaire_tornado_cash_response.txt`: "Centre … followed the US Treasury sanctions against Tornado Cash and blocked the related addresses"). The Centralized column's "Similar to traditional plus blockchain address blacklisting" enforcement profile in `tab:regulatory_evolution` fits exactly.

## Taxonomy 2 — Compliance Mechanism

**Primary: Address/Wallet Screening.** The decision input is a list of sanctioned addresses (the 44 OFAC SDN entries — `ofac_tornado_cash_aug2022.txt`); the contract action is an address-level blacklist control (`circle_allaire_tornado_cash_response.txt`: "blacklisted … all of the USDC controlled by that address is blocked"). **Secondary: KYT** because the operational trigger is often the detection of a transaction routing illicit funds through a USDC-holding address — Circle's general policy applies the freeze on a per-court-order, per-transaction-evidence basis (`circle_allaire_tornado_cash_response.txt`: "USDC will not be frozen without a court order").

## Taxonomy 3 — RegTech Lifecycle

**Primary: Ex-Ante (Preventive).** `tab:regtech_lifecycle` explicitly cites "compliant stablecoin blacklists (USDC freeze functions)" as a Web3-specific Ex-Ante implementation. The freeze prevents the listed address from spending USDC prospectively (`circle_allaire_tornado_cash_response.txt`). No secondary lifecycle phase: the per-transfer blacklist check is the mechanical realisation of the Ex-Ante control, not a separate In-Medias-Res activity.

## Mapping confidence

**High.** The case is explicitly named in `tab:regtech_lifecycle` as Ex-Ante; the Allaire quotes preserved in secondary coverage make the workflow self-validating.

## Sources

- `data/evidence/04_circle_usdc_freeze/circle_allaire_tornado_cash_response.txt`
- `data/evidence/04_circle_usdc_freeze/ofac_tornado_cash_aug2022.txt`
