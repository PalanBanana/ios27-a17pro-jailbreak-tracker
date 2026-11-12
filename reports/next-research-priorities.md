# Next research priorities (v0.5.0)

**Status:** data as of 2026-11-12. Target: iPhone 15 Pro Max (A17 Pro, `iPhone16,2`), iOS 27.0.1, build 24A446. **Readiness: LEVEL 0 / NO-GO.** These priorities are documentary and metadata-level. They include no test on any device, no exploit work, no binary-level comparison and no mapping of a binary to an advisory.

## 1. Scope rules for every priority

- No device is contacted, updated, restored, rebooted or used for research. No firmware is installed.
- No exploit, proof of concept or procedure from any project is run, adapted or reproduced.
- No code-level or binary-level differencing is performed. No binary is mapped to any advisory.
- External results are recorded as the source states them, with their evidence class. A result is not transferred from one SoC or device to another.
- Firmware packages are not extracted further unless a concrete question needs the extraction.
- Each priority records what would change a status. No priority assumes the answer.

## 2. Priorities, in order

1. **Resolve the recorded contradictions.** (a) The SKVLENT second-device build (24B115 or 24B119). (b) Whether the SKVLENT direction 03 result on 27.2 is the fixed behaviour or a different one. (c) Erosion's maximum iOS 26 version (26.6.2 or 26.7.2), and its tweak statements for iOS 26 (C-166). (d) Erosion's latest commit message about 27.2.1. (e) Dopamine's arm64 and arm64e classes against the target profile. Each is resolved only by a dated primary statement from the project concerned.
2. **Look for Apple statements that name the target for Secure Exclaves.** Apple's 2026-11-12 article names no A17 Pro or iPhone 15 Pro Max product (C-139). Record any later Apple statement that names the A17 Pro, the iPhone 15 Pro Max or build 24A446 for an exclave feature (C-162).
3. **Resolve the chip identifier of the target from an authoritative source.** The manifest identifier is 0x8130. The monitor token is t8122. The public XNU source groups T8122 with T8130, and a community wiki gives T8130 for the A17 Pro (C-154, C-159, C-160). Record a marketing mapping only from an authoritative source (C-124).
4. **Explain the A17 Pro manifest result from public documentation only.** Look for Apple statements on how exclave components are packaged in firmware. Do not extract further components unless a concrete question needs them (C-157, C-163).
5. **Read the public XNU source, at documentation level, for the conditions that gate exclave code by chip or configuration,** using a snapshot that matches iOS 27. This is a reading of public source only, with no binary work (C-153, C-154).
6. **Confirm the earliest public references to exclaves.** The 2025 press report dates the term to 2023 (C-156). Look for primary sources. Do not adopt the press dates until a primary source confirms them.
7. **Track the iOS 27 statements of the ecosystem projects** (C-167): Dopamine's README and releases, the official and former ElleKit repositories, Procursus and Sileo. Record any change as a dated statement. Do not infer support from a version list.
8. **Track the SKVLENT repository at new commits** (C-164). Record changes to its statements, withdrawn findings and licence. Do not reproduce its procedures or its open-work steps.
9. **Track Erosion's README, releases and commits** (C-126, C-127, C-166). Record any change. Do not install or download the tool.
10. **Keep the metadata comparison current.** When Apple publishes a new build for the target, retrieve its manifest by range request and record component names, identifiers and digests only.

## 3. What is not a priority

- **The SKVLENT open-work "what to do next" list.** It describes continued exploit development on another device. It is not adopted, and its items are not tracked as tasks for this project.
- **Device testing of any kind**, including on the primary device, including of any tool listed in the ecosystem update.
- **Installing or signing Erosion**, or downloading its IPA.
- **Reading the exploit-development folders** of any external project.
- **Binary-level or code-level differencing between builds**, and mapping any advisory to code. These were declined and remain declined.
- **Upgrading any readiness level** on the basis of an external statement, a version list, a manifest name or a second device.

## 4. What would change the target's status

| Status | What would change it | Readiness scale step it would bear on |
|---|---|---|
| Sandbox escape or cross-application access (A17 Pro) | A dated, independently checkable result on the exact device and build, from a source the tracker can verify | LEVEL 1 (relevant vulnerability publicly disclosed for the target) |
| Kernel read or write (A17 Pro) | The same, for kernel access, with the boundary category stated | LEVEL 1 for disclosure; LEVEL 3 requires a complete chain |
| SPTM bypass (A17 Pro, 27.0.1) | A published, verifiable result for the exact build | LEVEL 1 for disclosure; LEVEL 3 requires a complete chain |
| Secure Exclaves applicability (A17 Pro, 24A446) | An Apple statement that names the product or build for an exclave feature, or an independent result on the exact target | LEVEL 5 for any compatibility claim |
| Bootstrap or package manager (A17 Pro, 27.0.1) | A project statement with an exact device and build, and a working environment | LEVEL 2 (public components) or LEVEL 4 (public release) |
| Exact compatibility (A17 Pro, 24A446) | An independent verification on the exact device and build | LEVEL 5 |
| Daily-driver stability | Independent evidence over time on the exact device and build | LEVEL 6 |

None of these changes is expected from the current work. Readiness stays at LEVEL 0 until the evidence supports a change.
