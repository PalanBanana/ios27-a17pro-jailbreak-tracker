# Upstream reconciliation

**Status:** research record, 2026-11-12. Compares the community reference archive (S-026) with this repository's sources. Items are cited by the upstream's own IDs (V1 to V33, E1 to E3, P1 to P6, O1 to O3) so that the two files can be read side by side.

## Rules used

- The upstream is a Chinese-language community fact-check archive. Its original content is CC BY 4.0. Its statements are leads and are recorded as reported unless a primary source in this repository confirms them.
- Statements are summarised, not quoted.
- Personal details about individuals that appear in the upstream file (names, ages, locations and account links) are not reproduced here. Identity claims are not published unless a primary source confirms them (METHODOLOGY section 4.7).
- The upstream's verdicts are not adopted. Where it rates an item verified on second-hand or single-party evidence, this repository records the lower verdict and the reason.

## 2026-11-04 items

Several items carry the upstream's 2026-11-04 annotations (V30 to V32, and parts of V2, V7, V19 and V20). They are upstream snapshot items. They are not discoveries made on 2026-11-12. This review first recorded them on 2026-11-12. The event dates in `data/timeline.json` keep the dates reported for them (E-013, E-020, E-021).

## Focus items

| Upstream | Upstream statement (summary) | Upstream verdict | This repository | Basis here | Discrepancy |
|---|---|---|---|---|---|
| V7 | An SPTM bypass valid through 27.0.1 exists, reportedly patched in a 27.2 beta | partially true, medium | Unverified (C-051) | Upstream only. The 2026-10-17 PSA was not located | No difference on the verdict. The upstream describes the bypass as the only public SPTM route. This repository does not adopt that framing (see [sptm-evidence-audit.md](sptm-evidence-audit.md)). |
| V8 | An SPTM bypass alone is not enough beyond 26.0.1. The existing ClearSword and DarkSword kernel bugs cover only up to 26.0.1 | verified, high (a direct quote of opa334) | Unverified (C-054) | Dopamine 3.0 notes name both exploits without a range (C-068). An analysis dated 2026-05-03 gives Apple's fixed-in versions for the DarkSword CVEs as 26.2 and 26.3 (C-069) | **Open.** The upstream's verdict rests on a quote this review did not retrieve. Its 26.0.1 bound describes exploit support, which may differ from the exposure of the bug. The sources here do not reconcile the two. |
| V10 | A Calif.io team member says the jailbreak applies to any iPhone on iOS 27.0.1, possibly including iPads | verified, high (interview, 2026-10-19) | Unverified (C-052) | The English and German heise pages and the t3n page do not quote the statement. The interview was not retrieved | **Open.** The upstream classifies the claim as verified from the interview. This review did not see the interview. |
| V11 | Most of the chain's bugs were fixed in the 27.2 beta | verified, high | Partially verified (C-051 for the beta report; C-039 to C-042 for the 27.2 entries) | Apple's 27.2 notes list 23 kernel-memory entries and six Calif.io credits, none of them kernel memory. No Apple beta notes were checked, and no entry is mapped to the chain | Chain membership cannot be checked from Apple's notes. Recorded as not established. |
| V30 | A Calif.io team member said on 2026-11-04 that kernel read/write exploit code and a write-up would follow in about a week | verified, high (two reprints, a profile and an Apple credit line) | Partially verified (C-022, C-049; E-013, E-022) | Press (PBX Science, 2026-11-04, fetched) relays the post. The post itself was not retrieved. Apple's pages credit the handle with Calif.io on two entries (C-043). No publication was found on 2026-11-12 | **Open.** The upstream's verdict is higher than this review can check. The one-week window lapsed on 2026-11-11 with no publication found. |
| V31 | opa334 (2026-11-04) expects the kernel exploit within the week, can add A12 and A13 support with momentarius, and says A14 and later still need an n-day SPTM bypass | verified, high (two Chinese reprints of an infosec.exchange post) | Unverified (C-050) | The original post was not retrieved. Dopamine 3.0 notes already list momentarius for A12 and A13 on 16.6 to 18.7.1 and 26.0 to 26.0.1 (C-067) | **Open.** The upstream's verdict is higher than this review's, because the original was not retrieved. The momentarius part matches Dopamine's own notes. |
| V32 | A Calif.io video shows Lockdown Mode, an over-the-air update to 27.2 and a plugin that survives reboot | verified, high (two reprints with video stills) | Unverified (C-053) | Not retrieved. The upstream notes that the update segment was edited and that a team member said an uncut version could be shared | **Open.** The upstream's verdict is higher than this review's. Persistence on a build with a fix is not the same as a fix (see V11). |
| V33 | opa334's tier vocabulary: Full, Semi Full, Semi and Semi Semi, with the reported Calif.io demonstration in the last class | partially true, medium (second-hand, from a news article) | Not adopted as a claim | Not checked against the original post | Second-hand. No readiness level changes. |

