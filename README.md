# iOS 27 A17 Pro Jailbreak Tracker

Independent research and compatibility tracker for the **iPhone 15 Pro Max** (Apple A17 Pro, device identifier `iPhone16,2`) on **iOS 27.0.1** (build `24A446`).

> **Status (data as of 2026-11-11): NO-GO. Readiness LEVEL 0 for the target.** No verified jailbreak exists for this device and build. This repository is not a jailbreak tool. It supplies no exploit code, tools or installation steps.

## 1. Project Introduction

This repository collects, checks and scores public information about jailbreak research for the iPhone 15 Pro Max on iOS 27.0.1 (build 24A446). It is an independent research and compatibility project. It is not affiliated with Apple, Calif.io, Hexacon or the Dopamine project.

Every claim is recorded with its sources, dates, scope, verdict and limitations. Press-only facts are labelled "reported". Community claims stay leads until a primary source confirms them.

**AI assistance disclosure.** Drafting and research assistance was provided by Claude, an AI model made by Anthropic. The maintainer reviews the work, and every claim cites its sources. Apple's iOS 27 security notes credit "Claude and Anthropic Research" alongside Calif.io for two CVE entries (C-006). This project quotes Apple's wording only and does not infer how that collaboration worked. The project is maintained independently and is not an Anthropic product.

## 2. Project Objectives

- Establish, with evidence, whether any jailbreak path exists for the target device and build.
- Track the research areas that could lead to one: SPTM, kernel research, sandbox and privilege escalation, build compatibility, exploit-chain integration, the jailbreak ecosystem, persistence, and scam detection.
- Protect the owner's primary device. The project never connects to it and never recommends operations on it.
- Keep firmware facts accurate: what is installed, what is signed, and what is not known.
- Publish evidence that others can check, correct and reuse under the licences in section 19.

## 3. Target Hardware

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
| Signing status | Unresolved. A third-party index lists the build as not signed. A community reference reported it as signed on 2026-11-02 (C-021). |
| Owner-reported baseline | Installed build iOS 27.0.1 (24A446). The owner reports that the build is unsigned, which is consistent with the third-party index, and that over-the-air update blocking is enabled. The project has not verified either. |

The target is fixed. The owner reports that the research device runs iOS 27.0.1 (build 24A446). The project does not connect to or query the device, so it cannot verify this.

## 5. Research Status

**Data snapshot (2026-11-11):** 32 claims (10 verified, 15 partially verified, 7 unverified), 32 sources, 17 timeline events, 15 compatibility rows and 4 firmware builds.

**Current position: LEVEL 0 for the target.** Calif.io reportedly demonstrated an untethered iOS 27.0.1 jailbreak on an iPhone 18 Pro (A20 Pro) on 2026-10-16 (C-001, partially verified). That demonstration did not use the target. No write-up or tool has been verified. Dopamine's documented range for A15 to A17 devices ends at iOS 17.3.1, and no iOS 27 support is documented for the A17 Pro (C-018).

Research status by dimension (details in [research/](research/)):

| Dimension | Status |
|---|---|
| DIM01 Event verification | Partially researched |
| DIM02 A17 Pro architecture | Partially researched |
| DIM03 SPTM research | Partially researched |
| DIM04 Kernel vulnerability intelligence | Partially researched |
| DIM05 Sandbox escape and privilege escalation | Not researched in depth |
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
| CMP-003 | Kernel Vulnerability | unverified | C-005 | Apple credits Calif.io for iOS 27 entries, including a kernel-memory impact on CVE-2026-28968. |
| CMP-004 | Kernel Read | unverified | C-022 | A kernel read primitive is reported as planned by a Calif.io-linked researcher. |
| CMP-005 | Kernel Write | unverified | C-022 | Same basis as CMP-004. |
| CMP-006 | Sandbox Escape | not established | - | No verified public sandbox escape for this target. |
| CMP-007 | Privilege Escalation | not established | - | No verified public privilege escalation for this target. |
| CMP-008 | AMFI Compatibility | not researched | - | AMFI (code signing enforcement) was not researched in this pass. |
| CMP-009 | Complete Exploit Chain | reported, unverified | C-001, C-002, C-027 | A complete chain is reported only for an iPhone 18 Pro (A20 Pro) demonstration. |
| CMP-010 | Bootstrap | not established | C-016 | No bootstrap for iOS 27.0.1 is verified. |
| CMP-011 | Package Manager | not established | C-030 | Sileo: the repository named Sileo/Sileo has 2.5.1 (2024-10-08) as its latest release, and its notes do not mention iOS 27. |
| CMP-012 | Persistence | reported, unverified | C-004 | Reboot persistence is reported for an iPhone 18 Pro demonstration, not for the target. |
| CMP-013 | Public Jailbreak Tool | not established | C-028 | No publicly installable tool is verified for this target. |
| CMP-014 | Independent A17 Pro Reproduction | not established | - | No independent reproduction on A17 Pro hardware was found. |
| CMP-015 | Exact Build Verification | partially verified | C-003, C-024, C-025 | Build 24A446 for iPhone16,2 is corroborated by third-party sources and by the Apple index date. |

