# E1 v4 Calibration Notes — Coder R1

For each of the 25 cells coded, this file records reasoning, confidence,
and any rubric ambiguities encountered. Flagged categories:
(C1) Clear application, high confidence.
(C2) Ambiguous — judgment call required.
(C3) Rubric language that should be sharpened.

---

## P01 Chainalysis

### P01,D01 — Transaction Monitoring → Full (2)  [C1]
Vendor names "KYT" with real-time monitoring of crypto transactions and
explicit alert categories (suspicious deposits/withdrawals). The 2024 and
2025 Crypto Crime Reports — though Chainalysis-authored — are routinely
treated as analyst-tier industry reports and cite FBI/regulator use of
Chainalysis tracing (DMM heist attribution). Clear Full per the rubric's
worked example: "KYT real-time pipeline with Sanctioned, Mixing, Darknet
alert categories." High confidence.

### P01,D08 — Graph Neural Networks → Partial (1)  [C2, C3]
Rubric ambiguity: the SoK narrative says "Graph, Attribution" as the
technical approach but does not use the term "GNN" or any architecture
name (GCN/GraphSAGE/GAT). Per rubric: "'graph-based' or 'graph analytics'
alone is Partial." The narrative is T_indep so I did not flag
(vendor-only evidence). But the Pocher 2023 paper does NOT explicitly
name Chainalysis as using GNN — it uses Elliptic data, not Chainalysis.
Wu 2023 TRacer paper critiques Chainalysis heuristic/taint approaches —
which would actually argue AGAINST Chainalysis using GNN.

**Rubric sharpening suggestion:** The rule "'graph-based' alone is
Partial" is clear, but the boundary between "graph analytics" (Partial)
and "no graph evidence" (None) is fuzzy when the only T_indep mention
is a one-word technical-approach tag in a SoK summary table. Suggest
clarifying: "Tag-only technical-approach labels in narrative.md count as
Partial only if the rubric's Partial criterion is satisfied; a one-word
tag is insufficient if the vendor evidence is wholly silent on graph
analytics."

### P01,D13 — Zero-Knowledge Proofs → None (0)  [C1]
No mention of ZKP anywhere in the Chainalysis dossier. Clear None. The
rubric worked example explicitly lists "Chainalysis: no ZK in product
line → None." High confidence.

### P01,D17 — MEV Analysis → None (0)  [C2]
Tests the vendor-only rule. Chainalysis vendor pages do not mention MEV
explicitly. The 2024/2025 Crime Reports don't name MEV either. No
T_indep paper attributes MEV detection to Chainalysis. Per rubric, this
is None — even though the calibration set notes "vendor markets but no
T_indep — tests vendor-only rule," the actual vendor evidence does NOT
contain a specific MEV product name to support even Partial. Confident
None.

**Rubric sharpening suggestion:** Calibration-set hint "vendor markets
but no T_indep" implied the vendor DOES market it. Suggest the
calibration-set description align with the actual evidence content,
otherwise coder may second-guess a clear None.

### P01,D21 — API Integration → Partial (1) (vendor-only)  [C1]
KYT and Reactor are named products with API access implied, but no
endpoint family / authentication scheme is documented in the vendor
pages provided. Per rubric Note: "This dimension typically has the
highest T_vendor base rate ... only T_indep evidence (a paper or
analyst report describing the API) elevates to Full." High confidence.

---

## P09 Solidus Labs

