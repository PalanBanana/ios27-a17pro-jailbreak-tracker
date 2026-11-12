# Apple security terminology: SEP, Secure Enclave, Secure Exclaves, SPTM, TXM and related terms (v0.5.0)

**Status:** terminology reference. Each entry gives what the cited source says, not what the project infers. Sources: Apple's Secure Exclaves article (S-058, 2026-11-12), Apple's Platform Security guide pages (S-004 and S-059), the public XNU repository (S-057) and the tracker's manifest records (S-043 to S-045, S-055, S-056). Readiness: **LEVEL 0 / NO-GO**, unchanged.

These terms must not be treated as synonyms. The table below is organised by what each term names.

## 1. Terms

| Term | What the cited source says it is | Execution context (as stated) | Memory role (as stated) | Communication role (as stated) | Source | Do not confuse with |
|---|---|---|---|---|---|---|
| Secure Enclave Processor (SEP) | Named in the article. The article uses SEP queues as a design model for the Neural Engine | Not stated in the article | Not stated in the article | Not stated in the article | S-058 | Secure Enclave (the subsystem); Secure Exclaves (a different architecture) |
| Secure Enclave | The security subsystem whose firmware is sepOS, which Apple's guide describes as "based on an Apple-customised version of the L4 microkernel" | Firmware: sepOS | Not stated in the guide page read | Not stated in the guide page read | S-059 | Secure Exclaves |
| Secure Exclaves | Apple's architecture for isolated processing of camera and microphone data for ambient sensing. Built on isolation, a controlled interface and secure indication | Application processor cores (exclaveOS runs there, as stated) | Typed, exclave-private memory; memory filters (as stated) | Secure IPC with explicit capabilities (as stated) | S-058 | The Secure Enclave; SPTM |
| exclaveOS | The operating system built on the exclaves microkernel and isolated from XNU and Darwin user space | Application processor cores (as stated) | Isolated from XNU by the typed-page and capability rules (as stated) | Secure IPC; cross-boundary calls routed through XNU (summary) | S-058 | XNU; Darwin user space |
| Exclaves microkernel | A capability-based kernel that implements only what is needed to run and isolate services | Runs under exclaveOS; XNU donates CPU time (summary) | Capabilities set each exclave's memory permissions (as stated) | Endpoint capabilities for IPC (summary) | S-058 | The SPTM (a separate component); the sepOS L4 base (S-059) |
| SPTM (Secure Page Table Monitor) | A standalone component at a higher privilege level than the main OS kernel, loaded separately by the boot loader | Higher privilege level than the main OS kernel (stated) | Enforces page-table policy; types physical pages; separate memory views per context (as stated) | Not a communication channel in the article | S-058, S-004 | TXM; the exclaves microkernel |
| TXM (Trusted Execution Monitor) | Named in the Platform Security guide's title alongside the SPTM. The guide describes the SPTM and TXM as replacing the PPL on the relevant products (C-105) | Not described in the article | Not described in the article | Not described in the article | S-004; manifests (S-043) | SPTM |
| AOP (Always-On Processor) | A low-power coprocessor. It monitors for wake words in the Siri example | Separate coprocessor (as stated) | Compartment in its OS is built on the exclaves microkernel where sensing requires it (summary) | Passes audio to an audio exclave (summary) | S-058 | AOP2 (manifest name only; not defined in the article) |
| Apple Neural Engine (ANE) | An accelerator that the article extends with isolated workload queues | Not stated as a processor class | Memory filters block main-OS access to isolated queues; queues are flushed when switched (summary) | Not stated | S-058 | Manifest component names ANE, which are not defined in the article |
| XNU | The kernel that handles hardware, networking and resource management, in the article's description of traditional kernels | Application processor cores (as stated) | Under SPTM page-table policy (C-145) | Routes cross-boundary calls to exclaveOS (summary) | S-058, S-057 | The exclaves microkernel |
| Darwin user space | Where drivers, daemons and apps run (summary) | Application processor cores (as stated) | Not stated | Calls exclaveOS through access management (summary) | S-058 | exclaveOS |
| Exclave Indicator Controller (EIC) | An exclave that is the overall gatekeeper for sensor data | Exclave (as stated) | Not stated | Releases data only after the indicator check (C-144) | S-058 | Indicator Controller (the same component, shorter name in the article) |
| Display exclave | An exclave that checks drawn pixels through a hardware block in the display subsystem | Exclave (as stated) | Not stated | Reports to the EIC (summary) | S-058 | Secure display exclave (same component, alternative name) |
| Memory filters | Hardware between each protected resource and the shared fabric | Hardware | Protect resources; configurable only by the SPTM (C-148) | Not applicable | S-058 | MMU or IOMMU (not named in the article as the same thing) |
| Secure IPC | A system of interface description, compiler and runtime components that governs all communication into, out of and within exclaveOS | Exclaves (as stated) | Not applicable | Explicit capabilities; no default communication (C-143) | S-058 | Unrestricted IPC of the XNU kernel (not described by the article) |

## 2. Which components are separate processors

- **Stated as coprocessors in the article:** the Always-On Processor (AOP).
- **Stated as running on the application processor cores:** XNU, Darwin user space and exclaveOS (see C-142).
- **Not stated:** the processor class of the Secure Enclave Processor (SEP), of the Neural Engine and of the display exclave. The article does not give them.
- **Stated as a privilege level, not a processor:** the SPTM runs at a higher privilege level than the main OS kernel (C-146).

## 3. Execution contexts and memory permissions

- Exclaves run in a different processor execution context from the main OS (summary of S-058).
- The SPTM sets per-context permission views. The article says these are enforced in hardware (summary).
- Microkernel capabilities set each exclave's memory permissions (summary).
- Exclave-private memory is not mapped by the kernel or the SPTM (C-147).

## 4. Naming variants and mismatches

- **EIC:** "Exclave Indicator Controller" and "Indicator Controller" are both used for the same component.
- **Display exclave:** "display exclave" and "secure display exclave" are both used.
- **Architecture name:** the article uses "Secure Exclaves" for the architecture and "exclaves" for the kernel. The public XNU source uses identifiers beginning "exclaves" (C-153). These are naming variants, not evidence of identity.
- **L4:** the article says the microkernel is "an Apple-customized version of the L4 microkernel" and also "developed from scratch at Apple" (C-141). Apple's guide says sepOS is "based on an Apple-customised version of the L4 microkernel" (C-152). The two sources describe different components.
- **Secure Enclave and Secure Exclaves:** different terms for different architectures. The article uses the first only for SEP. Neither term implies the other.
- **Chip identifiers:** a monitor token in a firmware file name (for example t8122) is not a chip identifier. The manifest ApChipID is a separate field (see [the reconciliation](exclave-manifest-reconciliation.md)).

## 5. Limits

- Terms are summarised from one article, one guide page and public source search results. Terms that are not in those sources are marked as not stated.
- Summaries marked "summary" paraphrase text that was read in full but whose wording is not verified.
