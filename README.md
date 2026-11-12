# iOS 27 A17 Pro Jailbreak Tracker

Independent research and compatibility tracker for the **iPhone 15 Pro Max** (Apple A17 Pro, device identifier `iPhone16,2`) on **iOS 27.0.1** (build `24A446`).

> **Status (data as of 2026-11-12): NO-GO. Readiness LEVEL 0 for the target.** No verified jailbreak exists for this device and build. This repository is not a jailbreak tool. It supplies no exploit code, tools or installation steps.

## 1. Project Introduction

This repository collects, checks and scores public information about jailbreak research for the iPhone 15 Pro Max on iOS 27.0.1 (build 24A446). It is an independent research and compatibility project. It is not affiliated with Apple, Calif.io, Hexacon or the Dopamine project.

Every claim is recorded with its sources, dates, scope, verdict and limitations. Press-only facts are labelled "reported". Community claims stay leads until a primary source confirms them.

**AI assistance disclosure.** Drafting and research assistance was provided by Claude, an AI model made by Anthropic. The maintainer reviews the work, and every claim cites its sources. Apple's iOS 27 security notes credit "Claude and Anthropic Research" alongside Calif.io for two CVE entries (C-006). This project quotes Apple's wording only and does not infer how that collaboration worked. The project is maintained independently and is not an Anthropic product.

## 2. Project Objectives

- Establish, with evidence, whether any jailbreak path exists for the target device and build.
- Track the research areas that could lead to one: SPTM, kernel research, sandbox and privilege escalation, build compatibility, exploit-chain integration, the jailbreak ecosystem, persistence, and scam detection.
- Protect real devices from research risk. The project never connects to, inspects, or modifies any maintainer-owned device, and it never recommends operations on a real device.
- Keep firmware facts accurate: what is installed, what is signed, and what is not known.
- Publish evidence that others can check, correct and reuse under the licences in section 19.

## 3. Target Hardware

This repository maintains an independent research target profile for the iPhone 15 Pro Max (A17 Pro) running iOS 27.0.1 (build 24A446).

The target profile is used for compatibility research. It does not disclose or verify the personal device state of the repository maintainer.

The project does not connect to, inspect, or modify any maintainer-owned device.

| Field | Value |
|---|---|
| Product | iPhone 15 Pro Max |
| Device identifier | `iPhone16,2` (third-party index; C-025) |
| Chipset | Apple A17 Pro (C-026, partially verified) |
| Architecture | arm64 |

The five evidence levels, and which of them are not established, are in [docs/DEVICE_PROFILE.md](docs/DEVICE_PROFILE.md).

## 4. Target Firmware

| Field | Value |
|---|---|
| iOS version | 27.0.1, released 2026-09-28 (C-024) |
| Build | 24A446 (third-party index; C-003, partially verified) |
| Apple security notes | No published CVE entries for 27.0.1 (C-007) |
| Signing status (public observation) | Unresolved. A third-party firmware index (ipsw.me, S-014) lists build 24A446 as not signed, last checked 2026-11-12. A community reference (S-026) reported it as signed on 2026-11-02, so the status changed between observations. The change date is not known (C-021, E-030). Apple has not published a signing record that the project could check. |

The research target is fixed at iOS 27.0.1 (build 24A446), as described in the target profile above. Firmware observations in this section come from public sources, with attribution and the date each was last checked.

## 5. Research Status

**Data snapshot (2026-11-12):** 106 claims (62 verified, 24 partially verified, 20 unverified), 46 sources, 32 timeline events, 15 compatibility rows and 4 firmware builds.

**Current position: LEVEL 0 for the target.** Calif.io reportedly demonstrated an untethered iOS 27.0.1 jailbreak on an iPhone 18 Pro (A20 Pro) on 2026-10-16 (C-001, partially verified). That demonstration did not use the target. No write-up or tool has been verified. Dopamine's 3.0 release notes state that real-device SPTM support ends at iOS 17.3.1 (C-066), and no iOS 27 support is documented for the A17 Pro (C-018). The v0.2.0 research update maps Apple's iOS 27.2 and 27.2.1 advisories ([apple-27x-cve-mapping.md](research/apple-27x-cve-mapping.md)) and reconciles the community reference claim by claim ([upstream-reconciliation.md](research/upstream-reconciliation.md)). It does not change the readiness level.

Research status by dimension (details in [research/](research/)):

| Dimension | Status |
|---|---|
| DIM01 Event verification | Partially researched |
| DIM02 A17 Pro architecture | Partially researched |
| DIM03 SPTM research | Researched (graded audit: [sptm-evidence-audit.md](research/sptm-evidence-audit.md)) |
| DIM04 Kernel vulnerability intelligence | Researched for the Apple advisories ([apple-27x-cve-mapping.md](research/apple-27x-cve-mapping.md)) |
| DIM05 Sandbox escape and privilege escalation | Partially researched (Apple advisory text only) |
| DIM06 Firmware and build compatibility | Partially researched |
| DIM07 Exploit chain integration | Partially researched |
| DIM08 Jailbreak ecosystem | Partially researched |
| DIM09 Persistence and deployment | Partially researched |
| DIM10 Scam detection | Partially researched |
| DIM11 Daily-driver stability | Not evaluated |
| DIM12 Recovery and safety | Partially researched |

## 6. Compatibility Dashboard

Status key: `verified`; `partially_verified`; `reported_unverified` (reported, not verified); `unverified`; `not_established` (no verified evidence for the target); `not_researched`.

