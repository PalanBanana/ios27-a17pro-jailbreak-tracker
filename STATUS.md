# STATUS

Current project position for the iPhone 15 Pro Max (A17 Pro, `iPhone16,2`) on iOS 27.0.1 (build `24A446`).

| Item | Value |
|---|---|
| Data snapshot | 2026-11-12 |
| Target | iPhone 15 Pro Max; A17 Pro; iPhone16,2; iOS 27.0.1; build 24A446 |
| Readiness | **LEVEL 0** for the target (research only). See [reports/exploit-readiness.md](reports/exploit-readiness.md). |
| GO / NO-GO | **NO-GO.** Required conditions are unmet (see [docs/RESEARCH_METHODOLOGY.md](docs/RESEARCH_METHODOLOGY.md)). |
| Device operations performed by this project | None. The project does not connect to, inspect, or modify any maintainer-owned device. |
| Public repository | PalanBanana/ios27-a17pro-jailbreak-tracker (public) |
| Latest release | v0.2.0 (A17 Pro Deep Technical Research Update), created only after the CI workflows pass for the release commit. Earlier releases v0.1.1 and v0.1.0 are unchanged. See the Releases page. |

## Data

**Data snapshot (2026-11-12):** 76 claims (39 verified, 17 partially verified, 20 unverified), 42 sources, 30 timeline events, 15 compatibility rows and 4 firmware builds.

## Research priorities

- **P0:** A17 Pro SPTM research (graded audit: `research/sptm-evidence-audit.md`); kernel read/write research (`research/krw-release-audit.md`); Calif.io and Hexacon disclosures (`research/calif-hexacon-deep-audit.md`); upstream reconciliation (`research/upstream-reconciliation.md`); exact build compatibility (build 24A446).
- **P1:** sandbox escape; privilege escalation; AMFI and code signing; exploit chain integration.
- **P2:** bootstrap; Dopamine; Sileo; ElleKit; daily-driver stability.

No compatibility is marked verified without evidence. The target readiness stays at LEVEL 0 / NO-GO unless new evidence supports a change.

## Blockers

1. **Primary sources:** as of 2026-11-12, the Hexacon 2026 programme pages, any primary Calif.io statement, the opa334 PSA of 2026-10-17, and a primary write-up of the November kernel read/write announcement have not been located.
2. **Signing status:** a third-party index (ipsw.me, S-014; checked 2026-11-12) lists 24A446 as not signed. A community reference (S-026) reported it as signed on 2026-11-02, so the status changed between observations. The change date is not known (C-021, E-030).
3. **Apple records:** Apple's iOS 27, 27.2 and 27.2.1 advisories are parsed (`research/apple-27x-cve-mapping.md`). Apple states no affected version range for any entry, so the applicability of each entry to 24A446 is not established.

## Latest update

- 2026-11-12 (v0.2.0 research update): Apple's iOS 27.2 and 27.2.1 advisories parsed and mapped; the upstream reference reconciled claim by claim; Dopamine 3.0 release notes read; the independent SPTM paper's scope checked; a November project claim recorded as unverified; the 24A446 signing change recorded. Readiness unchanged (LEVEL 0 / NO-GO). Details in CHANGELOG.md.
- 2026-11-12: research re-check with no material change, except the CVE correction (four Calif.io-credited entries, not three). First public commit and release v0.1.0. Privacy correction: maintainer-specific device statements removed from the documentation; the research target and compatibility scope are unchanged.
- 2026-11-11: initial snapshot. Details in [CHANGELOG.md](CHANGELOG.md).
