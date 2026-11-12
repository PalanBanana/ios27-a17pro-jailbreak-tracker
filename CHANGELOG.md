# Changelog

All notable changes to this repository are recorded here. Dates use ISO 8601 (`YYYY-MM-DD`). Records are superseded, never deleted.

## [Unreleased]

### Added

- Claims C-089 to C-107 for builds 24A446, 24B119 and 24B156: manifest and container verification for the two 27.2 builds; identity of the SPTM and TXM containers between 27.2 and 27.2.1; kernel version strings; KEXT inventory counts; the arm64e header flag; the scope of a third-party symbolication signature set and the presence of its anchor strings in the kernelcache; name conflicts and a small cross-check; the mechanism of a standalone KEXT import failure; the KEXT inventory reconciliation; a disagreement on register-indirect control flow in the monitors; four methods on the `__DATA_SPTM` segment; and Apple's Platform Security guide statements on SPTM, MIE and the A15-A18 table column.
- Sources S-044 and S-045: Apple CDN objects for iOS 27.2 (24B119) and iOS 27.2.1 (24B156), retrieved in part by HTTP range requests on 2026-11-12. The complete packages were not hashed. Source S-046: the `kernel/27.0` signature folder of a community symbolication repository (MIT licence), read at a single commit.
- Timeline event E-032 (static research update; no release).
- Public reports: `reports/ghidra-kernel-symbolication.md`, `reports/ghidra-kext-loader-investigation.md`, `reports/sptm-semantic-analysis.md`, `reports/txm-semantic-analysis.md`, `reports/firmware-diff-27.0.1-27.2.md`, `reports/firmware-diff-27.0.1-27.2.1.md`, `reports/a17pro-memory-protection-analysis.md` and `reports/ghidra-cve-correlation.md`.
- Count-level inventories: `analysis/kext-reconciliation.json`, `analysis/firmware-diff-metadata.json` and `analysis/kernel-symbolication-metrics.json`.

### Changed

- S-004 (Apple Platform Security guide) was re-read on 2026-11-12. Its access date and reliability note are updated. C-013 is unchanged. C-107 records the range reading of the A15-A18 column and the fact that its cells could not be read.
- S-043 gained the claims that cite it. The firmware rows for 24B119 and 24B156 list S-044 and S-045.

### Notes

- Two analyses were declined and are not in this release: code-level differencing between 24A446 and later builds, and binary-to-advisory correlation. The firmware comparison is metadata only, and no difference is read as a security fix. The advisory page records advisory-level counts only.
- Standalone KEXT files are not imported for analysis, because the release kernelcache's stub tables make the standalone import fail. The fileset program is used instead.
- Symbol names, addresses, symbol listings, Ghidra projects and firmware bytes are not published. Symbolication is reported as counts.
- The monitor reference counts were taken from a read-only copy of the Ghidra project.
- No release was created. The findings support the research record and do not change readiness (LEVEL 0, NO-GO).

## [0.2.0] - 2026-11-12

### Added

- `research/apple-27x-cve-mapping.md`: every CVE entry on Apple's iOS 27, 27.2 and 27.2.1 security pages, with its component, Apple's impact text, device list and entry note. Generated from the saved pages. No credit names or handles are reproduced.
- `research/sptm-evidence-audit.md`: a graded audit of SPTM evidence (highest-priority research).
- `research/krw-release-audit.md`: the announced kernel read/write release, its timeline and the checks made.
- `research/upstream-reconciliation.md`: a claim-by-claim comparison with the community reference (V1 to V33, E1 to E3, P1 to P6, O1 to O3).
- `research/calif-hexacon-deep-audit.md`: directly sourced facts, secondary interpretations, and the differences between the A20 Pro demonstration and the A17 Pro target.
- `reports/dependency-matrix.md` and `reports/a17pro-exploit-readiness.md`: the dependency view, and the detailed readiness and GO/NO-GO analysis.
- Claims C-062 to C-077; timeline events E-024 to E-030; sources S-033 to S-042 (Apple iOS 27.2 and 27.2.1 pages, an independent SPTM paper, press articles, a third-party page, repository metadata and a security-company analysis).
- Source type `academic_paper` in `schemas/source.schema.json`.

