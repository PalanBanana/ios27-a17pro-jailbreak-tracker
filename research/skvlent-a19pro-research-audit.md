# SKVLENT iOS 27 research repository: evidence audit (v0.4.0)

**Status:** documentation audit at a fixed commit. Every technical result below is the repository's own statement. This tracker has not reproduced any of them, and no result is verified for the A17 Pro. Data as of 2026-11-12. Readiness remains **LEVEL 0 / NO-GO**.

This page does not reproduce any procedure, probe, payload or measurement parameter from the repository. It records what the repository states, how it classifies its own findings, what it does not claim, and where its documents disagree.

## 1. Identity and scope of this audit

| Item | Value |
|---|---|
| Repository | [SKVLENT/iOS27-Research-Exploits](https://github.com/SKVLENT/iOS27-Research-Exploits) (public) |
| Audited commit | [`73f7a579ce91`](https://github.com/SKVLENT/iOS27-Research-Exploits/tree/73f7a579ce91) on `main`, committed 2026-11-12 00:50:18 UTC |
| History | 925 commits; the earliest is dated 2026-10-30 |
| Releases and tags | None |
| Licence | GitHub metadata says "Other". The LICENSE file states: documentation and original analysis © SKVLENT, released for educational use. Firmware, symbol names and Apple trademarks belong to Apple |
| Attribution form used | SKVLENT, iOS 27 Research — Exploits, the repository URL above |

**Read in full:** LICENSE, CREDITS.md, the README's purpose-and-scope and tested-configuration sections, the STATUS verdict table and its kernel and jailbreak sections, `research/CONCLUSIONS.md` (a summary of four lines, written in Russian), and `docs/27.2.md` (method). **Read in part:** the README's direction list, and the opening paragraphs of the 17 direction folders. **Commit history:** the subjects of the most recent 40 commits.

**Not reviewed in depth, deliberately.** Several direction folders (including the patch-diff, physical-primitives, Brotli path and open-work pages) and their session logs contain exploit-development material. That content is operational, so this audit records only the verdict labels stated in the STATUS table.

**Not done.** No probe, bench app or tool from the repository was built or run. No device was used. No firmware binary, dyld cache or kernelcache from the repository was downloaded or examined. The open-work page's "what to do next" list is not followed, and nothing in it is a plan for this project.

## 2. Configurations the repository states

| Configuration | Source statement | Status in this audit |
|---|---|---|
| iPhone18,1 (iPhone 17 Pro), A19 Pro (T8150), iOS 27.0.1 (24A446), arm64e | README table; STATUS "Last measurements": every verdict "was produced on" this configuration | Primary. Not the tracker's target |
| iPhone17,2 (iPhone 16 Pro Max), A18 Pro, iOS 27.2 (24B119) | README tested-configuration table: directions 01–07 "reproduce"; the direction 04 temporal-layer trigger "no longer panics" | Secondary. Reproduction statement by the same author |
| 27.2 (24B119) and 27.2.1 (24B156) | Static comparison only (README; direction 15; direction 16) | Comparison artefacts |
| Tracker target: iPhone16,2, A17 Pro, 27.0.1, 24A446 | Not tested by the repository | Not established |

The repository states its own limits: one configuration, results "must not be carried over to other SoCs or OS versions without verification", and "the absence of a finding here does not mean the absence of a vulnerability".

## 3. Evidence classes

The repository's STATUS page uses three verdicts: **Demonstrated** (reproduced on the device, with the log in `research/`), **Partially demonstrated** (the first step is reproduced, the step that would matter is not), and **Not demonstrated** (a measurement statement, not a claim of impossibility). The task's four categories are mapped as follows. Where a repository states a result with a log, it is recorded as runtime-log evidence (L). Static readings are recorded as binary-analysis evidence (B). Readings of source-level or specification text are recorded as source or specification evidence (I). Hypotheses are recorded as (G).

For each finding this audit records three different things: the **repository statement** (what SKVLENT says), the **technical result** (whether the reported measurement is shown to hold, which the tracker has not checked), and the **A17 Pro status** (none).

## 4. Findings

Answers are the repository's own, or "not stated" where the repository does not say. "No" means the repository states that the event did not happen.

| Dir | Repository verdict | Evidence class (as stated) | Other process crossed | Other app's container accessed | Kernel memory accessed | Kernel privilege obtained | Persistence shown | Full jailbreak | Independently reproduced | A17 Pro status |
|---|---|---|---|---|---|---|---|---|---|---|
| 01 IOSurface size validation | Demonstrated (accepted, inert) | L | No (no extra memory mapped; consumer does not act on the value) | No | No | No | No | No | Author re-run on two sessions; no third party | Not tested |
| 02 Metal GPU virtual address | Partially demonstrated | L | No (same GPU context only) | No | No | No | No | No | None recorded by a third party | Not tested |
| 03 mediaplaybackd / FigXPC | Demonstrated (protocol; daemon crash; CVE-2026-112706 reproduced) | L | Not stated as a process crossing; a protected library file read and a directory descriptor obtained | No | No | No | No | No | None recorded by a third party | Not tested |
| 04 AppleAVE2 | Partially demonstrated | L | No | No | No | No | No | No | None recorded by a third party | Not tested |
| 05 ANE reachability | Not demonstrated | L | No | No | No | No | No | No | n/a | Not tested |
| 06 AppleM2ScalerCSCDriver | Not demonstrated | L | No | No | No | No | No | No | n/a | Not tested |
| 07 Container path disclosure | Demonstrated (paths disclosed; contents denied) | L | No | No (paths only) | No | No | No | No | None recorded by a third party | Not tested |
| 08 Image parser (AppleJPEGDriver) | Not demonstrated (client never open) | L | No | No | No | No | No | No | n/a | Not tested |
| 09 External leads | Not demonstrated (closed) | L | No | No | No | No | No | No | n/a | Not tested |
| 10 Sandbox escape to other containers | Demonstrated | L | **Yes** (reads and writes in other applications' containers and in shared system groups) | **Yes** (stated) | No | **No** ("not kernel code execution, not root") | Not stated | **No** | None recorded by a third party | Not tested |
| 11 HID property writes | Demonstrated (denial of service) | L | Affects a system process (aborts a UI daemon); no access gained | No | No | No | No (device recovers after restart) | No | None recorded by a third party | Not tested |
| 12 AppleKeyStore interface | Partially demonstrated (interface only) | L | No | No | No | No | No | No | n/a | Not tested |
| 13 CoreGraphics PDF shading | Demonstrated (a document-controlled value influences a memory write; the repository states that reaching anything reachable was "demonstrated not to happen") | L and I | No | No | No | No | No | No | n/a | Not tested |
| 14 CoreGraphics CMap | Not demonstrated (parser reached, copy not reached) | L and I | No | No | No | No | No | No | n/a | Not tested |
| 15 CoreGraphics fix diff | Demonstrated (static, own diff) | B | No | No | No | No | No | No | n/a | Not tested |
| 16 Brotli block-switch | Demonstrated for the fix difference; the write is **not demonstrated** | B | No | No | No | No | No | No | None recorded by a third party | Not tested |
| 17 Brotli consumers | Read demonstrated (over-read on the device); write only locally | L | Memory disclosure inside the consumer process; no other process reported | No | No (userland) | No | No | No | None recorded by a third party | Not tested |

Later additions in STATUS (the 2026-11-11 snapshot) are reflected in the rows above: the HID result was corrected, and direction 17's earlier figure was withdrawn (section 6).

## 5. Security categories kept separate

The repository's own results fall into different categories, and this audit keeps them apart, as the task requires. None of them is a generic "exploit successful" verdict.

- **Sandbox boundary crossing:** direction 10 (other applications' containers and shared groups, read and write); direction 03 (a protected library file and a directory descriptor, read through a system service). These are boundary observations in userland. The repository states that direction 10 is "a capability, not a bug hunt".
- **Information disclosure:** direction 07 (path names only); direction 03 (descriptor); direction 17 (memory beyond a decoded buffer, inside the consumer process).
- **Denial of service:** directions 04 and 11, and the daemon crash in direction 03. These are availability results, and the repository states that some probes can panic the kernel or reboot the device.
- **GPU memory behaviour:** direction 02 (same context only) and direction 01 (accepted but inert allocation).
- **Kernel memory access:** none demonstrated. The repository states "kernel read/write … not demonstrated on this configuration".
- **Privilege escalation:** none demonstrated. The STATUS jailbreak section states that the direction 10 escape "does not give kernel code execution, root, or the ability to run unsigned code outside the sandbox".
- **Persistent execution and full jailbreak:** none demonstrated. The STATUS page states "a jailbreak was not demonstrated".

## 6. Superseded, withdrawn and contradictory statements

### 6a. Withdrawn or corrected by the repository itself

| Item | What changed | Where stated |
|---|---|---|
| Direction 08 entitlement reading | Withdrawn on 2026-11-10: the driver does not build the value once read as a permission code, which is a "not open" status | STATUS row 08 |
| Direction 17 earlier figure | An earlier byte count was measured past the output buffer and is withdrawn; per-call accounting replaces it | STATUS row 17; commit subjects of 2026-11-12 |
| HID result | Corrected: the effect is a single string written into one property aborting the daemon, "not a volume effect" | STATUS, 2026-11-11 snapshot |
| Scaler closure | A closure from earlier testing is described as "a mistake in our own testing" | research folder 15 README |
| Direction 01 header-region reading | A field once read as a header-region value is a constant of the resource base | STATUS row 01 |
| F1 proof of concept (credited work) | The header value is a number in the response, not a mapped window; the cross-object access occurs with a plain buffer, so F1 is not its cause | CREDITS.md |

### 6b. Contradictions between the repository's own documents

1. **Build number of the second device.** `docs/27.2.md` says the second device runs "27.2 (24B115)". The README and STATUS say 27.2 (24B119). The two cannot both be right for the same device; the audit records the conflict and does not resolve it.
2. **Directive 03 on the A18 Pro.** The README's tested-configuration table says directions 01–07 "reproduce" on 27.2 (24B119). The same repository's CREDITS table lists CVE-2026-112706 as fixed in 27.2, and STATUS reproduces the same CVE on 27.0.1. Whether the 27.2 result reproduces the fixed behaviour is not stated. **Unresolved.**
3. **Applicability inference.** The open-work page says that CVE-2026-112705 is "fixed in 27.2, so open on this device" (27.0.1). Apple's advisory text does not state affected versions (tracker claim C-047). The inference is recorded here as an inference, **not established**.
4. **Patch-difference statement.** The repository states that the 27.0.1 and 27.2 copies of one decoder routine differ in a status check, and that "the device we measure on carries the vulnerable code by construction". That is the repository's static comparison. The tracker has not checked it and does not infer any vulnerability in 24A446 from a later build's difference.
5. **Scope nuance (not a contradiction).** STATUS says every verdict was produced on the A19 Pro configuration. The README says directions 01–07 "reproduce" on the A18 Pro. Reproduction on a second device is not the same as production there; the audit records both statements as they stand.

## 7. What the repository does not show for the target

- No measurement was made by the repository on iPhone16,2 (A17 Pro) or on build 24A446 of that device.
- The A19 Pro and A18 Pro results cannot be transferred to the A17 Pro. Component-level differences between the three configurations are recorded in the [compatibility matrix](../reports/a17pro-compatibility-matrix.md).
- The repository's own statement, that absence of a finding does not mean absence of a vulnerability, applies in both directions.

## 8. Attribution and licence compliance

- Quotations are limited to short phrases from the repository, with attribution. No code or documentation has been copied into this tracker.
- The repository credits other projects: F1OOB-PoC (IOSurface), cinder27 and ave27 (AppleAVE2 and mediaplaybackd), AppleResearch (sandbox and CoreGraphics leads), worse_query and bad_query (container paths), and GestaltX (MobileGestalt). This audit names the projects and their URLs, and it does not name individual authors.
- The repository's licence permits reading, quoting with attribution, and forking with attribution. It does not permit republication as one's own work, or presenting its measurements as a working exploit, a jailbreak or a vulnerability disclosure. This audit does none of the last three.

## 9. Claims recorded

Repository statements and technical results are recorded separately in `data/claims.json`: C-108 to C-118 for this repository. "Verified" in those claims means only that the repository makes the stated statement at the audited commit. Technical results are recorded as unverified or partially verified.

## 10. What this audit does not establish

- Kernel read or write, an SPTM bypass, a privilege escalation, or a jailbreak on the target.
- Any applicability of the A19 Pro or A18 Pro results to the A17 Pro.
- Whether any reported measurement reproduces on any device other than the author's.

Readiness is unchanged: LEVEL 0, NO-GO.
