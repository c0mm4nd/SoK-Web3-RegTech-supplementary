# R2 Calibration Notes

Per-cell reasoning, confidence flags, and rubric-clarification suggestions for the 25-cell calibration round.

Tier labels follow rubric: **CLEAR** = rubric unambiguous, high confidence; **AMBIG** = judgment call needed; **CLARIFY** = quote from rubric that should be sharpened.

---

## P01 Chainalysis

### P01,D01 (Transaction Monitoring) — Full (2) — CLEAR
Chainalysis KYT is the textbook Full case. Vendor explicitly names KYT with real-time monitoring; wu2023tracer paper (T_indep) names Chainalysis as a forensics service performing tracing; narrative also classifies P01 as "Tx Monitoring, Forensics". Rubric worked example matches almost verbatim. High confidence.

### P01,D08 (GNN) — Partial (1) vendor-only — AMBIG
Vendor says "hundreds of clustering heuristics" and "AI-powered" but never names a GNN architecture (GCN/GAT/GraphSAGE). The pocher2023 paper has P01 in its platform_ids field but the abstract says "the private sector" providing forensics rather than explicitly naming Chainalysis's GNN. **CLARIFY:** The decision rule says `"graph-based" or "graph analytics" alone is Partial`. But Chainalysis vendor doesn't even say "graph-based" — it says "clustering heuristics". I read "clustering heuristics" as a graph-clustering claim and coded Partial. Suggest sharpening the rule to: "clustering heuristics described in the context of transaction-graph analysis → Partial; pure address-list lookup → None". Also clarify whether platform_ids tagging in a paper's index counts as T_indep when the paper abstract itself doesn't name the platform.

### P01,D13 (ZKP) — None (0) — CLEAR
No ZK language anywhere in P01 evidence. Unambiguous None.

### P01,D17 (MEV) — None (0) — CLEAR
This was flagged in the calibration set as testing the vendor-only rule, but Chainalysis vendor doesn't actually name MEV at all — Hexagate is described as "exploit/scam prevention", not MEV. So this is None, not vendor-only Partial. The calibration row design assumed vendor markets MEV; it actually does not in the dossier excerpts.

### P01,D21 (API) — Partial (1) vendor-only — AMBIG
Vendor names discrete products (KYT, Reactor, Sentinel) as SaaS offerings, strongly implying API access, but no REST/GraphQL endpoint family or auth scheme appears in the captured pages. Per rubric note: "Most vendor sites mention an API; only T_indep evidence elevates to Full reliably." **CLARIFY:** The rubric says Full requires "name at least one endpoint family or authentication scheme". For Chainalysis, KYT itself is widely known as an API product (with industry usage). The rubric forced Partial here because the captured vendor page doesn't include endpoint specifics, even though KYT being API-delivered is widely attested. Suggest adding: "If multiple T_indep sources (regulator filings, analyst reports) describe the platform's product as programmatically consumed by VASPs without naming the endpoint scheme, that counts as Full equivalent to a named endpoint." Otherwise SaaS-by-design products get Partial purely from dossier-capture artifacts.

---

## P09 Solidus Labs

### P09,D17 (MEV) — Partial (1) — AMBIG, biggest tension with rubric
This is the worked-example case in the rubric: "Solidus: wash-trading + MEV monitoring → Full (Victor 2021 wash-trade paper as T_indep anchor)". But (a) the actual Victor 2021 abstract is about wash trading on DEXes, with zero mention of MEV; (b) the Solidus vendor page doesn't name a MEV strategy category (sandwich/JIT/arbitrage); (c) only the solidus_labs_wash_trading_sep2023 analyst piece says "wash trading is related to MEV bots" — a contextual implication, not direct attestation. I coded Partial because vendor names smart-contract scam/liquidity analysis without MEV taxonomy, but the rubric's worked example explicitly says Full. **CLARIFY:** The Victor 2021 paper is not a MEV paper. Suggest rewriting the D17 worked example to either (i) drop the Solidus example or (ii) explicitly justify why wash-trading anchors MEV scoring. As written, the worked example forces a Full that the underlying evidence does not support.

### P09,D11 (Travel Rule) — None (0) — CLEAR
Solidus is market surveillance; no Travel Rule mention anywhere. Unambiguous None per rubric ("Forta Network: DeFi monitoring, no Travel Rule → None") worked-example pattern.

### P09,D08 (GNN) — None (0) — CLEAR
Narrative says "ML, Anomaly"; vendor describes "behavioral analytics" and "order book analysis". No graph framing at all. Calibration row flagged "GNN claim ambiguous" but the dossier excerpts contain no GNN ambiguity — they contain no graph claim at all. Coded None per rubric (`"No GNN evidence; tabular ML only" → None`).

