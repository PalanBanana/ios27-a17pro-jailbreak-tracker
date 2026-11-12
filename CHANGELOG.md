# Changelog

All notable changes to this repository are recorded here. Dates use ISO 8601 (`YYYY-MM-DD`). Records are superseded, never deleted.

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
