# Case 03 — FTX / Alameda Asset Tracing (Nov 2022 onward)

<!-- mapping: case_id=03 case_name="FTX/Alameda asset tracing" year=2022 paradigm=VASP mechanism_primary=KYT mechanism_secondary=Screening lifecycle_primary=Ex-Post lifecycle_secondary=None confidence=High overlap=false -->

## Summary

FTX Trading Ltd. and its affiliates filed for Chapter 11 bankruptcy on 11 November 2022 following disclosed exposure between FTX and the hedge fund Alameda Research, which Coquidé et al. (2024) characterize as "a cryptocurrency trading firm implicated in the misuse of FTX customer funds" leading to "its bankruptcy in November 2022" (`data/evidence/03_ftx_alameda/coquide_alameda_2024_arxiv.txt`). The Coquidé multi-token network paper analyzes "the token transfer network on Ethereum, focusing on accounts associated with Alameda Research", using "node centralities and the network backbone to identify critical accounts, tokens, and activity groups" (same file) — i.e., a peer-reviewed on-chain forensic methodology applied entirely after-the-fact. On 28 March 2024, Sam Bankman-Fried was sentenced by Judge Lewis Kaplan (SDNY) to 25 years in prison and ordered to pay "$11 billion in forfeiture" after being convicted on wire fraud, securities fraud, commodities fraud, and "conspiracy to commit money laundering" counts (`data/evidence/03_ftx_alameda/doj_sbf_sentencing_mar2024.txt`). The DOJ release describes how Bankman-Fried "misappropriated billions of dollars of customer funds deposited with FTX, defrauded investors in FTX of more than $1.7 billion, and defrauded lenders to Alameda of more than $1.3 billion" (same file). Chainalysis's 2025 industry report contextualizes the case within wider stolen-funds and exchange-failure forensics (`data/evidence/03_ftx_alameda/chainalysis_2025_crypto_crime_report.txt`).

## Taxonomy 1 — Regulatory Paradigm

**Virtual Asset Regulation (Centralized).** FTX was a centralized VASP. The principal compliance and enforcement levers were intermediary-centric: bankruptcy trustee, DOJ prosecution, sentence and forfeiture (`doj_sbf_sentencing_mar2024.txt`). On-chain tracing was the technical instrument but the regulatory frame is the Centralized column in `tab:regulatory_evolution`: "Centralized VASP databases" plus "blockchain address blacklisting" by counterparty exchanges (Kraken, Binance) post-collapse.

## Taxonomy 2 — Compliance Mechanism

**Primary: KYT.** The dominant analytic activity is transaction tracing across multiple tokens and chains; the Coquidé paper's "multi-token network representation … node centralities and the network backbone to identify critical accounts" is a textbook KYT output (`coquide_alameda_2024_arxiv.txt`). The DOJ money-laundering conspiracy charge (`doj_sbf_sentencing_mar2024.txt`) directly depends on KYT-derived transaction evidence. **Secondary: Address/Wallet Screening** — counterparty exchanges acted by screening addresses flagged as FTX-related and freezing inbound funds in the hours surrounding the collapse.

## Taxonomy 3 — RegTech Lifecycle

**Primary: Ex-Post (Investigative).** The case is fundamentally a post-collapse forensic investigation supporting bankruptcy recovery and criminal prosecution. No real-time monitoring intercepted the outflow; work began only after disclosure. The Ex-Post row's "forensic analysis, suspicious activity detection, regulatory reporting, audit trails" objectives in `tab:regtech_lifecycle` describe the case exactly. The Coquidé paper exemplifies the Ex-Post row's "Transaction graph analysis, pattern recognition, behavioral profiling" technologies (`coquide_alameda_2024_arxiv.txt`).

## Mapping confidence

**High.** DOJ filings, the sentencing record, and the Coquidé et al. academic paper converge on a single Ex-Post / KYT mapping.

## Sources

- `data/evidence/03_ftx_alameda/coquide_alameda_2024_arxiv.txt`
- `data/evidence/03_ftx_alameda/doj_sbf_sentencing_mar2024.txt`
- `data/evidence/03_ftx_alameda/chainalysis_2025_crypto_crime_report.txt`