### P09,D01 — Transaction Monitoring → Full (2)  [C1]
Vendor names HALO platform with explicit detection categories ("spoofing,
layering/quote stuffing, wash trading") and the Solidus 2023 wash-trade
analyst report quantifies $2B detected. Solidus's wash-trade method is
the operational instantiation of Victor 2021 (T_indep paper). Clearly
Full.

### P09,D08 — Graph Neural Networks → None (0)  [C2]
Solidus vendor pages mention "behavioral analytics" and "AI" but no
graph architecture is named. The rubric's "ML/AI without graph" maps to
None for D08 (it would be Partial only if "graph analytics" were
claimed). Calibration-set hint said "GNN claim ambiguous in Solidus
docs" but I find NO GNN claim at all in the dossier. Confident None
given the evidence at hand.

**Rubric sharpening suggestion:** Calibration-set description "GNN claim
ambiguous" implies presence of a borderline claim; actual evidence had
no graph mention. Same calibration-description issue as P01,D17.

### P09,D11 — Travel Rule Support → None (0)  [C1]
Solidus is market-surveillance, not Travel Rule. Worked example in
rubric confirms: market-surveillance vendor with no Travel Rule = None.
High confidence.

### P09,D14 — Verifiable Credentials → None (0)  [C1]
No credential / W3C VC / DID layer in any Solidus source. Clear None.

### P09,D17 — MEV Analysis → None (0)  [C2]
This was the cell I expected to score Partial based on the calibration
set's "worked-example case: vendor+T_indep paper (Victor 2021)" hint.
But the Solidus HALO vendor pages do not actually name MEV — they name
spoofing, layering, wash trading. Victor 2021 paper covers wash trading
on DEXes, not MEV proper (sandwich/arbitrage). The rubric defines D17
narrowly as MEV strategy detection (sandwich, JIT, arbitrage,
liquidations). I therefore score None.

**Rubric sharpening suggestion:** The rubric's D17 worked example says
"Solidus: wash-trading + MEV monitoring → Full (Victor 2021 wash-trade
paper as T_indep anchor)." But Victor 2021 is wash-trade, NOT MEV per
the rubric's own D17 operational definition. This is an internal rubric
inconsistency — wash trading is not MEV. Suggest the D17 worked example
be revised: either narrow Solidus to D01/D10 (where wash-trade fits) or
broaden the D17 definition to include market-manipulation strategies
generally.

---

## P13 Lossless Protocol

### P13,D01 — Transaction Monitoring → Partial (1) (vendor-only)  [C1]
Vendor names Lossless Aegis with "Automated real-time freezing of
suspicious transactions" — a specific feature. But no T_indep source
mentions Lossless. Per rubric: specific T_vendor feature → Partial with
(vendor-only evidence) flag.

### P13,D06 — DeFi Semantic Analysis → Partial (1) (vendor-only)  [C2]
Vendor lists multi-chain support (Ethereum, Arbitrum, Polygon, BSC,
Avalanche, Fantom, Harmony, Elysium, Arthera) and describes "DeFi
protection," but does not name specific DeFi PROTOCOLS (Uniswap, Aave,
Compound). The rubric's D06 Partial criterion is "generic 'DeFi
monitoring' without named protocol list." This fits. Judgment call:
listing 9 chains is more than generic but not protocol-specific.

**Rubric sharpening suggestion:** Distinguish "chain list" (which D06
treats as Partial) from "protocol list" (which D06 treats as Full).
Suggest the rubric explicitly state: "Chain coverage alone (even
multi-chain) does not satisfy D06 Full — Full requires named DeFi
protocols (DEXes, lending markets, bridges) with semantic labels."

### P13,D17 — MEV Analysis → None (0)  [C1]
No MEV mention. Clear None.

### P13,D21 — API Integration → None (0)  [C1]
Vendor describes LERC-20 token standard and community freezing
mechanism, but no REST/GraphQL/SDK API. None.

### P13,D08 — Graph Neural Networks → None (0)  [C1]
Vendor evidence is community-stake-based reporting with no ML claim.
Clear None per the calibration-set hint.

---

## P29 Shyft Network

### P29,D11 — Travel Rule Support → Full (2)  [C1]
Shyft Veriscope is explicitly a Travel Rule network. Notabene 2024 State
of Travel Rule report (analyst, T_indep) names Shyft among the
Travel Rule platforms across 70+ jurisdictions. FATF regulator filings
list Shyft. Per worked example: "Notabene: itself a Travel Rule SaaS,
FATF stocktake names it → Full." Same logic applies to Shyft.

### P29,D14 — Verifiable Credentials → Partial (1) (vendor-only)  [C2, C3]
Vendor describes Shyft as a "global attestation and governance platform"
and references "patented security mechanisms." Attestations are
mentioned but no W3C VC, DID, or SD-JWT alignment is named. Per rubric:
"'Verifiable credentials' or 'attestation' mentioned without W3C
alignment; or proprietary attestation schema only" = Partial. Per
worked example: "Shyft Network: attestations via Veriscope → Partial."
This matches exactly.

**Rubric sharpening suggestion:** The line between Partial (proprietary
attestation) and Full (W3C-aligned) is clear in principle, but the
calibration question "W3C-aligned or proprietary?" cannot be answered
from the dossier alone — there is no statement either way. Suggest the
rubric clarify: "Absence of explicit W3C/DID/SD-JWT naming in the
vendor evidence defaults to Partial, not Full."

