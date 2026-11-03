"""E1 v4 — Cohen's kappa between two coders on the shared dossier.

Reads:
    data/coder_R1.csv   (coder R1)
    data/coder_R2.csv   (coder R2)

Both independent coders read the same `data/evidence/shared/` pack
under the coder instruction sheet `code/coding_protocol.md`, with
codebook `code/coding_rubric_v4.md` and the post-calibration
addendum `code/coding_rubric_v4_addendum.md`.

Writes:
    results/joint_distribution.csv       3x3 cross-tab of R1 vs R2
    results/kappa_per_dimension.csv      per-dim weighted + unweighted kappa
    results/kappa_summary.json           overall metrics
    results/disagreement_log.csv         per-cell disagreements with both rationales

Reproduce:
    python -m pip install -r code/requirements.txt
    python code/compute_kappa.py
"""
from __future__ import annotations

import csv
import json
from collections import Counter, defaultdict
from pathlib import Path

import pandas as pd
from sklearn.metrics import cohen_kappa_score

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
DATA = ROOT / "data" / "coding"
RESULTS = ROOT / "results"
RESULTS.mkdir(exist_ok=True)


def load_coder(name: str) -> dict[tuple[str, str], dict]:
    path = DATA / f"coder_{name}.csv"
    out = {}
    with path.open() as f:
        for r in csv.DictReader(f):
            out[(r["platform_id"], r["dim_id"])] = {
                "score": int(r["score"]),
                "evidence_citation": r.get("evidence_citation", ""),
                "rationale_short": r.get("rationale_short", ""),
            }
    return out


def joint_distribution(c1: dict, c2: dict) -> dict[tuple[int, int], int]:
    counts = Counter()
    for k in c1:
        counts[(c1[k]["score"], c2[k]["score"])] += 1
    return dict(counts)


def write_joint_csv(joint: dict, out_path: Path) -> None:
    rows = [["", "R2=0", "R2=1", "R2=2"]]
    for c1 in (0, 1, 2):
        rows.append(
            [f"R1={c1}"] + [str(joint.get((c1, c2), 0)) for c2 in (0, 1, 2)]
        )
    with out_path.open("w", newline="") as f:
        csv.writer(f).writerows(rows)


def kappa_metrics(y1: list[int], y2: list[int]) -> dict:
    out = {
        "n_cells": len(y1),
        "exact_agreement_pct": round(
            100 * sum(int(a == b) for a, b in zip(y1, y2)) / max(1, len(y1)), 4
        ),
        "kappa_unweighted": round(cohen_kappa_score(y1, y2), 4),
        "kappa_linear_weighted": round(
            cohen_kappa_score(y1, y2, weights="linear"), 4
        ),
        "kappa_quadratic_weighted": round(
            cohen_kappa_score(y1, y2, weights="quadratic"), 4
        ),
    }
    y1_b = [int(s > 0) for s in y1]
    y2_b = [int(s > 0) for s in y2]
    out["kappa_binary_collapsed"] = round(cohen_kappa_score(y1_b, y2_b), 4)
    return out


def per_dim_kappa(c1: dict, c2: dict) -> pd.DataFrame:
    by_dim = defaultdict(lambda: ([], []))
    for k, v1 in c1.items():
        v2 = c2[k]
        by_dim[k[1]][0].append(v1["score"])
        by_dim[k[1]][1].append(v2["score"])
    rows = []
    for dim in sorted(by_dim):
        y1, y2 = by_dim[dim]
        rows.append({"dim_id": dim, **kappa_metrics(y1, y2)})
    return pd.DataFrame(rows).sort_values("kappa_linear_weighted")


def write_disagreement_log(c1: dict, c2: dict, out_path: Path) -> int:
    rows = []
    for k in sorted(c1):
        a, b = c1[k]["score"], c2[k]["score"]
        if a == b:
            continue
        rows.append(
            {
                "platform_id": k[0],
                "dim_id": k[1],
                "score_R1": a,
                "score_R2": b,
                "abs_diff": abs(a - b),
                "R1_evidence": c1[k]["evidence_citation"],
                "R1_rationale": c1[k]["rationale_short"],
                "R2_evidence": c2[k]["evidence_citation"],
                "R2_rationale": c2[k]["rationale_short"],
            }
        )
    pd.DataFrame(rows).to_csv(out_path, index=False)
    return len(rows)


def main() -> None:
    c1 = load_coder("R1")
    c2 = load_coder("R2")
    keys = set(c1) & set(c2)
    assert len(keys) == 1025, f"expected 1025 shared keys, got {len(keys)}"

    joint = joint_distribution(c1, c2)
    write_joint_csv(joint, RESULTS / "joint_distribution.csv")

    y1 = [c1[k]["score"] for k in sorted(keys)]
    y2 = [c2[k]["score"] for k in sorted(keys)]
    overall = kappa_metrics(y1, y2)
    overall["multi_step_disagreements"] = sum(
        int(abs(a - b) >= 2) for a, b in zip(y1, y2)
    )
    overall["joint_distribution"] = {
        f"R1={c1s},C2={c2s}": joint.get((c1s, c2s), 0)
        for c1s in (0, 1, 2)
        for c2s in (0, 1, 2)
    }
    overall["populated_3x3_cells"] = sum(
        1 for v in overall["joint_distribution"].values() if v > 0
    )

    with (RESULTS / "kappa_summary.json").open("w") as f:
        json.dump(overall, f, indent=2)

    per_dim = per_dim_kappa(c1, c2)
    per_dim.to_csv(RESULTS / "kappa_per_dimension.csv", index=False)

    n_dis = write_disagreement_log(c1, c2, RESULTS / "disagreement_log.csv")

    print("=== Overall agreement ===")
    for k, v in overall.items():
        if isinstance(v, dict):
            continue
        print(f"  {k:35s} {v}")
    print()
    print("=== joint distribution ===")
    print("         R2=0   R2=1   R2=2")
    for c1s in (0, 1, 2):
        cells = "  ".join(
            f"{joint.get((c1s, c2s), 0):5d}" for c2s in (0, 1, 2)
        )
        print(f"  R1={c1s}  {cells}")
    print()
    print(f"disagreements logged: {n_dis}")
    print()
    print("=== per-dimension kappa (sorted ascending) ===")
    print(
        per_dim[
            ["dim_id", "kappa_linear_weighted", "kappa_unweighted", "exact_agreement_pct"]
        ].to_string(index=False)
    )


if __name__ == "__main__":
    main()