| ID | Category | Status | Evidence | Note |
|---|---|---|---|---|
| CMP-001 | SPTM Research | partially verified | C-013, C-014 | Apple defines SPTM for A15-or-later SoCs, which includes the A17 Pro by ordering. |
| CMP-002 | SPTM Bypass | unverified | C-015 | The only SPTM bypass mention is a community reference describing an undisclosed bypass. |
| CMP-003 | Kernel Vulnerability | unverified | C-037, C-039, C-041, C-070, C-071 | Apple's iOS 27 and iOS 27.2 notes list kernel-memory write and corruption entries (research/apple-27x-cve-mapping.md). |
| CMP-004 | Kernel Read | unverified | C-035, C-040 | Apple lists kernel-memory read, disclosure and layout impacts: eight on the iOS 27 page (including CVE-2026-84622, which needs root) and six on the iOS 27.2 page. |
| CMP-005 | Kernel Write | unverified | C-037, C-039, C-041 | Apple lists write and corruption impacts for kernel memory on the iOS 27 and iOS 27.2 pages. |
| CMP-006 | Sandbox Escape | not established | C-034, C-048, C-074 | Apple lists a WebContent sandbox escape reachable by a remote attacker (iOS 27.2: CVE-2026-112690) and a WebKit Process Model escape (iOS 27.2: CVE-2026-113897). |
| CMP-007 | Privilege Escalation | not established | C-035, C-036, C-074 | Apple lists a kernel entry in which a malicious app may gain root privileges (iOS 27: CVE-2026-43689) and an entry in which an app with root privileges reads uninitialised kernel memory (iOS 27: CVE-2026-84622). |
| CMP-008 | AMFI Compatibility | not researched | - | AMFI (code signing enforcement) was not researched in this pass. |
| CMP-009 | Complete Exploit Chain | reported, unverified | C-001, C-002, C-027, C-038, C-042, C-049 | A complete chain is reported only for an iPhone 18 Pro (A20 Pro) demonstration. |
| CMP-010 | Bootstrap | not established | C-016, C-055, C-065, C-066 | No bootstrap for iOS 27.0.1 is verified. |
| CMP-011 | Package Manager | not established | C-030, C-056, C-057 | Sileo's latest release is 2.5.1 (2024-10-08), with no iOS 27 mention (C-030). |
| CMP-012 | Persistence | reported, unverified | C-004, C-053 | Reboot persistence is reported for the iPhone 18 Pro demonstration (C-004). |
| CMP-013 | Public Jailbreak Tool | not established | C-028, C-058, C-064 | No publicly installable tool is verified for this target (C-028). |
| CMP-014 | Independent A17 Pro Reproduction | not established | C-049, C-062 | No independent reproduction on A17 Pro hardware was found. |
| CMP-015 | Exact Build Verification | partially verified | C-003, C-024, C-025, C-078, C-079 | Build 24A446 for iPhone16,2 is corroborated by third-party sources and by the Apple index date. |

Every row is scoped to the target profile: iPhone16,2, A17 Pro, iOS 27.0.1, build 24A446. `not_established` means no verified evidence exists for that row. It does not mean the answer is no.

## 7. SPTM Research

- Apple states that SPTM is supported on A15-or-later and M2-or-later SoCs, and replaces PPL on supported platforms (C-013). The A17 Pro is in that class (C-014, partially verified).
- No public A17 Pro SPTM bypass has been verified. A community reference reports an SPTM bypass valid through iOS 27.0.1, reportedly patched in a 27.2 beta. The primary post was not retrieved (C-051, unverified).
- Dopamine's 3.0 release notes state that real-device SPTM support ends at iOS 17.3.1, because no SPTM bypass is known for iOS 17.4 and later (C-066). The Titan bypass in those notes covers iOS 16.5.1 to 17.3.1 (C-065).
- The independent SPTM paper analyses an iPhone 16 on iOS 18.4. It does not cover the A17 Pro or any iOS 27 build (C-060).

Details: [research/sptm-evidence-audit.md](research/sptm-evidence-audit.md) and [research/DIM03-sptm-research.md](research/DIM03-sptm-research.md).

## 8. Kernel Research

- Apple's iOS 27 security notes credit Calif.io researchers for four CVE entries: CVE-2026-65409, CVE-2026-65410, CVE-2026-28968 and CVE-2026-86886 (C-038). CVE-2026-28968 is a Kernel entry with a kernel-memory corruption impact.
- Apple's iOS 27.2 security notes credit Calif.io researchers for six entries. None has a kernel-memory impact (C-042).
- Apple's iOS 27.2 notes list 23 kernel-memory entries: 4 write, 12 corruption, 1 copy-on-write and 6 read or disclosure. The notes state no affected version range (C-039 to C-041, C-047).
- Apple's index lists no published CVE entries for 27.0.1 (C-007).
- A kernel read/write release was announced on 2026-11-04. No publication was found on 2026-11-12 (C-022, C-049).
- No public kernel exploit is verified for the target.

Details: [research/DIM04-kernel-vulnerability.md](research/DIM04-kernel-vulnerability.md) and [research/apple-27x-cve-mapping.md](research/apple-27x-cve-mapping.md).

## 9. Exploit Chain Status

- The only reported complete chain was demonstrated on an iPhone 18 Pro (A20 Pro). It has no published write-up, and its components are not published (C-001, C-027).
- The target has no verified complete chain. Readiness: LEVEL 0.
- This project does not publish, run or explain exploit code.

Details: [research/DIM07-exploit-chain.md](research/DIM07-exploit-chain.md).

## 10. Jailbreak Ecosystem

- **Dopamine:** latest official release 3.0.13 (2026-11-03; C-017). Its notes for 3.0.2 to 3.0.13 do not mention iOS 27 (C-055). The 3.0 release states that real-device SPTM support ends at iOS 17.3.1 (C-066). No iOS 27 support is documented for the A17 Pro (C-018).
- **Sileo:** the latest release of the repository named Sileo/Sileo is 2.5.1 (2024-10-08). Its notes do not mention iOS 27 (C-030, partially verified).
- **ElleKit:** the former repository identifier redirects to a repository with no GitHub release (C-056). The upstream's claim that ElleKit 1.2 covers iOS 27 is unverified (C-057).
- **Project announcement:** a project claim from November 2026 for iOS 27.0 to 27.0.1 is unverified and carries a high risk (C-064). No release was reviewed in this pass.
- **BootROM issue:** reported for A12 and A13 chips, not the A17 Pro (C-019, partially verified).

Details: [research/DIM08-jailbreak-ecosystem.md](research/DIM08-jailbreak-ecosystem.md).

## 11. Daily Driver Readiness

**Not evaluated.** No jailbreak is verified for the target, so there is no basis to assess stability, battery, Face ID, banking or authentication apps, or any other daily-use category. LEVEL 6 is not reached. Details: [research/DIM11-daily-driver-stability.md](research/DIM11-daily-driver-stability.md).

## 12. Firmware Preservation

| Version | Build | Released | Signing (as recorded) | Apple CVE status |
|---|---|---|---|---|
| 27.0 | 24A437 | 2026-09-14 | not signed (third-party index), 2026-11-12 | listed on Apple page |
| 27.0.1 | 24A446 | 2026-09-28 | not signed (third-party index), 2026-11-12 | none published |
| 27.2 | 24B119 | 2026-10-26 | signed (third-party index), 2026-11-12 | listed on Apple page |
| 27.2.1 | 24B156 | 2026-11-09 | signed (third-party index), 2026-11-12 | listed on Apple page |

