# Ghidra static analysis: sandbox component, iOS 27.0.1 (build 24A446)

**Status:** research summary, data as of 2026-11-12. Offline, static, read-only. See [ghidra-kernel-analysis.md](ghidra-kernel-analysis.md) for provenance and method.

## What was checked

- Presence of the sandbox component in the 24A446 kernelcache fileset, by exact bundle identifier `com.apple.security.sandbox`. **Verified.**
- The standalone sandbox bundle extracted from the kernelcache has an empty symbol table, and Ghidra could not import it on its own. The component was therefore examined inside the kernelcache fileset. **Verified** (import failure). The mechanism is verified (C-101): the loader's stub processing reads symbols from an empty table. Why the fileset load does not raise the same exception is **unresolved** (see [ghidra-kext-loader-investigation.md](ghidra-kext-loader-investigation.md)).
- Interface and log strings that refer to the sandbox. These include a message about an IOUC call failing the sandbox check in a named process, and the bundle identifier of the sandbox daemon. **Verified** for presence only.

## What was not checked

- The sandbox policy rules, their evaluation, and any policy-level boundary. No policy behaviour was reviewed.
- Whether any sandbox-related Apple advisory entry applies to build 24A446. Apple's pages state no affected version range. The entries are listed in [apple-27x-cve-mapping.md](../research/apple-27x-cve-mapping.md) and in [sptm-evidence-audit.md](../research/sptm-evidence-audit.md) for context only.
- Whether any sandbox boundary can be crossed. This summary makes no claim about escape conditions.

## Apple-listed sandbox-related entries (for context)

Apple's advisories list sandbox-related entries for iOS 27 and iOS 27.2. Their impact text is recorded in the mapping above. The listing shows that Apple describes these as fixed in the stated release. It does not show that iOS 27.0.1 was affected, or that any entry is reachable on the target. Records: C-034, C-048, C-074.

## Status

- Presence of the component on the target build: **verified**.
- Applicability of any sandbox-related advisory entry to 24A446: **not established**.
- Sandbox behaviour and boundaries: **not analysed**.