Every row is scoped to the target profile: iPhone16,2, A17 Pro, iOS 27.0.1, build 24A446. `not_established` means no verified evidence exists for that row. It does not mean the answer is no.

## 7. SPTM Research

- Apple states that SPTM is supported on A15-or-later and M2-or-later SoCs, and replaces PPL on supported platforms (C-013). By ordering, that covers the A17 Pro (C-014, partially verified).
- No public A17 Pro SPTM bypass has been verified. A community reference reports an undisclosed bypass. That report is unverified (C-015).
- Dopamine's documented A15 to A17 range ends at iOS 17.3.1 (C-016). It does not cover iOS 27.0.1.

Details: [research/DIM03-sptm-research.md](research/DIM03-sptm-research.md).

## 8. Kernel Research

- Apple's iOS 27 security notes credit Calif.io researchers for four CVE entries: CVE-2026-65409, CVE-2026-65410, CVE-2026-28968 and CVE-2026-86886 (C-005). One entry's impact text reads "corrupt kernel memory", and another reads "modify protected system files". Applicability to iOS 27.0.1 or the A17 Pro is not established.
- Apple's index lists no published CVE entries for 27.0.1 (C-007).
- A kernel read/write release was reported as planned. No primary release has been found (C-022, unverified).
- No public kernel exploit is verified for the target.

Details: [research/DIM04-kernel-vulnerability.md](research/DIM04-kernel-vulnerability.md).

## 9. Exploit Chain Status

- The only reported complete chain was demonstrated on an iPhone 18 Pro (A20 Pro). It has no published write-up, and its components are not published (C-001, C-027).
- The target has no verified complete chain. Readiness: LEVEL 0.
- This project does not publish, run or explain exploit code.

Details: [research/DIM07-exploit-chain.md](research/DIM07-exploit-chain.md).

## 10. Jailbreak Ecosystem

- **Dopamine:** latest official release 3.0.13 (2026-11-03; C-017). The five most recent commit subjects do not mention iOS 27 (C-033). The documented support range stops at iOS 17.3.1 for A15 to A17 (C-016). No iOS 27 support is documented for the A17 Pro (C-018).
- **Sileo:** the latest release of the repository named Sileo/Sileo is 2.5.1 (2024-10-08). Its notes do not mention iOS 27 (C-030, partially verified).
- **ElleKit:** the official upstream could not be confirmed in this pass. Status not established.
- **BootROM issue:** reported for A12 and A13 chips, not the A17 Pro (C-019, partially verified).

Details: [research/DIM08-jailbreak-ecosystem.md](research/DIM08-jailbreak-ecosystem.md).

## 11. Daily Driver Readiness

**Not evaluated.** No jailbreak is verified for the target, so there is no basis to assess stability, battery, Face ID, banking or authentication apps, or any other daily-use category. LEVEL 6 is not reached. Details: [research/DIM11-daily-driver-stability.md](research/DIM11-daily-driver-stability.md).

## 12. Firmware Preservation

| Version | Build | Released | Signing (as recorded) | Apple CVE status |
|---|---|---|---|---|
| 27.0 | 24A437 | 2026-09-14 | not signed (third-party index), 2026-11-12 | listed on Apple page |
| 27.0.1 | 24A446 | 2026-09-28 | not signed (third-party index), 2026-11-12 | none published |
| 27.2 | 24B119 | 2026-10-26 | signed (third-party index), 2026-11-12 | not located |
| 27.2.1 | 24B156 | 2026-11-09 | signed (third-party index), 2026-11-12 | not located |

- An installed build is not the same as a restorable build. Restore depends on Apple's signing at restore time.
- The signing status of 24A446 is unresolved (C-021). Do not assume a restore to it is possible.
- SHSH blobs do not guarantee a restore.
- The project does not recommend updating or downgrading. Those decisions belong to the device owner.
- Owner-reported: over-the-air update blocking is enabled. Its mechanism and coverage are not verified, and it does not guarantee protection against every update or restore pathway.
- A failed experiment or a recovery attempt could result in a newer firmware being installed, which would end the iOS 27.0.1 research baseline. The project recommends against any operation that carries that risk.

