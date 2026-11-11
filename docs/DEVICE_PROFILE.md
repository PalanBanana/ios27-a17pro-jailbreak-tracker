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

## Owner-reported research baseline

The repository owner has reported the current state of the research device. The project has not checked any of it. The project does not connect to, query or inspect the device, and it will not do so.

| Item | Owner-reported state | Project status |
|---|---|---|
| Device | iPhone 15 Pro Max | Consistent with the model identifier mapping (C-025) |
| Chip | Apple A17 Pro | Consistent with C-026 (partially verified) |
| Model identifier | iPhone16,2 | Third-party index (C-025) |
| Installed iOS version | 27.0.1 | Owner-reported baseline. Not independently verified. |
| Research build | 24A446 | Baseline. The build mapping is partially verified (C-003). The installed build is not independently confirmed. |
| Firmware signing status | Unsigned | Consistent with the third-party index (C-021). Not verified against Apple. |
| Over-the-air update blocking | Enabled | Owner-reported. The mechanism and its coverage are not verified. |
| Use | Primary daily-use phone | Governs every research decision: the project performs no operation on the device. |

How this baseline is used:

- It is the research baseline for the target profile. It is not evidence of compatibility, and it changes no verdict or readiness level.
- Confirmation of the installed build, if it is ever needed, is the owner's decision. It must be non-invasive. The project will not request device identifiers or device access.
- The owner records any change to this baseline by updating this section with a date.
- No serial number, UDID, ECID, IMEI, EID or Apple Account information is collected or published.

## Out of scope

The project never collects or publishes device identifiers (UDID, ECID, serial number, IMEI, EID), Apple Account information, tokens, backups or private device logs. See `docs/SAFETY_POLICY.md`.