- An installed build is not the same as a restorable build. Restore depends on Apple's signing at restore time.
- The signing status of 24A446 is unresolved. A third-party index (ipsw.me, S-014) lists it as not signed, last checked 2026-11-12. A community reference (S-026) reported it as signed on 2026-11-02, so the status changed between observations (C-021, E-030). Do not assume a restore to it is possible.
- SHSH blobs do not guarantee a restore.
- The project does not recommend updating or downgrading. Those decisions belong to the device owner.
- Update-deferral settings, where a device offers them, do not guarantee protection against every update or restore pathway. Their coverage is device-specific, and this project does not verify it.
- A failed experiment or a recovery attempt on any device could result in a newer firmware being installed, after which the affected build may no longer be restorable through ordinary channels. The project recommends against any operation that carries that risk.

Details: [docs/RECOVERY_AND_PRESERVATION.md](docs/RECOVERY_AND_PRESERVATION.md) and [reports/firmware-report.md](reports/firmware-report.md).

## 13. Research Timeline

| Date | Event | Verification | Sources |
|---|---|---|---|
| 2025-09 | Apple announces Memory Integrity Enforcement with the iPhone 17 and iPhone Air, naming the A19 and A19 Pro chips. | verified | S-003 |
| 2025-10-10 | Independent academic analysis of SPTM, TXM and Exclaves (arXiv:2510.09272) is submitted. Its firmware analysis uses iPhone 16 (A18) on iOS 18.4, not the A17 Pro or iOS 27. | verified | S-035 |
| 2026-06-18 | usbliter8 BootROM exploit for A12 and A13 devices is publicised (reported by secondary outlets and a national CERT). | partially verified | S-021, S-022, S-023 |
| 2026-08-07 | Dopamine 3.0 released; secondary coverage quotes a support table of iOS 15.0 to 17.3.1 for A8 to A17 and M1 to M2, and iOS 26.0 to 26.0.1 for A12 and A13. | partially verified | S-009 |
| 2026-08-07 | Dopamine 3.0 release notes state a Titan PPL/SPTM bypass for iOS 16.5.1 to 17.3.1, a momentarius PPL bypass for A12 and A13, and that real-device SPTM support ends at iOS 17.3.1 because no bypass is known for 17.4 and later. | verified | S-007 |
| 2026-09-14 | iOS 27.0 released (build 24A437 per the third-party index). | partially verified | S-014, S-001 |
| 2026-09-21 | Press reports Apple stopped signing iOS 26.6.2 after iOS 27 shipped. Used as a pattern example for how older builds lose signing. | partially verified | S-020 |
| 2026-09-28 | iOS 27.0.1 released (build 24A446). Apple's security releases index lists no published CVE entries for this build. | partially verified | S-002, S-014, S-016 |
| 2026-10-16 | Calif.io reportedly demonstrates an untethered iOS 27.0.1 jailbreak on an iPhone 18 Pro at Hexacon 2026 in Paris. | partially verified | S-010, S-011, S-012 |
| 2026-10-17 | An opa334 PSA dated 2026-10-17 is reported by the upstream reference to warn of an SPTM bypass valid through iOS 27.0.1. The original was not located in this review. | unverified | S-026 |
| 2026-10-19 | Apple's iOS 27 security notes are updated with CVE entries credited to Calif.io researchers, two of them jointly with Claude and Anthropic Research. | verified | S-001 |
| 2026-10-19 | The upstream reference reports a Calif.io team member's interview on end-user tools, the scope of the chain and a 27.2 patch statement. The interview was not retrieved. | unverified | S-026 |
| 2026-10-23 | Apple's index lists iOS 27.1 for iPhone Duo with no published CVE entries. | verified | S-002 |
| 2026-10-26 | iOS 27.2 released (build 24B119 per the third-party index). Secondary press reports 163 fixed vulnerabilities; Apple's 27.2 advisory was not located. | partially verified | S-002, S-014, S-017, S-018 |
| 2026-10-26 | Apple's iOS 27 security page is updated with entries marked as added on 2026-10-26, including CVE-2026-112608 (CoreMedia) and CVE-2026-86916 (kernel privilege impact). | verified | S-001 |
| 2026-10-30 | A Calif.io social account reportedly posted a bare hash without explanation (upstream reference). The content it commits to is unknown. | unverified | S-026 |
| 2026-10-30 | A company-branded account reportedly showed a root shell on iOS 27.2 (upstream reference). Single-party, unverified (C-063). | unverified | S-026 |
| 2026-11-01 | A project announced a semi-untethered iOS 27.0 to 27.0.1 jailbreak with a planned release one to two weeks later (upstream reference). The upstream reference found no proof of concept or third-party validation. No release was reviewed in this pass. Any future release should be treated as potentially malicious (C-064). | unverified | S-026 |
| 2026-11-02 | A community reference states that iOS 27.0.1 was still signed on 2026-11-02. This is not independently verified and conflicts with the third-party index checked on 2026-11-11. | unverified | S-026 |
| 2026-11-03 | Dopamine 3.0.13 published. Release notes describe a posix_spawn hook fix and a SpringBoard snapshot change. They do not state iOS 27 support. | verified | S-007 |
| 2026-11-03 | Press reports that Apple responded to MIE-bypass claims with an iOS update. Details were not verified. | unverified | S-024 |
| 2026-11-04 | Reported plan for a kernel read/write exploit and write-up from a Calif.io-linked researcher within about a week. Coverage conflicts; no primary announcement was located. | unverified | S-026, S-029 |
| 2026-11-04 | Reported (upstream reference, V31): opa334 says Dopamine A12 and A13 support could follow using momentarius once a kernel read/write exploit is public; A14 and later still need an SPTM bypass. Original not retrieved. | unverified | S-026 |
| 2026-11-04 | Reported (upstream reference, V32): a Calif.io video shows Lockdown Mode, an over-the-air update to iOS 27.2, and a reboot after which a plugin still works. Video and original post not retrieved. | unverified | S-026 |
| 2026-11-06 | Press coverage through about 2026-11-06 reports that Apple fixed most flaws in iOS 27.2 and that no public tool is planned. | partially verified | S-019 |
| 2026-11-09 | iOS 27.2.1 released (build 24B156 per the third-party index and the Wikipedia infobox). | partially verified | S-002, S-014, S-030 |
| 2026-11-11 | Tracker snapshot. The third-party index lists iOS 27.0.1 as not signed. A community reference reports the opposite for 2026-11-02, so the status is unresolved. | partially verified | S-014, S-026 |
| 2026-11-11 | The one-week window reported on 2026-11-04 for a kernel read/write write-up lapses. No publication, repository or source-code release for the announced work was found on 2026-11-12. | partially verified | S-029, S-013 |
| 2026-11-12 | Research pass for the v0.2.0 update: Apple's iOS 27.2 and 27.2.1 advisories parsed, the upstream reference reconciled, and the kernel, Calif.io and SPTM evidence re-classified. | verified | S-033, S-034, S-026 |
| 2026-11-12 | The third-party index lists iOS 27.0.1 (24A446) as not signed on 2026-11-12. The upstream reference recorded it as signed on 2026-11-02. The date of the change is not known (C-021). | partially verified | S-014, S-026 |
| 2026-11-12 | Local static provenance and Ghidra analysis of the 24A446 kernelcache and the SPTM and TXM monitor images. Manifest digests match the normal containers; restore-entry digests do not match (unresolved). The complete package was not hashed. Readiness is unchanged. | partially verified | S-043 |
| 2026-11-12 | Static research on the 24A446 kernelcache and monitors: symbolication with a third-party signature set, a KEXT import investigation, monitor structure counts, a memory-protection documentation re-read, and metadata comparison with the 24B119 and 24B156 builds. The v0.3.0 release was not created. Readiness is unchanged. | partially verified | S-004, S-043, S-044, S-045, S-046 |

