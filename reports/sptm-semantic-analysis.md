# Ghidra static analysis: SPTM semantic review, iOS 27.0.1 (build 24A446)

**Status:** function-level structure, call-structure counts and interface-string categories are verified. Behaviour and enforcement logic are not analysed. Data as of 2026-11-12. Target: iPhone 15 Pro Max (A17 Pro, `iPhone16,2`), iOS 27.0.1, build 24A446. Offline and static. The analysis used a read-only copy of the project.

Provenance (container, digests, encryption), the segment layout and the analysis summary are in [ghidra-sptm-analysis.md](ghidra-sptm-analysis.md). They are not repeated here. This page adds the function-level and call-structure counts, the interface-string categories, and the kernel-side reference methods.

This page does not describe how the SPTM enforces anything, and it does not assess any bypass. The companion TXM review is [txm-semantic-analysis.md](txm-semantic-analysis.md).

Claims: C-081 (container), C-083 (kernel strings), C-085 and C-104 (kernel-side references to `__DATA_SPTM`), C-103 (indirect control flow), C-105 and C-107 (documentation), C-051 (reported bypass, second-hand).

## 1. Functions and incoming references (verified: read-only Ghidra export)

| Measure | Value |
|---|---|
| Functions | 530 (529 with default names, and `entry`) |
| Thunk functions | 15 |
| Functions with at least one incoming call or jump reference | 326 |
| Functions with none | 204 |
| Instructions decoded by Ghidra | 82,915 |

The 204 functions without an incoming reference are not reviewed. Their count does not show that any of them is unused.

## 2. Call structure (counts only)

| Reference or encoding | Ghidra's reference model | Byte-level decoder (upper bound) |
|---|---|---|
| Direct call | 3,554 references | 3,458 encodings |
| Direct jump or branch | 9,386 references | 2,348 encodings |
| Register-indirect call | **none recorded** | 83 encodings |
| Register-indirect branch | **none recorded** | 7 encodings |
| Distinct direct-call targets | not counted | 294 |
| Data references | 20,270 | not counted |

- Calls are mostly direct. The two methods disagree on register-indirect control flow: Ghidra records none, and the decoder finds 83 encodings. The disagreement is not resolved (C-103). The decoder treats every aligned word in an executable segment as an instruction, so its counts are upper bounds.
- No conclusion about what any call target does is drawn from these counts.

## 3. Interface strings (presence only)

The printable strings of six or more characters number about 2,700. Grouped by category:

| Category | Distinct strings (approximate) | What the strings show |
|---|---|---|
| Names that mention SPTM or TXM | 261 | Log prefixes and names of operations |
| Page-table and pmap terms | 70 | Messages about table state and page validity |
| Assertion and panic text | 32 | Failure messages and assertion templates |
| ASID and address-space terms | 16 | Messages about address-space identifiers |
| Thread and context terms | 9 | Messages about exception context |
| Trust and entitlement terms | 1 | One message about a trust check |

Ghidra's defined-string count is 2,466. The strings show that these interfaces and their failure messages exist in this build. They do not show how the operations behave. No operation was reviewed.

## 4. Kernel-side references to `__DATA_SPTM` (verified for each method; cause unresolved)

The kernelcache has a 311,296-byte `__DATA_SPTM` segment. Four read-only methods were applied to it.

| Method | Result |
|---|---|
| Ghidra automatic analysis of the kernel program | No code reference recorded (C-085; analysis completed with 17 logged errors) |
| Raw scan of every aligned 8-byte word in the kernelcache | One value falls in the segment's range. It sits in a `__TEXT` segment. No PAC-style candidates |
| PC-relative pairs (`ADRP` with a following add, load or store) | None. The same decoder finds 350,748 page hits in `__DATA_CONST` and 247,224 in `__DATA` |
| 64-bit literal loads | None of 28 reads a value in the segment |
| Constants built from `MOVZ`/`MOVK` sequences | None among 570,910 sequences. The decoder was unit-tested on a synthetic example |

- No method found a code path that addresses the segment (C-104). The one raw value is not loaded by any decoded literal instruction.
- A null result from these methods does not show that the segment is unused. The methods do not cover every encoding. Accesses through other mappings, through the SPTM side, or through the interface have not been tested.

## 5. Documentation

Apple's Platform Security guide states that SPTM is supported on A15-or-later and M2-or-later SoCs, and that SPTM with TXM replaces the PPL on those SoCs (C-105, which re-reads the source of C-013). The feature table has an "A15-A18" column whose cells are images in the fetched copy (C-107). The A17 Pro is in range by generation, but no cell value was read. The full reading is in [a17pro-memory-protection-analysis.md](a17pro-memory-protection-analysis.md).

The reported SPTM bypass is second-hand and unverified (C-051). Nothing in this review tests or supports it.

## 6. What this review does not establish

- The SPTM's enforcement logic, or how it handles page tables.
- Any relationship between this image and the reported bypass.
- Whether the SPTM is active on the A17 Pro with this build. Activation is not established.
- Any vulnerability in the SPTM. No function was reviewed for correctness or security.

## 7. Status

| Question | Status |
|---|---|
| Image present, unencrypted, and matching its normal manifest digest | Verified (C-081; see the public SPTM summary) |
| Function counts, incoming references and analysis without errors | Verified (tool output) |
| Call-structure counts for Ghidra's reference model | Verified |
| Indirect control flow: the two methods disagree | Unresolved (C-103) |
| Interface strings: presence | Verified |
| Kernel-side code references to `__DATA_SPTM` | Not found by four methods; cause unresolved (C-104) |
| SPTM behaviour and enforcement logic | Not analysed |
| Relationship to the reported bypass | Not established |
| Activation on the A17 Pro with iOS 27.0.1 | Not established |

Readiness is unchanged: LEVEL 0, NO-GO.
