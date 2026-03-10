# Quantum-Safe Cryptography — Challenges & Writeups

Personal collection of post-quantum cryptography (PQC) challenges, solutions, and technical notes.

## Challenges

| #  | Name | Algorithms | Difficulty | Status |
|----|------|-----------|------------|--------|
| 01 | [Trident Collapse](./01-trident-collapse/) | ML-KEM-512, ML-DSA-44, SPHINCS+ | Easy | Solved |

## About

These challenges explore **post-quantum cryptographic systems** — not by breaking the mathematical hardness of PQC primitives, but by analyzing how they are composed into real designs. The focus is on understanding architectural weaknesses, flawed key derivation, and system-level vulnerabilities.

## Tools & Libraries Used

- Python 3.12+
- `cryptography` (AES-GCM, AESGCM)
- `hashlib` (SHA3-256, SHA3-512, SHAKE-256)
- Pure Python ML-KEM-512 implementation (FIPS 203)
- Liboqs: an Open Source library for PQC

## References

- [NIST FIPS 203 — ML-KEM](https://csrc.nist.gov/pubs/fips/203/final)
- [NIST FIPS 204 — ML-DSA](https://csrc.nist.gov/pubs/fips/204/final)
- [NIST FIPS 205 — SLH-DSA](https://csrc.nist.gov/pubs/fips/205/final)
