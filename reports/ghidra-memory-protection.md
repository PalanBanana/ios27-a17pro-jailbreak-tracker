# Ghidra static analysis: memory protection and memory-management interfaces, iOS 27.0.1 (build 24A446)

**Status:** research summary, data as of 2026-11-12. Offline, static, read-only. See [ghidra-kernel-analysis.md](ghidra-kernel-analysis.md) for provenance and method.

## What was checked

- Kernel strings that refer to pointer authentication (PAC) failures. Roughly 28 distinct strings were found. **Verified** for presence.
- Kernel strings that refer to the pmap layer (about 200). These include kernel activation and page-steal messages, and an assertion about nested-pmap write faults. **Verified** for presence.
- Kernel strings that refer to SPTM: messages about the SPTM version, the SPTM load address, and ASIDs supplied by SPTM. **Verified** for presence. These indicate that the kernel uses SPTM for address-space allocation.
- Memory-integrity terms. The string "MIE" appears in two contexts ("MIE factor" and "MIE update"), and "MTE" appears in one message about disabling MTE soft mode for ptraced processes. **Verified** for presence.
- PPL terms: about 33 strings, including the name "Page Protection Layer". **Verified** for presence. Whether the PPL code path is active on the A17 Pro is not established, since Apple's platform guide states that SPTM replaces PPL on A15 or later (C-013).
- Terms for KIP, fast permission restrictions and SCIP were searched for and not found as strings. **Verified** for absence of those strings only.

## What was not checked

- Whether MIE, MTE or any other tagging mechanism is active on the A17 Pro. Apple names Memory Integrity Enforcement for A19 and later (C-011, C-012). The presence of MIE strings in this build does not show activation on this device (C-084).
- The behaviour of the pmap, SPTM and PAC code paths. No function was reviewed.
- Whether a memory-protection mechanism can be bypassed. This summary makes no claim about that.

## Status

- Presence of the PAC, pmap and SPTM-related interface strings: **verified**.
- Presence of MIE and MTE strings: **verified**. Activation on the A17 Pro: **not established**.
- Presence of PPL terms: **verified**. Whether PPL is active on the A17 Pro: **not established**.
- Protection behaviour and effectiveness: **not analysed**.
