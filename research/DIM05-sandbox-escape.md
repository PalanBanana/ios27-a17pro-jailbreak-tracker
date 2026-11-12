# DIM05: Sandbox escape and privilege escalation

**Status:** Researched for this pass from Apple's advisory text. No verified public sandbox escape or privilege escalation exists for the target. Apple lists sandbox-related and privilege-related fixes. Their applicability to iOS 27.0.1 is not established, because Apple states no affected version range (C-047).

## Apple-listed sandbox entries

The iOS 27 page lists seven sandbox-related entries. The iOS 27.2 page lists two. Each row is Apple's impact text. The full tables are in [apple-27x-cve-mapping.md](apple-27x-cve-mapping.md).

| Page | CVE | Component | Apple impact (as published) |
|---|---|---|---|
| iOS 27 | CVE-2026-65354 | iWork | A malicious app may be able to break out of its sandbox |
| iOS 27 | CVE-2026-65363 | Security | An app may be able to break out of its sandbox |
| iOS 27 | CVE-2026-84607 | AVEVideoEncoder | A sandboxed app may be able to execute arbitrary code with kernel privileges |
| iOS 27 | CVE-2026-84624 | CoreML | A sandboxed app may be able to access restricted files |
| iOS 27 | CVE-2026-84628 | MediaRemote | A sandboxed app may be able to access the System Keychain |
| iOS 27 | CVE-2026-86876 | CoreMedia | A sandboxed process may be able to circumvent sandbox restrictions |
| iOS 27 | CVE-2026-86961 | Foundation | A malicious app may be able to break out of its sandbox |
| iOS 27.2 | CVE-2026-112690 | App Store | A remote attacker may be able to break out of the WebContent sandbox |
| iOS 27.2 | CVE-2026-113897 | WebKit Process Model | A remote attacker may be able to break out of Web Content sandbox |

## Apple-listed privilege entries

- **iOS 27:** CVE-2026-84607 (sandboxed app to kernel privileges, above), CVE-2026-86916 (app to kernel privileges), CVE-2026-43689 (malicious app to root) and CVE-2026-84622 (an app already holding root reads uninitialised kernel memory). Records: C-034, C-036, C-074.
- **iOS 27.2:** none (C-074).

## AMFI and code signing

- Apple's iOS 27 and 27.2 advisory text does not name AMFI or CoreTrust (C-073).
- Apple's platform guide states that PPL and SPTM enforce execution of signed and trusted code on all platforms except macOS (C-032). The guide text reviewed here does not describe AMFI.
- AMFI is therefore not researched in this pass (CMP-008).

## Why sandbox and privilege records are not linked to a chain

A sandbox entry describes a boundary that Apple says a bug could cross. It does not show that the bug is reachable on the target, that it existed in 24A446, or that it is part of any chain. Apple's text is the only primary source here. No exploit or proof of concept was reviewed.

## Gaps and next steps

1. Record the applicability of each Apple-listed sandbox entry once Apple states affected versions.
2. Find the code-signing section of Apple's guide that covers AMFI, and record it as a separate claim.
3. Do not infer a sandbox escape from a privilege entry, or the reverse.
