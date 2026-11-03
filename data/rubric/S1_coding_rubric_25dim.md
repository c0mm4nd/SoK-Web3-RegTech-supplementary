# E1 v4 Coding Rubric

This is the **single authoritative rubric** for both coders. v3's rubric
left "Full vs Partial" underspecified; v4 names specific evidence types,
provides worked examples, and gives a decision rule for ambiguous cases.

## Universal scoring scale

For every (platform, dimension) cell, choose exactly one of:

- **Full (2)** — at least one source in the shared dossier explicitly
  and unambiguously documents this platform offering this capability
  with a specific, named feature, product line, named protocol, named
  chain, or named integration.
- **Partial (1)** — at least one source mentions this platform in
  connection with this capability, but the evidence is qualified:
  beta-only, single-chain only, single-integration only, in a roadmap
  rather than production, marketing-only language without an underlying
  named feature, or only an indirect implication.
- **None (0)** — no source in the shared dossier links this platform
  to this capability.

## Universal evidence-quality rule (M4 vendor-bias built into rubric)

Before assigning Full or Partial, classify the supporting evidence by tier:

- **T_vendor:** vendor self-disclosure only (files under `platforms/<P>/vendor_*.txt`).
- **T_indep:** independent corroboration available (any file under
  `cross_platform/papers/`, `cross_platform/regulator/`,
  `cross_platform/analyst/`, OR the platform's `narrative.md` file
  explicitly naming the capability).

**Decision rule:**
- If T_indep evidence exists AND meets the dimension-specific criteria
  below → Full (2).
- If only T_vendor evidence exists, AND the vendor evidence is specific
  (named feature, named chain, named integration, named product line)
  → Partial (1), regardless of how confidently the vendor markets it.
