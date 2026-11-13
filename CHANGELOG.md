# Changelog

All notable changes to this repository are recorded here. Dates use ISO 8601 (`YYYY-MM-DD`). Records are superseded, never deleted.

## [Unreleased]

### Added

- Documentation completion for v0.5.0 (no new research, no data changes, no release): `research/cross-generation-security-matrix.md` (A17 Pro, A18 Pro and A19 Pro manifest comparison, metadata level), `reports/ghidra-exclave-research-integration.md` (counts and conclusions from the existing local static analysis, with no offsets or paths), `docs/RESEARCH_WORKFLOW.md`, `docs/AGENT_CONFIGURATION.md` and `docs/USAGE_EFFICIENCY.md`.
- Two read-only research agent definitions in `.claude/agents/` (`primary-source-auditor`, `manifest-auditor`). A restart of the Claude Code session may be needed before they are discovered.

## [0.5.0] - 2026-11-12

### Added

- Apple Secure Exclaves architecture from Apple's 2026-11-12 article, read in full; quoted phrases were checked by exact match. See `research/apple-secure-exclaves-architecture.md`, `research/apple-security-terminology.md` and `reports/secure-exclaves-architecture-map.md`.
- Manifest reconciliation: every BuildIdentity of the A17 Pro manifests (24A446, 24B119, 24B156), the A18 Pro manifest (24B119) and the A19 Pro manifest (24A446), with SHA-256 hashes preserved. See `research/exclave-manifest-reconciliation.md`, `reports/a17pro-exclave-applicability.md` and `analysis/exclave-buildidentity-summary.json`.
- Static exclave-identifier counts for the target build's decompressed kernelcache and SPTM image (counts only; identifier names are not published), and public XNU source observations (counts and paths only).
- Architecture matrix and boundary analysis: `reports/apple-silicon-security-matrix.md`, `research/a17pro-security-boundaries.md`, `research/exclave-security-implications-for-jailbreak.md` and `reports/a17pro-jailbreak-dependency-update.md`.
- Re-checks: SKVLENT (`research/skvlent-latest-update-audit.md`, `reports/skvlent-evidence-reconciliation.md`), Erosion (`research/erosion-current-status.md`, `reports/erosion-a17pro-risk-assessment.md`) and the ecosystem repositories (`research/jailbreak-ecosystem-v050-update.md`).
- Summary and priorities: `reports/v0.5.0-research-summary.md`; `reports/next-research-priorities.md` (updated).
- Claims C-138 to C-169, sources S-057 to S-061, timeline events E-036 to E-038, and compatibility rows CMP-019 and CMP-020.

### Changed

- C-122 and C-123 were re-enumerated against every identity. C-124 gained a limitation note. C-111 gained the direction 10 wording at commit 73f7a579ce91 (C-165).
- Compatibility rows CMP-001, CMP-010, CMP-011, CMP-016, CMP-017 and CMP-018 gained evidence and notes. Their statuses are unchanged.
- Firmware rows for 24A446, 24B119 and 24B156 gained the manifest note (C-157), and the 24A446 row gained the static-string note (C-161).
- Erosion, Dopamine, SKVLENT and ecosystem records were re-checked on 2026-11-12. Their `last_checked` dates were updated, and no verdict changed.

### Corrections

- A lookup in this release against `opa334/ElleKit` was a wrong target. The former ElleKit repository in the records is `tealbathingsuit/ellekit`, which matches the v0.4.0 record (C-167).
- The first-identity-only analysis of the A17 Pro manifest is superseded for exclave purposes by the complete enumeration (C-157, C-158). The earlier claims (C-119 to C-125) remain true.
- A search summary said that earlier chips lack exclaves, citing a 2025 press report. The press article does not say that, and the statement is not recorded as a claim.

### Notes

- Readiness is unchanged: LEVEL 0 / NO-GO. Secure Exclaves applicability to the A17 Pro is not established (C-162). Apple's article names no A17 Pro product (C-139).
- Manifest and string results are static metadata. A manifest entry or a static string is not a device or runtime result.
- No device was connected, updated, restored, rebooted or used. No firmware was installed. Erosion was not installed or downloaded. No exploit, probe or Bench27 build was run. No code-level or binary-level differencing was performed, and no binary was mapped to an advisory.
- Public metadata and public source were read only: BuildManifests, decompressed local copies of public payloads, Apple's article and public repository search results.

## [0.4.0] - 2026-11-12

### Added

- Research audit of the SKVLENT iOS 27 research repository at commit 73f7a579ce91: its identity, licence, configurations, verdict table, the twelve questions answered at outcome level, the separated security categories, and its withdrawn, corrected and contradictory statements. See `research/skvlent-a19pro-research-audit.md`.
- Cross-device compatibility analysis using exact device metadata: the BuildManifests of the A19 Pro (iPhone18,1, 24A446) and the A18 Pro (iPhone17,2, 24B119), compared with the A17 Pro (iPhone16,2, 24A446). See `research/cross-device-compatibility.md` and `reports/a17pro-compatibility-matrix.md`.
- Erosion compatibility audit and generic daily-driver risk assessment, from its README, release notes, website and metadata. Erosion was not installed, its IPA was not downloaded, and no device was used. See `research/erosion-compatibility-audit.md` and `reports/erosion-daily-driver-risk.md`.
- A sandbox-escape-versus-jailbreak explanation, with capability claims kept with the project that states them. See `research/sandbox-escape-vs-jailbreak.md`.
- Dated ecosystem update: Dopamine, ElleKit, Procursus, Sileo, an upstream tracker, and a community repository claim. See `research/jailbreak-ecosystem-update.md`.
- Summary and priorities: `reports/v0.4.0-research-summary.md` and `reports/next-research-priorities.md`.
- Claims C-108 to C-137, sources S-047 to S-056, timeline events E-034 and E-035, and compatibility rows CMP-016 to CMP-018.

