# DIM08: Jailbreak ecosystem

**v0.4.0 update (2026-11-12):** the ElleKit official repository states no version range and has no release (C-134); Procursus states no iOS range (C-135). Erosion and the SKVLENT repository are audited in [erosion-compatibility-audit.md](erosion-compatibility-audit.md) and [skvlent-a19pro-research-audit.md](skvlent-a19pro-research-audit.md). See [jailbreak-ecosystem-update.md](jailbreak-ecosystem-update.md) for the dated changes.

**Status:** Researched for this pass. Dopamine's release records, Sileo's latest release, ElleKit's repository move and the momentarius repository metadata are checked. Bootstrap and package-manager status for iOS 27.0.1 is not established.

## Dopamine (opa334)

| Item | Finding | Records |
|---|---|---|
| Latest official release | 3.0.13, published 2026-11-03. Its notes describe a posix_spawn hook fix and a SpringBoard snapshot change. | C-017, C-055, S-007 |
| Base release 3.0 | Published 2026-08-07. Its notes state: a Titan PPL/SPTM bypass for all devices on iOS 16.5.1 to 17.3.1; a momentarius PPL bypass for A12 and A13 devices on iOS 16.6 to 18.7.1 and 26.0 to 26.0.1; real-device SPTM support limited to iOS 17.3.1 because no SPTM bypass is known for 17.4 and later; iOS 27 betas testable on Corellium virtual devices; a ClearSword exploit named as an alternative to DarkSword. | C-065 to C-068, S-007 |
| Releases 3.0.2 to 3.0.13 | Published 2026-08-09 to 2026-11-03. The notes cover hook, panic, bootstrap, TrollStore and iOS 26 beta fixes. None mentions iOS 27 support. | C-055, S-007 |
| Update behaviour | The 3.0 notes say that a jbupdate from an earlier version triggers a full reboot by design. | S-007 |
| Earlier 2.5 betas | 2.5b1 (2026-03-26) added a DarkSword kernel exploit option for iOS 15.8.7 (A9 and A10) and 16.7 to 16.7.15 (arm64). | S-007 |
| Support range (third-party) | A third-party table lists iOS 15.0 to 17.3.1 for A14 to A17 and M1 to M2, and iOS 15.0 to 18.7.1 and 26.0 to 26.0.1 for A8 to A13. It is not an official source. | C-016, S-039 |
| Official README | The default-branch README describes an early rootless arm64e release for iOS 15.0 to 15.4.1. It has no current support matrix. **Superseded on 2026-11-12:** the default-branch README now lists rootless ranges to iOS 17.3.1 (arm64e) and 18.7.1 (arm64), and no iOS 27 range. See [jailbreak-ecosystem-update.md](jailbreak-ecosystem-update.md), C-133. | S-008, S-050 |
| iOS 27 on the A17 Pro | **No support documented.** Real-device SPTM support is limited to iOS 17.3.1 in the 3.0 notes. | C-018, C-066 |

Rootless and rootful status for the current 3.0.x line is not verified in this pass. The stale README's rootless wording refers to an early release only.

## Sileo

| Item | Finding | Records |
|---|---|---|
| Latest release | The repository named Sileo/Sileo has 2.5.1 as its latest release, published 2024-10-08. Its notes do not mention iOS 27. | C-030, S-031 |
| Identity | Taken from the repository name. Not confirmed against a project website. | C-030 |
| iOS 27 readiness | **Not established.** | CMP-011 |

## ElleKit

| Item | Finding | Records |
|---|---|---|
| Former repository | The former evelyneee/ellekit identifier (repository ID 559919558) redirects to tealbathingsuit/ellekit. The API confirms the ID match. | C-056, S-040 |
| Destination | Description: "yet another tweak injector / tweak hooking library for darwin systems". Created 2022-10-31. Last pushed 2026-07-31. No GitHub release. | C-056, S-040 |
| ElleKit 1.2 claim | The upstream reports that ElleKit 1.2 (2026-07-31) covers rootless injection on iOS 15 to 27. The upstream's source article was blocked to this review. The repository's push date matches the reported date but has no release record. | C-057 |
| iOS 27 readiness | **Not established.** | CMP-011 |

## momentarius

| Item | Finding | Records |
|---|---|---|
| Repository metadata | Description "A12/A13 PPL Bypass". Created 2026-08-07, last pushed 2026-08-07, updated 2026-11-05. MIT licence. Not archived or forked. | C-058, S-041 |
| Dopamine's notes | Dopamine 3.0 lists a momentarius PPL bypass for A12 and A13 on iOS 16.6 to 18.7.1 and 26.0 to 26.0.1. | C-067, S-007 |
| Scope | A12 and A13 only. Not applicable to the A17 Pro. The code was not reviewed or run. | C-058, C-067 |

## Bootstrap and package management

No verified bootstrap exists for iOS 27.0.1 on the A17 Pro (CMP-010). Dopamine's real-device SPTM limit is iOS 17.3.1 (C-066). Package-manager readiness is not established (CMP-011).

## BootROM issue (A12 and A13)

Several outlets and a national CERT advisory describe a BootROM (SecureROM) flaw in A12 and A13 chips, which later designs reportedly avoid (C-019, partially verified). The A17 Pro is not reported as affected.

## Tutorial pages and project announcements

- A tutorial-style web page claims a complete iOS 27 jailbreak using the BootROM issue. Its claims are unverified and it is not used as evidence (C-020, S-025).
- A project announced in November 2026 for iOS 27.0 to 27.0.1 is unverified and carries a high risk (C-064). No release was reviewed in this pass.

## Gaps and next steps

1. Identify the official ElleKit upstream and record its releases, if one is published.
2. Check Sileo's release records and project channels for any iOS 27 support statement.
3. Re-check Dopamine's release notes and default-branch activity at each update, including any change to the 17.3.1 real-device limit (C-066).
4. Record any official iOS 27 support statement as a new source, and update CMP-010 and CMP-011.
