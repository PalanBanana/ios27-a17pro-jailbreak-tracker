# Jailbreak ecosystem update (v0.5.0)

**Status:** re-check of the public sources of the jailbreak ecosystem projects on 2026-11-12, as an update to DIM08 and to the v0.4.0 ecosystem update. Metadata and public documents only. No project was installed, run or built. Readiness: **LEVEL 0 / NO-GO**, unchanged.

Summary: every project re-checked matches its v0.4.0 record, except for one lookup correction recorded below. No project states support for iOS 27.0.1 on the A17 Pro.

## 1. Table

| Project | Repository | Latest release | Default-branch head | Last push | Licence (metadata) | Official compatibility statement | Missing prerequisites | Build status | Change from v0.4.0 |
|---|---|---|---|---|---|---|---|---|---|
| Dopamine | opa334/Dopamine (branch 3.x) | 3.0.13 (2026-11-03) | 5b1d2c1c3bf5 | 2026-11-03 | MIT | README: rootless semi-untethered jailbreak for iOS 15.0 to 17.3.1 (arm64e), 15.0 to 18.7.1 (arm64) and 26.0 to 26.0.1 (A12 and A13). No iOS 27 entry | The target is in no listed range. Version-support requests are deleted without response | Not checked | None |
| Sileo | Sileo/Sileo | 2.5.1 (2024-10-08) | Commit dated 2024-10-08 | 2025-12-08 | BSD-4-Clause | No iOS 27 statement (S-031) | A package manager is not a jailbreak. No target statement | Not checked | None |
| ElleKit (official) | dhinakg/ellekit-official | None | 762e68ae9948 (2026-08-10) | 2026-08-10 | None in metadata | No iOS version range (C-134) | Version range and release absent | Not checked | None |
| ElleKit (former) | tealbathingsuit/ellekit (reached by redirect from evelyneee/ellekit) | None | Not re-listed | 2026-07-31 | BSD-3-Clause | Not stated | No release | Not checked | None (confirmed) |
| Procursus (bootstrap) | ProcursusTeam/Procursus | None | b6185221bf1c (commit dated 2026-05-30) | 2026-11-12 (any branch) | 0BSD | README: cross-compiled bootstrap; no iOS range in the lines read (C-135) | Bootstrap for 27.0.1 not established (CMP-010) | Not checked | None |
| iMaxTomas tracker | iMaxTomas/ios27-jb-tracker | Not applicable | 038b9f090564 (2026-11-06) | 2026-11-06 | NOASSERTION | Chip-status table: no publicly usable PPL or SPTM bypass known for 27.0.1 (C-136) | Its own statements only | Not checked | None |
| Community repository | Created 2026-11-09 (S-053); metadata only | None | Not applicable | 2026-11-09 | None | Its description claims kernel-surface exploitation on other devices (C-137) | Not analysed | Not checked | None |
| opa334/ElleKit | opa334/ElleKit | None | Not recorded | 2024-04-26 | BSD-3-Clause | Not relevant to the tracker's records | Not used | Not checked | Lookup corrected: this is not the former repository |
| momentarius | Not re-checked in this pass | Not applicable | Not applicable | Not applicable | Not applicable | A12 and A13 only (C-058) | Not re-checked | Not checked | No change recorded |

## 2. Correction

- The former ElleKit repository in the v0.4.0 records is tealbathingsuit/ellekit (S-040). On 2026-11-12 a lookup against opa334/ElleKit, a different repository pushed on 2024-04-26, was an error. It is not used as a record (C-167).
- The Dopamine repository's licence (MIT) is recorded here from metadata. The v0.4.0 records did not include it.

## 3. Reading the table

- Do not infer modern iOS 27 support from legacy A17 support. Dopamine's arm64e range ends at iOS 17.3.1, and its README names no iOS 27 entry.
- Do not infer package-manager compatibility from a standalone package-manager release. Sileo's latest release predates iOS 27 and makes no iOS 27 statement.
- Do not treat customisation tools as full jailbreaks. Erosion is recorded in its own note: [Erosion current status](erosion-current-status.md).

## 4. Device and architecture statements

- Dopamine's README distinguishes arm64e and arm64 devices. The repository's device profile (docs/DEVICE_PROFILE.md) records the target architecture as arm64 without a source. The planning brief for this release lists ARM64 and arm64e. The distinction is not resolved in this release.
- No ecosystem project named in this table names the A17 Pro.

## 5. Not checked

- Build status and CI results of third-party repositories.
- momentarius, in this pass.
- Any binary, package or release asset.

See the [dependency update](../reports/a17pro-jailbreak-dependency-update.md).
