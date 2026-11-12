# DIM06: Firmware and build compatibility

**Status:** Researched for this pass. Build list, release dates, Apple's CVE pages and third-party signing observations are checked. Per-build kernel and security-framework differences have not been reviewed.

## Builds for the target device family (iPhone16,2)

| Version | Build | Released | Apple CVE status | Signing (third-party index, 2026-11-12) | Records |
|---|---|---|---|---|---|
| 27.0 | 24A437 | 2026-09-14 | Listed on the Apple page: 162 identifiers. Four Calif.io-credited entries (C-038) | Not signed | S-001, S-014 |
| 27.0.1 | 24A446 | 2026-09-28 | No CVE entries (Apple index) | Not signed. Reported signed on 2026-11-02 (C-021, E-030) | C-007, C-021, S-002 |
| 27.2 | 24B119 | 2026-10-26 (18:33 UTC in the index; Apple's index gives 26 Oct 2026) | Listed on the Apple page: 162 identifiers. Six Calif.io-credited entries (C-042). Press reports 163 (C-046) | Signed | S-033, C-042, C-046 |
| 27.2.1 | 24B156 | 2026-11-09 | Listed on the Apple page: 9 identifiers, none kernel memory (C-045) | Signed | S-034, C-045 |

## Findings

- Apple's security releases index lists no CVE entries for iOS 27.0.1 (C-007). Build 24A446 is corroborated by the third-party index (C-003) and by its release date (C-024).
- The iOS 27 and 27.2 pages each list 162 distinct identifiers in the extracted text. The press figure of 163 for 27.2 differs by one (C-046).
- Apple's pages state no affected version range for any entry (C-047). The 27.0 page marks many entries as added or updated on 2026-10-19 and 2026-10-26 (C-071). The entries therefore show what was listed on each page, not when a fix shipped in a given build.
- iOS 27.1 was released for iPhone Duo on 2026-10-23 with no CVE entries (E-008). It does not apply to the A17 Pro.
- The signing status of 24A446 differs between two observations. The upstream reported it signed on 2026-11-02 from a live pull. The index on 2026-11-12 lists it as not signed. The date of the change is not known (C-021, E-030). Do not assume that a restore to this build is possible.
- Build-level applicability of any exploit is **not established** for any of these builds (CMP-015 covers build verification only).

## Community claims recorded but not verified

- A demonstration chain is reported to persist across an over-the-air update to 27.2 with Lockdown Mode enabled (C-053). This is a lead, not a verified claim.

## Gaps and next steps

1. Record Apple's per-build fix data for each 27.x build if Apple publishes it.
2. Re-check the signing status of 24A446 at each update, and record the basis and date.
3. Review any per-build change that Apple documents, without downloading or analysing firmware images.
