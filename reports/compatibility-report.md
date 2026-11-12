# Compatibility report

**Target:** iPhone 15 Pro Max (A17 Pro, `iPhone16,2`), iOS 27.0.1, build `24A446`. **Snapshot:** 2026-11-11.

## How to read this report

Every row answers one question for the exact target. A status of `not_established` means no verified evidence exists. It does not mean the answer is "no". A status of `reported_unverified` means the claim appears in press or community reports only. See [docs/DEVICE_PROFILE.md](../docs/DEVICE_PROFILE.md) for the five evidence levels.

## Matrix

| ID | Category | Status | Evidence | Note |
|---|---|---|---|---|
| CMP-001 | SPTM Research | partially verified | C-013, C-014, C-145, C-157 | Apple defines SPTM for A15-or-later SoCs, which includes the A17 Pro by ordering. |
| CMP-002 | SPTM Bypass | unverified | C-015 | The only SPTM bypass mention is a community reference describing an undisclosed bypass. |
| CMP-003 | Kernel Vulnerability | unverified | C-037, C-039, C-041, C-070, C-071 | Apple's iOS 27 and iOS 27.2 notes list kernel-memory write and corruption entries (research/apple-27x-cve-mapping.md). |
| CMP-004 | Kernel Read | unverified | C-035, C-040 | Apple lists kernel-memory read, disclosure and layout impacts: eight on the iOS 27 page (including CVE-2026-84622, which needs root) and six on the iOS 27.2 page. |
| CMP-005 | Kernel Write | unverified | C-037, C-039, C-041 | Apple lists write and corruption impacts for kernel memory on the iOS 27 and iOS 27.2 pages. |
| CMP-006 | Sandbox Escape | not established | C-034, C-048, C-074, C-111, C-114 | Apple lists a WebContent sandbox escape reachable by a remote attacker (iOS 27.2: CVE-2026-112690) and a WebKit Process Model escape (iOS 27.2: CVE-2026-113897). |
| CMP-007 | Privilege Escalation | not established | C-035, C-036, C-074 | Apple lists a kernel entry in which a malicious app may gain root privileges (iOS 27: CVE-2026-43689) and an entry in which an app with root privileges reads uninitialised kernel memory (iOS 27: CVE-2026-84622). |
| CMP-008 | AMFI Compatibility | not researched | - | AMFI (code signing enforcement) was not researched in this pass. |
| CMP-009 | Complete Exploit Chain | reported, unverified | C-001, C-002, C-027, C-038, C-042, C-049 | A complete chain is reported only for an iPhone 18 Pro (A20 Pro) demonstration. |
| CMP-010 | Bootstrap | not established | C-016, C-055, C-065, C-066, C-133, C-135, C-167 | No bootstrap for iOS 27.0.1 is verified. |
| CMP-011 | Package Manager | not established | C-030, C-056, C-057, C-134, C-167 | Sileo's latest release is 2.5.1 (2024-10-08), with no iOS 27 mention (C-030). |
| CMP-012 | Persistence | reported, unverified | C-004, C-053 | Reboot persistence is reported for the iPhone 18 Pro demonstration (C-004). |
| CMP-013 | Public Jailbreak Tool | not established | C-028, C-058, C-064 | No publicly installable tool is verified for this target (C-028). |
| CMP-014 | Independent A17 Pro Reproduction | not established | C-049, C-062 | No independent reproduction on A17 Pro hardware was found. |
| CMP-015 | Exact Build Verification | partially verified | C-003, C-024, C-025, C-078, C-079 | Build 24A446 for iPhone16,2 is corroborated by third-party sources and by the Apple index date. |
| CMP-016 | Sandbox Escape | reported, unverified | C-109, C-111, C-114, C-165 | The SKVLENT repository states boundary crossings into other applications' containers and shared groups on an A19 Pro configuration (27.0.1). |
| CMP-017 | Public Jailbreak Tool | reported, unverified | C-126, C-127, C-128, C-129, C-132, C-166 | The declared iOS range includes 27.0.1 by range only. |
| CMP-018 | Exact Build Verification | partially verified | C-119, C-120, C-121, C-122, C-123, C-124, C-125, C-157, C-159, C-160 | Manifest-level differences only. |
| CMP-019 | Exact Build Verification | not established | C-157, C-158, C-159, C-161, C-162, C-163 | Secure Exclaves applicability to the target. |
| CMP-020 | Exact Build Verification | partially verified | C-159, C-160, C-124 | Chip identifier for the target. |

## Reading the matrix

- **Verified or partially verified rows** concern the existence of a public Apple design feature (SPTM), the build mapping (24A446), or the iOS 27.2 release date. None of them shows that a jailbreak works.
- **Reported rows** rely on a demonstration on an iPhone 18 Pro (A20 Pro) or on community statements. They do not transfer to the target.
- **Not established rows** are the core gap. A jailbreak for the target would require evidence in these rows.
- **Not researched rows** (AMFI) need primary Apple sources before any status can be given.

Data: [data/compatibility.json](../data/compatibility.json).
