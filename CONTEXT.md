# CONTEXT.md: glossary

Definitions used across the repository. Where a term has a project-specific meaning, that meaning is given.

## Devices and silicon

- **iPhone 15 Pro Max (iPhone16,2)**: the research target. The device identifier comes from the third-party index (C-025).
- **A17 Pro**: the Apple system-on-chip in the iPhone 15 Pro family (C-026, partially verified).
- **A20 Pro**: the chip Apple lists for iPhone 18 Pro (S-005). The reported Calif.io demonstration used this device.
- **A19 / A19 Pro**: the chips Apple names for Memory Integrity Enforcement on iPhone 17 and iPhone Air (S-003).
- **A12 / A13**: chips affected by the usbliter8 BootROM issue, as reported (C-019).
- **BootROM / SecureROM**: first-stage boot code in silicon. Software updates generally cannot change it.

## Firmware and signing

- **Build number**: Apple's internal build identifier, for example 24A446.
- **IPSW**: Apple's firmware package for a device model and version.
- **Signing / signed window**: Apple signs a firmware build only for a limited period. An installed build is not necessarily restorable.
- **SHSH blobs**: signed restore tickets. They do not guarantee a restore after Apple stops signing a build.
- **Downgrade**: installing an older signed build. Not possible once that build is no longer signed.
- **BuildIdentity**: an entry in a BuildManifest for one restore path, such as Erase, Update or Recovery. A manifest lists several.
- **ApChipID**: the chip identifier in a BuildIdentity, for example 0x8130 for iPhone16,2. It is not the same as a monitor token.
- **Monitor token**: the token in a monitor image file name, for example t8122 in sptm.t8122. It is not a marketing name (C-159).

## Security architecture

- **PPL (Page Protection Layer)**: Apple's earlier page-table and code-signing protection. Replaced by SPTM on supported platforms (S-004).
- **SPTM (Secure Page Table Monitor)**: supported on A15-or-later and M2-or-later SoCs (C-013).
- **TXM (Trusted Execution Monitor)**: works with SPTM in Apple's design (S-004).
- **MIE (Memory Integrity Enforcement)**: Apple's always-on memory-safety feature, introduced on iPhone 17 and iPhone Air (C-011).
- **EMTE (Enhanced Memory Tagging Extension)**: the hardware tagging foundation that Apple names for MIE (S-003).
- **PAC (Pointer Authentication Codes)**: pointer-integrity feature that Apple's platform guide lists (S-004).
- **AMFI (Apple Mobile File Integrity)**: code-signing enforcement component. Not researched in this pass.
- **Secure Exclaves**: Apple's architecture for isolated camera and microphone processing in ambient sensing (S-058). Applicability to the target is not established (C-162).
- **exclaveOS**: the operating system built on the exclaves microkernel and isolated from XNU and Darwin user space (S-058).
- **Exclaves microkernel**: the capability-based kernel under exclaveOS. Apple gives two accounts of its origin (C-141).
- **Secure IPC**: the interface, compiler and runtime system that governs exclave communication (C-143).
- **Exclave Indicator Controller (EIC)**: the exclave that gates sensor data after an indicator check (C-144).
- **SEP and sepOS**: the Secure Enclave Processor and its firmware sepOS, which Apple's guide describes as based on an Apple-customised L4 microkernel (C-152).

## Vulnerabilities and exploitation

- **CVE**: a public vulnerability identifier. Apple's security notes list CVEs with credits and affected devices.
- **Primitive**: a single capability, such as a kernel read (KRW family). A primitive is not a jailbreak.
- **KRW**: kernel read/write primitive.
- **Chain**: a sequence of components that together reach a jailbreak state. A chain is not established by one component alone.
- **PoC**: proof-of-concept code. The project never executes or distributes PoC code.
- **n-day**: an exploit for a vulnerability that has been patched in some builds but may still work on others.
- **Sandbox escape**: a bypass of the app sandbox. Not verified for the target.
- **Independent reproduction**: confirmation by a party other than the original researcher, on the exact device and build.

## Jailbreak types and persistence

- **Tethered**: needs a host computer at each boot.
- **Semi-tethered**: boots normally but needs a host to re-enable the jailbreak.
- **Semi-untethered**: boots without a host, but the jailbreak is disabled until the user acts.
- **Untethered**: the jailbreak state survives reboot without a host.
- **Rootless / rootful**: rootless jailbreaks keep the system volume unmodified; rootful jailbreaks modify it.
- **Bootstrap**: the package environment installed by a jailbreak.
- **Package manager**: software that installs jailbreak packages (for example Sileo).
- **Dopamine**: a jailbreak project by opa334. Support ranges are recorded per release.
- **ElleKit**: a runtime hooking framework used by jailbreak tweaks. Upstream not confirmed in this project.

## Project terms

- **Evidence tier**: 1 (primary), 2 (independent or reputable), 3 (community), 4 (unverifiable). See `docs/RESEARCH_METHODOLOGY.md`.
- **Verification method**: how a source was checked: fetched full text, fetched partial text, API response, search snippet only, or not accessed.
- **Verdict**: verified, partially_verified, unverified, disproved or superseded.
- **Confidence**: high, medium or low.
- **Readiness level**: LEVEL 0 (research only) to LEVEL 6 (daily-driver stability). See `docs/RESEARCH_METHODOLOGY.md`.
- **GO / NO-GO**: the decision on a real-device jailbreak attempt. The current decision is NO-GO.
- **Daily-driver stability**: evidence that a jailbroken device remains reliable for daily use. None exists for the target.
- **Static string presence**: an identifier found in a public firmware image. It is not evidence of a function, an enabled feature or a runtime result.
