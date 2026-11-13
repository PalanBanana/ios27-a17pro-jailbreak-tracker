# Device Profile

This file fixes the research target. The validator requires every compatibility row in `data/compatibility.json` to match it.

## Target

| Field | Value | Evidence status |
|---|---|---|
| Product | iPhone 15 Pro Max | Task profile. Model identifier mapping from a third-party index (C-025). |
| Device identifier | iPhone16,2 | Third-party index, ipsw.me (S-014). Partially verified (C-025). |
| Chipset | Apple A17 Pro | Wikipedia lists A17 Pro for the iPhone 15 Pro (C-026). Apple's product page did not expose the chip name in this check. Partially verified. |
| iOS version | 27.0.1 | Listed in Apple's security releases index with no published CVE entries (C-007). Release date 2026-09-28 (C-024). |
| Build | 24A446 | Third-party index (S-014) and two community sources (S-015, S-016). Partially verified (C-003). Apple's pages checked do not list build numbers. |
| Architecture | arm64 | Task profile. Not separately sourced. |

## The five evidence levels

The project keeps five separate questions. A result for one does not answer the others. Results for another A17 device or another iPhone generation do not automatically apply to this device.

| Level | Question | Current status | Records |
|---|---|---|---|
| 1. A17 Pro compatibility | Is there public evidence that a jailbreak works on the A17 Pro? | **Not established.** The reported demonstration used an A20 Pro device. Dopamine's documented range for A15 to A17 ends at iOS 17.3.1 (secondary coverage). | C-002, C-016, C-027 |
| 2. iPhone 15 Pro Max compatibility | Is there public evidence for this model? | **Not established.** No verified record. | C-025, C-026, CMP-009 |
| 3. iOS 27.0.1 compatibility | Is there public evidence for a working jailbreak on 27.0.1? | **Not established.** No verified record. Apple lists no CVE entries for 27.0.1 (C-007). | C-007, C-024, C-028 |
| 4. Build 24A446 compatibility | Is there build-specific evidence? | **Not established.** The build mapping is partially verified (C-003). | C-003, CMP-015 |
| 5. Independently reproduced compatibility on the exact target | Has a third party reproduced a result on this device and build? | **Not established.** No reproduction found. | CMP-014 |

## Target profile statement

The profile has two separate parts.

### A. Public research target profile

This repository maintains an independent research target profile for the iPhone 15 Pro Max (A17 Pro, `iPhone16,2`) running iOS 27.0.1 (build 24A446). This is the only device description published here.

The target profile is used for compatibility research. It does not disclose or verify the personal device state of the repository maintainer.

### B. Private device identification results

By default the project does not connect to, inspect, or modify any maintainer-owned device. The only exception is the read-only identification in [SAFETY_POLICY.md](SAFETY_POLICY.md) section 8, which needs a separate authorisation from the user and is limited to six metadata fields.

Any result of such an identification stays local. It is never published, and no published text may confirm the state of a private device. It does not change the five evidence levels above.

## Public firmware signing observations

| Build | Observation | Source | Last checked |
|---|---|---|---|
| 24A446 (iOS 27.0.1) | Listed as not signed by a third-party firmware index | ipsw.me device index for iPhone16,2 (S-014) | 2026-11-12 |
| 24A446 (iOS 27.0.1) | Reported as still signed on 2026-11-02; not verified | Community reference repository (S-026). The report is dated 2026-11-02. | Reference fetched 2026-11-11 |
| 24B119 (iOS 27.2) and 24B156 (iOS 27.2.1) | Listed as signed by the same index | ipsw.me (S-014) | 2026-11-12 |

The status of build 24A446 is unresolved. No Apple-hosted signing record was checked (C-021). Signing status can change, so each observation carries its source and date.

## Out of scope

The project never collects or publishes device identifiers (UDID, ECID, serial number, IMEI, EID), Apple Account information, tokens, backups or private device logs. See `docs/SAFETY_POLICY.md`.