Details: [docs/RECOVERY_AND_PRESERVATION.md](docs/RECOVERY_AND_PRESERVATION.md) and [reports/firmware-report.md](reports/firmware-report.md).

## 13. Research Timeline

| Date | Event | Verification | Sources |
|---|---|---|---|
| 2025-09 | Apple announces Memory Integrity Enforcement with the iPhone 17 and iPhone Air, naming the A19 and A19 Pro chips. | verified | S-003 |
| 2026-06-18 | usbliter8 BootROM exploit for A12 and A13 devices is publicised (reported by secondary outlets and a national CERT). | partially verified | S-021, S-022, S-023 |
| 2026-08-07 | Dopamine 3.0 released; secondary coverage quotes a support table of iOS 15.0 to 17.3.1 for A8 to A17 and M1 to M2, and iOS 26.0 to 26.0.1 for A12 and A13. | partially verified | S-009 |
| 2026-09-14 | iOS 27.0 released (build 24A437 per the third-party index). | partially verified | S-014, S-001 |
| 2026-09-21 | Press reports Apple stopped signing iOS 26.6.2 after iOS 27 shipped. Used as a pattern example for how older builds lose signing. | partially verified | S-020 |
| 2026-09-28 | iOS 27.0.1 released (build 24A446). Apple's security releases index lists no published CVE entries for this build. | partially verified | S-002, S-014, S-016 |
| 2026-10-16 | Calif.io reportedly demonstrates an untethered iOS 27.0.1 jailbreak on an iPhone 18 Pro at Hexacon 2026 in Paris. | partially verified | S-010, S-011, S-012 |
| 2026-10-19 | Apple's iOS 27 security notes are updated with CVE entries credited to Calif.io researchers, two of them jointly with Claude and Anthropic Research. | verified | S-001 |
| 2026-10-23 | Apple's index lists iOS 27.1 for iPhone Duo with no published CVE entries. | verified | S-002 |
| 2026-10-26 | iOS 27.2 released (build 24B119 per the third-party index). Secondary press reports 163 fixed vulnerabilities; Apple's 27.2 advisory was not located. | partially verified | S-002, S-014, S-017, S-018 |
| 2026-11-02 | A community reference states that iOS 27.0.1 was still signed on 2026-11-02. This is not independently verified and conflicts with the third-party index checked on 2026-11-11. | unverified | S-026 |
| 2026-11-03 | Dopamine 3.0.13 published. Release notes describe a posix_spawn hook fix and a SpringBoard snapshot change. They do not state iOS 27 support. | verified | S-007 |
| 2026-11-03 | Press reports that Apple responded to MIE-bypass claims with an iOS update. Details were not verified. | unverified | S-024 |
| 2026-11-04 | Reported plan for a kernel read/write exploit and write-up from a Calif.io-linked researcher within about a week. Coverage conflicts; no primary announcement was located. | unverified | S-026, S-029 |
| 2026-11-06 | Press coverage through about 2026-11-06 reports that Apple fixed most flaws in iOS 27.2 and that no public tool is planned. | partially verified | S-019 |
| 2026-11-09 | iOS 27.2.1 released (build 24B156 per the third-party index and the Wikipedia infobox). | partially verified | S-002, S-014, S-030 |
| 2026-11-11 | Tracker snapshot. The third-party index lists iOS 27.0.1 as not signed. A community reference reports the opposite for 2026-11-02, so the status is unresolved. | partially verified | S-014, S-026 |

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
| C-017 | Dopamine 3.0.13 is the latest official Dopamine release (published 2026-11-03) | high | S-007 |
| C-029 | A GitHub account with the login pwnlambda exists | high | S-013 |
| C-032 | Apple states PPL and SPTM enforce execution of signed and trusted code on all platforms except macOS | high | S-004 |
| C-033 | The five most recent Dopamine default-branch commit subjects do not mention iOS 27 | high | S-032 |

## 15. Unverified Claims

Partially verified claims have checkable support, but a key element (scope, build, device or date) remains unverified. Unverified claims are leads only.

### Partially verified

