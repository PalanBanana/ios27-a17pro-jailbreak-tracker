# STATUS

Current project position for the iPhone 15 Pro Max (A17 Pro, `iPhone16,2`) on iOS 27.0.1 (build `24A446`).

| Item | Value |
|---|---|
| Data snapshot | 2026-11-11 |
| Target | iPhone 15 Pro Max; A17 Pro; iPhone16,2; iOS 27.0.1; build 24A446 |
| Device baseline (owner-reported; not verified by the project) | iPhone 15 Pro Max (A17 Pro, iPhone16,2); installed iOS 27.0.1 (build 24A446); signing reported as unsigned; over-the-air update blocking reported as enabled; primary daily-use device. |
| Readiness | **LEVEL 0** for the target (research only). See [reports/exploit-readiness.md](reports/exploit-readiness.md). |
| GO / NO-GO | **NO-GO.** Required conditions are unmet (see [docs/RESEARCH_METHODOLOGY.md](docs/RESEARCH_METHODOLOGY.md)). |
| Device operations performed by this project | None. The project does not connect to any iPhone. |
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
2. **Signing status:** build 24A446 remains unresolved (C-021). The owner reports it as unsigned.
3. **Apple records:** Apple's 27.2 advisory and the fixed-in release for each Calif.io-credited CVE have not been located.
4. **Installed-build confirmation:** the owner's report is the baseline. Any independent confirmation would have to be non-invasive and the owner's choice. The project does not query devices.

## Latest update

- 2026-11-12: research re-check with no material change, except the CVE correction (four Calif.io-credited entries, not three). Owner-reported device baseline and preservation limits documented. First public commit prepared.
- 2026-11-11: initial snapshot. Details in [CHANGELOG.md](CHANGELOG.md).
