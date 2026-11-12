# Ghidra static analysis: standalone KEXT import failure and KEXT inventory reconciliation, iOS 27.0.1 (build 24A446)

**Status:** the import failure's mechanism is verified. Why the fileset load does not raise the same exception is
unresolved. The inventory reconciliation is verified. Data as of 2026-11-12. Target: iPhone 15 Pro Max (A17 Pro,
`iPhone16,2`), iOS 27.0.1, build 24A446. Offline and static. No device was connected or operated on.

This page concerns the import path only. It does not analyse any KEXT's code, and it does not assess any
vulnerability. The original firmware files were not modified. One diagnostic copy was altered to test the mechanism;
it is not used for any result.

Claims: C-101 (import mechanism; extends C-086), C-102 (reconciliation), C-086 (standalone files have empty symbol tables).

## 1. Question

Why does Ghidra's Mach-O loader fail on the standalone KEXT files extracted from the kernelcache, and does the failure
depend on how those files were extracted?

## 2. Reproduction

- Tool: Ghidra 12.1.2 DEV, headless import, with analysis switched off so that only loading is tested.
- Work was done in a separate probe project, not in the analysis project.
- Inputs: byte-identical copies of the standalone files. The originals were hashed before and after; they were unchanged.
- Result: all eight standalone files (and a `--noimports` variant of one) fail with `Import failed`. The headless
  process still exits with status 0, so the log must be read to see the result.

## 3. Failure location

- The root exception is an index-out-of-bounds error (index 0 on an empty list). It is raised while the loader
  processes stub entries: it reads a symbol for each indirect-symbol entry, and the symbol table has no entries.
- The stack trace's frame in the outer loader method is a wrapper that rethrows the cause. It is the reporting site,
  not the cause.
- By reading the loader's bytecode (Ghidra 12.1.2 `Base.jar`), the stub step is called unconditionally during the build.
  It returns early only if the file has no dynamic symbol table or no indirect-symbol list. Neither holds for these files.

## 4. Mach-O table counts (verified)

| Measure | Standalone files | Same entry inside the kernelcache |
|---|---|---|
| Symbol count | 0 | 0 |
| Indirect-symbol count | 13 to 1,175 per file | identical |
| Indirect-symbol values | all 0, which is out of range for an empty table | identical |
| String-table size | 8 bytes | 1 byte |

- All 264 fileset entries, including the kernel entry itself, have empty symbol tables. The release kernel's own symbol
  table is empty, so symbol names are not present in the binary (consistent with the symbolication result).
- The extraction preserves symbol counts and indirect-symbol values. It rewrites the string table, which grows from
  1 byte to 8 bytes. That rewrite does not explain the failure.

## 5. Diagnostic experiment

- A copy of one standalone file was altered in one field only: its indirect-symbol count was set to zero.
- The copy imports successfully. The original still fails.
- Conclusion: the failing step is the stub processing. The empty symbol table on its own does not stop the import.
  The indirect-symbol references do.
- The altered copy was used only for this test. It is not an analysis result and is not published.

## 6. Inventory reconciliation (verified)

The tool's KEXT inventory lists 281 records. The kernelcache fileset has 264 entries.

| Category | Count | Basis |
|---|---|---|
| Fileset-backed | 263 | Identifier matches a fileset entry, and the load address equals the entry's header address |
| Codeless | 11 | No executable field and a sentinel load address. Personality or interface bundles (C-102) |
| Pseudo-KEXT | 7 | Kernel-programming-interface records (`com.apple.kpi.*`) with an executable field naming a kernel component and no fileset entry |
| Alias | 0 | No two fileset-backed records share a load address |
| Duplicate | 0 | No identifier is listed twice |
| Other | 1 (fileset-only) | The kernel image entry, which has no inventory record |
| Unresolved | 0 | None |

- Records outside the fileset are **not** treated as missing firmware components. Codeless and interface bundles are
  expected to have no fileset entry.
- Two display names are shared by two records each. In each pair the identifiers differ, and the fileset entries differ.

The full per-record classification is published as `analysis/kext-reconciliation.json`.

## 7. What is not established

- Why the fileset load does not raise the stub exception. The fileset path was not traced, and the import result is an
  observation, not an explanation.
- Whether the indirect-symbol references are intended by the build's linker. No source for that was available.
- Whether the same failure occurs in other Ghidra versions.
- Anything about the code of any KEXT.

## 8. Consequences for the analysis

- Standalone KEXT files are not imported. KEXT-level analysis uses the fileset program, which imported all 264 entries.
- The originals were not modified, and no workaround was applied to them.
- The headless exit status must not be read as success. A log check is required.

## 9. Status

| Question | Status |
|---|---|
| Standalone files fail to import (8 of 8, plus a variant) | Verified |
| Mechanism: stub processing reads symbols from an empty table | Verified (C-101) |
| Empty symbol tables in the release kernelcache | Verified |
| Extraction preserves symbol and indirect-symbol counts | Verified |
| Fileset path does not raise the same exception | Observed; mechanism unresolved |
| Inventory reconciliation categories | Verified (C-102) |

Readiness is unchanged: LEVEL 0, NO-GO.
