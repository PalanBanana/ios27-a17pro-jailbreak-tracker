# A17 Pro compatibility matrix (v0.4.0)

**Status:** data as of 2026-11-12. Target: iPhone 15 Pro Max (A17 Pro, `iPhone16,2`), iOS 27.0.1, build 24A446. **Overall: LEVEL 0 / NO-GO.** No row establishes compatibility with the target. A19 Pro and A18 Pro results are not transferred to the A17 Pro.

Reference configurations: **A19 Pro** (iPhone18,1, 27.0.1, 24A446; the repository's primary configuration), **A18 Pro** (iPhone17,2, 27.2, 24B119; the repository's reproduction statements). Evidence types: **L** = runtime log stated by the repository; **B** = static binary analysis stated by the repository; **I** = source or specification reading stated by the repository; **M** = build metadata retrieved for this tracker. Every SKVLENT result is a repository statement, not verified here (see the [audit](../research/skvlent-a19pro-research-audit.md)).

## 1. Findings matrix

| Research finding | A19 Pro result | A18 Pro result | A17 Pro result | Exact iOS build | Evidence type | Hardware dependency known? | Firmware dependency known? | Independent confirmation | Compatibility verdict |
|---|---|---|---|---|---|---|---|---|---|
| Container path disclosure (dir 07) | Demonstrated: paths disclosed, contents denied | Stated to reproduce (01–07) | Not tested | 27.0.1 (A19); 27.2 (A18) | L | Not stated | Build stated per configuration | None | Not established for A17 |
| Cross-application container access, shared groups (dir 10) | Demonstrated (repository statement): read and write in other apps' containers | Not reported | Not tested | 27.0.1 (A19) | L | Not stated | Build stated (A19 only) | None. Erosion declares a similar container capability for its own purposes (see below) | Not established for A17 |
| Protected file read and directory descriptor via a system service (dir 03; CVE-2026-112706) | Demonstrated on 27.0.1 | Stated to reproduce (01–07) | Not tested | 27.0.1 (A19); 27.2 (A18) | L | Not stated | Apple lists the CVE as fixed in 27.2; the repository's 27.2 statement is in conflict (see audit 6b) | None | **Unresolved** for 27.2 and for A17 |
| IOSurface size validation (dir 01) | Accepted and inert; no access gained | Stated to reproduce | Not tested | 27.0.1 (A19); 27.2 (A18) | L | IOSurface component present in the A17 inventory (presence only, M) | Build stated | None | Not transferable; no access result |
| Metal GPU access within one context (dir 02) | Partially demonstrated; other processes not reached | Stated to reproduce | Not tested | 27.0.1 (A19); 27.2 (A18) | L | GPU generation differs: G18 (A19), G17 (A18), G16 (A17) in firmware names (M) | Build stated | None | Not transferable |
| AppleAVE2 denial of service (dir 04) | Partially demonstrated: two denial-of-service defects via VideoToolbox; the addressed write not reachable | 27.2 trigger no longer panics (fixed as CVE-2026-112705) | Not tested. Driver component present (presence only, M) | 27.0.1 (A19); 27.2 (A18) | L | Not stated | Fix in 27.2 (Apple listing) | None | Not established for A17 |
| HID property write denial of service (dir 11) | Demonstrated: a single property write aborts a UI daemon | Not reported | Not tested. HID family present (presence only, M) | 27.0.1 (A19) | L | Not stated | Build stated | None | Not established for A17 |
| CoreGraphics shading (dir 13) | Demonstrated: a document-controlled value influences a write; reaching reachable memory demonstrated not to happen | Not reported | Not tested. Renderer is userland, outside the kernel inventory | 27.0.1 (A19) | L, I | Not stated | Build stated | None | Not established for A17 |
| CoreGraphics CMap (dir 14) | Not demonstrated (parser reached, copy not reached) | Not reported | Not tested | 27.0.1 (A19) | L, I | Not stated | Build stated | None | Not established for A17 |
| CoreGraphics fix difference (dir 15) | Static difference demonstrated | Not reported | Not tested | 27.0.1 vs 27.2 (A19) | B | Not stated | Build stated | None | Not transferable; the difference is a static observation |
| Brotli block-switch fix difference (dir 16; CVE-2026-111497) | Fix difference demonstrated statically; write not demonstrated. The repository states that 27.0.1 and 27.2 carry the unchecked status, and this tracker has not verified it | Not reported | Not tested | 27.0.1 vs 27.2.1 (A19) | B | Not stated | Apple lists the CVE as fixed in 27.2.1 | None | Not established. No inference from the difference |
| Brotli over-read in a networking process (dir 17) | Read demonstrated on the device; write only locally | Not reported | Not tested | 27.0.1 (A19) | L | Not stated | Build stated | None | Not established for A17 |
| AppleKeyStore interface (dir 12) | Partially demonstrated: 25 selectors answer; no data returned | Not reported | Exact name absent from the A17 inventory; a similarly named SEP key-store component is present (no equivalence claimed, M) | 27.0.1 (A19) | L | Component naming differs | Build stated | None | Not transferable |
| ANE reachability (dir 05) | Not demonstrated; closed | Not reported | Not tested. Neural-engine interface family H16 present; the repository's H11 name absent (M) | 27.0.1 (A19) | L | ANE firmware family differs (h16, h17, h18) | Build stated | None | Not established |
| AppleM2ScalerCSCDriver (dir 06) | Not demonstrated | Not reported | Not tested. Driver present (presence only, M) | 27.0.1 (A19) | L | Not stated | Build stated | None | Not established |
| Image parser (AppleJPEGDriver, dir 08) | Not demonstrated: client never opens | Not reported | Not tested. Driver present (presence only, M) | 27.0.1 (A19) | L | Not stated | Build stated | None | Not established |
| Exclave components in the firmware package (metadata) | Six exclave-related components per identity | Six per identity | **None in any identity** (M) | 24A446 (A19 and A17); 24B119 (A18) | M | Package difference, reason unknown | Package-level | None | **Recorded as a metadata difference only** |
| Erosion sandbox escape and customisation toolbox (declared) | Not stated | Not stated | Not stated; no device or SoC list in its documents | Declared range 27.0 to 27.2.1 (all devices) | Repository statement | Not declared | Declared range only | None (no issues or device reports in the repository) | **Unverified** for A17 and for 27.0.1 |
| Dopamine rootless jailbreak | Not applicable | Not applicable | Not supported in the current README for iOS 27; arm64e range ends at 17.3.1 | Not applicable | Repository statement | Not stated | Range stated to 17.3.1 | None for iOS 27 | Not established for A17 |
| Bootstrap for iOS 27 (Procursus) | Not stated | Not stated | Not stated; no iOS version range in the official README | Not stated | Repository statement | Not stated | Not stated | None | Not established |
| SPTM bypass (any published) | Not stated by the repository | Not stated | Not established | 27.0.1 | Upstream statement only (no public bypass for 27.0.1) | SPTM is documented for A15-or-later | Build stated | None | Not established |

