# Contradictions and conflicting reports

This file lists conflicts between sources, how each is recorded, and whether it is resolved. A conflict is never resolved by choosing the more popular source.

| # | Topic | Conflict | Status | Records |
|---|---|---|---|---|
| 1 | Calif.io's publication plans | A 2026-11-04 article reports code and a write-up within about a week. A 2026-11-06 snippet reports no public tool planned. | **Unresolved.** Both are recorded as reported. No primary announcement found. The window lapsed on 2026-11-11 (E-022). | C-022, C-049, S-029, S-019 |
| 2 | Reboot persistence | Press reports root access after a restart. A stage video is described as showing root over SSH after reboot. The upstream reports over-the-air persistence on 27.2. | **Partly consistent, unverified.** No reproduction. | C-004, C-053, S-010, S-026 |
| 3 | Signing status of build 24A446 | The third-party index (ipsw.me, S-014) lists 27.0.1 as not signed on 2026-11-12. The upstream reports it signed on 2026-11-02 from a live pull. | **Changed between observations.** The change date is not known. Both are third-party observations. Not confirmed by Apple. | C-021, E-030, S-014, S-026 |
| 4 | Apple credit and the researcher's handle | Apple credits the handle "pwnlambda" with a Calif.io affiliation on two iOS 27.2 entries. The upstream links the handle to a named person. | **Handle credit verified (C-043). Name link not published** (METHODOLOGY section 4.7). | C-023, C-043, S-001, S-033, S-026 |
| 5 | Fixed-flaw count for iOS 27.2 | Two outlets report 163. Apple's 27.2 text has 162 distinct identifiers. | **Unresolved.** The extraction does not explain the gap. | C-046, S-017, S-033 |
| 6 | Dopamine support for A15 to A17 | A third-party table lists iOS 15.0 to 17.3.1 for A14 to A17. Dopamine 3.0's notes state a Titan bypass for all devices on iOS 16.5.1 to 17.3.1 and no real-device SPTM support beyond 17.3.1. | **Resolved in part.** The release notes are primary and agree on 17.3.1. The chip table stays secondary. | C-016, C-065, C-066, S-039, S-007 |
| 7 | usbliter8 scope | Press and a national CERT advisory describe A12 and A13 devices. A tutorial page claims a full iOS 27 chain on an iPhone 11 Pro. | **Tutorial claim not adopted (unverified).** Press scope recorded as reported. | C-019, C-020, S-021, S-022, S-023, S-025 |
| 8 | MIE on newer chips | Apple names MIE for A19 and A19 Pro. The upstream says the Calif.io chain bypasses MIE on A19 and A20. | **Unverified** for the A20. Not used for the A17 Pro, which Apple does not name for MIE. | C-011, C-012, S-003, S-026 |
| 9 | Demonstration device model | Press reports an iPhone 18 Pro. The upstream reports the A20 Pro. | **Consistent.** | C-001, C-002 |
| 10 | Count of Calif.io-credited CVE entries | Earlier records listed three. Apple's iOS 27 page lists four, and its iOS 27.2 page lists six. | **Resolved by the primary source.** | C-005, C-038, C-042, S-001, S-033 |
| 11 | Apple's 27.2 release date | Apple's index and the ipsw record give 26 October 2026 (18:33 UTC). The upstream gives 27 October. | **Probably a time-zone difference.** Not material to the target. | E-009, S-033, S-026 |
| 12 | Kernel label for CVE-2026-112705 | The upstream describes it as kernel memory corruption. Apple lists the impact as unexpected system termination, with an out-of-bounds write in the description. | **Apple's text recorded.** The upstream label is not adopted. A third-party crash reproduction is reported and unverified. | C-044, C-062, S-026, S-033 |
| 13 | SPTM limit against a later bypass report | Dopamine's notes (2026-08-07) state no real-device SPTM bypass for iOS 17.4 and later. The upstream reports an SPTM bypass valid through 27.0.1 (2026-10-17). | **Not contradictory in time order.** The later report is unverified. | C-051, C-066 |
| 14 | DarkSword and ClearSword version bound | The upstream states that both exploits cover only up to iOS 26.0.1. 8kSec gives Apple's fixed-in versions for the DarkSword CVEs as 26.2 and 26.3. Dopamine's notes give no range for either exploit. | **Unresolved.** The exploit range and the bug's exposure may differ. | C-054, C-068, C-069, S-026, S-042, S-007 |
| 15 | ElleKit 1.2 coverage | The upstream reports ElleKit 1.2 as covering iOS 15 to 27 and rates it verified. The candidate repository has no release record. | **Unverified.** | C-057, C-056, S-040, S-026 |
| 16 | "First reboot-proof jailbreak since iOS 9" | Press wording (heise). The upstream says a 2021 public untethered jailbreak contradicts it. | **Unresolved.** The press claim is recorded as unverified. | C-075, S-036, S-026 |
| 17 | AI-assisted comparison of iOS 27.2 beta and 27.0.1 | t3n presents it as established. heise's German edition calls it theoretically possible. No team statement located. | **Unresolved.** | C-076, S-038, S-037 |
| 18 | Upstream verdicts against this review | The upstream rates V8, V10 and V30 to V32 as verified. This review records them as unverified or partially verified, because the primary sources were not retrieved. | **Not adopted.** See [upstream-reconciliation.md](upstream-reconciliation.md). | C-050 to C-054, S-026 |
| 19 | "Fixed in 27.0" against entry dates | Many iOS 27 entries are marked added or updated on 2026-10-19 or 2026-10-26, after the 27.0 release. | **Interpretation recorded.** The page shows the listing date of the entry, not the date a fix shipped in a given build. | C-071, S-001 |

## Method

1. Record each conflicting source, with its tier and verification method.
2. Do not delete a conflicting record. Add a note about the conflict to the affected claim's limitations.
3. Resolve a conflict only when a primary source settles it, and record the resolution as a new source and a new verdict.
