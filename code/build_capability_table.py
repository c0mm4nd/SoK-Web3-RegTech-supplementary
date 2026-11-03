"""Category x dimension capability counts for the main-text capability matrix (Table 7).

For each capability dimension and platform category, counts the platforms for
which BOTH independent codings score the capability at least Partial (>=1).
Also reports the 41-platform total under both / either coding, the number of
documented cells with an independent (T2) source, and linear-weighted kappa.

Reads:  data/platforms_41.csv, data/capability_dimensions_25.csv,
        data/coding/coder_R1.csv, data/coding/coder_R2.csv,
        results/tier_per_cell_r2.csv, results/kappa_per_dimension.csv
Writes: results/capability_by_category.csv
"""
from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATS = ["Comprehensive", "DeFi-Specialized", "Cross-Chain",
        "Privacy-Preserving", "Traditional+Web3"]


def read(path):
    with open(ROOT / path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def main():
    plats = {r["platform_id"]: r["category"] for r in read("data/platforms_41.csv")}
    dims = [(r["dim_id"], r["dimension"]) for r in read("data/capability_dimensions_25.csv")]
    s1 = {(r["platform_id"], r["dim_id"]): int(r["score"]) for r in read("data/coding/coder_R1.csv")}
    s2 = {(r["platform_id"], r["dim_id"]): int(r["score"]) for r in read("data/coding/coder_R2.csv")}
    tier = {(r["platform_id"], r["dim_id"]): r["evidence_tier"] for r in read("results/tier_per_cell_r2.csv")}
    kappa = {r["dim_id"]: r["kappa_linear_weighted"] for r in read("results/kappa_per_dimension.csv")}

    out = []
    for d, name in dims:
        row = {"dim_id": d, "dimension": name}
        for c in CATS:
            ps = [p for p, cat in plats.items() if cat == c]
            row[f"n_{c}"] = len(ps)
            row[f"both_{c}"] = sum(min(s1[p, d], s2[p, d]) >= 1 for p in ps)
        row["both_total"] = sum(min(s1[p, d], s2[p, d]) >= 1 for p in plats)
        row["either_total"] = sum(max(s1[p, d], s2[p, d]) >= 1 for p in plats)
        row["T2_documented"] = sum(tier.get((p, d)) == "T2" for p in plats)
        row["T3_documented"] = sum(tier.get((p, d)) == "T3" for p in plats)
        row["kappa_linear"] = kappa.get(d, "")
        out.append(row)

    with open(ROOT / "results/capability_by_category.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(out[0]))
        w.writeheader()
        w.writerows(out)
    for r in out:
        print(r["dim_id"], [r[f"both_{c}"] for c in CATS], r["both_total"], r["either_total"],
              r["T2_documented"], r["kappa_linear"])


if __name__ == "__main__":
    main()
