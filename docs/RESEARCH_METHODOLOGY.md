# Research Methodology

This document defines how claims are sourced, verified, scored and updated. The validator enforces the rules that can be checked mechanically (see `scripts/validate_tracker.py`).

## 1. Source tiers

- **Tier 1**: Apple official documentation and security advisories; original research publications; official developer announcements; official source repositories and their release records; official conference materials; published original code.
- **Tier 2**: independent technical analysis; reproduction reports; reputable security publications and news; government CERT advisories; third-party firmware indexes (cross-checked where possible).
- **Tier 3**: community forums; developer communities; social accounts; community wikis; community reference repositories.
- **Tier 4**: anonymous screenshots; unsupported claims; unverified videos; paid promotion; tutorial pages with no verifiable authorship.

## 2. Verification methods

Each source records how it was checked:

- `fetched_full_text`: the page was retrieved and read.
- `fetched_partial_text`: the page was retrieved, but the text extraction was truncated or incomplete. Dates or labels may need checking.
- `api_response`: a structured API response was retrieved (for example, a GitHub release record).
- `search_snippet_only`: only a search result or summary was seen. Snippets are leads, not evidence.
- `not_accessed`: the source is listed but was not checked.

## 3. Verdicts

- **verified**: primary or tier-1 evidence, checked by fetching or API, supports the claim as stated, within the recorded scope.
- **partially_verified**: part of the claim has checkable support. A key element (scope, build, device or date) remains unverified.
- **unverified**: no checkable support, or support that conflicts. Recorded as a lead only.
- **disproved**: checkable evidence contradicts the claim.
- **superseded**: a later record replaces the claim. The earlier record stays in the history.

Confidence is `high`, `medium` or `low`. The validator requires `verified` claims to have `high` confidence and `unverified` claims to have `low`.

## 4. Evidence rules

1. Primary sources first. Secondary sources are used for reported facts and must say so.
2. Never raise a verdict because a site, post, video or account is popular, repeated or confident.
3. Record contradicting sources. Do not delete them.
4. Scope every claim: device, chipset, iOS version, build, and the date it was observed.
5. Do not treat a demonstration on one device as evidence for another.
6. Keep history. Supersede a verdict with a new record rather than rewriting the old one.
7. Community identity claims, including claims that a handle belongs to a named person, are not published unless a primary source confirms them, and even then only as necessary.

## 5. Readiness levels

- **LEVEL 0**: research only.
- **LEVEL 1**: an individual vulnerability is publicly disclosed.
- **LEVEL 2**: public exploit components are available.
- **LEVEL 3**: a complete exploit chain is demonstrated.
- **LEVEL 4**: a public jailbreak release exists.
- **LEVEL 5**: exact-target compatibility is independently verified.
- **LEVEL 6**: daily-driver stability is independently established.

Levels are not skipped without evidence. Readiness is scored for the exact target. A disclosure that applies only to other devices or versions does not raise the target's level.

## 6. GO / NO-GO

A GO recommendation for a real-device jailbreak attempt requires all twelve conditions:

1. An authentic source.
2. An official public release.
3. Exact hardware support.
4. Exact firmware and build support.
5. A17 Pro compatibility evidence.
6. Complete chain evidence.
7. Credible independent reproduction.
8. Known installation behaviour.
9. Known reboot behaviour.
10. Recovery and failure analysis.
11. Data-protection considerations.
12. Explicit authorisation from the device owner.

Any unmet condition means NO-GO. The project keeps researching while NO-GO.

## 7. Update procedure

1. Check the date of the last update in `CHANGELOG.md`.
2. Search for new official security disclosures (Apple security releases and advisories).
3. Check researcher and developer announcements.
4. Check relevant GitHub releases and commit history.
5. Search for new SPTM research.
6. Search for new kernel read/write research.
7. Check jailbreak tool compatibility (official release notes first).
8. Check firmware changes (Apple index, third-party index).
9. Check firmware signing status, and record its basis and date.
10. Review contradictory claims.
11. Update `data/claims.json`.
12. Update `data/sources.json`.
13. Update `data/timeline.json`.
14. Update `data/compatibility.json`.
15. Update `data/firmware.json`.
16. Update the research documents in `research/`.
17. Regenerate the reports and README files.
18. Update `CHANGELOG.md`.
19. Run `python3 scripts/validate_tracker.py`.
20. Run the security checks (privacy patterns and secret scanning).
21. Commit and publish only after every publication gate passes.

If nothing material changed, record `NO MATERIAL CHANGE`. Do not invent changes.

## 8. Known limitations

- Search results are often snippets. Snippets are recorded as leads, and are not used to support `verified` verdicts.
- The search tool used for this research is US-based, so regional sources may be missing.
- Video material has not been analysed.
- Apple's web pages change, and extraction may truncate dates or labels. The affected sources are marked `fetched_partial_text`.
- The project does not test anything on hardware. Compatibility claims are reported, not reproduced.

## 9. Research dimensions

The project tracks twelve dimensions, each with a document in `research/`:

- DIM01: event verification
- DIM02: A17 Pro security architecture
- DIM03: SPTM research
- DIM04: kernel vulnerability intelligence
- DIM05: sandbox escape and privilege escalation
- DIM06: firmware and build compatibility
- DIM07: exploit chain integration
- DIM08: jailbreak ecosystem
- DIM09: persistence and deployment
- DIM10: scam detection and community verification
- DIM11: daily-driver stability
- DIM12: recovery and safety

Each dimension states what has been researched, what has not, and why.