### Changed

- The Dopamine record (C-016) is now based on the 3.0 release notes (C-065 to C-068) as well as on a third-party table. The release notes state that real-device SPTM support ends at iOS 17.3.1.
- Calif.io credit counts are recorded per page: four on the iOS 27 page (C-038) and six on the iOS 27.2 page (C-042). Kernel-memory impacts are recorded by page and category (C-034 to C-041).
- Claims C-016, C-021, C-034 to C-061 were corrected or re-scoped. Earlier wording is superseded in the records, not deleted; `last_checked` dates show the change.
- Firmware records for 24A437, 24B119 and 24B156 list every CVE identifier on the corresponding Apple page. Signing observations keep their checked dates.
- Compatibility rows CMP-003 to CMP-014 updated with the evidence above. CMP-014 records that the announced kernel read/write work is not published.
- Research documents DIM03 to DIM10 and `research/contradictions.md` updated. `reports/exploit-readiness.md` is now a summary that points to the detailed readiness report.

### Corrected

- The Dopamine 3.0 release notes were checked. They state a Titan bypass for iOS 16.5.1 to 17.3.1 and no real-device SPTM bypass for iOS 17.4 and later (C-065, C-066).
- Apple lists CVE-2026-112705 as unexpected system termination, not as kernel memory. The upstream reference's kernel label is recorded and not adopted (C-044).
- The former ElleKit repository identifier redirects to `tealbathingsuit/ellekit`, which has no GitHub release (C-056).
- Apple's iOS 27.2 release date is 26 October 2026 (18:33 UTC in the index). The upstream's 27 October is probably Beijing time (contradictions.md, row 11).
- A third-party index and a community reference disagree on the signing status of 24A446 at different dates. The change is recorded, not resolved (C-021, E-030).

### Recorded (2026-11-12)

- Apple's iOS 27 page lists 162 CVE-2026 identifiers; the iOS 27.2 page lists 162 (press reports 163); the iOS 27.2.1 page lists 9. The iOS 27.0.1 index lists none.
- The iOS 27.2 page lists 23 kernel-memory entries (4 write, 12 corruption, 1 copy-on-write, 6 read or disclosure) and no kernel or root privilege entry. Its six Calif.io-credited entries have no kernel-memory impact.
- The iOS 27 page lists four kernel or root privilege entries and marks many entries as added or updated on 2026-10-19 and 2026-10-26.
- Apple's advisory text contains no SPTM, TXM, PPL, AGX, IOGPU, CoreTrust, AMFI or Exclave term.
- The independent SPTM paper analyses an iPhone 16 on iOS 18.4 and 18.5 and does not mention the A17 Pro or iOS 27.

### Not changed

- The target profile, readiness level (LEVEL 0), GO/NO-GO (NO-GO) and the snapshot date (2026-11-12).
- No device was connected, updated, restored, rebooted or modified for this research. No exploit code was downloaded, run or linked.

### Notes

- Unverified claims kept as leads include: a reported SPTM bypass valid through iOS 27.0.1 (C-051); a reported kernel read/write release (C-022, C-049); a reported crash reproduction on another model (C-062); and a project claim for iOS 27.0 to 27.0.1 (C-064), which carries a high risk.
- Personal details about individuals in the upstream reference are not reproduced.

### Release rule

- v0.2.0 is tagged only after the CI workflows pass for the release commit. v0.1.1 and v0.1.0 are not moved.

## [0.1.1] - 2026-11-12

### Added

- Research priorities (P0, P1 and P2) recorded in `STATUS.md`. No data, verdict or readiness level changed.
- Validator check that fails when maintainer device-state phrases appear in published text (`scripts/validate_tracker.py`).

### Changed (privacy correction)

