# Exploit dependency matrix

**Snapshot:** 2026-11-12. **Target:** iPhone 15 Pro Max (A17 Pro, `iPhone16,2`), iOS 27.0.1 (build 24A446). **Readiness:** LEVEL 0 (unchanged).

Each row is one dependency that a full jailbreak would need. The status describes the evidence for the exact target. "Not met" means that no verified evidence exists. This matrix does not describe how any dependency could be met.

| # | Dependency | Why it matters | Status for the target | Evidence | Records |
|---|---|---|---|---|---|
| 1 | An entry point (a bug reachable from attacker-controlled input) | Starting point of any chain | Not established | The reported Calif.io chain has no component list. Apple's listed entries are not mapped to any chain | C-027, C-042 |
| 2 | Sandbox escape | Leaves an app or web sandbox | Apple-listed fixes only. Applicability not established | 27.2: WebContent escape (CVE-2026-112690) and WebKit Process Model escape (CVE-2026-113897). 27.0: seven sandbox-related entries, including CVE-2026-84607 (kernel privileges) | C-034, C-048, [mapping](../research/apple-27x-cve-mapping.md) |
| 3 | Kernel memory read | Information for a later stage | Apple-listed. Not mapped. Applicability not established | 27.0: 8 entries. 27.2: 6 entries | C-035, C-040 |
| 4 | Kernel memory write or corruption | A primitive for control | Apple-listed. Not mapped. The announced KRW is not published | 27.0: 2 write and 7 corruption entries. 27.2: 4 write, 12 corruption and 1 copy-on-write entry | C-037, C-039, C-041, C-022, C-049 |
| 5 | Kernel or root privilege | Privilege for code | Apple-listed on 27.0 only. Not mapped | 27.0: four entries. 27.2: none | C-034, C-036, C-074 |
| 6 | PPL or SPTM bypass (A15 and later) | The A17 Pro is in the class where signed-code enforcement uses SPTM | Not established | Reported only (C-051). Dopamine's real-device limit is iOS 17.3.1 (C-066). Apple's advisories name no SPTM fix (C-073) | C-013, C-051, C-066, C-073 |
| 7 | Code-signing or trust-cache bypass (AMFI, CoreTrust) | Lets unsigned code run | Not researched | Apple's advisories do not name AMFI or CoreTrust (C-073). The guide describes signed-code enforcement only in general terms (C-032) | C-032, C-073 |
| 8 | Pointer-authentication and memory-tagging protections | Protections a chain must work around | Not researched in depth | The guide lists PAC, KIP and fast permission restrictions for A15 to A18. MIE is not named for the A17 Pro (C-012) | C-012 |
| 9 | Persistence across reboot | Keeps state after restart | Reported only (unverified) | Press reports (C-004). The upstream reports over-the-air persistence on 27.2 (C-053) | C-004, C-053 |
| 10 | Bootstrap for the build | Creates the jailbreak environment | Not met | No iOS 27 support in Dopamine 3.0.2 to 3.0.13 (C-055). Dopamine 3.0's real-device limit is iOS 17.3.1 (C-066) | C-055, C-066, CMP-010 |
| 11 | Package manager and tweak injection | Installs and runs packages | Not established | Sileo's latest release is 2.5.1 with no iOS 27 mention (C-030). The former ElleKit repository has no release (C-056). The ElleKit 1.2 claim is unverified (C-057) | C-030, C-056, C-057, CMP-011 |
| 12 | A public installable tool | The user-facing route | Not met | None verified (C-028). A November project announcement is unverified and carries a high risk (C-064) | C-028, C-064 |
| 13 | A signed restore target (24A446) | Needed for any recovery | Not established | Index: not signed on 2026-11-12. Upstream: signed on 2026-11-02 (C-021, E-030) | C-021 |
| 14 | Exact-target compatibility evidence | Needed for LEVEL 5 | Not met | No independent reproduction (CMP-014) | CMP-014 |
| 15 | Daily-driver stability | Needed for LEVEL 6 | Not evaluated | See DIM11 | DIM11 |

## Rows that do not apply to the target

- **A12 and A13 BootROM route (usbliter8):** the reports concern A12 and A13 devices, not the A17 Pro (C-019).
- **iPhone Duo builds (iOS 27.1):** Apple's index lists 27.1 for iPhone Duo only (E-008).

## How to read the matrix

- A "not met" row blocks any GO decision. A listed Apple fix does not satisfy a dependency until its applicability to 24A446 is established.
- Rows 2 to 5 come from Apple's own text. They describe what Apple lists, not what any exploit does.
- No row is marked met on the basis of a demonstration on another device.

See [a17pro-exploit-readiness.md](a17pro-exploit-readiness.md) for the level and GO/NO-GO decision.