### P09,D01 (Tx Monitoring) — Full (2) — CLEAR
Vendor explicitly names "Transaction Monitoring: multidimensional screening of deposits and withdrawals", HALO is the named product, and the Solidus wash-trading analyst report is T_indep coverage of the surveillance methodology. Narrative classifies Solidus primary function around KYT/surveillance. Full is unambiguous.

### P09,D14 (Verifiable Credentials) — None (0) — CLEAR
Solidus is a surveillance platform with no credential layer. Unambiguous None.

---

## P13 Lossless Protocol

### P13,D01 (Tx Monitoring) — Partial (1) vendor-only — AMBIG
Lossless Aegis is named with "Automated real-time freezing of suspicious transactions" and "3+ billion scanned transactions" — that meets the rubric Full criterion for "named monitoring product with named integration channel" (on-chain freezing). But there is zero T_indep evidence for Lossless in the shared dossier — no paper, regulator, or analyst piece mentions it. Per the universal evidence-tier rule, this becomes Partial vendor-only. **CLARIFY:** Lossless is a well-defined, on-chain mitigation tool with a clear named product, yet the absence of academic attention drops it to Partial. Suggest the rubric explicitly acknowledge: "vendor-only Partial does NOT imply 'less capable than T_indep Full'; it reflects evidence-tier asymmetry due to coverage gaps in academic/regulatory literature, especially for newer DeFi-native tools."

### P13,D06 (DeFi Semantic Analysis) — None (0) — AMBIG
Calibration row explicitly says "tests Partial vs None". Vendor positions Lossless on DeFi (LERC-20, freeze on DEXes) but never decodes contract calls into Uniswap/Aave/Curve semantic labels. The rubric Full criterion requires "names at least 3 DeFi protocols supported with semantic labels". Partial allows "Generic 'DeFi monitoring' without named protocol list". Lossless does "DeFi protection via on-chain freezing" — that's DeFi-adjacent operational scope but not "decoding smart-contract calls into human-readable activities". I coded None because Lossless doesn't do contract-call decoding at all; the freeze mechanism operates at LERC-20 transfer level. **CLARIFY:** The Partial threshold "generic DeFi monitoring without named protocols" is fuzzy — does freeze-on-DeFi-contracts count as "DeFi monitoring"? Suggest: "Partial requires the platform to OBSERVE DeFi protocol activity (contract calls, swaps, deposits); pure protection/mitigation at token-transfer level without protocol semantic awareness → None."

### P13,D17 (MEV) — None (0) — CLEAR
No MEV reference anywhere in Lossless materials.

### P13,D21 (API) — None (0) — AMBIG
Lossless homepage lists three product lines but mentions no developer API, SDK, or endpoint. The protection model appears to be on-chain (LERC-20 extension) rather than off-chain SaaS API. I coded None because no API is mentioned. **CLARIFY:** A decentralized on-chain protection tool may not need an off-chain API. The rubric definition assumes SaaS architecture. Suggest adding: "For decentralized/on-chain-only platforms where capability is delivered via smart contracts rather than off-chain API, D21 may default to None without implying capability deficit."

### P13,D08 (GNN) — None (0) — CLEAR
Narrative explicitly tags "Heuristic, Governance" — no ML, no graph. Unambiguous None.

---

## P29 Shyft Network

### P29,D11 (Travel Rule) — Full (2) — CLEAR
Veriscope is itself the named Travel Rule product, with named counterparty VASPs (Binance, Bitfinex, Huobi, Gate.io) and Notabene's industry survey naming Shyft. Rubric worked example: "platforms that are themselves Travel Rule networks → Full." Unambiguous Full.

### P29,D14 (VC) — Partial (1) vendor-only — CLEAR
This is the rubric's worked example: "Shyft Network: attestations via Veriscope → Partial (attestations without explicit W3C VC alignment)". Vendor calls it "attestation and governance platform" with no W3C/DID/SD-JWT alignment. Direct rubric match.

### P29,D01 (Tx Monitoring) — None (0) — AMBIG
Shyft is identity infrastructure, not a monitoring product. Vendor mentions "patented security mechanisms that identifies malicious intent almost instantly" — that could be read as a monitoring claim, but no monitoring product, alert categories, or surveillance pipeline is named. **CLARIFY:** The phrase "identifies malicious intent almost instantly" is vague marketing copy. Per the D01 None criterion "pure data-indexing provider with no alert layer" — Shyft is identity infrastructure with no alert layer, so None. But the marketing language is suggestive enough that a different coder could plausibly call it Partial. Suggest the rubric explicitly direct: "marketing phrases like 'identifies threats instantly' without a named monitoring product → None, not Partial."

### P29,D21 (API) — Partial (1) vendor-only — AMBIG
Veriscope's "VASP-to-VASP customer data transfer" with "Pay-As-You-Go" per-transaction pricing strongly implies a programmatic API, but no REST/GraphQL/SDK endpoint family is documented. Same dimension-D21 issue as Chainalysis: SaaS implication without endpoint specifics → Partial vendor-only.

