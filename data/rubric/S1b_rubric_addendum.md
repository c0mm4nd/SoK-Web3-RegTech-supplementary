# E1 v4 Rubric Addendum (post-calibration)

This addendum was produced after the 25-cell calibration round
(`data/calibration_R1.csv`, `data/calibration_R2.csv`, plus the two
`calibration_R*_notes.md` files). It does **not** silently revise the
original `coding_rubric_v4.md`; instead it explicitly logs the rubric
ambiguities both coders flagged and resolves each.

Calibration κ (linear-weighted) was **0.805** with 21 of 25 cells in
exact agreement. The 4 disagreements all map onto rubric ambiguities
addressed below. With this addendum applied, projected agreement on
the calibration set rises to ≈ 24 / 25.

## A. Bug fix in D17 worked example

**Original rubric text (D17, "Worked examples"):**
> Solidus: wash-trading + MEV monitoring → **Full** (Victor 2021
> wash-trade paper as T_indep anchor).

**Problem.** Victor & Weintraud 2021 is a wash-trading paper that does
not discuss MEV. Both coders flagged this; the operational definition
of D17 (sandwich attacks, JIT, arbitrage, liquidations) is internally
inconsistent with using a wash-trading paper as the MEV anchor.

**Resolution.**
- Wash-trading detection is now treated as **D10 Behavioural Analytics**
  evidence, not D17 MEV evidence.
- For Solidus / D17 specifically: the shared dossier contains no
  evidence linking Solidus to sandwich attacks, JIT, arbitrage, or
  liquidations. Correct score → **None**.
- For all D17 cells: T_indep evidence requires a paper, regulator
  filing, or analyst report that explicitly discusses MEV strategies
  (Flash Boys 2.0 / Daian 2020 is the canonical academic anchor).

## B. D06 — chain list ≠ DeFi protocol list

**Both coders flagged.** A vendor listing "we cover 30+ chains" is
chain coverage, not DeFi semantic analysis. Semantic analysis requires
the vendor to name specific *DeFi protocols* it decodes — Uniswap,
Aave, Curve, Lido, GMX, etc.

**Resolution — D06 amended.**
- "Multi-chain coverage" alone, even with named chains, does not earn
  Partial on D06. The vendor must name decoded *protocols*, not chains.
- Partial requires: at least one named DeFi protocol with reference to
  decoded activity types (swap / borrow / lend / stake).
- Full requires: at least three named protocols + activity labelling.

For Lossless / D06 specifically: vendor names LERC-20 and "on-chain
freezing" but does not decode any DeFi protocol semantics → **None**.

## C. Full path via specific vendor evidence (NICE Actimize case)

**The over-strictness problem.** The universal evidence-tier rule
required T_indep for Full. But cases like NICE Actimize SAR (named
STAR / SAM product + scale claims + named jurisdictional report
formats CTR) are clearly Full-grade vendor evidence; the only reason
no T_indep names them is that academic literature does not benchmark
traditional enterprise AML vendors.

**Resolution — universal rule amended.** Full may be reached by EITHER:

- **(a) T_indep path:** T_indep evidence meets the dimension criteria
  (was: the only path).
- **(b) Vendor-multi-element-specific path (new):** T_vendor evidence
  satisfies dimension criteria AND names ≥ 2 of:
  - specific product line name (e.g., "SAM", "STAR", "Reactor")
  - specific feature set / alert categories / report formats
  - specific scale metric ("5B transactions daily", "650M+ addresses")
  - specific named integration (named chains, partners, regulators)
  - specific compliance protocol or standard reference (FATF R.16,
    W3C VC, FinCEN SAR)

  AND no T_indep contradicts it.

**Disclosure rule:** Vendor-multi-element-specific Full cells must end
the rationale with `(vendor-specific Full)` to flag that no academic /
regulator / analyst third-party benchmark exists. This preserves the
M4 vendor-bias guard transparency while not denying the score.

Tier of rationale-suffix flags after this amendment:
- `(vendor-specific Full)` — score=2, T_vendor multi-element only.
- `(vendor-only evidence)` — score=1, T_vendor specific but
  single-element.
- (no flag) — score=2 with T_indep, or score=1 with T_indep partial
  match, or score=0.

**Effect on the four calibration disagreements:**

| Cell | R1 | R2 | Resolution |
| --- | --- | --- | --- |
| P09 D17 | 0 | 1 | Both → 0 per Bug A. |
| P13 D06 | 1 | 0 | Both → 0 per Resolution B. |
| P38 D24 | 2 | 1 | Both → 2 with `(vendor-specific Full)` per Resolution C. |
| P38 D25 | 2 | 1 | Both → 2 with `(vendor-specific Full)` per Resolution C. |

## D. D14 — implicit Partial for unaligned attestations

**R1 flagged.** When a vendor mentions "attestations" without naming
W3C VC / DID / SD-JWT, the original D14 wording implies Partial but
does not state it.

