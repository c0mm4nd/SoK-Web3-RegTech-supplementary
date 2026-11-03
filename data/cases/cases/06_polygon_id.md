# Case 06 — Polygon ID Credential Issuance

<!-- mapping: case_id=06 case_name="Polygon ID credential issuance" year=2022 paradigm=Web3 mechanism_primary=KYA mechanism_secondary=KYC lifecycle_primary=Ex-Ante lifecycle_secondary=None confidence=Medium overlap=false -->

## Summary

Polygon ID was announced by Polygon Labs on **29 March 2022** (v1 incorrectly dated this to "March 2023"; the primary blog post `data/evidence/06_polygon_id/polygon_blog_intro_mar2022.txt` records the correct date). The platform is positioned as "the self-sovereign, decentralized and private identity for the next iteration of the Internet" and explicitly "leverages the Iden3 protocol and Circom ZK toolkit" plus "zkSNARKs circuits" (`polygon_blog_intro_mar2022.txt`). The Privado ID developer documentation — the continuation of Polygon ID docs after the 2024 spin-out — describes a "Triangle of Trust" of Issuer (signs VCs), Holder (holds VCs and generates ZK proofs), and Verifier (`data/evidence/06_polygon_id/privado_polygon_id_docs_intro.txt`). Identity uses "a unique DID (Decentralized Identifier) following W3C standards" and credentials let users "prove their identity without the need of exposing their private information" (same file). Polygon Labs explicitly names "KYC, KYB, attestation" as supported organizational use cases (`polygon_blog_intro_mar2022.txt`), and the Lee 2022 academic Travel-Rule paper held in the dossier (`data/evidence/06_polygon_id/yang2024researchidentitydata.txt`) provides the corresponding research backdrop for blockchain-based identity-data attestation.

## Taxonomy 1 — Regulatory Paradigm

**Web3 Regulation (Decentralized).** Polygon ID is precisely the artifact named in the Web3 column's "Identity Foundation" row in `tab:regulatory_evolution`: "Cryptographic identifiers with optional verifiable credential attestation". Verification is by zero-knowledge proof rather than document review (`privado_polygon_id_docs_intro.txt`: "prove their identity without the need of exposing their private information").

## Taxonomy 2 — Compliance Mechanism

**Primary: KYA.** The product binds a Verifiable Credential to a specific wallet/DID — the Triangle of Trust description in `privado_polygon_id_docs_intro.txt` shows the Holder's wallet "stores the private key of a user, fetch VCs from the Issuer, and create zero-knowledge proofs to be presented to the Verifier." This is the KYA row's verification target in `tab:compliance_comparison`: "Verified ownership or custody of a blockchain address by a known person or entity". **Secondary: KYC** because issuers are typically KYC-licensed entities whose underlying process is classical document-based KYC; Polygon Labs explicitly names "KYC, KYB, attestation" as supported applications (`polygon_blog_intro_mar2022.txt`).

## Taxonomy 3 — RegTech Lifecycle

**Primary: Ex-Ante (Preventive).** Credentials are issued and presented before a transaction or pool entry, gating access. This is the Ex-Ante row's "Decentralized identity protocols (DIDs, VCs), on-chain KYC attestations, permissioned DeFi pools" pattern in `tab:regtech_lifecycle`. The Privado documentation's age-verification example (`privado_polygon_id_docs_intro.txt`) — "proving someone is over 18 without revealing their actual age" — is the canonical Ex-Ante credential-gating use case.

## Mapping confidence

**Medium.** Confidence is reduced one step because Polygon ID is an identity *substrate* rather than a deployed compliance regime; the mapping depends on assumed downstream use. Within that scope the assignment is unambiguous and is supported by the Polygon Labs and Privado documentation in the dossier.

## Sources

- `data/evidence/06_polygon_id/polygon_blog_intro_mar2022.txt`
- `data/evidence/06_polygon_id/privado_polygon_id_docs_intro.txt`
- `data/evidence/06_polygon_id/yang2024researchidentitydata.txt`
