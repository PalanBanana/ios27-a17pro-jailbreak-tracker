# Ghidra static analysis: kernel symbolication, iOS 27.0.1 (build 24A446)

**Status:** partially verified. Data as of 2026-11-12. Target: iPhone 15 Pro Max (A17 Pro, `iPhone16,2`), iOS 27.0.1,
build 24A446. Offline and static. No device was connected or operated on.

This page records how the kernel's function names were recovered, how well the recovered names can be checked, and
what was applied. It does not describe what any function does, and it does not assess any vulnerability. Names,
addresses and symbol listings are kept by the maintainer and are not published. Counts are given below.

Claims: C-097 (signature range), C-098 (anchor presence), C-099 (conflicts), C-100 (cross-check).

## 1. Inputs

- **Kernelcache.** The decompressed release kernel from the 24A446 package (S-043). It is a fileset of 264 entries,
  darwin 27.0.0. Its hash was checked before and after every tool run; no run changed it.
- **Tools.** ipsw 3.1.739 (built-in symbolication, table commands); Ghidra 12.1.2 (headless).
- **Signature set.** The `kernel/27.0` folder of the symbolicator repository (S-046). The repository is MIT-licensed. Its
  README says the signatures were generated with IDA from kernel debug kits.
- **Ghidra script.** The official symbolicator script (MIT). It was read in full before any use. It reads a JSON map
  of address to name and creates or renames functions. It makes no network call and starts no external process. It was
  not installed. A headless variant, with one changed line (a path argument in place of a file dialog), was run on a
  project copy.
- **Other repository.** The ipsw skill package (MIT) was reviewed for its file layout only. It was not installed or run.

## 2. Built-in symbolication (no external signatures)

- The built-in pass produced a map of **13,798** entries. By segment: 6,455 in `__DATA_CONST`, 3,240 in `__DATA`,
  4,103 in `__TEXT_EXEC`.
- Table-derived names from the same tool: 558 syscall-table entries (441 distinct implementation addresses; two
  shared placeholder groups), 128 Mach-trap entries (65 placeholders), 18 MIG subsystems with 354 routines, and 3,239
  C++ classes.

## 3. The signature set and version compatibility

| Check | Result |
|---|---|
| Declared total, and entries present | 6,626 declared; 6,511 present |
| Declared darwin range | 27.0.0 to 27.2.0. This kernel is 27.0.0, inside the range (C-097) |
| Anchor strings present in this kernelcache | 11,317 of 14,189 distinct xnu anchors (79.8%); 4,714 of 6,003 signatures with anchors have all of them (C-098) |
| KEXT signature files | 773; all declare ranges that include 27.0.0. Their anchors are present for 98.1% of the 196 fileset entries that received names |

The declared total does not match the file's entry count (115 entries fewer than declared). The cause is not known.

## 4. Matching results

- The tool's own counter reports 4,920 matched of 6,511 (75.56%). The log records **5,320** distinct signature names at
  **4,257** kernel addresses. The counter's definition is not documented, so the two figures are not reconciled.
- Matched fractions by the signature's provenance label, using the log: direct 3,829 of 4,667 (82.1%); weak
  string plus callee 719 of 822 (87.5%); dual evidence 421 of 514 (81.9%); propagated 351 of 508 (69.1%). The labels'
  meanings are not documented upstream, so these are reported as labels only.
- Among the 5,320 matched names: all anchors present for 4,670; one or more anchors missing for 299; no anchors for 351.
- KEXT signatures named 196 fileset entries, with 30,527 log entries in total.

## 5. Internal consistency: the main caution

- **1,160** kernel addresses carry more than one signature name. For **1,139** of them the names belong to different
  families, after normalising constructor and destructor variants and cold-split suffixes (C-099).
- 400 of the conflicts involve only names labelled "direct". The strongest label does not resolve them.
- The tool's JSON output keeps one name per address and drops the rest. The log is the complete record, and the
  conflict counts above come from the log.

## 6. Checks against independent references

- Table-derived names and signature names at the same address (syscall and Mach-trap tables): **58** comparable
  addresses, **55** in agreement (94.8%). The 95% interval is 85.9% to 98.2% (C-100). The sample is small and is
  biased toward functions that the signatures found, so this rate does not establish accuracy for other names.
- Coverage: 54 of 441 syscall addresses and 4 of 63 Mach-trap addresses have any signature name. No MIG routine has one.
- Built-in names agree with signature names at 53 of 58 shared addresses. These samples overlap, so they are not
  independent evidence.
- C++ class prefixes: 656 of 681 checkable mangled kernel signature names (96.3%) have a class present in the built-in
  list. This is a consistency check, not a correctness check.

## 7. What was applied

- **Criteria.** One logged name at the address; the name is unique to that address; its provenance label is "direct"
  only; and every anchor string is present in this kernelcache. Result: **2,346** names.
- **Where.** A copy of the analysis project, never the original. The copy was saved.
- **Result.** 2,316 names applied, all to functions that already existed (no functions were created). 30 failed
  because the analysis has no decodable function at those addresses. Those 30 matches have no support in the
  disassembly.
- The applied names are signature-derived and unverified. They are for navigation only and are not findings.

## 8. Decision on the full signature set

The full set of 5,320 names was **not** applied. At least one name at each of the 1,139 conflicting addresses is
wrong, unless the pair is a true alias. No per-name accuracy estimate exists, so applying the full set would assert
names the evidence does not support.

## 9. Status

| Question | Status |
|---|---|
| Built-in symbolication produced a map of 13,798 entries | Verified |
| Signature set declared range covers this darwin version | Verified (declared range) |
| Anchor strings present in this kernelcache | Verified (C-098) |
| Accuracy of individual signature names | Unresolved |
| Conflicting names at 1,139 addresses | Verified (C-099) |
| Agreement with table-derived names (58 addresses) | Partially verified (C-100) |
| Conservative subset applied to a project copy | Verified |
| Reconciliation of the tool's counter (4,920) with the log (5,320) | Unresolved |
| Behaviour or security meaning of any named function | Not analysed |

## 10. Limits

- No ground truth: the matching debug-kit kernel was not used, and the signature method is only partly documented
  upstream.
- The analysis covers darwin 27.0.0 only, inside a declared range of 27.0.0 to 27.2.0.
- The table-derived sample is small. Its agreement rate is not a measure of the full set.
- Readiness is unchanged: LEVEL 0, NO-GO.
