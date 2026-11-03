"""Relevance screening of the 209 pre-screened candidates (S2).

Rules, applied to every candidate in this order:
  1. Title contains a noise term (off-topic false positives) -> exclude.
  2. Google Scholar listing marked [BOOK] -> exclude.
  3. Google Scholar listing marked [PDF] with relevance score < 10 -> exclude.
  4. Relevance score >= 5 -> include; otherwise exclude.

The relevance score is computed from the title: weighted domain and
compliance terms add points; non-scholarly formats subtract points.

Reads:  data/screening/academic_records_screened_cross_db_dedup.csv
Writes: data/screening/relevance_screening_decisions.csv
"""
from __future__ import annotations

import csv
import re
import unicodedata
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "data/screening/academic_records_screened_cross_db_dedup.csv"
OUTPUT = ROOT / "data/screening/relevance_screening_decisions.csv"

INCLUDE_THRESHOLD = 5

NOISE_TERMS = [
    "rail economy",
    "briefing note",
    "hemochromatosis",
    "ipv6",
    "rule based mechanism to detect denial of service",
]

WEIGHTED_TERMS = [
    ("anti money laundering", 6), ("money laundering", 5),
    # " aml " and " aml" are listed separately, so a title containing "aml"
    # receives both weights (8 points in total).
    ("aml", 4), ("aml", 4),
    ("travel rule", 4), ("kyc", 4), ("kyt", 4), ("vasp", 4),
    ("blockchain", 3), ("cryptocurrency", 3), ("bitcoin", 3), ("ethereum", 3),
    ("defi", 3), ("virtual asset", 3),
    ("compliance", 2), ("risk", 2), ("fraud", 2), ("forensic", 2),
    ("graph", 2), ("zero knowledge", 2),
]

PENALTIES = [("[pdf]", 4), ("[book]", 5), ("briefing note", 6), ("rail economy", 8)]


def norm(text: str) -> str:
    s = unicodedata.normalize("NFKC", text or "").lower()
    s = "".join(ch if ch.isalnum() or ch.isspace() else " " for ch in s)
    return re.sub(r"\s+", " ", s).strip()


def relevance_score(title: str) -> int:
    text = norm(title)
    score = sum(w for term, w in WEIGHTED_TERMS if term in text)
    raw = (title or "").lower()
    score -= sum(p for marker, p in PENALTIES if marker in raw)
    return score


def decide(title: str, source_key: str) -> tuple[str, str, int]:
    score = relevance_score(title)
    t = (title or "").lower()
    if any(term in t for term in NOISE_TERMS):
        return "exclude", "noise_term", score
    if source_key == "google_scholar" and "[book]" in t:
        return "exclude", "book_listing", score
    if source_key == "google_scholar" and "[pdf]" in t and score < 10:
        return "exclude", "pdf_listing_low_score", score
    if score >= INCLUDE_THRESHOLD:
        return "include", "score_at_or_above_threshold", score
    return "exclude", "score_below_threshold", score


def main() -> None:
    with open(INPUT, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    out = []
    for r in rows:
        decision, reason, score = decide(r.get("title", ""), r.get("source_key", ""))
        out.append({
            "source_key": r.get("source_key", ""), "source_name": r.get("source_name", ""),
            "year": r.get("year", ""), "title": r.get("title", ""), "venue": r.get("venue", ""),
            "url": r.get("url", ""), "decision": decision, "reason": reason,
            "relevance_score": score,
        })
    with open(OUTPUT, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(out[0]))
        w.writeheader()
        w.writerows(out)
    inc = Counter(r["source_key"] for r in out if r["decision"] == "include")
    print("candidates", len(out), "included", sum(inc.values()), dict(inc))
    print(dict(Counter(r["reason"] for r in out)))


if __name__ == "__main__":
    main()
