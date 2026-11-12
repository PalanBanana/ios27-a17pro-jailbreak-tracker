# Apple silicon security matrix (v0.5.0)

**Status:** component matrix for the security components named by Apple's Secure Exclaves article (S-058), its Platform Security guide (S-004, S-059) and the tracker's manifest records. The matrix is built to prevent overgeneralisation: each applicability cell names the evidence behind it. Target: iPhone16,2 (A17 Pro) at 24A446. Readiness: **LEVEL 0 / NO-GO**, unchanged.

## Evidence grades

- **AD**: Apple document statement (S-058, S-004, S-059). Applies to the products Apple names, if any.
- **OS**: Apple open-source repository presence (S-057). Shows source exists, not that it runs.
- **MM**: manifest metadata (S-043 to S-045, S-055, S-056). Shows a name is listed, not that it is enabled.
- **SS**: static string presence in a public image (local analysis of S-043). Not a function.
- **TP**: third-party or press report, or a community lead (S-060, S-061). Not verified.
- **NC**: not checked in this release.

## Table A: role and boundary

| Component | Purpose | Documented role | Execution environment | Memory boundary | Trust relationship |
|---|---|---|---|---|---|
| XNU | Kernel for hardware, networking and resource management (AD, traditional-kernel comparison) | Routes cross-boundary calls to exclaveOS and schedules exclaveOS code (summary; AD) | Application-processor cores (AD, C-142) | Under SPTM page-table policy (AD, C-145). Cannot retype, map or read exclave-private pages (AD, C-147) | Outside the SPTM's privilege level (AD, C-146) |
| Darwin user space | Drivers, daemons and apps | Reaches camera and microphone data only through exclaveOS access management (AD summary) | Application-processor cores (AD, C-142) | Not described beyond the kernel rules | Calls exclaveOS through access management (AD summary) |
| SPTM | Page-table policy, typed physical pages, exclave memory views and memory filter configuration (AD) | Validates every mapping change on SPTM-protected products (AD, C-145). Configures memory filters (AD, C-148) | Higher privilege level than the main OS kernel; loaded separately by the boot loader (AD, C-146) | Owns page-table state; keeps no mapping to exclave-private memory (AD, C-147) | Shares no code or data with the main OS (AD, C-146) |
| TXM | Trusted execution monitor. Named in the guide's title with the SPTM (AD, S-004) | Replaces PPL with SPTM on the relevant products (AD, C-105) | Not described in the article | Not described in the article | Not described in the article |
| SEP and sepOS | Secure Enclave processing; the Secure Enclave firmware is sepOS (AD, S-058, S-059) | Used as a design model for Neural Engine queues (AD, C-149). Not described further in the article | Processor class not stated | Not stated | Not stated |
| Exclaves microkernel | Minimal, capability-based kernel that runs and isolates exclave services (AD, C-140) | Sets each exclave's memory permissions through capabilities (AD summary). Runs exclaveOS and the AOP compartment (AD, summary) | Under exclaveOS, on the application-processor cores (AD, C-142) | Capability-controlled (AD, C-140) | No extraneous authority (AD, C-140) |
| exclaveOS | OS of the exclaves; holds camera and microphone access and access management (AD summary) | User-level servers with minimal capabilities (AD summary) | Application-processor cores (AD, C-142) | Isolated from XNU and Darwin user space (AD, C-142) | Integrity catalog; no code runs unless it shipped with Secure Exclaves (AD summary) |
| ExclaveCore | Static-lifetime address space for services and drivers (AD summary) | Launches conclaves (summary) | Within exclaveOS (summary) | Physical memory server grants read-only or read-write mappings (summary) | Root task sets it up and is then removed (summary) |
| ExclaveKit | Dynamic-lifetime address space grouped with a Darwin daemon into a conclave (AD summary) | Created and terminated by the conclave launcher (summary) | Within exclaveOS (summary) | Mappings from the physical memory server (summary) | The launcher cannot create connections (summary) |
| Secure IPC | Governs all communication into, out of and within exclaveOS (AD, C-143) | Interface description language, compiler, component runtime and RPC runtime (AD summary) | Software in exclaveOS and the XNU boundary (summary) | Buffers handed to XNU through a system call (summary) | Explicit capabilities; minimum metadata audited (AD, C-143; summary) |
| AOP | Low-power coprocessor that monitors for wake words (AD) | First-pass wake-word detection; a secure compartment in its OS is built on the exclaves microkernel where sensing requires it (AD, summary) | Coprocessor (AD) | Not described | Compartment communicates with exclaves (summary) |
| Apple Neural Engine | Neural accelerator (AD) | Isolated workload queues for exclave models, modelled on SEP queues (AD, C-149) | Accelerator; processor class not stated (AD) | Memory filters block main-OS access to isolated queues (AD summary) | Queues flushed when switched between isolated and standard (summary) |
| GPU | Graphics (not discussed in the article) | Not described | Not described | Not described | Not described |
| Display subsystem and display exclave | Screen output; indicator pixel check (AD, C-169) | Display exclave checks drawn pixels for screen indicators (AD, C-169) | Exclave, with a hardware block in the display subsystem (AD) | Not described | Trusted display-controller firmware shares backlight values (summary) |
| Memory filters | Protect resources between each resource and the shared fabric (AD, C-148) | Isolation for sensor memory and other resources (AD summary) | Hardware (AD) | Between resources and the fabric (AD, C-148) | Configurable only by the SPTM (AD, C-148) |
| Secure boot and integrity catalog | Boot-time integrity for exclave code and read-only files (AD summary) | iBoot places the microkernel, initial code bundle and integrity catalog in wired memory (AD verified phrase) | Boot (AD) | Wired memory (AD) | Signatures for dynamic code checked against the catalog at boot (AD summary) |
| Exclave Indicator Controller | Gatekeeper for sensor data (AD, C-144) | Releases data only after the indicator is active and visible (AD, C-144) | Exclave (AD) | Not described | Relies on the display exclave check for screen indicators (AD, C-169) |