## 14. Verified Claims

A `verified` verdict requires a fetched, API or tier-1 source and high confidence. Each claim is scoped in [data/claims.json](data/claims.json).

| ID | Claim | Confidence | Sources |
|---|---|---|---|
| C-002 | The reported demonstration device (iPhone 18 Pro) uses A20 Pro, so the demonstration is not direct evidence for A17 Pro | high | S-005, S-010 |
| C-005 | Apple's iOS 27 security notes credit Calif.io researchers for four CVE entries (CVE-2026-65409, CVE-2026-65410, CVE-2026-28968 and CVE-2026-86886) | high | S-001 |
| C-006 | Apple's iOS 27 security notes name Claude and Anthropic Research alongside Calif.io for two entries | high | S-001 |
| C-007 | iOS 27.0.1 has no published CVE entries in Apple's security releases index | high | S-002 |
| C-011 | Apple says Memory Integrity Enforcement is built into all iPhone 17 and iPhone Air models and names the A19 and A19 Pro chips | high | S-003 |
| C-013 | Apple states SPTM is supported on A15-or-later and M2-or-later SoCs | high | S-004 |
| C-016 | Dopamine 3.0 release notes state a Titan PPL/SPTM bypass for all devices on iOS 16.5.1 to 17.3.1 | high | S-007, S-039 |
| C-017 | Dopamine 3.0.13 is the latest official Dopamine release (published 2026-11-03) | high | S-007 |
| C-029 | A GitHub account with the login pwnlambda exists | high | S-013 |
| C-032 | Apple states PPL and SPTM enforce execution of signed and trusted code on all platforms except macOS | high | S-004 |
| C-033 | The five most recent Dopamine default-branch commit subjects do not mention iOS 27 | high | S-032 |
| C-034 | Apple's iOS 27 notes list two kernel-component entries with arbitrary code execution with kernel privileges (CVE-2026-84607 and CVE-2026-86916) | high | S-001 |
| C-035 | Apple's iOS 27 notes list eight kernel-memory read, disclosure, layout or state entries, one requiring root privileges | high | S-001 |
| C-036 | Apple's iOS 27 notes list a kernel entry that lets a malicious app gain root privileges (CVE-2026-43689) | high | S-001 |
| C-037 | Apple's iOS 27 notes list kernel-memory write and corruption entries, including the Calif.io-credited CVE-2026-28968 | high | S-001 |
| C-038 | Apple's iOS 27 notes credit Calif.io for four entries with different components and impacts | high | S-001 |
| C-039 | Apple's iOS 27.2 notes list 23 kernel-memory entries (4 write, 12 corruption, 1 copy-on-write, 6 read or disclosure) and no kernel or root privilege entry | high | S-033 |
| C-040 | Apple's iOS 27.2 notes list six kernel-memory read, disclosure or layout entries from several components | high | S-033 |
| C-041 | Apple's iOS 27.2 notes list further kernel-memory corruption and write entries in Apple Neural Engine and AVEVideoEncoder | high | S-033 |
| C-042 | The six Calif.io-credited entries in Apple's iOS 27.2 notes carry no kernel read or write impact | high | S-033 |
| C-043 | CVE-2026-112611 and CVE-2026-113912 credit a Calif.io-affiliated researcher by handle, but neither is a kernel entry | high | S-033 |
| C-044 | Apple's entry for CVE-2026-112705 lists the AVEVideoEncoder component with an impact of unexpected system termination, not a kernel-level impact | high | S-033 |
| C-045 | Apple's iOS 27.2.1 notes list nine CVE identifiers, none of them one of the six target kernel entries | high | S-034 |
| C-047 | Apple's iOS 27.2 notes state no affected iOS versions for the listed entries | high | S-033 |
| C-048 | Apple's iOS 27.2 notes list a WebContent sandbox-escape entry that a remote attacker may use (CVE-2026-112690) | high | S-033 |
| C-055 | No Dopamine 3.0.x release note from 3.0.2 to 3.0.13 mentions iOS 27 support | high | S-007 |
| C-056 | The repository formerly at evelyneee/ellekit redirects to tealbathingsuit/ellekit, which has no GitHub release | high | S-040 |
| C-058 | A public GitHub repository named staturnzz/momentarius is described as an A12/A13 PPL bypass | high | S-041 |
| C-059 | An independent SPTM analysis states that SPTM replaced PPL on A15 or newer and M2 or newer SoCs | high | S-035, S-004 |
| C-060 | The arXiv SPTM analysis's firmware work uses an iPhone 16 on iOS 18.4. The paper does not analyse the A17 Pro or any iOS 27 build | high | S-035 |
| C-065 | Dopamine 3.0 release notes state a Titan PPL/SPTM bypass for all devices on iOS 16.5.1 to 17.3.1 | high | S-007 |
| C-066 | Dopamine 3.0 release notes say real-device SPTM support stops at iOS 17.3.1 because no SPTM bypass is known for iOS 17.4 and later | high | S-007 |
| C-067 | Dopamine 3.0 release notes describe a momentarius PPL bypass for A12 and A13 devices on iOS 16.6 to 18.7.1 and 26.0 to 26.0.1 | high | S-007, S-041 |
| C-068 | Dopamine 3.0 release notes name ClearSword and DarkSword workarounds but state no iOS version range for either exploit | high | S-007 |
| C-070 | Apple's iOS 27 notes list CVE-2026-112608 (CoreMedia) as added on 2026-10-26 | high | S-001 |
| C-071 | Apple's iOS 27 page marks 45 identifiers as added or updated on 2026-10-19 or 2026-10-26 | high | S-001 |
| C-072 | Most Apple entries in iOS 27 and 27.2 apply to iPhone 11 and later; three Apple Intelligence entries apply to iPhone 15 Pro and later | high | S-001, S-033 |
| C-073 | Apple's iOS 27 and iOS 27.2 notes do not mention AGX, IOGPU, SPTM, TXM, PPL, CoreTrust, AMFI or Exclave | high | S-001, S-033 |
| C-074 | Apple's iOS 27 notes list four kernel or root privilege entries; the iOS 27.2 notes list none | high | S-001, S-033 |
| C-078 | The 24A446 manifest's KernelCache digest equals the SHA-384 of the raw IM4P container (identities 0, 1 and 2) | high | S-043 |
| C-079 | The analysed 24A446 kernelcache is the LZFSE decompression of the verified container (73,023,488 bytes, byte-identical) | high | S-043 |
| C-080 | Restore-entry digests for the 24A446 kernelcache and the SPTM and TXM monitors do not match the retrieved containers | high | S-043 |
| C-081 | The 24A446 package contains SPTM and TXM monitor containers that are unencrypted, with matching normal manifest digests | high | S-043 |
| C-082 | The 24A446 kernelcache fileset contains the sandbox, AMFI, CoreTrust and Image4 bundles, by exact identifier | high | S-043 |
| C-083 | The 24A446 kernelcache contains kernel log strings that name SPTM and TXM interfaces | high | S-043 |
| C-086 | Standalone KEXT files extracted from the 24A446 kernelcache have empty symbol tables, and Ghidra cannot import them | high | S-043 |
| C-088 | Ghidra's automatic analysis of the 24A446 TXM image completed without logged errors, recovering 1,654 functions (1,653 default-named) | high | S-043 |
| C-089 | The 24B119 (27.2) manifest's KernelCache, SPTM and TXM normal digests match the retrieved containers | high | S-044 |
| C-090 | The 24B119 (27.2) restore-entry digests for the kernelcache, SPTM and TXM do not match the retrieved containers | high | S-044 |
| C-091 | The 24B156 (27.2.1) manifest's KernelCache, SPTM and TXM normal digests match the retrieved containers | high | S-045 |
| C-092 | The 24B156 (27.2.1) restore-entry digests for the kernelcache, SPTM and TXM do not match the retrieved containers | high | S-045 |
| C-093 | The SPTM and TXM containers of 24B119 and 24B156 are byte-identical to each other and differ from 24A446 | high | S-043, S-044, S-045 |
| C-094 | The kernel version strings are darwin 27.0.0 (XNU 13432.2.10~2) for 24A446 and darwin 27.2.0 (XNU 13432.42.3~28) for 24B119 and 24B156 | high | S-043, S-044, S-045 |
| C-095 | The KEXT inventories of 24B119 and 24B156 contain the same 281 records as 24A446; 47 bundle-version and 48 short-version fields differ from 24A446 in each | high | S-043, S-044, S-045 |
| C-096 | The kernelcache and the SPTM and TXM monitor images of 24A446 carry the arm64e subtype bit in their Mach-O headers | high | S-043 |
| C-097 | The signature set kernel/27.0 in the symbolicator repository declares a darwin range of 27.0.0 to 27.2.0 | high | S-046 |
| C-098 | About 80% of the distinct xnu signature anchor strings occur in the 24A446 kernelcache | high | S-043, S-046 |
| C-099 | Signature-assisted symbolication of the 24A446 kernel assigns non-equivalent names to 1,139 addresses | high | S-043, S-046 |
| C-101 | Ghidra cannot import the standalone KEXT files extracted from the 24A446 kernelcache, because stub processing reads symbols from an empty table | high | S-043 |
| C-102 | Of the 281 KEXT inventory records of 24A446, 263 match a fileset entry, 11 are codeless and 7 are kernel-programming-interface pseudo-KEXTs with no fileset entry | high | S-043 |
| C-105 | Apple's Platform Security guide states that SPTM is supported on A15-or-later and M2-or-later SoCs, and that SPTM with TXM replaces the PPL there | high | S-004 |
| C-106 | Apple's Platform Security guide states that Memory Integrity Enforcement is available on A19 and M5 processors or later | high | S-004 |

