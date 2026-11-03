"""Round-2 evidence-tier derivation (supersedes E2 derive_tiers.py).

Applies the T1/T2/T3 definitions stated in the manuscript appendix to the
two independent coding sheets (E1 coder_R1.csv / coder_R2.csv):

    T1  vendor self-report only (platforms/<P>/vendor_*.txt)
    T2  independent source (regulatory/enforcement record, analyst or press
        report, or academic paper) whose own text NAMES the platform
    T3  peer-reviewed evaluation or third-party technical benchmark of the
        platform's implementation (verified manually; MANUAL_T3)

Changes relative to the round-1 script:
  * Name matching uses only the captured source text: file headers and the
    curator annotation block ("NAMED PLATFORMS:") are excluded.
  * Reports or papers authored/co-authored by a platform are not
    independent evidence for that platform.
  * platforms/<P>/narrative.md is a catalogue summary derived from this
    manuscript; it is not independent evidence and is ignored.
  * Regulatory filings are T2 (as defined in the appendix), not T3.
  * A cross-platform source upgrades a cell only if its text names the
    platform (alias match). Sources that describe the capability or the
    regulatory context in general, without naming the platform, do not
    corroborate a platform-level claim and are ignored.

Cell tier = highest qualifying tier across both coders' citations, for
cells that at least one coder scored Partial or Full (otherwise NA).

Outputs: ../results/tier_per_cell_r2.csv, tier_by_dimension_r2.csv,
         tier_overall_r2.csv
"""
from __future__ import annotations

import csv
import re
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
SUPP = HERE.parent
DATA = SUPP / "data"
OUT = SUPP / "results"
OUT.mkdir(exist_ok=True)
EVID = DATA / "evidence"

ALIASES = {
    "P01": ["Chainalysis"], "P02": ["Elliptic"], "P03": ["CipherTrace"],
    "P04": ["TRM Labs", "TRM"], "P05": ["Merkle Science"],
    "P06": ["Scorechain"], "P07": ["Coinfirm"],
    "P08": ["Crystal Intelligence", "Crystal Blockchain"],
    "P09": ["Solidus"], "P10": ["Blockchain Intelligence Group", "BIGG"],
    "P11": ["Chainalysis"], "P12": ["Forta"], "P13": ["Lossless"],
    "P14": ["Hypernative"], "P15": ["Dedaub"], "P16": ["Chaos Labs"],
    "P17": ["Gauntlet"], "P18": ["Nansen"], "P19": ["Arkham"],
    "P20": ["AnChain"], "P21": ["Bitquery"], "P22": ["Covalent"],
    "P23": ["Elementus"], "P24": ["Bison Trails", "Coinbase Cloud"],
    "P25": ["Notabene"], "P26": ["Sygna"], "P27": ["TRISA"],
    "P28": ["21 Analytics"], "P29": ["Shyft"], "P30": ["TransactID"],
    "P31": ["CipherBlade"], "P32": ["Privado"], "P33": ["Polygon ID"],
    "P34": ["KILT"], "P35": ["ComplyAdvantage"],
    "P36": ["World-Check", "Refinitiv"], "P37": ["Bridger", "LexisNexis"],
    "P38": ["Actimize"], "P39": ["Fenergo"], "P40": ["AMLBot"],
    "P41": ["ComplyAdvantage"],
}
# (paper file, platform) pairs verified to evaluate or benchmark the
# platform's implementation. None of the papers in the evidence pack does so.
MANUAL_T3: set[tuple[str, str]] = set()
RANK = {"NA": 0, "T1": 1, "T2": 2, "T3": 3}
_text_cache: dict[str, str] = {}

# Sources authored or co-authored by the platform itself are not independent
# of that platform (vendor research reports, vendor-co-authored papers).
SELF_AUTHORED = {
    "chainalysis_": {"P01", "P11"},
    "trm_labs_": {"P04"},
    "notabene_": {"P25"},
    "solidus_labs_": {"P09"},
    "elliptic_": {"P02"},
    "merkle_science_": {"P05"},
    "weber2019": {"P02"},  # co-authored by Elliptic staff
}
HEADER = re.compile(r"^(Source|Fetched|Status|Citation|Publication|URL)\s*:")
# curator lines that map a source to platform IDs / dimension codes
CURATOR_LINE = re.compile(r"\(P\d{2}\b|\bP\d{2}\)|^\s*-?\s*D\d{2}\b|\bD\d{2}\b.*:|[Ss]ubstantiates|third-party attestation|relevant to")
ANNOTATION = re.compile(r"^(NAMED PLATFORMS|RELEVANCE|CODING NOTE|NOTES?|Implications for coding)\b[^:]*:", re.I)


