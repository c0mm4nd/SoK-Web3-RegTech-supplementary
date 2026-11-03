# Case 02 — Ronin Bridge Exploit and Laundering (Mar 2022)

<!-- mapping: case_id=02 case_name="Ronin Bridge exploit" year=2022 paradigm=Web3 mechanism_primary=KYT mechanism_secondary=Screening lifecycle_primary=Ex-Post lifecycle_secondary=In-Medias-Res confidence=High overlap=true -->

## Summary

On 23 March 2022 attackers compromised five of nine validator keys controlling the Ronin Bridge and drained "173,600 ETH and 25.5 million USDC" for a total of approximately $624 million (`data/evidence/02_ronin_bridge/halborn_ronin_postmortem.txt`). The compromise exploited a temporary Sky Mavis signing delegation for the Axie DAO validator whose "allowlist was never revoked" after expiry (same file). The hack "wasn't noticed until six days after it occurred" when a user reported a failed withdrawal (same file), demonstrating that no In-Medias-Res control intercepted the drain. On 14 April 2022 OFAC added the exploiter address `0x098B716B8Aaf21512996dC57EB0615e2383E2f96` to the SDN list under the Lazarus Group designation, attributing the theft to "DPRK state-sponsored" hacking via FBI/Chainalysis investigation (`data/evidence/02_ronin_bridge/ofac_lazarus_ronin_apr2022.txt` and `data/evidence/02_ronin_bridge/merkle_science_ronin_analysis.txt`). Merkle Science traced ETH outflows to multiple exchanges ("3,749.92 ETH to exchange E2", "1,219.961 ETH to exchange E4") and documented the ~$402 million still held by the exploiter at the time of the designation (`merkle_science_ronin_analysis.txt`). The broader cross-chain bridge attack class is studied academically by Li et al. (2024/2025), who collect "49 attack transactions … totaling losses of nearly 4.3 billion dollars" with Ronin among them (`data/evidence/02_ronin_bridge/li2025blockchaincrosschainbridge.txt`).

## Taxonomy 1 — Regulatory Paradigm

**Web3 Regulation (Decentralized).** The compromised system is a cross-chain bridge; tracing required network-wide visibility, multi-hop graph reconstruction across Ethereum and bridge counterparties, and downstream sanctions enforcement against on-chain addresses. This matches the Web3 column's "Network-wide visibility … Multi-dimensional including address clustering, taint analysis, protocol risk" profile in `tab:regulatory_evolution`. The Li et al. paper (`li2025blockchaincrosschainbridge.txt`) frames bridge-attack pattern analysis as fundamentally a graph-network problem, not an institution-centric one.

## Taxonomy 2 — Compliance Mechanism

**Primary: KYT.** The core analytic activity is transaction-level tracing of stolen funds from the bridge through CEXes and unidentified addresses; Merkle Science's outflow breakdown by destination exchange is canonical KYT output (`merkle_science_ronin_analysis.txt`). **Secondary: Address/Wallet Screening.** Post-attribution, the SDN listing converted the analytic output into a prospective screening control consumed by every downstream VASP (`ofac_lazarus_ronin_apr2022.txt`: OFAC added the Ethereum address to SDN, becoming the input for downstream address screening).

## Taxonomy 3 — RegTech Lifecycle

**Primary: Ex-Post (Investigative).** The bulk of documented work is retrospective forensics — six-day detection lag (`halborn_ronin_postmortem.txt`), then post-hoc transaction graph reconstruction, exchange-level attribution, and Lazarus identification (`merkle_science_ronin_analysis.txt`). This is the Ex-Post row's "Transaction graph analysis, pattern recognition" pattern in `tab:regtech_lifecycle`. **Secondary: In-Medias-Res.** Once the exploiter address was SDN-listed on April 14, downstream VASPs began real-time screening to freeze inbound transfers — producing a genuine cross-phase footprint. **Overlap flagged.**

## Mapping confidence

**High.** The Ronin case is one of the best-documented Web3 incidents; the Ex-Post / In-Medias-Res overlap is the manuscript's canonical multi-phase example.

## Sources

- `data/evidence/02_ronin_bridge/ofac_lazarus_ronin_apr2022.txt`
- `data/evidence/02_ronin_bridge/merkle_science_ronin_analysis.txt`
- `data/evidence/02_ronin_bridge/halborn_ronin_postmortem.txt`
- `data/evidence/02_ronin_bridge/li2025blockchaincrosschainbridge.txt`
- `data/evidence/02_ronin_bridge/lin2024crosschainabnormaltransaction.txt`