### Changed

- DIM08's reading of the Dopamine README is superseded by the current default-branch README (C-133). The original text is kept and annotated.
- DIM05, DIM08 and the readiness report carry pointers to the new material. Their statuses are unchanged.
- Compatibility rows CMP-006, CMP-010 and CMP-011 gained evidence and notes. Their statuses are unchanged.

### Corrections

- The Dopamine README reading in DIM08 (15.0 to 15.4.1, no current matrix) is replaced by the current ranges (C-133).
- C-057 (an upstream claim that ElleKit 1.2 covers iOS 15 to 27) is not supported by the official ElleKit repository, which states no version range and has no release. C-057 stays unverified.
- The inference "fixed in 27.2, so open on 27.0.1", found in an external project's open-work page, is recorded as not established.

### Notes

- Readiness is unchanged: LEVEL 0 / NO-GO. No capability is upgraded for the target.
- Every external result is recorded as the source's own statement at the cited commit. None is verified as a technical result for the A17 Pro.
- No device was connected, updated, restored, rebooted or used. No firmware was installed. No external jailbreak or exploit software was installed, run or downloaded. The public tool ipsw was used to read public firmware manifests only.
- No code-level or binary-level differencing was performed, and no binary was mapped to an advisory. Both remain declined.
- Erosion's documents name no iPhone model or SoC, and its repository records no device reports.

## [0.3.0] - 2026-11-12

### Added

- Claims C-089 to C-107 for builds 24A446, 24B119 and 24B156: manifest and container verification for the two 27.2 builds; identity of the SPTM and TXM containers between 27.2 and 27.2.1; kernel version strings; KEXT inventory counts; the arm64e header flag; the scope of a third-party symbolication signature set and the presence of its anchor strings in the kernelcache; name conflicts and a small cross-check; the mechanism of a standalone KEXT import failure; the KEXT inventory reconciliation; a disagreement on register-indirect control flow in the monitors; four methods on the `__DATA_SPTM` segment; and Apple's Platform Security guide statements on SPTM, MIE and the A15-A18 table column.
- Sources S-044 and S-045: Apple CDN objects for iOS 27.2 (24B119) and iOS 27.2.1 (24B156), retrieved in part by HTTP range requests on 2026-11-12. The complete packages were not hashed. Source S-046: the `kernel/27.0` signature folder of a community symbolication repository (MIT licence), read at a single commit.
- Timeline event E-032 (static research update; no release).
- Public reports: `reports/ghidra-kernel-symbolication.md`, `reports/ghidra-kext-loader-investigation.md`, `reports/sptm-semantic-analysis.md`, `reports/txm-semantic-analysis.md`, `reports/firmware-diff-27.0.1-27.2.md`, `reports/firmware-diff-27.0.1-27.2.1.md`, `reports/a17pro-memory-protection-analysis.md` and `reports/ghidra-cve-correlation.md`.
- Count-level inventories: `analysis/kext-reconciliation.json`, `analysis/firmware-diff-metadata.json` and `analysis/kernel-symbolication-metrics.json`.
- Timeline event E-033 (release record).

### Changed

- S-004 (Apple Platform Security guide) was re-read on 2026-11-12. Its access date and reliability note are updated. C-013 is unchanged. C-107 records the range reading of the A15-A18 column and the fact that its cells could not be read.
- S-043 gained the claims that cite it. The firmware rows for 24B119 and 24B156 list S-044 and S-045.
- Existing reports carry pointers to the new analysis rather than repeating it: `reports/ghidra-kernel-analysis.md` (section 5a and the KEXT limitation) and `reports/ghidra-sandbox-analysis.md` (KEXT import). The SPTM, TXM and memory-protection reviews point to the existing summaries for provenance and structure.
- C-013 was re-read on 2026-11-12 (C-105). Its `last_checked` date is updated. Its verdict is unchanged.

### Corrections

- C-013's limitation is refined by C-107. Its statement that the extracted text does not name the A17 Pro remains literally true. The guide's "A15 or later" wording and its A15-A18 table column both cover the A17 generation, although the support cells could not be read.
- C-086's cause is refined by C-101: the import failure is raised in stub processing over an empty symbol table, which C-086 did not establish.

### Notes

- Two analyses were declined and are not in this release: code-level differencing between 24A446 and later builds, and binary-to-advisory correlation. The firmware comparison is metadata only, and no difference is read as a security fix. The advisory page records advisory-level counts only.
- Standalone KEXT files are not imported for analysis, because the release kernelcache's stub tables make the standalone import fail. The fileset program is used instead.
- Symbol names, addresses, symbol listings, Ghidra projects and firmware bytes are not published. Symbolication is reported as counts.
- The monitor reference counts were taken from a read-only copy of the Ghidra project.
- Release v0.3.0 was created after the validator, the secret scans and the CI workflows passed on the release-preparation commit. Earlier tags v0.1.0, v0.1.1 and v0.2.0 are unchanged. The findings support the research record and do not change readiness (LEVEL 0, NO-GO).

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
