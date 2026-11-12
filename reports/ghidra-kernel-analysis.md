# Ghidra static analysis: iOS 27.0.1 kernelcache (build 24A446), summary

**Status:** research summary, data as of 2026-11-12. Target: iPhone 15 Pro Max (A17 Pro, `iPhone16,2`), iOS 27.0.1, build 24A446.

**Scope:** offline, static, read-only analysis of a kernelcache taken from Apple's official iOS 27.0.1 firmware package. No device was connected or operated on. No firmware or analysis output is published here. The Ghidra project is kept outside the repository. No code was executed, and no exploit or bypass was developed.

This page records what the analysis shows at the level of provenance, structure and presence. It does not assess vulnerabilities, exploitability or reachability.

## 1. Provenance (verified)

| Artifact | Bytes | SHA-256 | Notes |
|---|---|---|---|
| Decompressed kernelcache (analysed) | 73,023,488 | `71d3232aff357cf0e26d7252230cbcbc366b1f48d902de3d7fa5c13feea6f243` | 64-bit arm64e Mach-O, `MH_FILESET` |
| Raw IM4P container (`kernelcache.release.iphone16`) | 22,511,975 | `33606c425d5b9ebc9db16f1e7cf5197e8437c0df09ff061c9bd16596547c4d96` | SHA-384 equals the manifest `KernelCache` digest |

- The manifest digest is the SHA-384 of the IM4P container as shipped in the package. The check passed for all three build identities, which share the same digest.
- The analysed file is the LZFSE-decompressed payload of that container. Its size matches the recorded uncompressed size, and it is byte-identical to the decompression output.
- Not verified: the SHA-256 of the complete firmware package. The origin metadata for the package and the third-party firmware index both list the expected value. The package itself was not downloaded in full.

Related records: [data/firmware.json](../data/firmware.json) (build 24A446), [data/claims.json](../data/claims.json) (C-078 to C-081).

## 2. Structure (verified, address level)

- Mach-O 64-bit arm64, `MH_FILESET`, 9 segments: `__TEXT`, `__PRELINK_TEXT`, `__DATA_CONST`, `__DATA_SPTM`, `__TEXT_EXEC`, `__TEXT_BOOT_EXEC`, `__PRELINK_INFO`, `__DATA`, `__LINKEDIT`.
- 264 fileset entries. Every entry start address and every segment boundary lies inside a loaded memory block.
- Kernel version string: Darwin 27.0.0, XNU 13432.2.10~2 (release build).
- The loader selected the ARM64e language variant (`AARCH64:LE:64:AppleSilicon`) automatically. No language was forced.

## 3. Analysis result (partially verified)

- Automatic analysis completed, and the program was saved. The log records 17 errors. These are 13 function-creation failures caused by thunk overlaps and 4 value-tracking failures. The affected regions were not analysed as functions.
- The analysis recovered about 230,000 functions. Almost all have default names. Original symbol names are essentially absent, so the results below rest on segment layout and on strings, not on recovered names.
- The standalone KEXT files extracted from the kernelcache could not be imported. Each has an empty symbol table. Analysis therefore covers the kernelcache fileset, not the separate files.

## 4. Presence of security-related components (verified, by exact bundle identifier)

These bundles exist in the 24A446 kernelcache fileset. Presence does not show that a bundle is affected by any advisory, or that it is reachable.

- `com.apple.security.sandbox`
- `com.apple.driver.AppleMobileFileIntegrity` (AMFI)
- `com.apple.kext.CoreTrust`
- `com.apple.security.AppleImage4` and `com.apple.security.Image4`
- `com.apple.iokit.IOSurface`, `com.apple.filesystems.apfs`, `com.apple.kec.Compression`
- Secure Enclave driver bundles (for example `com.apple.driver.AppleSEPKeyStore`)

## 5. Interface strings (verified for presence only)

The kernelcache contains kernel log and format strings that name these interfaces:

- SPTM and TXM: messages about the SPTM version and load address, ASID supply by SPTM, and TXM thread association.
- AMFI, CoreTrust and trust caches: messages about missing or stale AMFI interfaces, CoreTrust interface availability, and static and engineering trust-cache counts.
- Code-signing hashes: logging of executable code-directory hashes.
- Pointer authentication failures and page-table management (pmap).
- Page-protection terms: about 33 strings, including the name "Page Protection Layer". Their presence does not show that the PPL code path is active on this device (Apple's platform guide states that SPTM replaces PPL on A15 or later, C-013).
- Memory-integrity terms: the string "MIE" appears in two contexts, and "MTE" appears in one message about disabling soft mode for ptraced processes.

Presence of a string does not show how the corresponding code path behaves, whether it is reached, or whether the feature is active on the A17 Pro. Apple names Memory Integrity Enforcement for A19 and later (see [data/claims.json](../data/claims.json), C-011 and C-012), so activation on this device remains **not established** (C-084).

## 5a. The __DATA_SPTM segment (unresolved)

The `__DATA_SPTM` segment is a single read-only block of 311,296 bytes. In this analysis, Ghidra recorded no code reference into it. The one recorded reference is a data-table entry in the linkage segment, not code. The cause is not established. Possible explanations are indirect accesses that were not resolved, accesses made from the monitor side, and the analysis errors above (C-085). This is a limitation of the analysis, not a finding about the segment's behaviour.

## 6. What this analysis does not establish

- Whether any Apple advisory entry applies to build 24A446. Apple's pages give no affected version ranges (C-047).
- Exploitability, reachability from an unprivileged context, or any chain of components.
- The behaviour of any function. No function was reviewed for correctness or for security.
- Any cross-build difference. No comparison with another build was made.

The compatibility status of the A17 Pro is unchanged: readiness remains LEVEL 0, and the decision remains NO-GO. See [STATUS.md](../STATUS.md).

## 7. Method and limits

- Tools: ipsw 3.1.739 (extraction and inspection), Ghidra 12.1.2 DEV in headless mode with its default analysis options.
- Read-only exports were used for function, string and reference inventories. Export scripts did not modify the program.
- Limits: 17 analysis errors; original symbols absent; standalone KEXT import failure; full-package hash not computed.
