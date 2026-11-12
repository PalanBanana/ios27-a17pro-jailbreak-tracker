# Apple Secure Exclaves architecture (v0.5.0)

**Status:** summary of one Apple document, read in full on 2026-11-12 (source S-058). Quoted phrases were checked by exact match against the fetched text. Other statements summarise that text. Nothing here is a device, firmware or implementation result. Target readiness: **LEVEL 0 / NO-GO**, unchanged.

## 1. Provenance

- Title: "Secure Exclaves and Ambient Sensing". Authors as printed: Security Engineering and Architecture (SEAR) and Core Operating Systems (Core OS). Published 2026-11-12. No update date is shown. Accessed 2026-11-12.
- Read: the full article text (about 36,000 visible characters after markup removal). Three embedded images (perception flow, Hey Siri flow and architecture diagram) were not read.
- Not fetched: an Apple PDF on audio-intelligence privacy and an Apple article on formally verified corecrypto (both linked from the body), and the other linked pages (Apple Platform Security, Night Shift support, Isabelle/HOL and AutoCorres2).
- Claims C-138 to C-151 and C-168 to C-169 cite this article.

## 2. Purpose

- Ambient sensing, for example HomeView person recognition and Hey Siri detection, must not expose raw camera or microphone data to the main OS.
- Apple's design goal is to run ambient sensing "in a strongly isolated environment with the full power of the main application processor", with a controlled interface and a secure indication mechanism (C-138).
- Apple calls the architecture "the most advanced architecture for ambient sensing in the industry". This is Apple's own assessment and is not verified here.
- The article names three requirements: isolation, a controlled interface and secure indication (summary of the article's structure).

## 3. Components, as the article describes them

### 3.1 Isolation and memory
- Shared resources, mainly system memory and communication with coprocessors, are isolated for the exclusive use of Secure Exclaves (summary; the phrase "system memory and communication with coprocessors" is verified).
- Memory filters sit between each protected resource and the shared fabric. Only the SPTM can configure them (C-148).

### 3.2 Exclaves microkernel
- The kernel is capability-based. Capabilities are "secure resource handles that both identify and authorize access to the underlying resource" (C-140). The article compares the design with seL4 and keyKOS.
- Unlike "traditional kernels, such as XNU or Linux", the microkernel implements only what is needed to run and isolate services (verified phrase; summary of the rest).
- Scheduling is user-level and inspired by Composite (name verified; detail summarised).
- Origin: the article calls the microkernel "an Apple-customized version of the L4 microkernel" in one place and says it "was developed from scratch at Apple" in another (C-141).

### 3.3 exclaveOS
- exclaveOS "builds on the exclaves microkernel to create an environment isolated from XNU and Darwin user space" (C-142).
- Software with direct access to cameras and microphones, and the access-management software, runs in exclaveOS. Darwin drivers, daemons and apps reach it through that access management (summary).
- Structure (summary): a static build-time system description; a root task that sets up the system and is then removed; ExclaveCores with static lifetime; ExclaveKits with dynamic lifetime, grouped with a Darwin daemon into a conclave. The article says the ability to create new connections between address spaces is "irreversibly removed" after boot.
- Files and code (summary): read-only files are checked against an integrity catalog shipped with the OS, and dynamic code is checked against signatures before it runs. The article says: "No code can execute that did not ship with Secure Exclaves."
- Boot (summary): iBoot places the microkernel, an initial static code bundle and the integrity catalog into "wired memory".

### 3.4 Secure IPC
- Secure IPC has an interface description language, a compiler, a component runtime and an RPC runtime. It is "written in Swift for memory safety" (C-143).
- By default, exclaves are "unable to communicate or even refer to one another". An exclave "may only initiate IPC if it has an explicit capability to an IPC connection" (C-143).
- Each exclave-to-main-OS interface is audited so that only the minimum metadata for the use case can cross (summary).

### 3.5 Secure indication and the Exclave Indicator Controller
- The article defines "ambient mode" and "active mode" for each sensor.
- The Exclave Indicator Controller is "the overall system gatekeeper for sensor data" (C-144). It allows data to flow only after the indicator is active and visible.
- Products with an LED indicator need only the controller. "For products like iPhone that use an indicator dot on the screen", a display exclave checks drawn pixels with "a specialized hardware block in the display subsystem" (C-169).
- In the Siri example the indicator stays on screen for "a minimum duration of three seconds" (C-144).

### 3.6 SPTM
- The SPTM "runs at a higher privilege level than the main OS kernel", "doesn't share data or code with the main OS", and "is separately loaded by the boot loader" (C-146).
- Page-table management moved into the SPTM. "On SPTM-protected products, the kernel cannot write a page table entry itself." Each change is a request that the SPTM validates against policy (C-145).
- Every page has a type. Retyping is subject to "an allow-list of permitted transitions and security policy decisions" (verified phrase).
- Exclave-private memory "is assigned types that only the Secure Exclave context owns". "The OS kernel cannot retype these pages", and "Even the SPTM itself, by design, keeps no mapping to this memory" (C-147).
- The article says that groundwork for isolation was laid "in earlier releases" and does not name them (C-168).

### 3.7 Coprocessors and the Neural Engine
- AOP: the article calls the Always-On Processor "a low-power coprocessor" that monitors for wake words in the Siri example. Where a coprocessor is essential to sensing, a secure compartment in its OS is built on the exclaves microkernel (summary).
- Neural Engine: Apple "extended the Apple Neural Engine (ANE) by adding isolated workload queues, like those we use in the SEP" (C-149). Memory filters protect those queues (verified phrase; summary of the protection).
- SEP: the article names the "Secure Enclave Processor (SEP)" and uses its queues as a design model. It does not state SEP's processor class. Apple's Platform Security guide says the Secure Enclave firmware, sepOS, is "based on an Apple-customised version of the L4 microkernel" (C-152).

## 4. Products and scope

| Name in article | Where it appears | What the article says |
|---|---|---|
| iPhone 18 Pro | Opening; Hey Siri heading | On-screen camera and microphone indicators; the Hey Siri flow |
| iPhone 18 Pro Max | Opening | On-screen camera and microphone indicators |
| iPhone Duo | Opening | On-screen camera and microphone indicators |
| MacBook Neo | Opening | Camera indicator |
| HomeView | Opening; person recognition | Camera indicator; recognises up to six people |
| "latest iPhone models" | Hey Siri section | The Hey Siri flow is shown on the latest iPhone models |

- Not named: any A-series, M-series or T-series chip; iPhone 15, iPhone 16 or iPhone 17 models; the A17 Pro; iPhone16,2 (C-139).
- The article does not map its product names to ProductType identifiers. The article's "iPhone 18 Pro" is not the tracker's iPhone18,1 (A19 Pro) profile. C-001 records the A20 Pro for the iPhone 18 Pro, as reported.

## 5. Documented statements and implementation-specific support

| Kind of statement | Examples | Status in this project |
|---|---|---|
| Apple statement of architecture | Isolation, typed pages, capability model, no default IPC, indicator gating | Verified as Apple statements (C-140 to C-149) |
| Apple statement of product scope | Named products with indicators; HomeView | Verified as Apple statements (C-139, C-169) |
| Implementation on a specific device | Which chips run exclaveOS; which features are enabled | Not stated by the article; not established for the target |
| Independent verification | Reproduction on hardware | None recorded |

## 6. Inconsistencies and naming variants
- Origin of the microkernel: "an Apple-customized version of the L4 microkernel" against "developed from scratch at Apple" (C-141). The article does not reconcile them.
- "Exclave Indicator Controller" and "Indicator Controller" both refer to the same component. "display exclave" and "secure display exclave" both appear.
- The article calls the architecture "Secure Exclaves" and the kernel "the exclaves microkernel". The public XNU source uses identifiers beginning "exclaves" (C-153).

## 7. What the article does not establish
- Whether any named product, or any device this tracker profiles, runs any described feature.
- Which chip generation, firmware build or configuration any statement applies to.
- Whether formal verification covers components other than the microkernel's C implementation (the article claims coverage only for that).
- Any independent measurement of the isolation properties.

## 8. How this summary was checked
- Each quoted phrase was searched for in the extracted text. Phrases that did not match exactly were paraphrased, not quoted.
- Summaries describe text the project read in full. Where the wording is not verified, the text says "summary".

Readiness: LEVEL 0 / NO-GO, unchanged. See the [applicability assessment](../reports/a17pro-exclave-applicability.md) and the [terminology note](apple-security-terminology.md).
