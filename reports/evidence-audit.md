# Evidence audit

**Snapshot:** 2026-11-11. This audit checks how well each claim is supported, which sources carry the most weight, and where the evidence is weakest.

## Verdict counts

| Verdict | Claims |
|---|---|
| verified | 87 |
| partially verified | 27 |
| unverified | 22 |
| disproved | 0 |
| superseded | 0 |

## Source tiers and verification methods

| Source tier | Sources |
|---|---|
| Tier 1 | 27 |
| Tier 2 | 20 |
| Tier 3 | 8 |
| Tier 4 | 1 |

| Verification method | Sources |
|---|---|
| fetched (full text) | 26 |
| fetched (partial text) | 11 |
| API response | 8 |
| search snippet only | 11 |
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
- C-021: iOS 27.0.1 (24A446) is unsigned in the ipsw.me index on 2026-11-12, after a 2026-11-02 report that it was signed (supporting tiers: 2)
- C-022: A Calif.io-linked researcher reportedly announced a kernel read/write exploit and write-up within about a week (supporting tiers: 2, 3)
- C-023: An Apple CVE credit confirms the identity of the lambda handle, according to the reference repository (supporting tiers: 3)
- C-025: The device identifier iPhone16,2 corresponds to the iPhone 15 Pro Max (supporting tiers: 2)
- C-026: The iPhone 15 Pro Max uses the Apple A17 Pro chip (supporting tiers: 2)
- C-027: No public complete exploit chain applicable to iPhone 15 Pro Max on iOS 27.0.1 has been verified (supporting tiers: 2)
- C-030: The latest GitHub release of the repository named Sileo/Sileo is 2.5.1 (2024-10-08), and its notes do not mention iOS 27 (supporting tiers: 2)
- C-050: opa334 is reported (2026-11-04) to plan A12/A13 Dopamine support via momentarius once a kernel read/write exploit is public, with A14 and later still needing an SPTM bypass (supporting tiers: 3)
- C-051: A 2026-10-17 opa334 statement is reported to warn of an SPTM bypass valid through iOS 27.0.1 (upstream V7) (supporting tiers: 3)
- C-052: A Calif.io researcher is reported to have said the jailbreak applies to any iPhone running iOS 27.0.1, possibly including iPads (upstream V10) (supporting tiers: 3)
- C-053: A Calif.io video is reported to show a jailbreak state surviving an over-the-air update to iOS 27.2 with Lockdown Mode enabled (upstream V32) (supporting tiers: 3)
- C-054: The upstream states that DarkSword and ClearSword kernel exploits support iOS only up to 26.0.1 (V8); no primary source confirms the range (supporting tiers: 3)
- C-056: The repository formerly at evelyneee/ellekit redirects to tealbathingsuit/ellekit, which has no GitHub release (supporting tiers: 2)
- C-057: ElleKit 1.2 is reported to cover iOS 15 to 27 (upstream reference) (supporting tiers: 3)
- C-058: A public GitHub repository named staturnzz/momentarius is described as an A12/A13 PPL bypass (supporting tiers: 3)
- C-060: The arXiv SPTM analysis's firmware work uses an iPhone 16 on iOS 18.4. The paper does not analyse the A17 Pro or any iOS 27 build (supporting tiers: 2)
- C-061: Press coverage reports that AI helped build the Calif.io jailbreak (not confirmed by the team) (supporting tiers: 2)
- C-062: A third party is reported to have reproduced CVE-2026-112705 as a crash on iPhone 17 Pro, iOS 27.0.1 (unverified) (supporting tiers: 3)
- C-063: A company-branded account is reported to have shown a root shell on iOS 27.2 (unverified) (supporting tiers: 3)
- C-064: A project announced on 2026-11-01 claims a semi-untethered iOS 27.0 to 27.0.1 jailbreak for iPhone 15 Pro Max (A17 Pro); no release or validation was located (supporting tiers: 3)
- C-069: 8kSec reports Apple's fixed-in versions for the two DarkSword kernel CVEs as iOS 26.2 and 26.3 (secondary analysis) (supporting tiers: 2)
- C-075: heise reports the Calif.io jailbreak as 'the first reboot-proof jailbreak since iOS 9' (press claim; unverified) (supporting tiers: 2)
- C-076: t3n reports AI-assisted exploit-chain discovery and an iOS 27.2 beta comparison as established; heise calls the comparison theoretical (supporting tiers: 2)
- C-077: The upstream reports a Calif.io team member saying the team will not release an end-user jailbreak tool (unverified) (supporting tiers: 3)
- C-097: The signature set kernel/27.0 in the symbolicator repository declares a darwin range of 27.0.0 to 27.2.0 (supporting tiers: 3)
- C-136: The upstream iMaxTomas tracker, at commit 038b9f09 (2026-11-06), states that no publicly usable PPL or SPTM bypass is known for iOS 27.0.1 (supporting tiers: 3)
- C-137: A community repository created on 2026-11-09 claims IOSurface kernel-surface exploitation on devices described as iPhone 13 Pro and iPhone 17 Pro (supporting tiers: 3)

## Claims with contradicting sources

- C-021: iOS 27.0.1 (24A446) is unsigned in the ipsw.me index on 2026-11-12, after a 2026-11-02 report that it was signed (contradicting: S-026)
- C-022: A Calif.io-linked researcher reportedly announced a kernel read/write exploit and write-up within about a week (contradicting: S-019)
- C-023: An Apple CVE credit confirms the identity of the lambda handle, according to the reference repository (contradicting: S-001)
- C-042: The six Calif.io-credited entries in Apple's iOS 27.2 notes carry no kernel read or write impact (contradicting: S-026)
- C-044: Apple's entry for CVE-2026-112705 lists the AVEVideoEncoder component with an impact of unexpected system termination, not a kernel-level impact (contradicting: S-026)
- C-046: Apple's iOS 27.2 notes contain 162 distinct CVE identifiers in the extracted text; press reports 163 (contradicting: S-017)
- C-054: The upstream states that DarkSword and ClearSword kernel exploits support iOS only up to 26.0.1 (V8); no primary source confirms the range (contradicting: S-042)
- C-057: ElleKit 1.2 is reported to cover iOS 15 to 27 (upstream reference) (contradicting: S-040)
- C-075: heise reports the Calif.io jailbreak as 'the first reboot-proof jailbreak since iOS 9' (press claim; unverified) (contradicting: S-026)

## Checks applied

- Every claim has at least one supporting source.
- Every `verified` claim has a fetched, API or tier-1 supporting source and high confidence.
- Every `unverified` claim has low confidence.
- Each source lists the claims that cite it, and the reverse.
- All identifiers resolve, and all dates are valid and not in the future.

The mechanical checks are run by `scripts/validate_tracker.py`. They confirm structure, not truth.
