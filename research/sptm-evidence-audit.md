# SPTM evidence audit

**Status:** research record, 2026-11-12. Highest-priority dimension (DIM03). Target: iPhone 15 Pro Max (A17 Pro, `iPhone16,2`), iOS 27.0.1 (build 24A446).

This audit grades evidence. It does not describe any bypass. It records no exploit steps, code or tools.

## Bottom line

1. **A public SPTM bypass for the target is not established.** No primary source verifies a public SPTM bypass for the A17 Pro on any iOS 27 build.
2. **Apple places the A17 Pro in the SPTM class.** Apple's platform security guide says SPTM is supported on A15-or-later and M2-or-later SoCs and replaces PPL on supported platforms (C-013). The A17 Pro is an A15-or-later chip. C-014 stays partially verified, because the guide states the class and not the device.
3. **Dopamine's own notes place the public limit at iOS 17.3.1.** The Dopamine 3.0 release notes (2026-08-07) say that real-device SPTM support "only works up to 17.3.1 ... due to lack of an SPTM bypass on >=17.4" (C-066).
4. **A bypass is reported, not verified.** A community reference reports an SPTM bypass valid through iOS 27.0.1, reportedly patched in a 27.2 beta (C-051, unverified). The primary post was not retrieved. No technical detail is public.
5. **Independent public SPTM research does not cover this target.** The arXiv analysis of October 2025 uses an iPhone 16 (A18) on iOS 18.4 and 18.5. It does not mention the A17 Pro or any iOS 27 build (C-060).
6. **Apple's iOS 27 and 27.2 advisories name no SPTM, TXM, PPL, AGX or IOGPU component** (C-073). Apple's notes name components and impacts, not mitigations, so a change to PPL or SPTM would not necessarily appear in them.

## Evidence graded

| # | Evidence | Source and tier | Method | What it states | Scope | Grade | Records |
|---|---|---|---|---|---|---|---|
| E1 | Apple platform security guide: SPTM is supported on A15-or-later and M2-or-later SoCs and replaces PPL on supported platforms | S-004, tier 1 | Fetched | Support class | General | Verified | C-013 |
| E2 | Apple guide: PPL and SPTM enforce signed-and-trusted code on all platforms except macOS | S-004 | Fetched | Enforcement | General | Verified | C-032 |
| E3 | Apple guide table: SPTM is grouped with A15 to A18 in the feature table | S-004 | Fetched | Table grouping (cell layout not fully extracted) | A15 to A18 | Partially verified | C-014 |
| E4 | arXiv 2510.09272 (submitted 2025-10-10): SPTM and TXM were released for A15 or M2 and later SoCs in 2023, and SPTM replaced PPL on those SoCs | S-035, tier 2 | Fetched full text | Independent description of the architecture | A15 and M2 or later | Verified (as stated) | C-059 |
| E5 | arXiv 2510.09272: the firmware analysis used iOS 18.4 (22E240) for an iPhone 16. A research device ran iOS 18.5 | S-035 | Fetched full text | Scope of the paper's work | iPhone 16; iOS 18.4 and 18.5 | Verified (scope) | C-060 |
| E6 | Dopamine 3.0 release notes (2026-08-07): a Titan PPL/SPTM bypass introduces support for all devices on iOS 16.5.1 to 17.3.1 | S-007, tier 1 (release record) | API | The project's own support statement | iOS 16.5.1 to 17.3.1 | Verified (as stated) | C-065 |
| E7 | Dopamine 3.0 release notes: real-device SPTM support ends at iOS 17.3.1 because no bypass is known for 17.4 and later. iOS 27 betas can be tested on Corellium virtual devices | S-007 | API | The project's own limit as of 2026-08-07 | Real devices on iOS 17.4 and later | Verified (as stated) | C-066 |
| E8 | 8kSec analysis (dated 2026-05-03): SPTM is an A15-and-later replacement for PPL | S-042, tier 2 | Fetched | Conceptual description | A15 and later | Consistent with E1 | — |
| E9 | Upstream V7: an opa334 PSA dated 2026-10-17 warns of an SPTM bypass valid through 27.0.1 | S-026 (upstream) | Not retrieved | Reported statement | Through 27.0.1 (as reported) | Unverified | C-051 |
| E10 | Upstream V31: opa334 (2026-11-04) says A14 and later still need an n-day SPTM bypass | S-026 (reprints) | Not retrieved | Reported statement | A14 and later (as reported) | Unverified | C-050 |
| E11 | Upstream V8: the bypass alone is not enough for iOS above 26.0.1 | S-026 | Not retrieved | Reported quote | Not stated | Unverified | C-054 |
| E12 | Apple iOS 27 and 27.2 advisory text: no SPTM, TXM, PPL, AGX or IOGPU term | S-001, S-033 | Text search | Absence in the advisories | iOS 27 and 27.2 | Verified (absence) | C-073 |
| E13 | Demonstration reported on an iPhone 18 Pro (A20 Pro) on iOS 27.0.1 | S-036, S-037 (press); S-026 (upstream) | Fetched (press) | A demonstration on a different chip | A20 Pro | Not evidence for the A17 Pro | C-001, C-002 |

