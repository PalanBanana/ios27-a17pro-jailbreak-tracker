# STATUS

Current project position for the iPhone 15 Pro Max (A17 Pro, `iPhone16,2`) on iOS 27.0.1 (build `24A446`).

| Item | Value |
|---|---|
| Data snapshot | 2026-11-11 |
| Target | iPhone 15 Pro Max; A17 Pro; iPhone16,2; iOS 27.0.1; build 24A446 |
| Readiness | **LEVEL 0** for the target (research only). See [reports/exploit-readiness.md](reports/exploit-readiness.md). |
| GO / NO-GO | **NO-GO.** Required conditions are unmet (see [docs/RESEARCH_METHODOLOGY.md](docs/RESEARCH_METHODOLOGY.md)). |
| Device operations performed by this project | None. The project does not connect to, inspect, or modify any maintainer-owned device. |
| Public repository | PalanBanana/ios27-a17pro-jailbreak-tracker (public) |
| Latest release | v0.1.0 (Initial Public Research Tracker), created only after the CI workflows pass for the release commit. See the Releases page. |

## Data

**Data snapshot (2026-11-11):** 32 claims (10 verified, 15 partially verified, 7 unverified), 32 sources, 17 timeline events, 15 compatibility rows and 4 firmware builds.

## Research priorities

- **P0:** A17 Pro SPTM research; kernel read/write research; Calif.io and Hexacon disclosures; lambda / pwnlambda research; exact build compatibility (build 24A446).
- **P1:** sandbox escape; privilege escalation; AMFI and code signing; exploit chain integration.
- **P2:** bootstrap; Dopamine; Sileo; ElleKit; daily-driver stability.

No compatibility is marked verified without evidence. The target readiness stays at LEVEL 0 / NO-GO unless new evidence supports a change.

## Blockers

1. **Primary sources:** as of 2026-11-12, the Hexacon 2026 talk listing, any primary Calif.io statement, and a primary write-up of the lambda kernel read/write work have not been located.
2. **Signing status:** build 24A446 remains unresolved (C-021). A third-party index (ipsw.me, S-014; checked 2026-11-12) lists it as not signed, and a community reference (S-026) reported it as signed on 2026-11-02.
3. **Apple records:** Apple's 27.2 advisory and the fixed-in release for each Calif.io-credited CVE have not been located.

## Latest update

- 2026-11-12: research re-check with no material change, except the CVE correction (four Calif.io-credited entries, not three). First public commit and release v0.1.0. Privacy correction: maintainer-specific device statements removed from the documentation; the research target and compatibility scope are unchanged.
- 2026-11-11: initial snapshot. Details in [CHANGELOG.md](CHANGELOG.md).
