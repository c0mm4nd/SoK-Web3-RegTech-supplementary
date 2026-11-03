# Case 05 — Notabene Travel Rule Deployment

<!-- mapping: case_id=05 case_name="Notabene Travel Rule deployment" year=2024 paradigm=VASP mechanism_primary=KYC mechanism_secondary=KYB lifecycle_primary=In-Medias-Res lifecycle_secondary=Ex-Ante confidence=Medium overlap=true -->

## Summary

Notabene is a Travel Rule SaaS platform that implements FATF Recommendation 16 by exchanging originator and beneficiary VASP information at transaction time. The October 2021 FATF guidance specifies that "VASPs must obtain, hold, and securely transmit originator and beneficiary information (name, account number, physical address or government-issued ID) when transferring virtual assets above the de-minimis threshold (USD/EUR 1,000 in most jurisdictions)" (`data/evidence/05_notabene_travel_rule/fatf_updated_guidance_vasp_oct2021.txt`). Notabene's 2024 industry survey of 70 VASPs reports that "96% of companies now Travel Rule compliant or on track to compliance by end of 2024" and that "66% of VASPs enforce restrictions on withdrawals to self-hosted (non-custodial) wallets that cannot exchange Travel Rule messages" (`data/evidence/05_notabene_travel_rule/notabene_state_of_travel_rule_2024.txt`). The FATF June 2023 targeted update confirms continuing pressure: "75% of jurisdictions are only partially or not compliant with the FATF's requirements" on R.15 (`data/evidence/05_notabene_travel_rule/fatf_targeted_update_vasp_jun2023.txt`), driving ongoing Notabene-style deployments. The Notabene workflow performs counterparty VASP discovery, beneficiary identification, sanctions screening, and policy-based hold-and-release of outgoing transactions before settlement.

## Taxonomy 1 — Regulatory Paradigm

**Virtual Asset Regulation (Centralized).** The Travel Rule is a VASP-to-VASP information-exchange obligation that exactly instantiates the Centralized column's "Extended to VASP's complete customer base with Travel Rule exchange" transaction-visibility row in `tab:regulatory_evolution`. The FATF guidance (`fatf_updated_guidance_vasp_oct2021.txt`) frames the obligation entirely around licensed VASPs.

## Taxonomy 2 — Compliance Mechanism

**Primary: KYC.** The transmitted payload is the originator's identity ("name, account number, physical address or government-issued ID" — `fatf_updated_guidance_vasp_oct2021.txt`) and the beneficiary's identity, which is the canonical KYC verification target in `tab:compliance_comparison`. **Secondary: KYB** because the message also identifies the counterparty VASP and its licensing status; the Notabene survey emphasizes counterparty due-diligence ("counterparty risk based on address attribution" and self-hosted-wallet restrictions in `notabene_state_of_travel_rule_2024.txt`).

## Taxonomy 3 — RegTech Lifecycle

**Primary: In-Medias-Res (Real-Time).** The exchange happens at transaction time and gates settlement — the canonical FATF R.16 use case named in the In-Medias-Res row of `tab:regtech_lifecycle` ("automated Travel Rule protocols, transaction blocking"). The Notabene survey's "23% do not allow any withdrawals unless a Travel Rule message can be sent" finding (`notabene_state_of_travel_rule_2024.txt`) is direct evidence of real-time gating. **Secondary: Ex-Ante** because pre-transaction counterparty due diligence (VASP discovery, sanctions screening) is performed before each transaction is initiated. **Overlap flagged.**

## Mapping confidence

**Medium.** The In-Medias-Res placement is unambiguous, but the mechanism axis legitimately spans KYC, KYB, and (for self-hosted-wallet attestation) KYA — exposing a genuine multi-mechanism profile rather than a taxonomy defect.

## Sources

- `data/evidence/05_notabene_travel_rule/notabene_state_of_travel_rule_2024.txt`
- `data/evidence/05_notabene_travel_rule/fatf_updated_guidance_vasp_oct2021.txt`
- `data/evidence/05_notabene_travel_rule/fatf_targeted_update_vasp_jun2023.txt`
