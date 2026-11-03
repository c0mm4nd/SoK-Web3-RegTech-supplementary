# Case 08 — Chainalysis Reactor Multi-Hop Investigation

<!-- mapping: case_id=08 case_name="Chainalysis Reactor multi-hop investigation" year=2024 paradigm=Web3 mechanism_primary=KYT mechanism_secondary=Screening lifecycle_primary=Ex-Post lifecycle_secondary=None confidence=High overlap=false -->

## Summary

Chainalysis Reactor is the flagship blockchain investigation product of Chainalysis Inc. and is the underlying graph engine behind Chainalysis's *Crypto Crime Report* series. The 2024 report attributes "$24.2 billion" in illicit cryptocurrency volume for 2023, with "Sanctions-related transactions: 61.5% of illicit transaction volume (~$14.9 billion)" and an explicit methodology disclosure that "Estimates use Chainalysis's address-attribution database" (`data/evidence/08_chainalysis_reactor/chainalysis_2024_crypto_crime_report.txt`). The Reactor workflow starts from seed addresses (e.g., a hack exploiter wallet or a ransomware payment address), constructs transaction graphs, applies heuristic and ML clustering, annotates clusters with attribution labels, and supports analysts in following fund flows through arbitrary multi-hop paths. Wu et al.'s 2022/2023 IEEE TIFS paper on TRacer independently names Chainalysis as a forensics service performing this work: "a common practice is to track stolen money in blockchain transaction networks, which has been done by some forensics services like Chainalysis and Elliptic" (`data/evidence/08_chainalysis_reactor/wu2023tracerscalablegraphbased.txt`). Wu et al. critique the heuristic / taint-analysis approach and propose a graph PageRank alternative ("To the best of our knowledge, TRacer is the first intelligent transaction tracing tool in account-based blockchains that can handle complex transaction actions in DeFi"; same file), which both validates Reactor's market positioning and identifies its known limitations in DeFi semantics.

## Taxonomy 1 — Regulatory Paradigm

**Web3 Regulation (Decentralized).** Reactor exercises the "Network-wide visibility across all participants and intermediaries" and "Graph-based behavioral analytics across entire transaction network" rows of the Web3 column in `tab:regulatory_evolution` (`wu2023tracerscalablegraphbased.txt`: "track stolen money in blockchain transaction networks … forensics services like Chainalysis and Elliptic"). Attribution is derived from public-ledger data plus proprietary labelling rather than from privileged access to a single institution's records (`chainalysis_2024_crypto_crime_report.txt`: "Chainalysis's address-attribution database").

## Taxonomy 2 — Compliance Mechanism

**Primary: KYT.** Reactor's verification target is transactions and transaction patterns; its outputs are taint propagation, multi-hop paths, and counterparty graphs — the KYT row of `tab:compliance_comparison` almost verbatim (`wu2023tracerscalablegraphbased.txt`: "transaction tracing", "taint analysis"). **Secondary: Address/Wallet Screening** because attribution clusters feed Chainalysis's downstream KYT and address-screening products consumed by VASP compliance teams; the Crypto Crime Report breakdowns of darknet / ransomware / sanctioned-address volume (`chainalysis_2024_crypto_crime_report.txt`) are essentially screening-oriented summaries of Reactor output.

## Taxonomy 3 — RegTech Lifecycle

**Primary: Ex-Post (Investigative).** Reactor is explicitly a forensic / investigative product and is the canonical example of the Ex-Post row's "Blockchain forensics tools, address clustering algorithms, cross-chain fund tracing, mixing service detection" toolset in `tab:regtech_lifecycle`. Wu et al.'s framing — "track stolen money" as a graph-search task done *after* incidents — confirms Ex-Post as primary (`wu2023tracerscalablegraphbased.txt`).

## Mapping confidence

**High.** Reactor is the prototype Ex-Post tool; the mapping is self-evident, supported by an independent peer-reviewed academic source (Wu 2023) that names Chainalysis by name.

## Sources

- `data/evidence/08_chainalysis_reactor/chainalysis_2024_crypto_crime_report.txt`
- `data/evidence/08_chainalysis_reactor/wu2023tracerscalablegraphbased.txt`
