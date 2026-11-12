# Next research priorities (v0.4.0)

**Status:** data as of 2026-11-12. Target: iPhone 15 Pro Max (A17 Pro, `iPhone16,2`), iOS 27.0.1, build 24A446. **Readiness: LEVEL 0 / NO-GO.** These priorities are documentary and metadata-level. They do not include any test on any device, any exploit work, any binary-level comparison, or any mapping of a binary to an advisory.

## 1. Scope rules for every priority

- No device is contacted, updated, restored, rebooted or used for research. No firmware is installed.
- No exploit, proof of concept or procedure from any project is run, adapted or reproduced.
- No code-level or binary-level differencing is performed. No binary is mapped to any advisory.
- External results are recorded as the source states them, with their evidence class. A result is not transferred from one SoC to another.
- Each priority records what would change a status, and no priority assumes the answer.

## 2. Priorities, in order

1. **Resolve the four recorded contradictions.** (a) The SKVLENT second-device build (24B115 or 24B119). (b) Whether the SKVLENT direction 03 result on 27.2 is the fixed behaviour or a different one. (c) Erosion's maximum iOS 26 version (26.6.2 or 26.7.2). (d) Erosion's latest commit message about 27.2.1. Each is resolved only by a dated primary statement from the project concerned.
2. **Track Apple's affected-version statements.** Apple's advisories currently give no affected version ranges (C-047). Record any change, and update the advisory-level claims only from Apple's text.
3. **Resolve the chip-token mapping.** The monitor images are named by token (t8122, t8140, t8150), and the A17 Pro's inventory contains T8130 and T8122. Record a mapping only from an authoritative public source. Until then, it stays unresolved (C-124).
4. **Explain the exclave difference in the packages, from public documentation only.** The A18 Pro and A19 Pro manifests list exclave-related components and the A17 Pro manifest does not. Look for Apple's public documentation on which generations use exclaves. Record what it states and what it does not.
5. **Track the iOS 27 support statements of the ecosystem projects.** Dopamine's README and releases (current range: arm64e to 17.3.1), the official ElleKit repository (no version range and no release), and Procursus (no iOS range). Record any change as a dated statement. Do not infer support from a version list.
6. **Track the SKVLENT repository at new commits.** Record changes to its statements, its withdrawn findings, and its licence. Do not reproduce its procedures or its open-work steps.
7. **Keep the metadata comparison current.** When Apple publishes a new build for the target, retrieve its manifest by range request and record component names and digests only.

## 3. What is not a priority

- **The SKVLENT open-work "what to do next" list.** It describes continued exploit development on another device. It is not adopted. Its items are not tracked as tasks for this project.
- **Device testing of any kind**, including on the primary device, including of any tool listed in the ecosystem update.
- **Installing or signing Erosion**, or downloading its IPA.
- **Binary-level differencing between builds**, and mapping any advisory to code. These were declined and remain declined.
- **Upgrading any readiness level** on the basis of an external statement, a version list, or a second device.

## 4. What would change the target's status

| Status | What would change it | Readiness scale step it would bear on |
|---|---|---|
| Sandbox escape or cross-application access (A17 Pro) | A dated, independently checkable result on the exact device and build, from a source the tracker can verify | LEVEL 1 (relevant vulnerability publicly disclosed for the target) |
| Kernel read or write (A17 Pro) | The same, for kernel access, with the boundary category stated | LEVEL 1 for disclosure; LEVEL 3 requires a complete chain |
| SPTM bypass (A17 Pro, 27.0.1) | A published, verifiable result for the exact build | LEVEL 1 for disclosure; LEVEL 3 requires a complete chain |
| Bootstrap or package manager (A17 Pro, 27.0.1) | A project statement with an exact device and build, and a working environment | LEVEL 2 (public components) or LEVEL 4 (public release) |
| Exact compatibility (A17 Pro, 24A446) | An independent verification on the exact device and build | LEVEL 5 |
| Daily-driver stability | Independent evidence over time on the exact device and build | LEVEL 6 |

None of these changes is expected from the current work. Readiness stays at LEVEL 0 until the evidence supports a change.