## 15. Unverified Claims

Partially verified claims have checkable support, but a key element (scope, build, device or date) remains unverified. Unverified claims are leads only.

### Partially verified

| ID | Claim | Confidence | Sources |
|---|---|---|---|
| C-001 | Calif.io reportedly demonstrated an untethered iOS 27.0.1 jailbreak on an iPhone 18 Pro at Hexacon 2026 | medium | S-005, S-010, S-011, S-012, S-036, S-037 |
| C-003 | iOS 27.0.1 build 24A446 is the build for iPhone16,2 (iPhone 15 Pro Max) | medium | S-014, S-015, S-016 |
| C-008 | iOS 27.2 (build 24B119) was released on 2026-10-26 | medium | S-002, S-014 |
| C-009 | iOS 27.2.1 (build 24B156) was released on 2026-11-09 | medium | S-002, S-014 |
| C-012 | A17 Pro is not among the chips Apple names for Memory Integrity Enforcement | medium | S-003 |
| C-014 | The A17 Pro falls within Apple's A15-or-later SPTM class | medium | S-004, S-030 |
| C-018 | No Dopamine release is documented to support iOS 27.0.1 on A17 Pro | medium | S-009, S-007, S-008 |
| C-019 | The usbliter8 BootROM exploit is reported to affect A12 and A13 chips and not A14 or later | medium | S-021, S-022, S-023 |
| C-024 | iOS 27.0.1 was released on 2026-09-28 | medium | S-002, S-014, S-016 |
| C-025 | The device identifier iPhone16,2 corresponds to the iPhone 15 Pro Max | medium | S-014 |
| C-026 | The iPhone 15 Pro Max uses the Apple A17 Pro chip | medium | S-030 |
| C-027 | No public complete exploit chain applicable to iPhone 15 Pro Max on iOS 27.0.1 has been verified | medium | S-010, S-019 |
| C-028 | No publicly installable jailbreak tool is verified for iOS 27.0.1 on A17 Pro | medium | S-010, S-019, S-009, S-007 |
| C-030 | The latest GitHub release of the repository named Sileo/Sileo is 2.5.1 (2024-10-08), and its notes do not mention iOS 27 | medium | S-031 |
| C-046 | Apple's iOS 27.2 notes contain 162 distinct CVE identifiers in the extracted text; press reports 163 | medium | S-033 |
| C-049 | No public kernel read/write write-up or exploit code by the researcher announced on 2026-11-04 was found as of 2026-11-12 | medium | S-013, S-029 |
| C-069 | 8kSec reports Apple's fixed-in versions for the two DarkSword kernel CVEs as iOS 26.2 and 26.3 (secondary analysis) | medium | S-042 |
| C-084 | The 24A446 kernelcache contains MIE-related strings; whether MIE is active on the A17 Pro is not established | medium | S-043 |
| C-085 | Ghidra recorded no code reference into the 24A446 __DATA_SPTM segment; the cause is unresolved | medium | S-043 |
| C-087 | Ghidra's automatic analysis of the 24A446 kernelcache completed, recovering 230,298 functions (3 named) with 17 logged errors | medium | S-043 |
| C-100 | On 58 kernel addresses that have independent table-derived names, signature names agree in 55 (94.8%) | medium | S-043, S-046 |
| C-103 | Ghidra's reference model records no register-indirect call references in the 24A446 SPTM or TXM images, while a byte-level decoder finds such encodings in both | medium | S-043 |
| C-104 | Four methods found no code path that addresses the 24A446 __DATA_SPTM segment; the cause of the absence is unresolved | medium | S-043 |
| C-107 | The A15-A18 column of the Platform Security guide's feature table includes the A17 generation; the support cells are not readable from the fetched copy | medium | S-004 |

