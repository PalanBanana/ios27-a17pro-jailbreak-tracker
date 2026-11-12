# Ghidra static analysis: AMFI, code-signing and trust-cache interfaces, iOS 27.0.1 (build 24A446)

**Status:** research summary, data as of 2026-11-12. Offline, static, read-only. See [ghidra-kernel-analysis.md](ghidra-kernel-analysis.md) for provenance and method.

## What was checked

- Presence of the AMFI bundle `com.apple.driver.AppleMobileFileIntegrity`, the CoreTrust bundle `com.apple.kext.CoreTrust`, and the image-verification bundles `com.apple.security.AppleImage4` and `com.apple.security.Image4` in the 24A446 kernelcache fileset. **Verified.**
- Kernel log and format strings that refer to AMFI, CoreTrust, trust caches and code-directory hashes. **Verified** for presence only. The strings include messages for an unavailable or stale AMFI interface, a missing AMFI bridge, an unavailable CoreTrust interface, static and engineering trust-cache counts, and logging of code-directory hashes for platform binary execution. Checks in the fileset also show that the kernel contains trust-cache plumbing that reads device-tree properties.

## What was not checked

- The code-signing decision logic, entitlement checks, trust-cache lookup semantics, and any bypass condition. No function was reviewed.
- Whether an AMFI or CoreTrust component is affected by any advisory entry. Apple's advisories state no affected version range, and they do not name AMFI or CoreTrust in their text (C-073).
- The relationship between the kernel's AMFI interface and the underlying signature enforcement. Apple's platform guide describes signed-code enforcement in general terms (C-032). This summary does not assess it.

## Status

- Presence of the AMFI and CoreTrust components on the target build: **verified**.
- Interface strings for AMFI, CoreTrust and trust caches: **verified** for presence.
- Enforcement behaviour, and any applicability of advisories: **not established**.
- Code-signing and trust-cache logic: **not analysed**.
