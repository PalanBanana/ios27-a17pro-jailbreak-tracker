# A17 Pro memory protection: documentation, evidence and limits (iOS 27.0.1, build 24A446)

**Status:** documentation read and the activation question assessed. Presence is verified in the existing report. Implementation and activation on the target are **not established**. Data as of 2026-11-12. Target: iPhone 15 Pro Max (A17 Pro, `iPhone16,2`), iOS 27.0.1, build 24A446. Offline and static. No device was involved.

This page adds the documentation reading and the activation assessment. It does not repeat the presence analysis, which is in [ghidra-memory-protection.md](ghidra-memory-protection.md). The kernel-side references to `__DATA_SPTM` are in [sptm-semantic-analysis.md](sptm-semantic-analysis.md), section 4.

Each mechanism is judged on four separate questions. Presence of a string or a header flag is not evidence of implementation. Implementation is not evidence of activation on a given device.

1. **Documentation:** what Apple's Platform Security guide says (S-004, re-read 2026-11-12; the page shows a published date of January 28, 2026).
2. **Presence:** whether the 24A446 kernelcache or monitor images contain the mechanism's strings or header flags.
3. **Implementation:** whether a code path has been reviewed. Only SPTM and TXM structure and call counts were reviewed.
4. **Activation on iPhone16,2:** whether build evidence shows the mechanism is on for this device.

Labels: **Verified**, **Partially verified**, **Unresolved**, **Not analysed**, **Not established**.

## 1. Documentation as read (verified text; table cells not readable)

- **SPTM.** The guide states that the Secure Page Table Monitor is supported on A15-or-later and M2-or-later SoCs. On those SoCs, SPTM with TXM replaces the Page Protection Layer (C-105).
- **Feature table.** The table has a column headed **A15-A18**, which includes the A17 generation. Its cells are images in the fetched copy, so support marks in that column could not be read (C-107).
- **TXM.** The guide describes TXM as designed to work with SPTM, and as enforcing code-execution policy at a lower privilege level.
- **MIE.** The guide states that Memory Integrity Enforcement is available on A19 and M5 processors or later. The A17 family is not named in that passage (C-106).
- **MTE and EMTE.** The guide describes them alongside MIE. Per-chip support is in the image-only table.
- **Fast Permission Restrictions.** The guide says a new hardware primitive of this kind was introduced starting with the A11 Bionic and S3 SoCs.
- **Pointer authentication.** The guide has a "Pointer Authentication Codes" row whose cells are images. The text does not name the chip generation that introduced PAC.

## 2. Mechanism-by-mechanism status

| Mechanism | Documentation | Build-level evidence | Implementation reviewed | Activation on iPhone16,2 |
|---|---|---|---|---|
| SPTM | Supported on A15-or-later SoCs (text); A17 is in the A15-A18 column (cells unreadable) | Interface strings (C-083); monitor image present and unencrypted (C-081); `__DATA_SPTM` segment (see the SPTM review) | Monitor structure and call counts only | **Not established.** The documentation covers the generation; build evidence does not show activation |
| PPL | Replaced by SPTM with TXM on A15-or-later SoCs (text) | PPL-related strings present, including "Page Protection Layer" (see the presence report) | Not reviewed | **Not established.** Strings do not show that the PPL code path runs. The documentation, if it applies to this SoC, points to replacement |
| TXM | Works with SPTM and enforces code-execution policy at lower privilege (text) | Monitor image present (C-081); TXM interface strings (see the TXM review) | Structure and call counts only | **Not established** |
| MIE | Available on A19 and M5 or later (text) | "MIE factor" and "MIE update" strings (C-084) | Not reviewed | **Not supported by the documentation for A17**: a negative inference from the stated scope (C-012, partially verified). Strings do not establish activation |
| MTE | Described with MIE; per-chip support not readable | One message about MTE soft mode for traced processes (see the presence report) | Not reviewed | **Not established** |
| PAC | Introducing generation not stated in the text | arm64e subtype bit set in the kernel, SPTM and TXM headers (C-096); PAC failure strings (see the presence report) | Not reviewed | **Not established.** The arm64e subtype shows the code is built for pointer authentication. It does not show enforcement on a device |
| Fast Permission Restrictions | Hardware primitive introduced with A11 and S3 (text) | Terms searched; none found as strings (see the presence report) | Not reviewed | **Not established.** Absence of strings does not show absence of the mechanism |
| KIP and SCIP | Not checked in the fetched excerpt | Terms searched; none found as strings (see the presence report) | Not reviewed | **Not established** |

## 3. Reading the documentation against the build

- **SPTM and PPL.** The guide's generation-level statement ("A15 or later") covers the A17 family, and the table header "A15-A18" includes it. The page does not name the A17 Pro explicitly, and its cells cannot be read. The earlier limitation of C-013 ("does not name the A17 Pro") remains literally true, but it understates the range. This is recorded as C-107, and C-013 is cross-referenced rather than changed in verdict.
- Read this way, the documentation says PPL is replaced by SPTM and TXM on the A17 generation. PPL strings in the 24A446 kernel are then consistent with a codebase shared across platforms. They do not show that the PPL path runs on this device. Activation was not verified in the build, on hardware, or in code.
- **MIE.** The guide limits MIE to A19 and M5 or later. That supports the negative inference in C-012. MIE strings in the kernel (C-084) are presence-only evidence and do not show activation on iPhone16,2.
- **PAC.** The arm64e subtype bit in the kernelcache and both monitor headers is a build-level fact (C-096). It means the code is compiled for pointer authentication. It does not establish that pointer authentication is enforced on this device.

## 4. What this does not establish

- How any of these mechanisms is implemented, or how it behaves when it runs.
- Whether any of them is active on iPhone16,2 with build 24A446. No device evidence is available.
- Whether any memory-protection mechanism can be bypassed. The reported SPTM bypass is second-hand and unverified (C-051) and is not evaluated here.
- Whether the A17 Pro is in the SPTM "A15-A18" column in practice. The cells are images and could not be read.

## 5. Status

| Question | Status |
|---|---|
| Documentation text on SPTM, PPL, TXM, MIE, MTE and PAC, read 2026-11-12 | Verified (text read; table cells not readable) |
| SPTM and PPL statements cover the A17 generation by range | Verified text (C-105, C-107); explicit A17 entry not readable |
| MIE stated for A19 and M5 or later | Verified text (C-106); A17 not named (negative inference only, C-012) |
| Presence of SPTM, PPL, MIE, MTE, PAC and FPR strings | Verified for presence (see the presence report; C-083, C-084) |
| arm64e subtype in kernel and monitor headers | Verified (C-096) |
| Implementation of any memory-protection mechanism | Not reviewed (SPTM and TXM: structure and counts only) |
| Activation of any mechanism on iPhone16,2 with 24A446 | **Not established** |
| Bypass or weakness of any mechanism | Not analysed |

Readiness is unchanged: LEVEL 0, NO-GO.

## 6. Limits of the source

- The fetched copy is the Platform Security guide's OS-integrity section. Its feature table is image-only in the text extraction, so no per-chip cell values are available from the text.
- The MIE section links to a separate Apple Security Research post, which was not fetched for this record.
- The page may have been updated since its published date.
