# Latest status

**Snapshot date:** 2026-11-11. **Target:** iPhone 15 Pro Max (A17 Pro, `iPhone16,2`), iOS 27.0.1, build `24A446`.

## Summary

- **Readiness:** LEVEL 0 for the target. No verified public jailbreak, exploit component or complete chain applies to this device and build.
- **Decision:** NO-GO.
- **Most significant reported development:** Calif.io reportedly demonstrated an untethered iOS 27.0.1 jailbreak on an iPhone 18 Pro (A20 Pro) at Hexacon 2026 on 2026-10-16. The demonstration device is not the target, and no write-up or tool has been verified (C-001, C-002, C-027).
- **Apple's security notes** credit Calif.io researchers for four CVE entries in iOS 27 (C-005). Apple's index lists no CVE entries for 27.0.1 (C-007).
- **Firmware:** the third-party index lists 27.0.1 as not signed and 27.2.1 as signed on 2026-11-11. The 27.0.1 signing status conflicts with a community report and is unresolved (C-021).

## Material changes in this snapshot

**2026-11-12 re-check:** no new iOS 27 build, no signing change in the third-party index, no Dopamine release or default-branch commit since 3.0.13 (2026-11-03), no new pwnlambda repository, and no published kernel read/write write-up found. **Correction:** Apple's page lists four Calif.io-credited CVE entries, not three; CVE-2026-86886 was missed in the first extraction. Changes are listed in [CHANGELOG.md](../CHANGELOG.md).

## Update procedure check

| Step | Done in this snapshot | Notes |
|---|---|---|
| Last update date | Yes | No previous snapshot exists. |
| Official security disclosures | Yes | Apple iOS 27 security notes and security releases index. |
| Researcher announcements | Partially | Press coverage and a community reference only. No primary announcement found. |
| GitHub releases | Yes | Dopamine, Sileo. ElleKit upstream not confirmed. |
| GitHub commit history | Yes | Dopamine default branch (five most recent commits). |
| SPTM research search | Partially | Apple statements checked. No public A17 Pro bypass verified. |
| KRW research search | Partially | Reported plans recorded as unverified. |
| Jailbreak tool compatibility | Yes | Dopamine support range from secondary coverage; official README stale. |
| Firmware changes | Yes | Apple index and third-party index. |
| Signing status | Yes | Third-party index only. No Apple-hosted signing record. |
| Contradictory claims | Yes | See [research/contradictions.md](../research/contradictions.md). |
| Validation | Yes | See [reports/evidence-audit.md](evidence-audit.md) and the validator output. |

## Dataset

**Data snapshot (2026-11-11):** 32 claims (10 verified, 15 partially verified, 7 unverified), 32 sources, 17 timeline events, 15 compatibility rows and 4 firmware builds.

## Open items

See [STATUS.md](../STATUS.md) for the blockers list.
