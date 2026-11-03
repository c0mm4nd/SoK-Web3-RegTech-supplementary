# E1 Coder Instruction Sheet

This is the instruction sheet used by both independent coders.
The only differences between the two coding sheets are the coder
identifier and the output path. Both coders read the same evidence
pack at `data/evidence/shared/`. This is classical inter-rater
reliability: same evidence, two independent applications of the
codebook.

## Identifiers

- Coder identifier: `R1` or `R2`
- Output sheet: `data/coder_R1.csv` or `data/coder_R2.csv`

## Required reading before scoring

1. `code/coding_rubric_v4.md` — the codebook. It defines:
   - The universal Full / Partial / None scale.
   - The universal evidence-tier rule (T_vendor vs T_indep).
   - Per-dimension Full / Partial / None criteria with worked examples
     for each of the 25 dimensions.
2. `code/coding_rubric_v4_addendum.md` — post-calibration resolutions.
   The addendum supersedes any conflicting language in the base
   codebook. Key amendments:
   - D17 worked example: wash-trading is not MEV; re-anchor to
     Daian 2020 Flash Boys 2.0.
   - D06: a chain list is not a DeFi protocol list.
   - Full may be reached via (a) T_indep or (b) vendor-multi-element
     specific evidence (≥ 2 named elements), flagged
     `(vendor-specific Full)` in the rationale.
   - D21 for on-chain / decentralised platforms: legitimate None;
     mark `(on-chain architecture; D21 not applicable)`.
   - Marketing-only language → None on D01 / D17 / D22.
   - Catalog tags in `narrative.md` count as T_indep; a
     cross-platform `platform_ids` tag does not count unless the
     source text itself names the platform.
3. `data/evidence/shared/shared_index.csv` — index of all evidence
   files with source type (vendor / narrative / paper / regulator /
   analyst) and the platforms each cross-platform source names.
4. `experiments/shared/platforms_41.csv` — platform metadata.
5. `experiments/shared/capability_dimensions_25.csv` — short
   dimension definitions (the codebook governs boundary cases).

## Scoring procedure

For each (platform_id, dim_id) cell:

1. From `shared_index.csv`, identify evidence files relevant to this
   platform: all files under `platforms/<platform_id>/` plus any
   cross-platform file whose `platform_ids` field includes this
   platform.
2. Read those files. Classify each piece of evidence as **T_vendor**
   (vendor-disclosed) or **T_indep** (peer-reviewed paper, regulator
   filing, named analyst report, or narrative passage that explicitly
   names the capability).
3. Apply the dimension's Full / Partial / None criteria from the
   codebook, including the universal evidence-tier rule.
4. Write the row to the output sheet with the schema below.

## Output schema

Columns: `platform_id, dim_id, score, evidence_citation, rationale_short`

- `platform_id` ∈ P01..P41
- `dim_id` ∈ D01..D25
- `score` ∈ {0, 1, 2}
- `evidence_citation`:
  - score = 2 or 1: a path relative to `data/evidence/shared/`
    (for example `platforms/P01/vendor_solutions.txt` or
    `cross_platform/papers/weber2019....txt`). The path must exist
    on disk. Multiple citations are allowed, separated by semicolons.
  - score = 0: the literal string `no evidence in shared dossier`.
- `rationale_short`: one sentence that (i) quotes or paraphrases a
  specific fragment from the cited file(s), and (ii) names the
  evidence tier (T_vendor / T_indep). Apply exactly one suffix flag
  when applicable (addendum §C and §E):
  - `(vendor-specific Full)` — score = 2 via the vendor-multi-element
    path (no T_indep).
  - `(vendor-only evidence)` — score = 1 with T_vendor specific but
    single-element.
  - `(on-chain architecture; D21 not applicable)` — score = 0 on D21
    for decentralised platforms.

Different rationales are required across cells in the same dimension.

## Independence rules

- Code only from the shared evidence pack. Do not retrieve additional
  web pages during scoring, and do not fill gaps from memory.
- Do not read the other coder's CSV.
- Do not read `_archive_C1_v3split/` or `_archive_C2_v3split/`
  (pilot dossiers retained for audit only).
- Do not project scores from a per-platform source matrix. Each cell
  is coded individually from the codebook.
- Do not use templated rationales. Forbidden phrases: "documented as
  production capability", "documented but with caveats", "outside
  this platform's market scope", "vendor docs describe X as available".

## Required outputs

1. The 1,025-row coding sheet, unique on (platform_id, dim_id).
2. `data/coder_<ID>_methodology.md` recording: (a) how many cells
   had T_indep evidence, (b) which dimensions had the thinnest pack
   coverage, (c) platforms where the pack was essentially empty,
   (d) any remaining rubric ambiguities.

## Self-check before submitting the sheet

1. Run `python3 code/verify_evidence_paths.py` — must exit 0.
2. The score distribution must include all three values (0, 1, 2).
3. Random-sample 10 non-None rows: open each cited file and confirm
   the rationale's substance appears there. Correct any cell that
   fails this check.
4. For any cell with score = 1 and `(vendor-only evidence)`, confirm
   that no T_indep evidence was available.

## Coding-sheet summary (under 200 words)

(a) Score distribution counts of 0 / 1 / 2.
(b) Number of cells where T_indep evidence supported Full.
(c) Number of cells flagged `(vendor-only evidence)`.
(d) Three dimensions with the strongest pack coverage.
(e) Three platforms with the thinnest pack.
(f) Rubric ambiguities encountered.
(g) Verification-script exit code.