def verbatim_text(raw: str) -> str:
    """Keep only the captured source text: drop file header lines and the
    curator annotation block (which lists platforms the source is
    'relevant to' and is not part of the source)."""
    keep = []
    for line in raw.splitlines():
        if ANNOTATION.match(line):
            break
        if HEADER.match(line) or CURATOR_LINE.search(line):
            continue
        keep.append(line)
    return "\n".join(keep)


def names_platform(path: str, pid: str) -> bool:
    if path not in _text_cache:
        f = EVID / path
        _text_cache[path] = verbatim_text(f.read_text(errors="ignore")) if f.exists() else ""
    txt = _text_cache[path]
    fname = path.rsplit("/", 1)[-1]
    if any(fname.startswith(k) and pid in v for k, v in SELF_AUTHORED.items()):
        return False
    aliases = ALIASES[pid]
    if pid == "P02":  # avoid "elliptic curve"
        return re.search(r"\bElliptic\b(?! curve)", txt) is not None
    return any(re.search(r"\b" + re.escape(a) + r"\b", txt) for a in aliases)


def tier_of(path: str, pid: str) -> str:
    p = path.strip().strip('"')
    if not p or p.lower().startswith("no "):
        return "NA"
    if p.startswith("platforms/") and "/vendor_" in p:
        return "T1"
    if p.endswith("narrative.md"):
        return "NA"
    if p.startswith(("cross_platform/analyst/", "cross_platform/regulator/")):
        return "T2" if names_platform(p, pid) else "NA"
    if p.startswith("cross_platform/papers/"):
        # a paper that names the platform corroborates it (T2); T3 requires
        # an evaluation/benchmark of the platform's own implementation
        if (p.rsplit("/", 1)[-1], pid) in MANUAL_T3:
            return "T3"
        return "T2" if names_platform(p, pid) else "NA"
    return "NA"


def load(coder: str) -> dict:
    with (DATA / "coding" / f"coder_{coder}.csv").open() as f:
        return {(r["platform_id"], r["dim_id"]): r for r in csv.DictReader(f)}


def main() -> None:
    r1, r2 = load("R1"), load("R2")
    rows = []
    for key in sorted(r1):
        pid, did = key
        a, b = r1[key], r2[key]
        s1, s2 = int(a["score"]), int(b["score"])
        cites = [c for r in (a, b) for c in r["evidence_citation"].split(";")]
        best = max((tier_of(c, pid) for c in cites), key=RANK.get, default="NA")
        if max(s1, s2) == 0:
            tier = "NA"
        else:
            # a claimed capability always has at least the vendor tier
            tier = best if RANK[best] >= 1 else "T1"
        rows.append({"platform_id": pid, "dim_id": did, "score_R1": s1,
                     "score_R2": s2, "evidence_tier": tier,
                     "citations": ";".join(sorted({c.strip() for c in cites if c.strip()}))})
    with (OUT / "tier_per_cell_r2.csv").open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)

    dims = sorted({r["dim_id"] for r in rows})
    with (OUT / "tier_by_dimension_r2.csv").open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["dim_id", "T1", "T2", "T3", "NA", "claimed",
                    "claimed_R1", "claimed_R2", "claimed_both"])
        for d in dims:
            sub = [r for r in rows if r["dim_id"] == d]
            c = Counter(r["evidence_tier"] for r in sub)
            w.writerow([d, c["T1"], c["T2"], c["T3"], c["NA"],
                        c["T1"] + c["T2"] + c["T3"],
                        sum(r["score_R1"] > 0 for r in sub),
                        sum(r["score_R2"] > 0 for r in sub),
                        sum(min(r["score_R1"], r["score_R2"]) > 0 for r in sub)])
    c = Counter(r["evidence_tier"] for r in rows)
    claimed = c["T1"] + c["T2"] + c["T3"]
    with (OUT / "tier_overall_r2.csv").open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["tier", "cells", "pct_of_1025", "pct_of_claimed"])
        for t in ("T1", "T2", "T3", "NA"):
            w.writerow([t, c[t], round(100 * c[t] / len(rows), 1),
                        round(100 * c[t] / claimed, 1) if t != "NA" else ""])
    print(dict(c), "claimed", claimed)


if __name__ == "__main__":
    main()