## 2. Capability status

Each capability has its own status. None is upgraded by any row above, and the overall readiness remains LEVEL 0.

| Capability | Repository statement (A19 Pro) | A18 Pro | A17 Pro status | Level for the target |
|---|---|---|---|---|
| Sandbox escape | Demonstrated (a boundary crossing, not kernel code execution) | Not reported | Not established | LEVEL 0 |
| Cross-application access | Demonstrated (read and write in other apps' containers and shared groups) | Not reported | Not established | LEVEL 0 |
| Kernel read | Not demonstrated | Not reported | Not established | LEVEL 0 |
| Kernel write | Not demonstrated | Not reported | Not established | LEVEL 0 |
| Privilege escalation | Not demonstrated | Not reported | Not established | LEVEL 0 |
| SPTM bypass | Not stated; no public bypass for 27.0.1 in the upstream reference | Not stated | Not established | LEVEL 0 |
| AMFI compatibility | Not researched | Not researched | Not researched (CMP-008) | LEVEL 0 |
| Bootstrap | Not stated | Not stated | Not established (CMP-010) | LEVEL 0 |
| Package manager | Not stated | Not stated | Not established (CMP-011) | LEVEL 0 |
| Complete jailbreak | Not demonstrated | Not reported | Not established | LEVEL 0 |
| Persistence | Not stated | Not stated | Not established | LEVEL 0 |
| Daily-driver stability | Not evaluated | Not evaluated | Not established (no evidence of any kind) | LEVEL 0 |

## 3. Readiness scale (unchanged)

- **LEVEL 0:** research only.
- **LEVEL 1:** a relevant vulnerability publicly disclosed.
- **LEVEL 2:** public components available.
- **LEVEL 3:** complete exploit chain demonstrated.
- **LEVEL 4:** public jailbreak release.
- **LEVEL 5:** exact A17 Pro and exact-build compatibility independently verified.
- **LEVEL 6:** daily-driver stability independently established.

The target is at **LEVEL 0 / NO-GO**. The scale is not skipped, and the matrix does not establish any upgrade.

## 4. What the matrix does not do

- It does not assess any exploit's reliability or applicability, and it does not describe any procedure.
- It does not treat presence of a component in the A17 inventory as evidence that the component is affected by any result.
- It does not infer a vulnerability from an Apple fix listing, a later build, or a firmware difference.
- It does not treat the A19 Pro or A18 Pro results as evidence for the A17 Pro.

## 5. Records

Claims: C-108 to C-125. Compatibility rows: CMP-006, CMP-008, CMP-010, CMP-011 (updated), CMP-016 to CMP-018 (new). Sources: S-043 (target manifest), S-047 (repository), S-048 and S-049 (Erosion), S-050 (Dopamine), S-051 (ElleKit), S-052 (Procursus), S-053 (community repository), S-055 and S-056 (reference manifests).