- Removed statements about a maintainer's personal device, including its installed firmware, its update configuration and its usage, from the documentation.
- Added a target profile statement to `docs/DEVICE_PROFILE.md`, `README.md` and `README_KR.md`. It describes the research target only.
- Revised the preservation, recovery and safety guidance so that it refers to any real device rather than to a particular one. The guidance is otherwise unchanged.
- Public firmware signing observations keep their sources and last-checked dates.
- The research target, compatibility scope, evidence records, verdicts and readiness level are unchanged.

### Notes

- Published history was not rewritten. Earlier commits and the v0.1.0 release (its tag and release notes) still contain the earlier wording. This release does not erase them.
- The `[0.1.0]` section of this file was revised to remove the same wording. The v0.1.0 tag and release were not changed.

## [0.1.0] - 2026-11-12

### Added

- Initial public research tracker for the iPhone 15 Pro Max (A17 Pro, `iPhone16,2`) on iOS 27.0.1 (build 24A446): 32 sources, 32 claims, 17 timeline events, 15 compatibility rows and 4 firmware builds.
- JSON Schemas for claims, sources, timeline, compatibility and firmware records.
- `scripts/validate_tracker.py`: schema, reference, reciprocity, verdict, privacy-pattern, link and README checks.
- Research documents DIM01 to DIM12 and `research/contradictions.md`.
- Reports: latest status, compatibility, firmware, exploit readiness and evidence audit.
- Governance and documentation: README (English and Korean), CONTRIBUTING, CODE_OF_CONDUCT (adapted from the Contributor Covenant, version 2.1), SECURITY, CLAUDE.md, SKILL.md, CONTEXT, STATUS, and documents on the device profile, research methodology, safety policy, FAQ and recovery.
- Issue forms, a pull request template, and two workflows: `validate` and `secret-scan`. Third-party actions are pinned to commit SHAs.
- Licences: MIT for code (`LICENSE`) and CC BY 4.0 for documentation (`LICENSE-DOCS`).

### Recorded (2026-11-11 snapshot)

- Apple's security releases index lists no published CVE entries for iOS 27.0.1 (C-007).
- Apple's iOS 27 security notes credit Calif.io researchers for four CVE entries (C-005).
- Apple's Memory Integrity Enforcement post names iPhone 17, iPhone Air, the A19 and the A19 Pro (C-011).
- Apple's Platform Security guide states SPTM availability on A15-or-later and M2-or-later SoCs (C-013).
- Dopamine's latest official release is 3.0.13, published 2026-11-03 (C-017). Its recent commit subjects do not mention iOS 27 (C-033).
- The latest GitHub release of the repository named Sileo/Sileo is 2.5.1, published 2024-10-08, and its notes do not mention iOS 27 (C-030, partially verified).
- A third-party index marks build 24A446 as not signed, and a community reference reports it as signed on 2026-11-02. The conflict is unresolved (C-021).

### Corrected

- Apple's page lists four Calif.io-credited CVE entries, not three. CVE-2026-86886 (impact: an app may be able to modify protected system files) was missed in the first extraction. C-005, S-001, the firmware record for build 24A437 and the affected reports were updated. Earlier records were not deleted; the correction is recorded in `research/contradictions.md`.

### Documented (2026-11-12)

- Research target profile, firmware preservation limits, and public firmware signing observations with their sources (see `docs/DEVICE_PROFILE.md` and `docs/RECOVERY_AND_PRESERVATION.md`).
- Research re-check on 2026-11-12: no new iOS 27 build, no signing change in the third-party index, no Dopamine release or default-branch commit since 3.0.13, no new pwnlambda repository, and no published kernel read/write write-up found. Result: no material change, apart from the correction above.

### Changed

- Sources S-001, S-002, S-007, S-014 and S-032 were re-checked on 2026-11-12, and their access dates updated. Claims re-checked on that date have their `last_checked` dates updated.
- The `notes` field in source records may now be `null` (schema change in `schemas/source.schema.json`). No record was altered to meet it.
- Sources S-031 and S-032 and claims C-030, C-032 and C-033 were added, and the Sileo compatibility row (CMP-011) was updated.

### Release rule

- v0.1.0 is tagged only after the CI workflows pass for this commit. Open research items are listed in `STATUS.md`.
