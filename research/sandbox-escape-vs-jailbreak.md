# Sandbox escape versus full jailbreak (v0.4.0)

**Status:** conceptual and documentation-level. It describes the layers that separate a sandbox escape from a jailbreak, and it attributes each capability to the project that states it. It contains no procedure, and it describes no mechanism beyond what the cited sources state. Data as of 2026-11-12. Readiness remains **LEVEL 0 / NO-GO**.

## 1. Why the terms are not interchangeable

- A **sandbox escape** crosses a boundary between a restricted process and something it should not reach, such as another application's data or a shared group. It does not, by itself, give privileged code execution.
- A **kernel read or write** primitive gives access to kernel memory. It does not, by itself, defeat code signing or the monitors that enforce it.
- An **SPTM or PPL bypass** defeats the layer that protects page tables and enforces signed code. It does not, by itself, give persistence, a bootstrap or a package manager.
- A **complete jailbreak** combines the enforcement defeats needed for unsigned or privileged code to run, plus a bootstrap, package management and persistence, on a named device and build.
- **Daily-driver stability** is a separate question again. Working once is not stable use.

Each step in that list is a different claim with a different evidence requirement. A result at one step is not evidence for the next.

## 2. The layers

| Layer | What it separates | Where the tracker records it |
|---|---|---|
| App sandbox | A process's permitted operations | Apple's platform security documentation (general); DIM05 |
| Inter-application container isolation | One application's data from another's | DIM05; SKVLENT directions 07 and 10 (repository statements) |
| Shared application groups | Data shared between a set of applications and system groups | SKVLENT direction 10; Erosion's App Group signing caveat |
| GPU context isolation | GPU memory belonging to one context from another | SKVLENT direction 02 (same context only) |
| Kernel privilege separation | Kernel code from user processes | DIM04; Apple's listed kernel entries (C-034 to C-041) |
| Kernel memory protection | Protected kernel memory | Apple's platform guide, PPL and SPTM (C-013, C-105) |
| SPTM | Page tables and signed-code enforcement, on A15-or-later SoCs | C-013; C-105 |
| TXM | Trusted code-execution policy, working with SPTM | C-105; C-106 |
| AMFI and code signing | Whether a binary is allowed to run | CMP-008 (not researched); Apple's guide (C-032) |
| Root filesystem | The sealed system volume | Not researched for the target |
| Bootstrap | The filesystem layout that packages install into | DIM08; the ecosystem update (Procursus, Dopamine) |
| Package manager | Installing and updating packages | DIM08 (Sileo, ElleKit); CMP-011 |
| Persistence | Keeping any of the above across relaunch or reboot | Not established for the target (CMP-006, CMP-007) |

## 3. Capabilities claimed, by project

Each project's statements are kept with that project. No capability is carried across projects.

### 3.1 SKVLENT iOS 27 research (repository statements, A19 Pro, 27.0.1)

- **Demonstrated, per the repository:** a sandbox boundary crossing into other applications' containers and shared system groups (direction 10); a protected library read and a directory descriptor obtained through a system service (direction 03); path-name disclosure with contents denied (direction 07); denial-of-service results (directions 04 and 11); and information disclosure inside a networking consumer (direction 17).
- **Not demonstrated, per the repository:** kernel read, kernel write, kernel code execution, root, unsigned code outside the sandbox, and a jailbreak. The STATUS page states this directly.
- **Source:** [audit](skvlent-a19pro-research-audit.md); repository commit `73f7a57`.

### 3.2 Erosion (declared iOS 26 to 27.2.1)

- **Documented:** a sandbox escape (worse_query), container browsing and modification through a file browser, dialer and wallpaper customisation, and MobileGestalt tweaks.
- **Not documented:** kernel access, root, a bootstrap, a package manager, persistence, or any SPTM or PPL bypass.
- **Source:** [audit](erosion-compatibility-audit.md); README and release notes at commit `585a24a`.

### 3.3 Dopamine (opa334, current release 3.0.13)

- **Documented:** a rootless, semi-untethered jailbreak for listed iOS ranges. The default-branch README lists arm64e devices up to iOS 17.3.1, and no iOS 27 entry.
- **Release-note statements in the tracker's records:** a Titan PPL and SPTM bypass for iOS 16.5.1 to 17.3.1; real-device SPTM support ends at iOS 17.3.1 because no SPTM bypass is known for 17.4 and later (C-065, C-066). These are the project's own statements, recorded as such.
- **Source:** the [ecosystem update](jailbreak-ecosystem-update.md); README at commit `5b1d2c1c3bf5`.

### 3.4 Calif and Hexacon reported demonstration (second-hand)

- **Reported:** an untethered iOS 27.0.1 demonstration on an iPhone 18 Pro (A20 Pro) at a 2026 conference, reported by press and an upstream reference (S-010, S-036, S-037; C-001, C-004, C-027).
- **Not established:** the components, the exploit chain, the target device, or independent reproduction. The reported device is not the tracker's target (CMP-009).

## 4. What the evidence so far separates

- **Userland boundary crossings** (SKVLENT 03 and 10; Erosion's documented container access) are results about boundaries between processes and containers. They do not imply kernel access.
- **Kernel-level results:** none is demonstrated by SKVLENT on the A19 Pro. Apple lists kernel-memory and privilege entries in iOS 27 and 27.2 (DIM05). Apple gives no affected version range for them (C-047), so their applicability to 27.0.1 is not established.
- **Monitor-level results:** none is demonstrated by the repository. The upstream reference reports no publicly usable SPTM or PPL bypass for 27.0.1 (S-026). Dopamine's real-device SPTM support ends at iOS 17.3.1 (C-066).
- **Package-level results:** bootstrap and package-manager support for iOS 27.0.1 on the A17 Pro are not established (CMP-010, CMP-011).

## 5. Misreadings this document guards against

- "Sandbox escape" does not mean "kernel code execution".
- "Kernel read or write" does not mean "SPTM bypass".
- "SPTM bypass" does not mean "complete jailbreak".
- "Complete jailbreak" does not mean "daily-driver stable".
- "A19 Pro demonstration" does not mean "A17 Pro compatibility".
- "Supported version range" does not mean "device compatibility".
- "Apple lists a fix in 27.2" does not mean "27.0.1 was affected". Apple gives no affected version ranges (C-047).

## 6. Status

| Capability | Status for the target (A17 Pro, 27.0.1, 24A446) |
|---|---|
| Sandbox escape | Not established |
| Cross-application access | Not established |
| Kernel read | Not established |
| Kernel write | Not established |
| Privilege escalation | Not established |
| SPTM bypass | Not established |
| Complete jailbreak | Not established |
| Persistence | Not established |

Readiness is unchanged: LEVEL 0, NO-GO.
