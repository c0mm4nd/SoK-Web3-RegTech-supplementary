# Supplementary Material

*SoK: Web3 Regulatory Technology for Cryptocurrency VASP AML/CFT Compliance*

This archive contains the records behind the systematic classification and
the platform-level statements in the manuscript. Item numbers S1–S5 match
the "Supplementary Material" appendix of the manuscript.

## Contents

| Item | Path | Content | Supports |
|---|---|---|---|
| **S1** Coding rubric | `data/rubric/S1_coding_rubric_25dim.md` | Full 25-dimension rubric: definitions, Full / Partial / None criteria, evidence rule, worked examples | Capability matrix (Table 7), Appendix D (Table A1 is an abridged version) |
| | `data/rubric/S1b_rubric_addendum.md` | Post-calibration addendum (resolutions of the boundary cases found in calibration) | |
| | `data/rubric/S1c_coding_protocol.md` | Coder instruction sheet | |
| | `data/coding/calibration_set.csv`, `calibration_R1/R2.csv`, `calibration_R*_notes.md` | 25-cell calibration round (5 platforms × 5 dimensions) | Section 3, inter-coder reliability |
| | `data/capability_dimensions_25.csv` | Dimension list with operational tests | |
| **S2** Search and screening | `data/screening/search_log.csv` | Retrieval channel, export date, and hit counts per source | Table 2, Appendix A |
| | `data/screening/crossref/` | Separated ACM and IEEE Crossref result sets (`acm_digital_library.csv`, `ieee_xplore.csv`) plus a results-only summary | Table 2 |
| | `data/screening/academic_records_cross_db_dedup.csv` | Cross-database deduplicated record set (574) | Table 2 |
| | `data/screening/academic_records_screened_cross_db_dedup.csv` | Records after title/abstract keyword pre-screening (209) | Table 2 |
| | `data/screening/relevance_screening_decisions.csv` | Decision (`include`/`exclude`), reason, and title relevance score for each of the 209 candidates (96 included) | Table 2, Appendix C |
| | `code/relevance_screening.py` | Applies the relevance-screening rules (title score; inclusion at score ≥ 5) and writes the decision file | Section 3 |
| **S3** Platform coding | `data/platforms_41.csv` | Platform inventory: category, type, primary function, architecture, chain coverage, homepage | Table 8 (catalogue), Section 4.4 |
| | `data/coding/coder_R1.csv`, `data/coding/coder_R2.csv` | The two independent 1,025-cell codings: score (0 None / 1 Partial / 2 Full), cited evidence file(s), rationale | Table 7, Section 5 counts |
| | `results/disagreement_log.csv` | All 123 cells where the codings differ, with both scores, citations, and rationales | Section 3 |
| | `results/adjudication_log.csv` | Adjudication of each of the 123 disagreements: both scores, final score, decision (`R1_upheld` / `R2_upheld` / `third_value`), governing rubric clause, and adjudication note | Section 3 |
| | `results/consensus_matrix.csv`, `results/consensus_matrix_long.csv` | Final 41 × 25 matrix after adjudication (wide and long form; long form marks each cell as `agreement` or `adjudicated`) | Section 3 |
| | `results/kappa_per_dimension.csv`, `results/kappa_summary.json`, `results/joint_distribution.csv` | Agreement statistics (Cohen's κ unweighted / linear / quadratic, exact agreement) | Section 3 |
| | `results/capability_by_category.csv`, `code/build_capability_table.py` | Platform counts per category and dimension (both codings ≥ Partial), totals under both / either coding, T2 cells, and κ — the values of Table 7 | Table 7 |
| **S4** Sources and evidence tiers | `data/evidence/` | Archived evidence pack: `platforms/Pxx/vendor_*.txt` (vendor pages), `cross_platform/{regulator,analyst,papers}/` (independent sources). Each file starts with its source URL and capture date | All platform-level statements |
| | `data/evidence/shared_index.csv` | Index of the evidence pack | |
| | `results/tier_per_cell_r2.csv` | Evidence tier (T1/T2/T3/NA) and all citations for every one of the 1,025 cells | Table 7 (*T2* column), Appendix D |
| | `results/tier_by_dimension_r2.csv`, `results/tier_overall_r2.csv` | Tier counts per dimension and overall; documented-platform counts under both / either coding | Table 7 (*Total* column), Section 5 |
| **S5** Case mapping | `data/cases/cases/` | Eight case write-ups with per-taxonomy assignment and justification citing archived files | Table A2, Appendix E |
| | `data/cases/evidence/` | 24 archived case sources (with `_dossier_index.csv`) | |
| | `data/cases/mapping.csv`, `data/cases/overlap_analysis.md` | Mapping table and overlap analysis | Section 4.2 (taxonomy validity), Appendix E |

## Rules used in the manuscript

**Adjudication.** The third coder decided each disagreement by applying the
rubric and the post-calibration addendum (S1) to both rationales and the
cited evidence. The final score may equal either coder's score or, where the
evidence supports neither, a third value (`third_value`, 9 rows). No score is
averaged. Main-text platform counts do not use the final matrix; they use
the conservative rule below, so they do not depend on adjudication.

**Platform counts.** "*n* of 41 platforms" counts a capability for a
platform when both codings score it at least Partial (`min(score_R1,
score_R2) ≥ 1`). The figure in parentheses is the count when either coding
does (`max ≥ 1`). Both are in `results/tier_by_dimension_r2.csv`
(`claimed_both`, `claimed`).

**Evidence tiers** (`code/derive_tiers_r2.py`). For every cell that either
coder scored at least Partial:

- **T1** — supported only by the vendor's own material.
- **T2** — at least one cited source not authored by the vendor names the
  platform in its own text (regulatory/enforcement record, analyst or press
  report, academic paper). Name matching uses the captured source text
  only, not the archive header or the curator annotation block.
  Vendor-authored or vendor-co-authored sources are excluded for that
  vendor. `platforms/Pxx/narrative.md` files are catalogue summaries
  derived from the manuscript and are never counted as evidence.
- **T3** — an evaluation or benchmark of the platform's own implementation
  (manually verified list `MANUAL_T3`; empty for this evidence pack).

Result: 417 documented cells; T1 = 397 (95.2 %), T2 = 20 (4.8 %), T3 = 0.

## Reproduction

```bash
python3 -m pip install 'pandas>=2.0' 'scikit-learn>=1.3,<2.0'
python3 code/relevance_screening.py  # relevance-screening decisions (S2)
python3 code/compute_kappa.py      # agreement statistics + disagreement log
python3 code/derive_tiers_r2.py    # evidence tiers and platform counts
python3 code/build_capability_table.py  # Table 7 (run after the two above)
```

The scripts read only files in this archive and overwrite the
corresponding files in `results/`.

## Dates

- Literature: publications from 1 January 2015. The database exports in S2
  were generated on 6 March 2026. The 31 December 2025 upper
  limit is applied in the IEEE Xplore, ACM Digital Library, and arXiv
  queries; Google Scholar and Web of Science records extend to the export
  date (two included records are dated 2026).
- Platforms: observation window to December 2025. The evidence pack in S4
  was captured in May 2026; the capture date is recorded at the top of each
  file.
- `platforms/P11/vendor_kyt_api.txt` is cited only in the adjudication of
  P11/D21; neither coder cites it, so it does not affect the agreement
  statistics, evidence tiers, or main-text counts.
- Case sources (S5): captured May 2026.