| ID | Claim | Confidence | Sources |
|---|---|---|---|
| C-001 | Calif.io reportedly demonstrated an untethered iOS 27.0.1 jailbreak on an iPhone 18 Pro at Hexacon 2026 | medium | S-010, S-011, S-012, S-005 |
| C-003 | iOS 27.0.1 build 24A446 is the build for iPhone16,2 (iPhone 15 Pro Max) | medium | S-014, S-015, S-016 |
| C-008 | iOS 27.2 (build 24B119) was released on 2026-10-26 | medium | S-002, S-014 |
| C-009 | iOS 27.2.1 (build 24B156) was released on 2026-11-09 | medium | S-002, S-014 |
| C-012 | A17 Pro is not among the chips Apple names for Memory Integrity Enforcement | medium | S-003 |
| C-014 | The A17 Pro falls within Apple's A15-or-later SPTM class | medium | S-004, S-030 |
| C-016 | Dopamine 3.0 lists iOS 16.5.1 to 17.3.1 support for A15, A16, A17 and M2 devices | medium | S-009, S-007 |
| C-018 | No Dopamine release is documented to support iOS 27.0.1 on A17 Pro | medium | S-009, S-007, S-008 |
| C-019 | The usbliter8 BootROM exploit is reported to affect A12 and A13 chips and not A14 or later | medium | S-021, S-022, S-023 |
| C-024 | iOS 27.0.1 was released on 2026-09-28 | medium | S-002, S-014, S-016 |
| C-025 | The device identifier iPhone16,2 corresponds to the iPhone 15 Pro Max | medium | S-014 |
| C-026 | The iPhone 15 Pro Max uses the Apple A17 Pro chip | medium | S-030 |
| C-027 | No public complete exploit chain applicable to iPhone 15 Pro Max on iOS 27.0.1 has been verified | medium | S-010, S-019 |
| C-028 | No publicly installable jailbreak tool is verified for iOS 27.0.1 on A17 Pro | medium | S-010, S-019, S-009, S-007 |
| C-030 | The latest GitHub release of the repository named Sileo/Sileo is 2.5.1 (2024-10-08), and its notes do not mention iOS 27 | medium | S-031 |

### Unverified

| ID | Claim | Confidence | Sources |
|---|---|---|---|
| C-004 | The demonstrated jailbreak state persisted across a reboot | low | S-010 |
| C-010 | iOS 27.2 fixed 163 vulnerabilities | low | S-017, S-018 |
| C-015 | A publicly disclosed SPTM bypass applies to A17 Pro on iOS 27.0.1 | low | S-026 |
| C-020 | A tutorial page claims a full iOS 27 jailbreak using usbliter8 | low | S-025 |
| C-021 | iOS 27.0.1 (24A446) is currently unsigned by Apple | low | S-014 |
| C-022 | A Calif.io-linked researcher reportedly announced a kernel read/write exploit and write-up within about a week | low | S-026, S-029 |
| C-023 | An Apple CVE credit confirms the identity of the lambda handle, according to the reference repository | low | S-026 |

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
| S-029 | [PBX Science: Calif iPhone jailbreak coverage (2026-11-04)](https://pbxscience.com/?p=24999) | PBX Science | 2 | 2026-11-04 | search snippet only |
| S-030 | [iPhone 15 Pro](https://en.wikipedia.org/wiki/IPhone_15_Pro) | Wikipedia | 2 | - | fetched (full text) |
| S-031 | [Sileo/Sileo: latest GitHub release (2.5.1)](https://github.com/Sileo/Sileo/releases/tag/2.5.1) | Sileo project (GitHub repository named Sileo/Sileo) | 2 | 2024-10-08 | API response |
| S-032 | [Dopamine default-branch commit history](https://github.com/opa334/Dopamine/commits) | opa334 (Dopamine project, GitHub) | 1 | 2026-11-03 | API response |

## 17. Contribution Instructions

Contributions are welcome for new sources, corrections, evidence-backed verdict changes, and scam reports. Start with [CONTRIBUTING.md](CONTRIBUTING.md). Never include exploit code, tool links, installation packages, device identifiers or personal data. Run `python3 scripts/validate_tracker.py` before opening a pull request.

Maintainers do not run code from pull requests, and no pull request is merged automatically.

## 18. Safety Policy

- This project never connects to, operates on, or recommends operations on an iPhone. Permission to research a jailbreak is not permission to execute one.
- Do not install IPA files, configuration profiles or jailbreak tools from unverified sources. Treat them as malware until shown otherwise.
- Never publish or submit serial numbers, UDIDs, ECIDs, IMEI or EID values, Apple Account data, tokens, backups or device logs.
- The owner's primary device is preserved as it is: no change to its firmware, over-the-air update blocking or configuration; no DFU or Recovery Mode; no reboots for research.
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
- The data is a dated snapshot (2026-11-11). Events are moving quickly. Check the `last_checked` date on every record.