### Unverified

| ID | Claim | Confidence | Sources |
|---|---|---|---|
| C-004 | The demonstrated jailbreak state persisted across a reboot | low | S-010 |
| C-010 | iOS 27.2 fixed 163 vulnerabilities | low | S-017, S-018 |
| C-015 | A publicly disclosed SPTM bypass applies to A17 Pro on iOS 27.0.1 | low | S-026 |
| C-020 | A tutorial page claims a full iOS 27 jailbreak using usbliter8 | low | S-025 |
| C-021 | iOS 27.0.1 (24A446) is unsigned in the ipsw.me index on 2026-11-12, after a 2026-11-02 report that it was signed | low | S-014 |
| C-022 | A Calif.io-linked researcher reportedly announced a kernel read/write exploit and write-up within about a week | low | S-026, S-029 |
| C-023 | An Apple CVE credit confirms the identity of the lambda handle, according to the reference repository | low | S-026 |
| C-050 | opa334 is reported (2026-11-04) to plan A12/A13 Dopamine support via momentarius once a kernel read/write exploit is public, with A14 and later still needing an SPTM bypass | low | S-026 |
| C-051 | A 2026-10-17 opa334 statement is reported to warn of an SPTM bypass valid through iOS 27.0.1 (upstream V7) | low | S-026 |
| C-052 | A Calif.io researcher is reported to have said the jailbreak applies to any iPhone running iOS 27.0.1, possibly including iPads (upstream V10) | low | S-026 |
| C-053 | A Calif.io video is reported to show a jailbreak state surviving an over-the-air update to iOS 27.2 with Lockdown Mode enabled (upstream V32) | low | S-026 |
| C-054 | The upstream states that DarkSword and ClearSword kernel exploits support iOS only up to 26.0.1 (V8); no primary source confirms the range | low | S-026 |
| C-057 | ElleKit 1.2 is reported to cover iOS 15 to 27 (upstream reference) | low | S-026 |
| C-061 | Press coverage reports that AI helped build the Calif.io jailbreak (not confirmed by the team) | low | S-036, S-037, S-038 |
| C-062 | A third party is reported to have reproduced CVE-2026-112705 as a crash on iPhone 17 Pro, iOS 27.0.1 (unverified) | low | S-026 |
| C-063 | A company-branded account is reported to have shown a root shell on iOS 27.2 (unverified) | low | S-026 |
| C-064 | A project announced on 2026-11-01 claims a semi-untethered iOS 27.0 to 27.0.1 jailbreak for iPhone 15 Pro Max (A17 Pro); no release or validation was located | low | S-026 |
| C-075 | heise reports the Calif.io jailbreak as 'the first reboot-proof jailbreak since iOS 9' (press claim; unverified) | low | S-036 |
| C-076 | t3n reports AI-assisted exploit-chain discovery and an iOS 27.2 beta comparison as established; heise calls the comparison theoretical | low | S-038 |
| C-077 | The upstream reports a Calif.io team member saying the team will not release an end-user jailbreak tool (unverified) | low | S-026 |

## 16. Source Index

Tiers: 1 primary (Apple, original research, official repositories and conference sites); 2 independent or reputable (news, government CERT, third-party indexes, encyclopedia); 3 community; 4 unverifiable. See [docs/RESEARCH_METHODOLOGY.md](docs/RESEARCH_METHODOLOGY.md).