- If only T_vendor evidence exists AND it is generic ("we provide AML
  compliance" without naming a specific feature) → None (0).
- If T_indep evidence contradicts T_vendor (independent benchmark shows
  the capability is poor / not deployed) → None (0).

This rule is the **vendor-bias guard built directly into the scoring
scale**, so M4 is satisfied by every Full and Partial assignment.

## Universal hard rules

1. The evidence-citation field must point to a relative path under
   `data/evidence/shared/` that exists on disk.
2. Rationale must (i) quote or closely paraphrase a specific fragment
   from the cited file, AND (ii) state which tier the evidence is
   (T_vendor or T_indep). One sentence, no template phrases.
3. If a cell scores Full or Partial on T_vendor evidence alone, the
   rationale must end with the phrase "(vendor-only evidence)".
4. Code only from the shared evidence pack. Do not retrieve additional
   web pages during scoring, do not fill gaps from memory, and do not
   read the other coder's CSV.

---

## Per-dimension criteria

### D01 — Transaction Monitoring

**Operational definition:** Continuous or near-continuous surveillance
of on-chain transactions emitting rule-based or model-based alerts.

**Full (2)** — Source documents a named monitoring product/pipeline
(e.g., "Chainalysis KYT", "Forta Detection Bots", "Hypernative
Sentinels") with at least one of: named alert types, named rule
families, named latency target, named integration channel (webhook,
SDK, API).

**Partial (1)** — Mention of "monitoring" as a general capability
without a named product line; or batch/report-only output (no real-time
alerting); or only chain-explorer style query without alert generation.

**None (0)** — No monitoring documentation; or pure data-indexing
provider with no alert layer; or audit-time analytics only.

**Worked examples.**
- Chainalysis: "KYT real-time pipeline with Sanctioned, Mixing, Darknet
  alert categories" → **Full**. T_indep: TRacer paper names
  Chainalysis monitoring as a forensics service.
- Bitquery: "blockchain data API and webhooks for transactions" but
  no named alert categories → **Partial**.
- Privado ID: identity-issuance platform, no transaction monitoring
  mentioned → **None**.

**Decision rule for ambiguous:** if the source describes an "alert" or
"detection" function tied to specific transaction types, Full; if it
only describes data delivery (index/query), Partial; if it's purely
identity or compliance-workflow, None.

---

### D02 — Real-Time Risk Scoring

**Operational definition:** Numeric or banded risk score returned for
an address or transaction within seconds-to-minutes via API or UI.

**Full (2)** — Source names a scoring product (e.g., "Elliptic Lens",
"TRM Wallet Screening", "Merkle Science Compass") AND specifies either
score range/banding, scoring inputs, or API latency.

**Partial (1)** — Source mentions "risk scoring" or "risk profile"
generally; or report-only delivery (no API); or one-feature score
without composite output.

**None (0)** — No scoring claim; or only attribution/labels without
a derived risk number.

**Worked examples.**
- Elliptic Lens: "real-time wallet risk scoring banded 1–10 with
  Sanctions, Hack, Mixing inputs" → **Full**. T_indep: SoK narrative
  on Elliptic.
- Scorechain: vendor page mentions "risk scoring" without inputs or
  banding → **Partial** (vendor-only evidence).
- KILT Protocol: credential infrastructure, no risk scoring → **None**.

---

### D03 — Address Attribution

**Operational definition:** A curated database mapping blockchain
addresses to real-world entities (exchanges, mixers, ransomware
operators, sanctioned wallets, etc.).

**Full (2)** — Source documents an attribution database with at least
one of: named coverage figure (e.g., "650M+ addresses"), named entity
types covered, named clustering technique, or T_indep paper that
explicitly benchmarks the platform's attribution.

**Partial (1)** — Source mentions "attribution" or "entity labels"
generally; or labels limited to public sanctions lists only (no
proprietary clustering); or label coverage limited to one chain.

**None (0)** — No attribution capability; or pure infra/identity
platform without entity labels.

**Worked examples.**
- Elementus: "650M+ addresses attributed" in vendor + Forbes profile
  → **Full**. T_indep: Forbes Fintech 50.
- Crystal Intelligence: "verified data on 118,000+ entities" →
  **Full** (specific entity-count number).
- AMLBot: "address risk check" without attribution database mentioned
  → **None**.

---

### D04 — Multi-Hop Tracing

**Operational definition:** Following fund flows through chains of
intermediate addresses across arbitrary numbers of hops.

**Full (2)** — Source names a tracing product/feature (e.g.,
"Chainalysis Reactor", "TRM Forensics", "Elementus Investigator") and
explicitly documents multi-hop tracing UI or API.

**Partial (1)** — Single-hop tracing only; or graph-visualization tool
without explicit tracing logic; or only available in batch reports.

**None (0)** — No tracing capability documented.

**Worked examples.**
- Chainalysis Reactor: "trace funds across multiple addresses and
  hops" → **Full**. T_indep: Wu et al. 2023 TRacer paper explicitly
  names Chainalysis tracing.
- Bitquery: graph-API access but no explicit multi-hop tracing UI →
  **Partial**.
- Polygon ID: identity platform, no tracing → **None**.

---

### D05 — Cross-Chain Tracking

**Operational definition:** Tracking assets as they move between
different blockchains via bridges, wrapped tokens, or atomic swaps.

**Full (2)** — Source documents support for at least 5 chains AND
explicitly names bridge monitoring or wrapped-asset tracking.

**Partial (1)** — Multi-chain coverage but no explicit bridge tracking;
or bridge tracking limited to one bridge protocol; or "multi-chain
visibility" claim without bridge-event correlation.

**None (0)** — Single-chain platform; or chain-agnostic infra without
correlation logic.

**Worked examples.**
- TRM Labs: "30+ chains plus bridge attribution across Wormhole,
  Synapse, LayerZero" → **Full** if independent corroboration exists,
  else **Partial** if only on vendor page.
- Bitquery: "indexes 20+ chains via unified GraphQL" but no bridge
  correlation → **Partial**.
- Solidus Labs: surveillance focus on one venue → **None**.

---

### D06 — DeFi Semantic Analysis

**Operational definition:** Decoding smart-contract calls into
human-readable activities (e.g., "swap USDC→ETH on Uniswap v3",
"borrow on Aave"), naming specific DeFi protocols.

**Full (2)** — Source names at least 3 DeFi protocols supported with
semantic labels; or documents a labelling framework (Nansen Smart
Money, Hypernative protocol map).

**Partial (1)** — Generic "DeFi monitoring" without named protocol
list; or contract-call decoding without protocol semantics.

**None (0)** — No DeFi semantic layer; or contract data delivered as
raw bytes/ABI without labelling.

**Worked examples.**
- Nansen: "labels Uniswap, Aave, Curve, Compound, Lido, GMX, dYdX
  pools and pools" → **Full**.
- Hypernative: "monitors lending protocols, DEXs, bridges" listing
  specific protocols → **Full**.
- ComplyAdvantage: traditional AML with no DeFi labelling → **None**.

---

### D07 — Smart Contract Analysis

**Operational definition:** Static/dynamic analysis of contract code
for vulnerabilities, anomalies, or compliance-relevant patterns.

**Full (2)** — Source names a contract-analysis product/methodology
(decompilation, formal verification, taint analysis on bytecode); a
T_indep paper points to the platform's contract analytics; or the
platform itself is a contract-security tool with documented detector
families.

**Partial (1)** — Generic "smart contract risk" claim without named
analysis approach; or contract scanning limited to deploy-time without
runtime analysis.

**None (0)** — No contract analysis; pure on-chain monitoring of
transaction patterns.

**Worked examples.**
- Dedaub: documented decompilation + formal-method contract analysis,
  with peer-reviewed founder publications → **Full**. T_indep
  available.
- Hypernative: "smart contract attack detection" in vendor with
  named detector categories → **Partial** (vendor-only specifics).
- AMLBot: address screening only → **None**.

---

### D08 — Graph Neural Networks (GNNs)

**Operational definition:** Use of GNN architectures (GCN, GraphSAGE,
GAT, temporal-GNN variants) for fraud or AML detection in production
analytics.

**Full (2)** — A peer-reviewed paper benchmarks the platform's GNN
(e.g., Weber 2019 on Elliptic; Wu 2023 TRacer); OR vendor whitepaper
explicitly names a GNN architecture in use.

**Partial (1)** — Vendor mentions "graph analytics" or "graph-based ML"
without naming GNN; or research preview/blog only, not production.

**None (0)** — No GNN evidence; or tabular ML only.

**Worked examples.**
- Elliptic: Weber 2019 explicitly uses Elliptic dataset to benchmark
  GCN → **Full** (T_indep).
- Chainalysis: "graph analytics" in vendor blog without GNN
  architecture → **Partial**.
- AMLBot: no ML claims → **None**.

**Decision rule for ambiguous:** "graph-based" or "graph analytics"
alone is Partial; explicit "neural", "GCN", "GraphSAGE", "attention
over graph" is Full when in a peer-reviewed or technical context.

---

### D09 — ML/DL Techniques (Beyond GNN)

**Operational definition:** Use of supervised/unsupervised classifiers
(RF, XGBoost, MLP, NLP-style language models) for compliance-relevant
detection.

**Full (2)** — Source names a specific model family (RF, XGBoost,
transformer, autoencoder) AND a use case; OR a peer-reviewed paper
benchmarks the platform's ML.

**Partial (1)** — "ML-powered" / "AI-driven" without named architecture;
or rule-engine + light statistics only.

**None (0)** — Pure rule-based; or pure heuristic taint analysis
without learned components.

**Worked examples.**
- Pocher 2023 anomaly detection paper benchmarks ComplyAdvantage's
  algorithmic class → **Full** for P35 D09.
- Hypernative "AI-powered anomaly detection" → **Partial**.
- TransactID: pure messaging protocol → **None**.

---

### D10 — Behavioural Analytics

**Operational definition:** Profiles of address or entity behaviour
(activity patterns, peer-group comparison, deviation detection)
beyond single-transaction features.

**Full (2)** — Source names a behavioural profile/cluster product
(Nansen "Smart Money", Solidus "Behaviour-of-Interest", Arkham
"Entities") with named segments.

**Partial (1)** — Generic "behavioural risk" claim; or single-feature
"velocity" or "frequency" rule without composite profile.

**None (0)** — No behavioural framing; transaction-level only.

**Worked examples.**
- Nansen Smart Money: documented behaviour-based segments → **Full**.
- Forta: rule-based monitoring with some heuristic flags → **Partial**.
- Polygon ID: identity, no behaviour → **None**.

---

### D11 — Travel Rule Support

**Operational definition:** Implementation of FATF Recommendation 16:
exchange of originator/beneficiary information between VASPs.

**Full (2)** — Platform is itself a Travel Rule network (Notabene,
Sygna, TRISA, Shyft Veriscope, 21 Analytics, TransactID, CipherTrace
TRISA bridge); OR Travel Rule support documented with specific
counterparty integration list.

**Partial (1)** — Travel Rule integration via partner; or "Travel
Rule-ready" claim without active counterparty network; or roadmap
status only.

**None (0)** — No Travel Rule capability.

**Worked examples.**
- Notabene: itself a Travel Rule SaaS, FATF stocktake names it →
  **Full** (T_indep).
- ComplyAdvantage: "Travel Rule via partner" without specifics →
  **Partial**.
- Forta Network: DeFi monitoring, no Travel Rule → **None**.

---

### D12 — KYC Integration

**Operational definition:** Identity verification (KYC) integrated
into the compliance workflow, either first-party or via documented
partner.

**Full (2)** — First-party KYC pipeline documented with named
documents/biometric flow; OR named KYC partner integration; OR
T_indep regulatory filing describing the KYC workflow.

**Partial (1)** — "KYC-ready" claim without partner specifics; or KYC
mentioned only in marketing without integration documentation.

**None (0)** — Pure address-only platform; no identity layer.

**Worked examples.**
- ComplyAdvantage: KYC + sanctions screening core product →
  **Full** (T_indep: UK FCA / industry coverage).
- TRM Labs: documents KYC partner integrations → **Full** if named.
- Privado ID: identity wallet infrastructure, no compliance workflow
  → **Partial** for D12 (it's an identity platform but its compliance
  use is downstream).

---

### D13 — Zero-Knowledge Proofs

**Operational definition:** Use of ZKP (Groth16, PLONK, STARK,
Bulletproofs, etc.) for compliance verification or credential
disclosure.

**Full (2)** — Source names the ZK scheme family AND its use case
(Polygon ID circuits, Privado ID Issuer Node, KILT credentials).

**Partial (1)** — "Zero-knowledge" mentioned without scheme; or ZKP
in roadmap/research-blog only.

**None (0)** — No ZK mention.

**Worked examples.**
- Polygon ID / Privado ID / KILT Protocol: ZK circuits documented as
  core stack → **Full**.
- Chainalysis: no ZK in product line → **None**.
- TRM Labs: blog mentions ZK exploration → **Partial**.

---

### D14 — Verifiable Credentials

**Operational definition:** W3C VC / DID model usage for issuing or
verifying credentials.

**Full (2)** — Source names W3C VC, DID, SD-JWT, or specific
credential schema (Polygon ID Issuer, KILT credentials, Shyft
attestations).

**Partial (1)** — "Verifiable credentials" or "attestation" mentioned
without W3C alignment; or proprietary attestation schema only.

**None (0)** — No credential layer.

**Worked examples.**
- KILT Protocol: W3C DID + VC credential platform → **Full**.
- Shyft Network: attestations via Veriscope → **Partial**
  (attestations without explicit W3C VC alignment).
- Crystal Intelligence: forensics tool, no credential layer → **None**.

---

### D15 — Privacy Coin Analysis

**Operational definition:** Analytics on Monero, Zcash, Dash, or
other privacy-focused chains.

**Full (2)** — Source explicitly names privacy-coin coverage with at
least one of: chain name (Monero, Zcash), heuristic technique, or
T_indep paper (Kumar 2017 Monero traceability; Kappos 2018 Zcash).

**Partial (1)** — "Privacy coin support" claim without named chain;
or partial heuristic coverage limited to view-key analysis.

**None (0)** — No privacy-chain coverage; only mainstream blockchains.

**Worked examples.**
- Chainalysis: Monero / Zcash tracing claimed in vendor + analyst
  reports → **Full** if T_indep.
- Elementus: "deep multi-chain coverage" without naming privacy chains
  → **None**.
- KILT: identity protocol, no chain analysis → **None**.

---

### D16 — Mixer Detection

**Operational definition:** Identification of transactions involving
mixing services (Tornado Cash, Wasabi CoinJoin, Samourai Whirlpool,
custodial mixers).

**Full (2)** — Source names a specific mixer-detection capability or
named mixer-cluster identification (T_indep paper: Wu 2021 mixing
service detection).

**Partial (1)** — "Mixer risk" tag without detection methodology; or
sanctions-list match only.

**None (0)** — No mixer-detection layer.

**Worked examples.**
- TRM Labs: mixer-detection alert categories named → **Full**.
- ComplyAdvantage: sanctions screening that catches OFAC Tornado Cash
  → **Partial** (passive sanctions match, not active mixer detection).
- Bitquery: data API, no mixer logic → **None**.

---

### D17 — MEV Analysis

**Operational definition:** Detection or quantification of MEV
(maximal extractable value) extraction patterns: sandwich attacks,
arbitrage, liquidations, JIT liquidity.

**Full (2)** — Source names a MEV-detection product with named MEV
strategy categories (Hypernative MEV-detect, Solidus MEV monitor,
Forta MEV bots); OR T_indep paper (Daian 2020) names the platform.

**Partial (1)** — "DeFi risk" or "front-running protection" without
named MEV strategy.

**None (0)** — No MEV layer.

**Worked examples.**
- Hypernative: documented MEV protection → **Full**.
- Solidus: wash-trading + MEV monitoring → **Full** (Victor 2021
  wash-trade paper as T_indep anchor).
- Notabene: Travel Rule platform, no MEV → **None**.

---

### D18 — Intent Recognition

**Operational definition:** Recognition of user-stated intents in
intent-centric architectures (Across, UniswapX, CowSwap).

**Full (2)** — Source names support for an intent protocol; OR
analytics over intent expression / solver routing.

**Partial (1)** — Generic "DeFi monitoring" that incidentally captures
intent-related orders, without explicit intent-layer recognition.

**None (0)** — No intent-layer awareness.

**Worked examples.**
- Across, UniswapX integration documented in vendor → would be
  **Full** but unlikely in our sample.
- Hypernative: general DeFi monitoring → **None** for intent-specific.
- Most platforms in our sample → **None** (this is a known coverage gap).

---

### D19 — Account Abstraction Support

**Operational definition:** Analytics on ERC-4337 / AA smart wallets.

**Full (2)** — Source names ERC-4337 or AA smart-wallet support;
explicitly handles UserOperation traces or named bundlers/paymasters.

**Partial (1)** — General "smart wallet" coverage without ERC-4337
mention.

**None (0)** — EOA-only analytics or no specific AA handling.

**Worked examples.**
- Most platforms in our sample → **None** (known gap).
- Hypernative or Forta if they document AA support → **Partial**
  unless specific.

---

### D20 — Solver Monitoring

**Operational definition:** Monitoring of solver behaviour in
intent-centric systems (price improvement audit, routing fairness).

**Full (2)** — Source names solver monitoring with metrics; very
unlikely in our sample.

**Partial (1)** — Mention of "auction" or "competitive routing"
analytics.

**None (0)** — No solver-layer awareness — expected default for
nearly all platforms.

**Worked examples.**
- Nearly universal **None** is correct here.

---

### D21 — API Integration

**Operational definition:** Public / partner / on-premise API for
programmatic access to platform functionality.

**Full (2)** — Vendor docs name a specific API (REST, GraphQL, gRPC,
SDK), AND name at least one endpoint family or authentication scheme.

**Partial (1)** — "API available" claim without endpoint details; or
docs hidden behind sales contact.

**None (0)** — UI-only; no programmatic access.

**Worked examples.**
- Bitquery: documented GraphQL endpoints + auth tokens → **Full**.
- Chainalysis KYT API: explicitly named with endpoint families →
  **Full**.
- Refinitiv World-Check: "available via integration" but no
  named endpoints visible → **Partial**.

**Note:** This dimension typically has the highest T_vendor base rate.
Most vendor sites mention an API; only T_indep evidence (a paper or
analyst report describing the API) elevates to Full reliably.

---

### D22 — Real-Time Alerting

**Operational definition:** Push notification of compliance events
(webhook, streaming API, real-time UI) within seconds-to-minutes.

**Full (2)** — Source names a webhook / streaming-alert capability
with named alert categories AND named delivery mechanism.

**Partial (1)** — "Alerts" generic; or email-only daily digest; or
in-UI notifications without push channel.

**None (0)** — Batch-only output; no alerting layer.

**Worked examples.**
- Forta: "real-time bots emit alerts via webhook subscriptions" →
  **Full**.
- Coinfirm: alerts mentioned in vendor without delivery channel →
  **Partial**.
- Refinitiv: data delivery only → **None**.

---

### D23 — Case Management

**Operational definition:** Workflow tooling for compliance officers
to triage, assign, investigate, resolve alerts.

**Full (2)** — Source names a case-management UI/API with workflow
states, evidence attachments, audit trail.

**Partial (1)** — "Case-management" mentioned without UI specifics;
or export-to-spreadsheet workflow only.

**None (0)** — Pure detection / risk-scoring tool without
investigator-facing workflow.

**Worked examples.**
- TRM Labs / Chainalysis Reactor: documented case-management →
  **Full**.
- Bitquery: data API, no workflow → **None**.
- Coinfirm: "case mgmt" claim without UI details → **Partial**.

---

### D24 — SAR Generation

**Operational definition:** Suspicious Activity Report generation —
template, regulator-format export, or workflow to file SAR.

**Full (2)** — Source names a SAR template / SAR filing integration /
specific regulator format (FinCEN SAR, MAS STR).

**Partial (1)** — "SAR-ready" claim without specific template / format;
or general report-export capability framed as SAR.

**None (0)** — No SAR capability.

**Worked examples.**
- NICE Actimize: FinCEN SAR templates documented → **Full**.
- ComplyAdvantage: SAR-ready workflow → **Partial** to **Full**
  depending on what doc says.
- Forta: open monitoring, no SAR layer → **None**.

---

### D25 — Regulatory Reporting

**Operational definition:** Jurisdiction-specific regulatory reports
beyond SAR (CTR, MiCA Travel Rule, MAS, FCA reports).

**Full (2)** — Source names jurisdiction-specific report format/types
with at least one named jurisdiction.

**Partial (1)** — "Regulatory reporting" generic; or CSV export only.

**None (0)** — No reporting capability.

**Worked examples.**
- NICE Actimize: CTR + jurisdiction-specific filings named →
  **Full**.
- Fenergo: client-lifecycle management touching reporting → **Partial**.
- Polygon ID: identity, no reporting → **None**.

---

## Worked example of the evidence-tier rule (M4 guard) in action

Suppose for (P01 Chainalysis, D03 Address Attribution):

- Vendor file `platforms/P01/vendor_solutions.txt` says "Chainalysis
  maintains the industry's largest address attribution database" — but
  no number, no benchmark.
- Cross-platform file `cross_platform/papers/wu2023tracerscalablegraphbased.txt`
  says "forensics services like Chainalysis and Elliptic perform
  attribution".

Both pieces support D03 = at-least-Partial. The T_indep paper makes it
**Full** under the universal rule. The rationale should cite the paper
as the primary anchor and mention vendor as corroborating.

Now suppose for (P09 Solidus Labs, D17 MEV Analysis):

- Vendor file says "MEV anomaly detection".
- No third-party file names Solidus + MEV.

This is T_vendor-only with a specific feature name. Score **Partial**,
not Full, and append "(vendor-only evidence)" to the rationale.

---

## Calibration mandate

Before full coding, both coders code the same 25-cell calibration
sample (5 platforms × 5 dimensions chosen to span easy, ambiguous, and
hard cells). Disagreements are logged; any rubric ambiguity revealed
is documented as an *addendum* to this rubric file (not silently
revised). After calibration both coders then code all 1025 cells.
