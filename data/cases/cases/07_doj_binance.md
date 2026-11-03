# Case 07 — DOJ Binance USD 4.3B Settlement (Nov 2023)

<!-- mapping: case_id=07 case_name="DOJ Binance settlement" year=2023 paradigm=VASP mechanism_primary=KYC mechanism_secondary=KYT lifecycle_primary=Ex-Post lifecycle_secondary=None confidence=High overlap=false -->

## Summary

On 21 November 2023 the U.S. Department of Justice, Treasury (FinCEN/OFAC), and CFTC announced a coordinated settlement with Binance Holdings Ltd. and its founder Changpeng Zhao. Binance pleaded guilty to "Conspiracy to conduct an unlicensed money transmitting business in violation of 18 U.S.C. Section 1960", "Conspiracy to violate the Bank Secrecy Act (BSA) by failing to implement and maintain an effective anti-money laundering program", "Failure to register as a money transmitting business", and "Violations of the International Emergency Economic Powers Act (IEEPA) for willful sanctions violations" (`data/evidence/07_doj_binance/doj_binance_settlement_nov2023.txt`). Total penalties were "Over $4.3 billion across DOJ, OFAC, FinCEN, and CFTC components" (same file). Zhao personally pleaded to "failing to maintain an effective AML program" and "paid $50 million" (same file). The earlier CFTC complaint (`data/evidence/07_doj_binance/cftc_v_binance_mar2023.txt`, filed 27 Mar 2023) had already alleged "Failure to implement KYC/AML controls" and "Causing employees to circumvent compliance controls (including VIP customer guidance to evade compliance via VPNs)". The settlement is structured around classical VASP obligations and is the largest crypto-related enforcement action in U.S. history at the time.

## Taxonomy 1 — Regulatory Paradigm

**Virtual Asset Regulation (Centralized).** Binance is a centralized VASP and the entire action is built around classical VASP obligations: BSA registration, AML programme, SAR filing, sanctions compliance (`doj_binance_settlement_nov2023.txt`). The Centralized column in `tab:regulatory_evolution` — "Centralized VASP databases" plus "VASP compliance plus regulatory oversight" verification model — describes the regulatory frame exactly.

## Taxonomy 2 — Compliance Mechanism

**Primary: KYC.** The agreed-fact narrative focuses on Binance's failure to verify customer identities, particularly U.S. customers "routed through workarounds" (`cftc_v_binance_mar2023.txt`: "Failure to implement KYC/AML controls" and VIP guidance to "evade compliance via VPNs"). **Secondary: KYT** because the same documents detail failures to monitor transactions linked to sanctioned jurisdictions and ransomware addresses (`doj_binance_settlement_nov2023.txt`: IEEPA willful sanctions violations imply unmonitored transactions to sanctioned counterparties).

## Taxonomy 3 — RegTech Lifecycle

**Primary: Ex-Post (Investigative).** The settlement itself is a retrospective multi-year enforcement action — SAR review, audit trails, statement of facts, deferred prosecution. The Ex-Post row's "regulatory reporting, audit trails" objective in `tab:regtech_lifecycle` frames the case. The CFTC complaint (`cftc_v_binance_mar2023.txt`) was filed 8 months earlier and is the parallel ex-post enforcement vehicle. No secondary lifecycle phase: the remedial monitorship's forward-looking obligations are a *consequence* of the settlement rather than part of the case itself.

## Mapping confidence

**High.** Public DOJ, FinCEN, OFAC, and CFTC documents converge on the classification; the SoK manuscript already cites this case as a canonical centralized-VASP enforcement event.

## Sources

- `data/evidence/07_doj_binance/doj_binance_settlement_nov2023.txt`
- `data/evidence/07_doj_binance/cftc_v_binance_mar2023.txt`
