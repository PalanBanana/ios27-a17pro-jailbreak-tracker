# Latest status

**Snapshot date:** 2026-11-12. **Target:** iPhone 15 Pro Max (A17 Pro, `iPhone16,2`), iOS 27.0.1, build `24A446`.

## Summary

- **Readiness:** LEVEL 0 for the target. No verified public jailbreak, exploit component or complete chain applies to this device and build.
- **Decision:** NO-GO.
- **Most significant reported development:** Calif.io reportedly demonstrated an untethered iOS 27.0.1 jailbreak on an iPhone 18 Pro (A20 Pro) at Hexacon 2026 on 2026-10-16. The demonstration device is not the target, and no write-up or tool has been verified (C-001, C-002, C-027).
- **Apple's security notes** credit Calif.io researchers for four CVE entries in iOS 27 (C-038) and six in iOS 27.2 (C-042). None of the six iOS 27.2 entries is a kernel-memory impact. Apple's index lists no CVE entries for 27.0.1 (C-007).
- **Firmware:** the third-party index lists 27.0.1 as not signed and 27.2.1 as signed on 2026-11-12. The upstream reported 27.0.1 as signed on 2026-11-02, so the status changed between observations. The change date is not known (C-021, E-030).

## Material changes in this snapshot

**2026-11-12 (v0.2.0 research update):** Apple's iOS 27.2 and 27.2.1 advisories were parsed and mapped ([apple-27x-cve-mapping.md](../research/apple-27x-cve-mapping.md)). The upstream reference was reconciled claim by claim ([upstream-reconciliation.md](../research/upstream-reconciliation.md)). The Dopamine 3.0 release notes were read: real-device SPTM support ends at iOS 17.3.1 (C-066). An independent SPTM paper's scope was checked (C-060). A November project claim for iOS 27.0 to 27.0.1 is recorded as unverified (C-064). **Corrections:** Apple's iOS 27 page lists four Calif.io-credited entries and its iOS 27.2 page lists six; an earlier count of three was wrong (C-005). Readiness is unchanged. Changes are listed in [CHANGELOG.md](../CHANGELOG.md).

## Update procedure check

| Step | Done in this snapshot | Notes |
|---|---|---|
| Last update date | Yes | No previous snapshot exists. |
| Official security disclosures | Yes | Apple iOS 27, 27.2 and 27.2.1 security content pages, and the Apple release index. |
| Researcher announcements | Partially | Press coverage and a community reference only. No primary announcement found. |
| GitHub releases | Yes | Dopamine release records (30 most recent, with bodies), Sileo, the former ElleKit repository (ID redirect checked), momentarius metadata. |
| GitHub commit history | Yes | Dopamine default branch (five most recent commits). |
| SPTM research search | Yes | Apple's platform guide, an independent SPTM paper and Dopamine's release notes checked. No public A17 Pro bypass verified. See research/sptm-evidence-audit.md. |
| KRW research search | Yes | Announced on 2026-11-04; no publication found on 2026-11-12. See research/krw-release-audit.md. |
| Jailbreak tool compatibility | Yes | Dopamine 3.0 release notes (primary) and a third-party support table. |
| Firmware changes | Yes | Apple pages for iOS 27, 27.2 and 27.2.1; Apple index; ipsw.me. |
| Signing status | Yes | Third-party index and one reported change. No Apple-hosted signing record. |
| Contradictory claims | Yes | See [research/contradictions.md](../research/contradictions.md). |
| Validation | Yes | See [reports/evidence-audit.md](evidence-audit.md) and the validator output. |

## Dataset

**Data snapshot (2026-11-12):** 76 claims (39 verified, 17 partially verified, 20 unverified), 42 sources, 30 timeline events, 15 compatibility rows and 4 firmware builds.

## Open items

See [STATUS.md](../STATUS.md) for the blockers list.
