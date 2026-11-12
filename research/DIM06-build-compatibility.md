# DIM06: Firmware and build compatibility

**Status:** Partially researched. Build list, release dates and Apple's CVE status are checked. Per-build kernel and security-framework differences have not been reviewed.

## Builds for the target device family (iPhone16,2)

| Version | Build | Released | Apple CVE status | Signing (third-party index, 2026-11-12) | Records |
|---|---|---|---|---|---|
| 27.0 | 24A437 | 2026-09-14 | Listed on Apple page; subset of Calif.io-credited entries recorded | Not signed | S-001, S-014 |
| 27.0.1 | 24A446 | 2026-09-28 | No published CVE entries (Apple index) | Not signed; conflicting report (C-021) | C-007, C-024, C-021 |
| 27.2 | 24B119 | 2026-10-26 | Apple advisory not located; press reports 163 fixes (unverified) | Signed | C-008, C-010 |
| 27.2.1 | 24B156 | 2026-11-09 | Not located | Signed | C-009 |

## Findings

- Apple's security releases index states that iOS 27.0.1 has no published CVE entries (C-007). Build 24A446 is corroborated by third-party sources (C-003) and by the index's release date (C-024).
- Press reports 163 vulnerabilities fixed in iOS 27.2 (C-010). The count is not verified, because Apple's 27.2 advisory was not located.
- iOS 27.1 was released for iPhone Duo on 2026-10-23 with no published CVE entries (timeline E-008). It does not apply to the A17 Pro.
- Build-level applicability of any exploit is **not established** for any of these builds (CMP-015 covers build verification only).

## Community claims recorded but not verified

A community reference reports that a demonstration chain persists across an over-the-air update to 27.2 with Lockdown Mode enabled. This is a lead, not a verified claim. It has no claim record yet and should not be cited until a primary source appears.

## Gaps and next steps

1. Fetch Apple's entries for 27.2 and 27.2.1, and record the CVE count and components for each.
2. Confirm the 27.0.1 release date directly from Apple, if an Apple-hosted page for that build becomes available.
3. Review the per-build changes that Apple documents, without downloading or analysing firmware images.