**Resolution — D14 amended.**
- Explicit Partial: "attestations" / "claims" / "credentials" mentioned
  without W3C VC / DID / SD-JWT framing → **Partial**.
- Full still requires W3C VC, DID, or SD-JWT explicit alignment, OR a
  T_indep source confirming the platform implements one of those
  standards.

## E. D21 — decentralized / on-chain platforms

**R2 flagged.** D21's operational definition assumes a SaaS / off-chain
architecture. On-chain protection tools (Lossless, Forta when used as
on-chain detection only) may genuinely not have an off-chain API —
that's not a capability deficit, it's a different architecture.

**Resolution — D21 amended.**
- For decentralized / on-chain-only platforms (architecture =
  `Decentralized` in the platform catalog) where the capability is
  delivered via smart contracts rather than off-chain API:
  - D21 score = **None** is acceptable WITHOUT implying capability
    deficit.
  - Rationale must include the phrase `(on-chain architecture; D21 not
    applicable)`.
- This handles platforms that "have no API by design," not platforms
  that "have an API but didn't document it."

## F. Marketing-language threshold for D01 / D22 / D17

**R2 flagged.** Phrases like "identifies threats instantly" or
"detects malicious intent" are vague marketing rather than named
monitoring / alerting / MEV capabilities. The original rubric let
these slip into Partial.

**Resolution — marketing-only language clarification.**
- For D01, D22, D17: marketing claims without a named product line,
  named alert category, or named MEV strategy → **None**, not Partial.
- A phrase like "identifies threats instantly" is None unless the
  vendor also names the product or detection categories.

## G. T_indep boundary — what counts and what doesn't

**R2 flagged two boundary issues.** Addendum resolves both.

### G.1 Narrative.md catalog tags

Catalog-table tags inside `platforms/<P>/narrative.md` (e.g.,
"Primary function: Tx Monitoring", "Technical approach: Graph,
Attribution") **do count as T_indep attestation of the dimension named
in the tag**. The catalog row was compiled by the SoK authors from
multiple sources and is treated as a third-party synthesis.

Caveat: a single technical-approach tag like "Graph" attests the
*existence* of graph-based methods at the platform but does not by
itself prove GNN (D08). For D08, the tag is Partial-grade T_indep
support; T_indep Full for D08 requires a peer-reviewed paper that
explicitly benchmarks the platform's GNN architecture (e.g., Weber 2019
for Elliptic).

### G.2 Cross-platform paper `platform_ids` tagging

Many cross-platform sources list multiple platforms in their
`platform_ids` field of `shared_index.csv` (e.g.,
`azad2025machinelearningblockchain.txt` tagged P01;P02;P04;P05;P08).
But the abstract may directly name only one platform; the others were
inferred from the file's "Implications for Web3 RegTech coding:"
section rather than named in the source text.

**Resolution.** T_indep evidence for a platform from a cross-platform
source requires the platform to be **named in the source text itself**
(abstract, paper body, regulator filing text, analyst report text),
**not** merely tagged in the dossier index. The index is a navigation
aid only.

## H. Calibration set hints vs evidence content

**R1 flagged.** Two calibration-set hints implied claims that the
shared dossier doesn't actually contain (e.g., "GNN claim ambiguous in
Solidus docs" — no GNN ambiguity was actually present). Coders should
code from evidence, not from hints.

**No rubric change required** — this is already the rule. But the
addendum explicitly affirms it for the full coding round: ignore any
metadata about the cell except the evidence files themselves.

---

## Effect summary

| Source of disagreement | Resolution | Effect on full coding |
| --- | --- | --- |
| D17 wash-trading bug | A | -1 false-positive Partial across sample |
| D06 chain-list confusion | B | several None corrections expected |
| Over-strict Full rule | C | NICE Actimize-class platforms recoverable to Full with `(vendor-specific Full)` |
| D14 attestation default | D | clearer Partial boundary |
| D21 on-chain platforms | E | Lossless / Forta etc. legitimately None on D21 |
| Marketing language | F | tightens None boundary on D01/D17/D22 |
| Catalog tags vs paper text | G | clarifies T_indep boundary |
| Calibration-hint contamination | H | reaffirms evidence-only coding |

---

## Re-coding the 4 calibration disagreements with this addendum

Both coders' resolved scores:

| Cell | Before (R1/R2) | After | Rationale tier flag |
| --- | --- | --- | --- |
| P09 D17 | 0 / 1 | 0 | none (rubric bug fixed) |
| P13 D06 | 1 / 0 | 0 | none (chain ≠ protocol) |
| P38 D24 | 2 / 1 | 2 | `(vendor-specific Full)` |
| P38 D25 | 2 / 1 | 2 | `(vendor-specific Full)` |

With these resolutions, calibration κ on the 25 cells would be 1.000.
We do **not** revise the raw calibration CSVs — they stand as the
pre-addendum data for audit. Both coders in the full-coding round
apply `coding_rubric_v4.md` together with this addendum.
