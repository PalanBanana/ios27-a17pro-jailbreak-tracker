# Ghidra analysis and the Secure Exclaves record: integration summary (v0.5.0)

**Status:** documentation-only summary of analysis completed earlier, data as of 2026-11-12. Target: iPhone 15 Pro Max (A17 Pro, `iPhone16,2`), iOS 27.0.1, build 24A446. **Readiness: LEVEL 0 / NO-GO, unchanged.**

This page connects the existing offline static analysis with Apple's Secure Exclaves article and the v0.5.0 manifest record. It contains no new analysis. The Ghidra project and its databases stay on the maintainer's local workstation and are not published. This page gives counts, architectural observations and the conclusions already recorded in the claim database. It gives no function address, offset, control-flow path or local path.

**This analysis does not establish any of the following.** No vulnerability was confirmed. No exploit was developed. No A17 Pro jailbreak compatibility was established. Static function analysis is not runtime validation. The physical device was not involved.

## 1. Analysis environment

- Offline, static and read-only. Ghidra was used in headless mode. The ARM64e language variant (`AARCH64:LE:64:AppleSilicon`) was selected automatically for the monitor images.
- No code was executed, no firmware was modified, and no device was connected or operated on.
- The analysis project is kept outside this repository. Its reports were reviewed only for the counts below.

## 2. Binary provenance

- All three binaries come from Apple's official iOS 27.0.1 firmware package for `iPhone16,2` (S-043). The kernelcache container digest matches the manifest digest, and the analysed file is its decompressed payload. Details are in [ghidra-kernel-analysis.md](ghidra-kernel-analysis.md), section 1.
- The SPTM and TXM images were retrieved by HTTP range request. The complete package was not downloaded or hashed.
- No binary, firmware image or Ghidra database is published.

## 3. Results reused, by component

| Component | Format and scope | Recovered | Analysis errors | Naming |
|---|---|---|---|---|
| Kernelcache (fileset) | 64-bit arm64e Mach-O fileset with 264 entries | 230,298 functions, 4,115 memory blocks | 17 logged: 13 function-creation failures from thunk overlaps and 4 value-tracking failures | 3 named functions after analysis. Original symbols essentially absent (C-087) |
| SPTM image | 64-bit arm64 Mach-O, 22 memory blocks | 530 functions | none logged | 529 default names |
| TXM image | 64-bit arm64 Mach-O, 21 memory blocks | 1,654 functions | none logged | 1,653 default names |

Because original names are essentially absent, the results rest on segment layout and on strings. No function-level review of any image is part of the public record.

## 4. KEXT handling

- The KEXT inventory built with the IPSW tooling lists 281 entries. The kernelcache fileset lists 264 entries. The reconciliation is in [ghidra-kext-loader-investigation.md](ghidra-kext-loader-investigation.md) (C-102).
- Eight standalone KEXT files fail to import in Ghidra. The recorded mechanism is an empty symbol table, which the loader's stub processing (`processStubs`) does not accept (C-086, C-101).
- The fileset import path behaves differently and imported all 264 entries. Why it does not raise the same exception is unresolved.
- KEXT-level work therefore uses the fileset program. No KEXT's code was analysed for behaviour.

## 5. Memory protection observations

Observations are string presence in the kernelcache only (see [ghidra-memory-protection.md](ghidra-memory-protection.md)):

- Pointer authentication (PAC): about 28 distinct strings.
- Page-table layer (pmap): about 200 strings.
- Page Protection Layer (PPL): about 33 strings.
- SPTM: messages about the SPTM version, the load address and ASIDs supplied by SPTM. They indicate that the kernel contains paths that use an SPTM interface for address-space allocation.
- MIE: two contexts. MTE: one message.

**String presence is not evidence of activation.** Whether PPL, MIE, MTE or any tagging mechanism is active on the A17 Pro is not established. Apple names Memory Integrity Enforcement for later products (C-011, C-012).

## 6. Exclave-related observations from the analysed images

- Static strings only. The target build's decompressed kernelcache contains 702 exclave-prefixed identifier occurrences (187 distinct forms). Its SPTM image contains 13 (10 distinct). The SPTM image also contains strings that name exclaveOS integrity-catalog and trust-cache concepts (C-161, C-163). Identifier names are not published.
- The `__DATA_SPTM` segment of the kernelcache is a single read-only block. Ghidra recorded no code reference into it, and the cause is not established (C-085).
- These strings are metadata about names that exist in the images. They do not show that any exclave feature runs, is enabled or is reachable on the target.
- The manifests list no exclave-named component for the target (C-157), while the A18 Pro and A19 Pro manifests do (C-158). The two observations are recorded side by side and are not reconciled by this page. See [the reconciliation](../research/exclave-manifest-reconciliation.md) and [the cross-generation matrix](../research/cross-generation-security-matrix.md).

## 7. Mapping to Apple's terminology

| Apple term (S-058) | What the existing analysis can say | What it cannot say |
|---|---|---|
| SPTM | An SPTM image exists in the package. The kernel contains SPTM-interface strings | How SPTM enforces anything on the target, or that any bypass exists |
| TXM | A TXM image exists in the package | Its behaviour |
| Exclaves, exclaveOS, Secure IPC | Exclave-prefixed strings exist in two images (counts above) | That any of them is active on the A17 Pro |
| Memory filters, indicator controller, ANE queues | Not examined | Anything |

## 8. Known analysis errors

- Kernelcache: 17 logged errors, in regions not analysed as functions. The effect on the function count is not quantified.
- Standalone KEXT import failure: see section 4.
- No analysis error was logged for the SPTM or TXM images. A clean log is not a statement of correctness.

## 9. Unresolved references

- The missing code references to the `__DATA_SPTM` segment (C-085).
- The fileset-versus-standalone loader difference (C-101).
- The marketing mapping of the token `t8122` (C-124).
- Whether the public XNU source gates exclave code by chip or configuration. The source was searched, not read in full.

## 10. Architectural limitations

- Original symbols are absent. Function names are default labels, so the analysis cannot identify functions by name.
- Apple's article states that the kernel cannot read exclave-private memory. A kernelcache analysis therefore sees only the kernel side of any exclave interface.
- The analysed images are one build for one device. Nothing is transferred to another SoC or build.

## 11. What this analysis does not prove

- No vulnerability, primitive or exploit was found, tested or developed.
- No compatibility with any jailbreak, tool or tweak is established for `iPhone16,2` on 24A446.
- The presence of strings is not enablement. A function count is not a behaviour. A manifest name is not a runtime component.
- Static analysis is not runtime validation, and the physical device was not involved.
- No code-level comparison against later builds and no mapping of a binary to an advisory was made. Both remain declined.
