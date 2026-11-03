# Case 01 — Tornado Cash OFAC Designation (Aug 2022)

<!-- mapping: case_id=01 case_name="Tornado Cash OFAC designation" year=2022 paradigm=Web3 mechanism_primary=Screening mechanism_secondary=KYT lifecycle_primary=Ex-Ante lifecycle_secondary=None confidence=High overlap=false -->

## Summary

On 8 August 2022 the U.S. Treasury's Office of Foreign Assets Control (OFAC) added the Ethereum smart-contract mixer Tornado Cash and a list of associated Ethereum addresses to the Specially Designated Nationals (SDN) list under Executive Order 13694 (`data/evidence/01_tornado_cash/ofac_tornado_cash_aug2022.txt`: "Date of action: August 8, 2022. Sanctioning agency: Office of Foreign Assets Control (OFAC), under Executive Order 13694 (as amended)"). Treasury cited "more than $7 billion worth of virtual currency" laundered since 2019 and "over $455 million stolen by the Lazarus Group … via the Ronin Bridge hack" (same file). Tornado Cash itself is described by Chainalysis as "a decentralized, non-custodial smart contract" whose contracts "cannot be changed or destroyed by anyone" (`data/evidence/01_tornado_cash/chainalysis_tornado_cash_sanctions.txt`). Within hours, Circle "froze all USDC held in OFAC-designated Tornado Cash addresses," Infura and Alchemy began blocking RPC access, and the 44 listed addresses became a screening input for every regulated counterparty (same Chainalysis file). In November 2024 the Fifth Circuit held in *Van Loon v. Treasury* that the immutable contracts were not "property" under OFAC's statutory authority and on 21 March 2025 OFAC removed Tornado Cash from the SDN list (`ofac_tornado_cash_aug2022.txt`).

## Taxonomy 1 — Regulatory Paradigm

**Web3 Regulation (Decentralized).** The target of the action was a set of immutable on-chain smart contracts and an associated address list, not a licensed VASP. Enforcement was implemented through smart-contract-level address blacklisting that propagated through downstream stablecoin issuers and RPC providers — precisely the Web3 column's "Smart contract restrictions, protocol-level compliance, limited retroactive control" pattern in `tab:regulatory_evolution`. The Fifth Circuit's later narrowing (`ofac_tornado_cash_aug2022.txt`) confirms the paradigm-novelty of the action: traditional VASP enforcement tools could not reach the contracts themselves.

## Taxonomy 2 — Compliance Mechanism

**Primary: Address/Wallet Screening.** OFAC published a discrete set of Ethereum addresses; downstream compliance is implemented by screening counterparty addresses against the SDN list (`ofac_tornado_cash_aug2022.txt`: "VASPs must screen against OFAC SDN list"). **Secondary: KYT.** Issuer-side enforcement (Circle's USDC freeze workflow) fires on transactions that touch the screened cluster, and the FinCEN CVC mixing NPR (`fincen_cvc_mixing_npr_oct2023.txt`) likewise targets mixing *transactions* as a class of activity — KYT verification target.

## Taxonomy 3 — RegTech Lifecycle

**Primary: Ex-Ante (Preventive).** The designation creates a prospective prohibition: regulated parties must screen and block interaction with the listed addresses before transactions execute, which is the Ex-Ante row's "sanctions screening … compliant stablecoin blacklists (USDC freeze functions)" pattern from `tab:regtech_lifecycle`. The Chainalysis post (`chainalysis_tornado_cash_sanctions.txt`) explicitly enumerates the Ex-Ante enforcement layer (CEX blocks, Infura/Alchemy RPC blocks, Circle USDC freezes). No secondary lifecycle phase: contract-time enforcement is the *implementation* of the Ex-Ante control rather than a separate In-Medias-Res activity.

## Mapping confidence

**High.** Treasury action and Circle's response are documented across primary and secondary sources in the dossier; the taxonomy maps cleanly onto a sanctions screening regime explicitly named in `tab:regtech_lifecycle`.

## Sources

- `data/evidence/01_tornado_cash/ofac_tornado_cash_aug2022.txt`
- `data/evidence/01_tornado_cash/chainalysis_tornado_cash_sanctions.txt`
- `data/evidence/01_tornado_cash/fincen_cvc_mixing_npr_oct2023.txt`
- `data/evidence/01_tornado_cash/wu2021detectingmixingservices.txt`