## Classification

- **Public, verified, applicable to the target:** none.
- **Public, verified, different scope:** the arXiv analysis (A18 class, iOS 18.4 and 18.5); the Dopamine Titan bypass (iOS 16.5.1 to 17.3.1, released 2026-08-07).
- **Reported, unverified:** the 2026-10-17 bypass (E9); the A14-and-later statement (E10); the "above the silicon ceiling" remark that accompanies E10 (C-050).
- **Unpublished:** the technical content of any reported bypass. No public proof of concept, write-up or repository for an SPTM bypass applicable to the target was found.

## A17 Pro applicability

- The A17 Pro falls in the A15-or-later class (E1, E3).
- Dopamine's own limit (E7) puts the last documented public real-device SPTM route before iOS 17.4. No public tool documents an SPTM bypass on iOS 27.0.1.
- If the reported 2026-10-17 bypass is real and valid through 27.0.1, it would be the first documented route past that limit. The reports do not name device families, so applicability to the A17 Pro is **not established**.
- The demonstration on an A20 Pro does not establish A17 Pro support (C-002).
- The arXiv analysis does not establish any property of the A17 Pro's SPTM.

## Comparison with the upstream

The upstream rates V7 as partially true (medium) and V8 as verified (high). This audit records both as unverified. The reasons: the primary PSA was not retrieved, the upstream's quotes are second-hand, and V8's version bound conflicts with the fixed-in versions that 8kSec reports for the DarkSword CVEs (C-069). See [upstream-reconciliation.md](upstream-reconciliation.md).

## Contradictions and gaps

- **Timing:** Dopamine's 2026-08-07 statement that no bypass exists for iOS 17.4 and later predates the reported 2026-10-17 PSA. The two are not contradictory in time order. The later report remains unverified.
- **Gap:** the opa334 PSA of 2026-10-17, the post behind E10, and any primary technical write-up of an SPTM bypass were not retrieved.
- **Gap:** Apple's SPTM documentation specific to iOS 27. The platform guide saved on 2026-11-12 is general, and its publication date was not captured.
- **Gap:** Apple's advisories do not describe mitigations, so they cannot show whether PPL or SPTM changed in 27.2.

## What would change this audit

1. A primary technical publication of an SPTM bypass that names device families and iOS versions, with independent reproduction on the exact target. This project does not run exploit code on any device.
2. An Apple statement or advisory entry that names an SPTM or TXM fix with affected versions.
3. An official Dopamine or other project release note that extends real-device SPTM support beyond iOS 17.3.1.

The project does not download, run or test any code that claims to be an SPTM bypass.
