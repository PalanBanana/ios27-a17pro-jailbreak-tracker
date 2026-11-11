# Evidence audit

**Snapshot:** 2026-11-11. This audit checks how well each claim is supported, which sources carry the most weight, and where the evidence is weakest.

## Verdict counts

| Verdict | Claims |
|---|---|
| verified | 10 |
| partially verified | 15 |
| unverified | 7 |
| disproved | 0 |
| superseded | 0 |

## Source tiers and verification methods

| Source tier | Sources |
|---|---|
| Tier 1 | 14 |
| Tier 2 | 14 |
| Tier 3 | 3 |
| Tier 4 | 1 |

| Verification method | Sources |
|---|---|
| fetched (full text) | 14 |
| fetched (partial text) | 1 |
| API response | 5 |
| search snippet only | 12 |
| not accessed | 0 |

## Claims supported only by search snippets

A search snippet is a lead, not evidence. These claims need a fetched or API source before any verdict can rise.

- C-010: iOS 27.2 fixed 163 vulnerabilities
- C-019: The usbliter8 BootROM exploit is reported to affect A12 and A13 chips and not A14 or later
- C-020: A tutorial page claims a full iOS 27 jailbreak using usbliter8

## Claims with no tier-1 support

These claims rest on secondary, community or unverifiable sources. They are recorded for transparency and should not be treated as established.

- C-003: iOS 27.0.1 build 24A446 is the build for iPhone16,2 (iPhone 15 Pro Max) (supporting tiers: 2, 3)
- C-004: The demonstrated jailbreak state persisted across a reboot (supporting tiers: 2)
- C-010: iOS 27.2 fixed 163 vulnerabilities (supporting tiers: 2)
- C-015: A publicly disclosed SPTM bypass applies to A17 Pro on iOS 27.0.1 (supporting tiers: 3)
- C-019: The usbliter8 BootROM exploit is reported to affect A12 and A13 chips and not A14 or later (supporting tiers: 2)
- C-020: A tutorial page claims a full iOS 27 jailbreak using usbliter8 (supporting tiers: 4)
- C-021: iOS 27.0.1 (24A446) is currently unsigned by Apple (supporting tiers: 2)
- C-022: A Calif.io-linked researcher reportedly announced a kernel read/write exploit and write-up within about a week (supporting tiers: 2, 3)
- C-023: An Apple CVE credit confirms the identity of the lambda handle, according to the reference repository (supporting tiers: 3)
- C-025: The device identifier iPhone16,2 corresponds to the iPhone 15 Pro Max (supporting tiers: 2)
- C-026: The iPhone 15 Pro Max uses the Apple A17 Pro chip (supporting tiers: 2)
- C-027: No public complete exploit chain applicable to iPhone 15 Pro Max on iOS 27.0.1 has been verified (supporting tiers: 2)
- C-030: The latest GitHub release of the repository named Sileo/Sileo is 2.5.1 (2024-10-08), and its notes do not mention iOS 27 (supporting tiers: 2)

## Claims with contradicting sources

- C-021: iOS 27.0.1 (24A446) is currently unsigned by Apple (contradicting: S-026)
- C-022: A Calif.io-linked researcher reportedly announced a kernel read/write exploit and write-up within about a week (contradicting: S-019)
- C-023: An Apple CVE credit confirms the identity of the lambda handle, according to the reference repository (contradicting: S-001)

## Checks applied

- Every claim has at least one supporting source.
- Every `verified` claim has a fetched, API or tier-1 supporting source and high confidence.
- Every `unverified` claim has low confidence.
- Each source lists the claims that cite it, and the reverse.
- All identifiers resolve, and all dates are valid and not in the future.

The mechanical checks are run by `scripts/validate_tracker.py`. They confirm structure, not truth.
