# 01 — Trident Collapse

## Overview

| Field | Value |
|-------|-------|
| **Difficulty** | Easy |
| **Backend** | Open Quantum Safe (OQS) |
| **Algorithms** | ML-KEM-512, ML-DSA-44, SPHINCS+-SHAKE-128f-simple |
| **Flag Format** | `I314{...}` |
| **Key Insight** | Vault key derived from a 20-bit `sigma` parameter — trivially brute-forceable |

## Challenge Description

A cryptographic system composed of post-quantum primitives (KEM, lattice signatures, hash-based signatures) protects an encrypted flag. The primitives themselves are secure — the vulnerability is in how they are **composed**.

The vault that stores the KEM secret key is protected by a key derived from a small integer `sigma` with only 2²⁰ possible values. Once the vault is broken, the entire chain collapses: KEM decapsulation yields a shared secret, which combined with public signature hashes derives the final AES-GCM key.

## Attack Path

```
sigma (brute-force 2²⁰)
    → vault key = SHA3-256("TRIDENT|MASTER|" || sigma)
        → vault.bin decryption → sk_kem
            → ML-KEM-512 decapsulation → shared_secret
                → flag_key = SHA3-256(shared_secret || SHA3-256(sig_mldsa) || SHA3-256(sig_slh))
                    → flag.enc decryption → FLAG
```

## Files

- `challenge/` — Original distributed files
- `solution/solve.py` — Complete automated solver
- `solution/writeup.md` — Step-by-step technical writeup
- `notes/learnings.md` — Key takeaways

## Quick Solve

```bash
cd solution
python3 solve.py
```
