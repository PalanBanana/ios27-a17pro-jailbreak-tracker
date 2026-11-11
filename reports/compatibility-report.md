# Compatibility report

**Target:** iPhone 15 Pro Max (A17 Pro, `iPhone16,2`), iOS 27.0.1, build `24A446`. **Snapshot:** 2026-11-11.

## How to read this report

Every row answers one question for the exact target. A status of `not_established` means no verified evidence exists. It does not mean the answer is "no". A status of `reported_unverified` means the claim appears in press or community reports only. See [docs/DEVICE_PROFILE.md](../docs/DEVICE_PROFILE.md) for the five evidence levels.

## Matrix

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

## Reading the matrix

- **Verified or partially verified rows** concern the existence of a public Apple design feature (SPTM), the build mapping (24A446), or the iOS 27.2 release date. None of them shows that a jailbreak works.
- **Reported rows** rely on a demonstration on an iPhone 18 Pro (A20 Pro) or on community statements. They do not transfer to the target.
- **Not established rows** are the core gap. A jailbreak for the target would require evidence in these rows.
- **Not researched rows** (AMFI) need primary Apple sources before any status can be given.

Data: [data/compatibility.json](../data/compatibility.json).
