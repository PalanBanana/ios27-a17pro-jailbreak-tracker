# DIM08: Jailbreak ecosystem

**Status:** Partially researched. Dopamine (release record, commit history and support table), Sileo (latest release) and the BootROM issue are checked. ElleKit and bootstrap or rootless status for iOS 27 are not established in this pass.

## Dopamine (opa334)

| Item | Finding | Records |
|---|---|---|
| Latest official release | 3.0.13, published 2026-11-03. | C-017, S-007 |
| Recent commits | The five most recent default-branch commit subjects (2026-10-30 to 2026-11-03) mention SpringBoard snapshot and posix_spawn hook fixes, detection for the iOS 26.0 beta, and the 3.0.13 release. None mentions iOS 27. Commit bodies were not reviewed. | C-033, S-032 |
| Documented support range | Secondary coverage quotes support for A15, A16, A17 and M2 devices up to iOS 17.3.1, and for A12 and A13 up to 26.0.1. Not confirmed from an official page. | C-016, S-009 |
| Official README | The main-branch README describes an early rootless arm64e release for iOS 15.0 to 15.4.1 and states that more details will follow. It contains no current support matrix. | S-008 |
| iOS 27 on A17 Pro | **No support documented.** | C-018 |

Rootless and rootful status for the current 3.0.x line is **not verified** in this pass. The stale README's "rootless" wording refers to an early release only.

## Sileo

| Item | Finding | Records |
|---|---|---|
| Latest release | The repository named Sileo/Sileo has 2.5.1 as its latest release, published 2024-10-08. Its release notes do not mention iOS 27. | C-030, S-031 |
| Identity | Taken from the repository name. Not confirmed against a project website. | C-030 |
| iOS 27 readiness | **Not established.** | CMP-011 |

## ElleKit

A name search returned several candidate repositories. None was confirmed as the official upstream. The top two candidates have no GitHub release. ElleKit's status for iOS 27 is therefore **not established**. No upstream has been identified in this pass.

## Bootstrap and package management

No verified bootstrap exists for iOS 27.0.1 on the A17 Pro (CMP-010). Package-manager readiness is not established (CMP-011).

## BootROM issue (A12 and A13)

Several outlets and a national CERT advisory describe a BootROM (SecureROM) flaw in A12 and A13 chips, which later designs reportedly avoid (C-019, partially verified). The A17 Pro is not reported as affected. The reports reviewed do not include an original researcher write-up.

## Tutorial pages

A tutorial-style web page claims a complete iOS 27 jailbreak using this BootROM issue. Its claims are unverified and it is not used as evidence (C-020, S-025).

## Gaps and next steps

1. Identify the official ElleKit upstream and record its releases.
2. Check Sileo's release records and project channels for any iOS 27 support statement.
3. Check Dopamine's release notes and default-branch activity at each update.
4. Record any official iOS 27 support statement as a new source, and update CMP-010 and CMP-011 accordingly.