## Table B: firmware representation, documentation and applicability

| Component | Firmware representation (manifest) | Public documentation | A17 Pro, 24A446 | A18 Pro, 24B119 | A19 Pro, 24A446 | Evidence grade | Unknowns |
|---|---|---|---|---|---|---|---|
| XNU | KernelCache entries, two per full identity | S-058 (AD); S-057 (OS) | Present (MM). 702 exclave-prefixed identifier occurrences in the kernelcache (SS, C-161) | Present (MM) | Present (MM) | AD, OS, MM, SS | Whether the target runs any exclave code path |
| Darwin user space | System volume and OS components (not compared in this release) | S-058 (AD) | NC for the OS image name; access management not verified | NC | NC | AD | Target access-management details |
| SPTM | SecurePageTableMonitor entries; monitor image sptm.&lt;token&gt; | S-058, S-004 (AD) | Present (MM; token t8122, C-159). Exclave-related strings (SS, C-163) | Present (MM; token t8140) | Present (MM; token t8150) | AD, MM, SS | Whether the target is SPTM-protected in Apple's terms; runtime |
| TXM | TrustedExecutionMonitor entries; txm.iphoneos.release image | S-004 (AD) | Present (MM, C-125) | Present (MM) | Present (MM) | AD, MM | Role details beyond the guide |
| SEP and sepOS | SEP, RestoreSEP and SepStage1 entries | S-058, S-059 (AD) | Present (MM) | NC | NC | AD, MM | Processor class; relation to exclaves |
| Exclaves microkernel | cL4 and RestorecL4 entries | S-058 (AD); XNU exclave code (OS) | Absent (MM, C-157). Kernelcache strings naming exclave components (SS) | Present (MM, C-158) | Present (MM, C-158) | AD, OS, MM, SS | Whether the target runs an exclaves microkernel |
| exclaveOS | ExclaveOS, volume, trust cache and integrity catalog entries | S-058 (AD) | Absent (MM, C-157). Integrity-catalog and trust-cache strings in the SPTM (SS, C-163) | Present (MM, C-158) | Present (MM, C-158) | AD, MM, SS | Packaging of any exclaveOS image for the target |
| ExclaveCore | No separate manifest name | S-058 (AD) | Not in manifests. Kernelcache contains 4 exclavecore-prefixed occurrences (SS) | NC | NC | AD, SS | Packaging and enablement |
| ExclaveKit | No separate manifest name | S-058 (AD) | NC (not counted in this release) | NC | NC | AD | Presence on the target |
| Secure IPC | No manifest name | S-058 (AD); XNU IPC files (OS, C-153) | Kernelcache contains exclaveproxy-prefixed identifiers (SS) | NC | NC | AD, OS, SS | Use on the target |
| AOP | AOP entry | S-058 (AD) | Present (MM) | AOP and AOP2 entries (MM) | NC | AD, MM | Whether the target's AOP has the secure compartment |
| Apple Neural Engine | ANE entry | S-058 (AD) | Present (MM) | NC | NC | AD, MM | Queue generation; isolation on the target |
| GPU | GFX entry | None in the article | Present (MM) | GFX1Firmware entry (MM) | NC | MM | No exclave role stated |
| Display subsystem and display exclave | DCP and RestoreDCP entries | S-058 (AD, C-169) | Present (MM) | NC | NC | AD, MM | Target indicator path |
| Memory filters | No manifest name | S-058 (AD, C-148) | NC | NC | NC | AD | Which resources on the target |
| Secure boot and integrity catalog | Integrity catalog entries for exclaveOS | S-058 (AD) | No catalog entry (MM); SPTM strings name the concept (SS) | Present (MM, C-158) | Present (MM, C-158) | AD, MM, SS | Boot path on the target |
| Exclave Indicator Controller | No manifest name | S-058 (AD, C-144) | NC | NC | NC | AD | Target gate behaviour |

## Reading the matrix

- A cell marked "present" means the name is listed. It does not mean the component runs.
- "Absent" means no matching entry in the inspected identities of the manifest (C-157, C-158).
- "NC" means not checked in this release. It is not a claim of absence.
- Applicability for the target follows [the applicability assessment](a17pro-exclave-applicability.md), which uses the verdict vocabulary.
- Target LEVEL 0 / NO-GO is unchanged.