## Other upstream items

| Upstream | Summary | Status here | Note |
|---|---|---|---|
| V1 | Hexacon demonstration on an iPhone 18 Pro (A20 Pro), build 24A446 | Partially verified (C-001, C-002) | Press confirms the demonstration and the device model. The upstream's "official agenda" was not verified because the programme pages were unavailable (S-011). Technical details of the demonstration are not reproduced. |
| V2 | Calif.io's "released in due time" statement | Not retrieved | Recorded as reported in the upstream only. |
| V3 | Demonstration on an unlocked device | Not recorded | Upstream only. |
| V4 | Company profile, and Apple's credit to "Calif.io in collaboration with Claude and Anthropic Research" | Credit verified (C-006); profile not recorded | The credit line is in Apple's iOS 27 notes. |
| V5 | usbliter8 BootROM issue for A12 and A13; a court-ordered takedown of the original write-up | Scope partially verified (C-019). Takedown not verified | Not applicable to the A17 Pro. |
| V6 | No public iOS 27 tool; sites claiming iOS 27 jailbreaks are mostly scams | Consistent with C-028 and DIM10 | Scam indicators are in DIM10. |
| V9 | Calif.io does not plan an end-user tool, may disclose so that others can build one, and may release a PoC after Apple's patch | Unverified (C-077) | The upstream classifies it as verified from the interview. |
| V12 | Calif.io's iPhone Duo post and short video on release day | Not applicable to the target | iPhone Duo is a separate build line (E-008). |
| V13 | Duo chain fixes not in 27.1 | Not applicable to the target | Duo-only build. |
| V14 | A reported code name for the Calif.io tool | Not recorded | Single secondary source. Not relevant to the target. |
| V15 | 27.2 release-candidate timing; 27.0.1 signed on 2026-10-24; 27.1 for Duo only | Partially verified. Signing changed later (C-021, E-030) | The index now lists 27.0.1 as not signed. |
| V16 | 27.2 released 2026-10-27; 163 CVEs; six Calif.io credits; the 27.0 page updated on 2026-10-19 with CVE-2026-28968 | Mostly verified (C-042, C-046, C-071). Date differs | Apple's index and the ipsw record give 26 October 2026 (18:33 UTC). The upstream's 27 October is probably Beijing time. The 163 figure is a press count (C-046). The upstream describes CVE-2026-112705 as kernel memory corruption. Apple's impact text is unexpected system termination (C-044). |
| V17 | A third-party crash reproduction of CVE-2026-112705 on iPhone 17 Pro, iOS 27.0.1 | Unverified (C-062) | No repository was visited, downloaded or linked. Apple's impact text ("unexpected system termination") is consistent with a crash. |
| V18 | A company-branded root-shell demonstration on iOS 27.2 | Unverified (C-063) | Device not stated. Single party. |
| V19 | Calif.io bare-hash posts (2026-10-30) and an earlier one from a team member (2026-10-14) | Recorded as timeline event E-027 only | The hashes have no content. Nothing can be checked until a preimage is published. |
| V20 | Community expectation of a write-up after 27.1 | Superseded by V30 | The upstream's own note. |
| V21 | A project announced on 2026-11-01 for iOS 27.0 to 27.0.1, described as semi-untethered | Unverified (C-064) | Recorded with a risk note. The project's identity is not recorded here. |
| V22 | The project's reported chain, with iPhone 15 Pro Max (A17 Pro) as its only stated test device | Unverified (C-064) | Apple's 27.2 text has no AGX, IOGPU, SPTM or TXM entry (C-073). The reported SPTM stage cannot be mapped to any Apple entry. |
| V23 | "CASKR" is a typo for "CASLR" in a screenshot | Not recorded | Terminology only. |
| V24 | Identity links for a project's author | Not reproduced | Identity claims are not published (METHODOLOGY section 4.7). |
| V25 | 27.0.1 signed on 2026-11-02 in a live pull; 27.0 no longer signed | Signing change recorded (C-021, E-030). 27.0 is unsigned in the firmware record | The upstream's 2026-11-02 pull and this review's 2026-11-12 check disagree on 27.0.1. The change date is not known. |
| V26 | ElleKit 1.2 covers rootless injection on iOS 15 to 27 | Unverified (C-057) | The upstream's source article was blocked to this review (S-026 notes). The candidate repository has no release record. |
| V27 | Personal details about a project's author | Not reproduced | Rule 5 and METHODOLOGY section 4.7. |
| V28 | A triage plan for the project's stated ETA | Not recorded beyond C-064 | The plan is the upstream's own. |
| V29 | A 27.0.1 root-shell screenshot on another device model | Not recorded | The upstream says it extends a known BootROM line on an older device. Not the target. |
| E1 | Press framing that a demonstration is the first untethered jailbreak since iOS 9 | Press claim unverified (C-075) | The upstream says a 2021 public untethered jailbreak contradicts the framing. |
| E2 | "iOS 27 drops iPhone 11" | Contradicted by Apple's device lists (C-072) | Apple's lists read "iPhone 11 and later". |
| E3 | A patch expected in a 27.0.x or 27.1 update | Partially true, per the upstream | Apple's notes place the listed fixes on the 27.2 page (C-039 to C-042). No 27.0.2 evidence was found. |
| P1, P2, P5, P6, O2 | iOS 27 performance and feature claims, conference wording, incentive reasoning, and staying on the iOS 26 branch | Out of scope | Not recorded. |
| P3 | A research implementation on an A13 device | Out of scope (A12 and A13) | See C-019. |
| P4 | The Calif.io chain probably needs adaptation for A14 and A15 | Unverifiable | Not recorded as a claim. A15 depends on the reported SPTM bypass (C-051). |
| O1 | Dopamine 3.0's iOS 26 coverage: A12 and A13 only, with no 26.x jailbreak for A14 and A15 | Consistent with Dopamine's notes and the third-party table (C-016, C-067) | |
| O3 | Downgrades are not possible on A12 and later (SHSH) | Not recorded here | [docs/RECOVERY_AND_PRESERVATION.md](../docs/RECOVERY_AND_PRESERVATION.md) covers the signing principle. |

## Discrepancies still open

1. V8 against C-069: a 26.0.1 bound against fixed-in versions of 26.2 and 26.3. Not reconciled.
2. V10 against heise and t3n: the interview was not seen, and the quoted statement is absent from the fetched text.
3. V25 against the ipsw index: 27.0.1 signed on 2026-11-02 per the upstream, unsigned on 2026-11-12 per the index. The change date is not known (C-021, E-030).
4. V26 against the candidate repository: no release record (C-057).
5. V16 date: 27 October in the upstream, probably Beijing time. Apple's index gives 26 October.
6. V16 and V17 against Apple's text for CVE-2026-112705: "kernel memory corruption" in the upstream against "unexpected system termination" in Apple's impact text (C-044).
7. V30 to V32 verdicts against this review: the upstream relies on second-hand reprints, and the original posts were not retrieved.

## Repository changes made from this comparison

- Claims corrected or added: C-016, C-021, C-034 to C-061 (corrections), C-062 to C-077 (new).
- Timeline events added: E-024 to E-030.
- Sources added or corrected: S-033 to S-042, S-026 (access date and reliability note).
- See [CHANGELOG.md](../CHANGELOG.md) for the release record.