### P29,D17 (MEV) — None (0) — CLEAR
Identity/Travel Rule platform; no MEV layer. Unambiguous None.

---

## P38 NICE Actimize

### P38,D24 (SAR Generation) — Partial (1) vendor-only — AMBIG
Vendor explicitly names "Suspicious Transaction Activity Reporting (STAR)" — that satisfies rubric Full criterion "named SAR template / SAR filing integration". But no T_indep source in the dossier names NICE's STAR specifically. The rubric Full requires T_indep meeting the criterion; vendor-only specific named feature → Partial. **CLARIFY:** This is the cleanest case of the vendor-bias guard working as designed — but it produces a Partial for a well-documented enterprise product (NICE STAR is broadly known). The dossier coverage gap (no analyst report / regulator filing in our shared set specifically names NICE Actimize's SAR module) drops a textbook Full to Partial. Suggest noting in the rubric: "For traditional enterprise vendors with mature products but thin dossier coverage, vendor-only Partial is expected and not a capability judgment."

### P38,D25 (Regulatory Reporting) — Partial (1) vendor-only — CLEAR
Vendor names CTR (a US-specific FinCEN format) — satisfies "named jurisdiction-specific report format". No T_indep. → Partial vendor-only. Same logic as D24.

### P38,D01 (Tx Monitoring) — Full (2) — CLEAR
Vendor names "Suspicious Activity Monitoring (SAM)" with scale metrics ("5 billion+ transactions daily", "$6 trillion protected daily"), and the SoK narrative classifies P38 as "Primary function: Tx Monitoring". Narrative = T_indep per rubric. Unambiguous Full.

### P38,D08 (GNN) — None (0) — CLEAR
Narrative says "Rule-Based, ML" — implies tabular ML, not graph. Vendor positions "entity-centric AML... infused with AI and machine learning" without graph framing. Per rubric: tabular ML only → None.

### P38,D11 (Travel Rule) — None (0) — CLEAR
NICE Actimize is traditional AML; no FATF Recommendation 16 / VASP messaging anywhere. Calibration row design explicitly flagged "no Travel Rule".

---

## Cross-cutting rubric ambiguities to feed back

1. **Narrative-as-T_indep ambiguity.** The rubric says `T_indep` includes "the platform's narrative.md file explicitly naming the capability". But the cleaned narratives are short Table-4 catalog excerpts plus generic Section-4 quotes. When the catalog row says "Primary function: Tx Monitoring" for P38, is that "explicitly naming the capability"? I interpreted Yes (and used it for P01/D01, P09/D01, P38/D01). Suggest the rubric explicitly affirm or limit this: "Catalog-table function tags in narrative.md count as T_indep attestation of the dimension named in the tag."

2. **Platform_ids tagging in cross-platform papers.** Many papers have a `platform_ids` field listing several platforms even when the paper abstract names only one or none. For example, pocher2023 lists `P01;P02;P03;P04;P08` but the abstract only directly attests Elliptic via the Elliptic Data Set. Should `platform_ids` tagging count as T_indep, or only direct abstract mentions? I treated direct-mention as T_indep and indirect-tagging as supporting T_vendor-only Partial. Suggest the rubric clarify: "T_indep requires the platform to be named in the paper abstract/body, not merely tagged via the dossier index."

3. **D21 (API) baseline-skew problem still present.** Despite the rubric's explicit note that D21 has the highest T_vendor base rate, the requirement to name an endpoint family is so strict that mature SaaS products (Chainalysis KYT, Veriscope) get Partial. Suggest a clearer escalator: "API delivery attested by ≥2 T_indep sources describing the platform's product as programmatically consumed → Full equivalent."

4. **Decentralized/on-chain products and D21.** For Lossless (D21), the protection layer is on-chain; there may be no off-chain API by design. The rubric implicitly assumes SaaS architecture. Suggest: "For platforms whose capability is delivered via smart contracts, D21 may default to None without that implying capability deficit."

5. **D17 (MEV) worked example for Solidus is inconsistent with the underlying evidence.** The rubric says Solidus → Full anchored by Victor 2021. But Victor 2021 is a wash-trading paper, not a MEV paper. This creates direct tension between the worked example and the evidence-tier rule. Suggest either re-anchoring the example to a different paper or moving Solidus/D17 to Partial in the worked example.

6. **"Marketing-only" boundary on monitoring dimensions.** P29 (Shyft) markets "identifies malicious intent almost instantly" — this is vague but suggestive. Currently the None/Partial boundary lets this go either way. Suggest tighter language: "phrases like 'detects threats instantly' without a named monitoring product or alert category → None."
