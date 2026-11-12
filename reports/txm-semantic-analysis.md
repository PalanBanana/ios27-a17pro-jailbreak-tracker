# Ghidra static analysis: TXM semantic review, iOS 27.0.1 (build 24A446)

**Status:** function-level structure, call-structure counts and interface-string categories are verified. Behaviour and enforcement logic are not analysed. Data as of 2026-11-12. Target: iPhone 15 Pro Max (A17 Pro, `iPhone16,2`), iOS 27.0.1, build 24A446. Offline and static. The analysis used a read-only copy of the project.

Provenance (container, digests, encryption), the segment layout and the analysis summary are in [ghidra-txm-analysis.md](ghidra-txm-analysis.md). They are not repeated here. This page adds the function-level and call-structure counts and the interface-string categories. The kernel-side evidence of TXM interfaces (C-083) is in the public TXM summary.

This page does not describe how the TXM enforces anything, and it does not assess any bypass. The companion SPTM review is [sptm-semantic-analysis.md](sptm-semantic-analysis.md).

Claims: C-081 (container), C-083 (kernel strings), C-103 (indirect control flow), C-105 and C-106 (documentation).

## 1. Functions and incoming references (verified: read-only Ghidra export)

| Measure | Value |
|---|---|
| Functions | 1,654 (1,653 with default names, and `entry`) |
| Thunk functions | 45 |
| Functions with at least one incoming call or jump reference | 1,167 |
| Functions with none | 487 |
| Instructions decoded by Ghidra | 74,071 |

The 487 functions without an incoming reference are not reviewed. Their count does not show that any of them is unused.

## 2. Call structure (counts only)

| Reference or encoding | Ghidra's reference model | Byte-level decoder (upper bound) |
|---|---|---|
| Direct call | 4,721 references | 4,546 encodings |
| Direct jump or branch | 9,653 references | 2,504 encodings |
| Register-indirect call | **none recorded** | 279 encodings |
| Register-indirect branch | **none recorded** | 87 encodings |
| Return | not counted | 1,521 encodings |
| Distinct direct-call targets | not counted | 1,106 (all inside executable segments) |
| Data references | 12,688 | not counted |

- Calls are mostly direct. The two methods disagree on register-indirect control flow: Ghidra records none, and the decoder finds 279 call and 87 branch encodings. The disagreement is not resolved (C-103). The decoder counts every aligned word in an executable segment, so its counts are upper bounds. Ghidra decodes 74,071 instructions against the decoder's 90,112 words.
- The TXM has more distinct call targets (1,106) than the SPTM (294). This is a count and nothing more.
- No conclusion about what any call target does is drawn from these counts.

## 3. Interface strings (presence only)

The printable strings of six or more characters number about 1,100, and Ghidra counts 797 defined string items. Grouped by category:

| Category | Distinct strings (approximate) | What the strings show |
|---|---|---|
| Names that mention TXM or SPTM | 19 | Log prefixes and module names |
| Trust and entitlement terms | 26 | Messages about loading trust caches, and entitlement names used in that context |
| Assertion and panic text | 38 | Panic and assertion templates for nonce, digest, property, chip-definition and iteration conditions |
| Page-table and pmap terms | 15 | Messages about page enforcement and executable mappings |
| ASID and address-space terms | 2 | A message about initialising an ASID table, and one about the shared page for the secure channel |
| Thread and context terms | 2 | Messages about panics on thread stacks |

The listed matches (capped at 60 in the export) include trust-cache messages, entitlement names for loading and unloading trust caches (kept in the local listing), panic and assertion templates, and a message about the image-verification module's version and build metadata.

The strings show that these conditions and interfaces exist in this build. They do not show how the code handles them. No function was reviewed.

## 4. Documentation

Apple's Platform Security guide states that TXM is designed to work with SPTM, and that TXM enforces code-execution policy at a lower privilege level (see the SPTM review, C-105). The guide's MIE passage names A19 and M5 processors or later (C-106). The guide does not describe the TXM's behaviour on any particular chip.

## 5. What this review does not establish

- The TXM's enforcement logic. Apple's guide describes SPTM and TXM as working together to protect page tables. That statement is general, and this review adds no detail to it.
- Any relationship between this image and the reported SPTM bypass, which is second-hand and unverified (C-051).
- Whether the TXM behaves the same way on the A17 Pro as on other devices.
- Any vulnerability in the TXM. No function was reviewed for correctness or security.

## 6. Status

| Question | Status |
|---|---|
| Image present, unencrypted, and matching its normal manifest digest | Verified (C-081; see the public TXM summary) |
| Function counts, incoming references and analysis without errors | Verified (tool output) |
| Call-structure counts for Ghidra's reference model | Verified |
| Indirect control flow: the two methods disagree | Unresolved (C-103) |
| Kernel-side strings referring to TXM interfaces | Verified for presence (C-083) |
| TXM behaviour and enforcement logic | Not analysed |
| Relationship to the reported bypass | Not established |
| Activation on the A17 Pro with iOS 27.0.1 | Not established |

Readiness is unchanged: LEVEL 0, NO-GO.