| ID | Source | Publisher | Tier | Published | Checked by |
|---|---|---|---|---|---|
| S-001 | [About the security content of iOS 27 and iPadOS 27](https://support.apple.com/en-us/149034) | Apple Inc. | 1 | 2026-09-14 | fetched (full text) |
| S-002 | [Apple security releases](https://support.apple.com/en-us/100100) | Apple Inc. | 1 | - | fetched (partial text) |
| S-003 | [Memory Integrity Enforcement](https://security.apple.com/blog/memory-integrity-enforcement/) | Apple Inc. (Apple Security Research) | 1 | 2025-09 | fetched (full text) |
| S-004 | [Apple Platform Security: Secure Page Table Monitor and Trusted Execution Monitor](https://support.apple.com/guide/security/sec8b776536b/web) | Apple Inc. | 1 | - | fetched (full text) |
| S-005 | [iPhone 18 Pro - Technical Specifications](https://www.apple.com/iphone-18-pro/specs/) | Apple Inc. | 1 | - | fetched (full text) |
| S-006 | [iPhone 15 Pro - Technical Specifications](https://www.apple.com/iphone-15-pro/specs/) | Apple Inc. | 1 | - | fetched (full text) |
| S-007 | [Dopamine releases](https://github.com/opa334/Dopamine/releases) | opa334 (Dopamine project, GitHub) | 1 | 2026-11-03 | API response |
| S-008 | [Dopamine repository README](https://github.com/opa334/Dopamine) | opa334 (Dopamine project, GitHub) | 1 | - | fetched (full text) |
| S-009 | [Dopamine 3.0 Jailbreak Released With iOS 17.3.1 Support, iOS 26 on A12/A13](https://www.iclarified.com/101697/dopamine-30-jailbreak-released-with-ios-1731-support-ios-26-on-a12a13) | iClarified | 2 | 2026-08-07 | fetched (full text) |
| S-010 | [Hackers Jailbreak iPhone 18 Pro on Stage, and It Survives a Reboot](https://decrypt.co/381177/hackers-jailbreak-iphone-18-pro-survives-reboot) | Decrypt | 2 | 2026-10-16 | fetched (full text) |
| S-011 | [Hexacon 2026](https://hexacon.fr) | Hexacon (conference organiser) | 1 | - | fetched (full text) |
| S-012 | [Calif.io](https://calif.io) | Calif.io | 1 | - | fetched (full text) |
| S-013 | [GitHub user record: pwnlambda](https://api.github.com/users/pwnlambda) | GitHub | 1 | - | API response |
| S-014 | [ipsw.me device firmware index: iPhone16,2](https://api.ipsw.me/v4/device/iPhone16,2?type=ipsw) | ipsw.me | 2 | - | API response |
| S-015 | [Keys:Rave 24A446 (iPhone16,2)](https://theapplewiki.com/wiki/Keys:Rave_24A446_(iPhone16,2)) | The Apple Wiki | 3 | - | search snippet only |
| S-016 | [iOS 27.0.1 bug fixes, changes and improvements](https://forums.macrumors.com/threads/ios-27-0-1-bug-fixes-changes-and-improvements.2490674/) | MacRumors Forums | 3 | - | search snippet only |
| S-017 | [Apple Fixes 163 iPhone, iPad Flaws in iOS 27.2 Update](https://www.esecurityplanet.com/threats/news-apple-ios-27-2-ipados-163-security-flaws/) | eSecurityPlanet | 2 | - | search snippet only |
| S-018 | [Apple Just Patched 163 iPhone Security Flaws - Here's What Was at Risk](https://www.techrepublic.com/article/news-ios-27-2-security-flaws-patched/) | TechRepublic | 2 | - | search snippet only |
| S-019 | [Calif's iPhone Jailbreak: Apple Patches Most Flaws in iOS 27.2, but No Public Tool Is Planned](https://pbxscience.com/califs-iphone-jailbreak-apple-patches-most-flaws-in-ios-27-2-but-no-public-tool-is-planned/) | PBX Science | 2 | - | search snippet only |
| S-020 | [No More Downgrading: Apple Stops Signing iOS 26.6.2 and iOS 26.7 Following Release of iOS 27](https://www.mactrast.com/2026/09/no-more-downgrading-apple-stops-signing-ios-26-6-2-and-ios-26-7-following-release-of-ios-27/) | MacTrast | 2 | - | search snippet only |
| S-021 | [Vulnerability in iPhones with A12 and A13 processors](https://www.incibe.es/en/incibe-cert/publications/cybersecurity-highlights/vulnerability-iphones-a12-and-a13-processors) | INCIBE-CERT (Spain) | 2 | - | search snippet only |
| S-022 | [Apple's A12 and A13 Chips Facing New Unpatchable Exploit](https://www.macrumors.com/2026/06/18/a12-and-a13-chips-facing-exploit/) | MacRumors | 2 | 2026-06-18 | search snippet only |
| S-023 | [usbliter8 Brings Unpatchable BootROM Exploit to Apple A12 and A13 Devices](https://securityaffairs.com/193965/hacking/usbliter8-brings-unpatchable-bootrom-exploit-to-apple-a12-and-a13-devices.html) | Security Affairs | 2 | - | search snippet only |
| S-024 | [Apple rains on MIE-bypassing iPhone jailbreak parade with iOS update](https://www.itnews.com.au/news/apple-rains-on-mie-bypassing-iphone-jailbreak-parade-with-ios-update-629978) | iTnews | 2 | 2026-11-03 | search snippet only |
| S-025 | [How usbliter8 enables a full jailbreak of iOS 27 (tutorial page)](https://www.besthub.dev/articles/how-usbliter8-enables-a-full-jailbreak-of-ios-27-complete-technical-guide-0a0ebb30bb7d) | Unknown (tutorial-style website) | 4 | - | search snippet only |
| S-026 | [iOS 27.0.1 Jailbreak Fact-Check and Ongoing Tracker (iMaxTomas/ios27-jb-tracker)](https://github.com/iMaxTomas/ios27-jb-tracker) | iMaxTomas (GitHub) | 3 | 2026-11-04 | fetched (full text) |
| S-027 | [Creative Commons Attribution 4.0 International - Legal Code](https://creativecommons.org/licenses/by/4.0/legalcode) | Creative Commons | 1 | - | fetched (full text) |
| S-028 | [Contributor Covenant Code of Conduct, version 2.1](https://www.contributor-covenant.org/version/2/1/code_of_conduct/) | Contributor Covenant project | 1 | - | fetched (full text) |
| S-029 | [PBX Science: Calif iPhone jailbreak coverage (2026-11-04)](https://pbxscience.com/?p=24999) | PBX Science | 2 | 2026-11-04 | fetched (full text) |
| S-030 | [iPhone 15 Pro](https://en.wikipedia.org/wiki/IPhone_15_Pro) | Wikipedia | 2 | - | fetched (full text) |
| S-031 | [Sileo/Sileo: latest GitHub release (2.5.1)](https://github.com/Sileo/Sileo/releases/tag/2.5.1) | Sileo project (GitHub repository named Sileo/Sileo) | 2 | 2024-10-08 | API response |
| S-032 | [Dopamine default-branch commit history](https://github.com/opa334/Dopamine/commits) | opa334 (Dopamine project, GitHub) | 1 | 2026-11-03 | API response |
| S-033 | [About the security content of iOS 27.2 and iPadOS 27.2](https://support.apple.com/en-us/149230) | Apple Inc. | 1 | 2026-10-26 | fetched (full text) |
| S-034 | [About the security content of iOS 27.2.1 and iPadOS 27.2.1](https://support.apple.com/en-us/149715) | Apple Inc. | 1 | 2026-11-09 | fetched (full text) |
| S-035 | [Modern iOS Security Features: A Deep Dive into SPTM, TXM, and Exclaves (arXiv:2510.09272)](https://arxiv.org/abs/2510.09272) | arXiv (independent academic analysis) | 2 | 2025-10-10 | fetched (full text) |
| S-036 | [Works on iPhone 18 Pro: AI helps create untethered jailbreak for iOS 27.0.1](https://www.heise.de/en/news/Works-on-iPhone-18-Pro-AI-helps-create-untethered-jailbreak-for-iOS-27-0-1-11490907.html) | heise online | 2 | 2026-10-16 | fetched (full text) |
| S-037 | [Dank KI: Rebootfester Jailbreak für iOS 27.0.1 bis zum iPhone 18 Pro, untethered](https://www.heise.de/news/Untethered-Jailbreak-fuer-iOS-27-0-1-auf-iPhone-18-Pro-der-Reboots-ueberlebt-11490726.html) | heise online | 2 | 2026-10-16 | fetched (full text) |
| S-038 | [iOS-27-Jailbreak: Sicherheitsforscher greifen auf KI-Support zurück](https://t3n.de/news/untethered-jailbreak-ios-27-1768775/) | t3n | 2 | 2026-10-18 | fetched (full text) |
| S-039 | [Dopamine Jailbreak (third-party page, ellekit.space)](https://ellekit.space/dopamine) | ellekit.space (authorship not verified) | 3 | - | fetched (full text) |
| S-040 | [tealbathingsuit/ellekit (repository reached by redirect from evelyneee/ellekit)](https://github.com/tealbathingsuit/ellekit) | GitHub (repository owner: tealbathingsuit) | 2 | - | API response |
| S-041 | [staturnzz/momentarius (repository metadata)](https://api.github.com/repos/staturnzz/momentarius) | GitHub (repository owner: staturnzz) | 3 | 2026-08-07 | API response |
| S-042 | [Inside the DarkSword Kernel Escalation: From GPU Process to Kernel R/W (CVE-2025-43510 & CVE-2025-43520)](https://www.8ksec.io/darksword-kernel-escalation-cve-2025-43510-43520/) | 8kSec | 2 | 2026-05-03 | fetched (full text) |
| S-043 | [iOS 27.0.1 (24A446) iPhone16,2 firmware package: BuildManifest and IM4P components (Apple CDN object)](https://updates.cdn-apple.com/2026FallFCS/531d0d56-6e43-4fb9-b4ee-abb5aab5c04f/iPhone16,2_27.0.1_24A446_Restore.ipsw) | Apple Inc. (CDN object listed by the ipsw.me firmware index) | 1 | 2026-09-28 | fetched (partial text) |
| S-044 | [iOS 27.2 (24B119) iPhone16,2 firmware package: BuildManifest and IM4P components (Apple CDN object)](https://updates.cdn-apple.com/2026FallFCS/dcf3b441-e473-4c28-a936-99d6af8c60a2/iPhone16,2_27.2_24B119_Restore.ipsw) | Apple Inc. (CDN object; URL resolved by a firmware index lookup) | 1 | 2026-10-26 | fetched (partial text) |
| S-045 | [iOS 27.2.1 (24B156) iPhone16,2 firmware package: BuildManifest and IM4P components (Apple CDN object)](https://updates.cdn-apple.com/2026FallFCS/079a8de1-4a8d-4aa2-b5fb-7c33a7ffbf19/iPhone16,2_27.2.1_24B156_Restore.ipsw) | Apple Inc. (CDN object; URL resolved by a firmware index lookup) | 1 | 2026-11-09 | fetched (partial text) |
| S-046 | [blacktop/symbolicator: ipsw symbolication signatures (kernel/27.0 folder, MIT licence)](https://github.com/blacktop/symbolicator) | blacktop/symbolicator repository (community; MIT licence) | 3 | 2026-11-05 | fetched (partial text) |

## 17. Contribution Instructions

Contributions are welcome for new sources, corrections, evidence-backed verdict changes, and scam reports. Start with [CONTRIBUTING.md](CONTRIBUTING.md). Never include exploit code, tool links, installation packages, device identifiers or personal data. Run `python3 scripts/validate_tracker.py` before opening a pull request.

Maintainers do not run code from pull requests, and no pull request is merged automatically.

## 18. Safety Policy

- This project never connects to, operates on, or recommends operations on an iPhone. Permission to research a jailbreak is not permission to execute one.
- Do not install IPA files, configuration profiles or jailbreak tools from unverified sources. Treat them as malware until shown otherwise.
- Never publish or submit serial numbers, UDIDs, ECIDs, IMEI or EID values, Apple Account data, tokens, backups or device logs.
- The project never connects to, inspects, or modifies any maintainer-owned device. Research never requires operating on a real device, and any operation on a real device needs explicit authorization from that device's owner for that operation.
- Full policy: [docs/SAFETY_POLICY.md](docs/SAFETY_POLICY.md). Security reports: [SECURITY.md](SECURITY.md).

## 19. License

- Original code (scripts, schemas, validator, workflows): MIT. See [LICENSE](LICENSE).
- Original documentation and research writing: CC BY 4.0, where the maintainer holds the rights. See [LICENSE-DOCS](LICENSE-DOCS).

### Third-party research attribution

- **Community reference:** [iMaxTomas/ios27-jb-tracker](https://github.com/iMaxTomas/ios27-jb-tracker) (S-026). Its original content is CC BY 4.0 under its own licence. This project read its README, SKILL.md and LICENSE for methodology and as a list of leads. No text is copied. Its conclusions were not adopted without independent checks, and its personal-name attributions are not reproduced here.
- **Press coverage, firmware indexes and encyclopedia articles** are cited individually in [data/sources.json](data/sources.json). Their copyright remains with their owners. They are cited for fact-checking and comment.
- **Apple's security content and specification pages** are cited as factual references.

## 20. Disclaimer

- This is an independent research and compatibility project. It is not affiliated with, endorsed by, or sponsored by Apple, Calif.io, Hexacon, the Dopamine project, or Sileo.
- It is not a jailbreak tool, and it does not provide one.
- Information is provided for research and reference only. It is not legal, security or device-repair advice. Owners are responsible for complying with the law where they live and with their device and service agreements.
- The data is a dated snapshot (2026-11-12). Events are moving quickly. Check the `last_checked` date on every record.