### P29,D01 — Transaction Monitoring → None (0)  [C2]
Vendor describes Shyft as an identity/attestation/Travel Rule layer.
The single line "patented security mechanisms that 'identifies malicious
intent almost instantly'" is too vague to qualify as a transaction-
monitoring product per the rubric's D01 Full criterion (named monitoring
product/pipeline + alert types/rules/latency/integration channel). No
named alert categories. → None. Judgment call: this could be argued
Partial under a generous read of "monitoring" but I followed the
rubric's "no named product line → None" decision rule.

**Rubric sharpening suggestion:** The rubric's D01 Decision Rule says
"if it's purely identity or compliance-workflow, None." Shyft is
identity-and-Travel-Rule; this confirms None. The rubric is clear here.

### P29,D21 — API Integration → Partial (1) (vendor-only)  [C2]
Vendor describes "OAuth2-type interface" for VASP-to-VASP transfer —
this is a specific integration pattern but not a named REST/GraphQL/SDK
endpoint family. Per rubric: "'API available' claim without endpoint
details" = Partial. Judgment call: OAuth2-type is more specific than
"API available" but less specific than "GraphQL with /tx endpoint."

### P29,D17 — MEV Analysis → None (0)  [C1]
Shyft is identity/Travel Rule infrastructure. No MEV layer. Clear None.

---

## P38 NICE Actimize

### P38,D24 — SAR Generation → Full (2)  [C1]
Vendor explicitly names "Suspicious Transaction Activity Reporting (STAR)"
and "Suspicious Activity Monitoring (SAM)" as discrete AML products. DOJ
Binance settlement (T_indep regulator) names mandatory SAR-filing
obligations. NICE Actimize is the canonical "named SAR template product"
example in the rubric worked example. High confidence.

### P38,D25 — Regulatory Reporting → Full (2)  [C1]
Vendor names "Currency Transaction Reporting (CTR)" — a US-specific
named regulatory report — plus sanctions screening and X-Sight Entity
Risk. FinCEN CVC-mixing NPR (T_indep regulator) substantiates regulator-
driven CTR demand. Worked example in rubric: "NICE Actimize: CTR +
jurisdiction-specific filings named → Full." Direct match.

### P38,D01 — Transaction Monitoring → Full (2)  [C2]
Vendor names Suspicious Activity Monitoring (SAM) as a named product
with ML+rule-based methodology, and homepage cites "5 billion+
transactions monitored daily." SoK narrative classifies NICE Actimize as
"Tx Monitoring" with "Rule-Based, ML" technical approach (T_indep). This
combines T_vendor (named SAM product) with T_indep (narrative
classification). → Full. Confident.

### P38,D08 — Graph Neural Networks → None (0)  [C1]
Vendor describes "entity-centric AML" with ML but no GNN architecture
is named, and no T_indep paper benchmarks an Actimize GNN. Per
calibration hint "traditional vendor — GNN unlikely." Clear None.

### P38,D11 — Travel Rule Support → None (0)  [C1]
NICE Actimize is traditional AML (chain coverage L0 per SoK catalog).
No Travel Rule capability is documented. Clear None.

---

## Summary of rubric ambiguities for v4 addendum

1. **D08 graph-tag boundary:** A single-word "Graph" tag in narrative.md
   should be classified more precisely — current rubric's "graph-based
   alone is Partial" is ambiguous when the only graph mention is a
   technical-approach tag rather than a product description.

2. **D17 wash-trading vs MEV worked example:** The Solidus D17 worked
   example treats wash trading as substantiation for MEV, but the D17
   operational definition is narrowly MEV strategies (sandwich, JIT,
   liquidations). This is internally inconsistent; either broaden D17 or
   move the Solidus example to D01/D10.

3. **D06 chain list vs protocol list:** Multi-chain coverage (a
   chain list) does not satisfy D06's named-DeFi-protocol criterion, but
   the rubric does not explicitly state this. Suggest adding: "Chain
   coverage alone does not satisfy D06 Full."

4. **D14 default for missing W3C statement:** When vendor mentions
   "attestations" without naming W3C VC/DID, the default should be
   Partial. The rubric implies this but doesn't state it.

5. **Calibration-set descriptions vs evidence content:** Two
   calibration-set hints (P01,D17 "vendor markets but no T_indep" and
   P09,D08 "GNN claim ambiguous in Solidus docs") implied vendor claims
   that the actual evidence files did not contain. Coders should code
   from evidence, not from hints — but the discrepancy is worth noting
   for v4.
