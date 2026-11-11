# Contradictions and conflicting reports

This file lists conflicts between sources, how each is recorded, and whether it is resolved. A conflict is never resolved by choosing the more popular source.

| # | Topic | Conflict | Status | Records |
|---|---|---|---|---|
| 1 | Calif.io's publication plans | A 2026-11-04 article reports code and a write-up within about a week. A later article (coverage through about 2026-11-06) reports no public tool planned. | **Unresolved.** Both are recorded as reported. No primary announcement found. | C-022, S-029, S-019 |
| 2 | Reboot persistence | Press reports root access after a restart, and one outlet describes stage video of an SSH session as root after reboot. A community reference repeats the persistence claim. Accounts of reboot behaviour differ in wording. | **Partly consistent, unverified.** No reproduction. | C-004, S-010, S-026 |
| 3 | Signing status of build 24A446 | The third-party index marks 27.0.1 as not signed on 2026-11-11. A community reference reports it as still signed on 2026-11-02. | **Unresolved.** Time-dependent and not confirmed by Apple. | C-021, S-014, S-026 |
| 4 | Apple credit and the lambda handle | A community reference says Apple's CVE-2026-112611 credit confirms the identity of the lambda handle. The iOS 27 security page checked does not contain that identifier or the handle. | **Unverified.** Identity is not published here. | C-023, S-001, S-026 |
| 5 | Fixed-flaw count for iOS 27.2 | Two outlets report 163 fixes. Apple's 27.2 advisory was not located. | **Unverified.** | C-010, S-017, S-018 |
| 6 | Dopamine support for A15 to A17 | Secondary coverage quotes support up to iOS 17.3.1. The official main-branch README is a stale iOS 15 description and has no matrix. | **Partly verified.** Not confirmed from an official page. | C-016, S-009, S-008 |
| 7 | usbliter8 scope | Press and a national CERT advisory describe A12 and A13 devices (with some watch chips). A tutorial page claims a full iOS 27 chain on an iPhone 11 Pro. | **Tutorial claim not adopted (unverified).** Press scope is recorded as reported. | C-019, C-020, S-021, S-022, S-023, S-025 |
| 8 | MIE on newer chips | Apple names A19 and A19 Pro for MIE. A community reference describes MIE on the A20 Pro, which Apple's text does not name. | **Unverified** for the A20 Pro. Not used for the A17 Pro. | C-011, C-012, S-003, S-026 |
| 9 | Demonstration device model | Press reports an iPhone 18 Pro. A community reference reports the A20 Pro. | **Consistent.** Apple's page confirms the chip for the model. | C-001, C-002 |
| 10 | Count of Calif.io-credited CVE entries | Earlier records listed three. Apple's iOS 27 security page, re-fetched on 2026-11-12, lists four, including CVE-2026-86886 (impact: an app may be able to modify protected system files). | **Resolved by the primary source.** C-005 corrected. | C-005, S-001 |

## Method

1. Record each conflicting source, with its tier and verification method.
2. Do not delete a conflicting record. Add a note about the conflict to the affected claim's limitations.
3. Resolve a conflict only when a primary source settles it, and record the resolution as a new source and a new verdict.
