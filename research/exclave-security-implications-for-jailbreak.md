# Exclave security implications for jailbreak research (v0.5.0)

**Status:** security dependency assessment at the level of architecture. It records why each documented boundary matters for a jailbreak dependency. It contains no bypass method, no exploit chain, no offsets and no attack path. Target: iPhone16,2 (A17 Pro), iOS 27.0.1, build 24A446. Readiness: **LEVEL 0 / NO-GO**, unchanged.

## 1. Why the SPTM is separate from the XNU kernel
- Apple states that the SPTM is a standalone component at a higher privilege level than the main OS kernel, separately loaded by the boot loader, and sharing no code or data with the main OS (C-146).
- Dependency consequence: by Apple's description, control of the kernel is not the same as control of the component that enforces page-table policy. A path that depends on changing that policy is a separate dependency.

## 2. Why protected page tables matter
- On SPTM-protected products the kernel cannot write page-table entries, and each mapping change is validated against policy (C-145).
- Dependency consequence: mapping outcomes depend on the monitor's policy as well as on kernel state. Apple does not state which products are SPTM-protected, so the target's status is not established (C-162).

## 3. Why physical-page ownership matters
- Every physical page has a type. Retyping is subject to an allow-list and security policy (S-058).
- Exclave-private memory has types that only the exclave context owns. The kernel cannot retype, map or read it, and the SPTM keeps no mapping to it (C-147).
- Dependency consequence: page ownership is a separate property from the ability to map a page. Changing ownership is a separate dependency.

## 4. Why capability-based memory permissions matter
- The exclaves microkernel uses capabilities that identify and authorise access, and Apple states the design has no extraneous authority (C-140).
- Dependency consequence: a component's memory access is bounded by the capabilities it holds, not by its privilege alone. A container-level result, such as the repository's direction 10 (C-165), does not show that the holder has any exclave capability.

## 5. Why Secure IPC differs from unrestricted IPC
- Under Secure IPC, exclaves by default cannot communicate or refer to one another, and an exclave needs an explicit capability to an IPC connection (C-143). Interfaces are declared in advance and audited for minimum metadata (summary of S-058).
- Dependency consequence: the documented design fixes the set of connections at configuration time. The article states that after boot the ability to create new connections between address spaces is "irreversibly removed" (S-058). Any dependency on new connections after boot is therefore contrary to the documented design, and would need evidence that the design does not describe.

## 6. Why separate microkernel environments add boundaries
- exclaveOS is isolated from XNU and Darwin user space (C-142). Cross-boundary calls are routed through XNU, which schedules exclaveOS code (summary of S-058).
- Dependency consequence: each boundary (XNU to exclaveOS, Darwin user space to exclaveOS, and the monitor boundary) has its own mechanism. A result on one boundary does not transfer to another.

## 7. Why an application sandbox escape does not automatically reach exclave-private memory
- Apple states that exclave-private memory is typed for the exclave context, that the kernel cannot retype, map or read it, and that the SPTM keeps no mapping to it (C-147). Apple also states that the main OS and apps cannot access data processed in exclaves (summary of S-058).
- The repository's direction 10 is a container-level result in userland (C-165). It does not name an exclave interface.
- Dependency consequence: a container result is not a result on exclave-private memory.

## 8. Why kernel read/write does not automatically imply SPTM bypass
- Apple describes the SPTM as a separately loaded component with its own privilege level (C-146) and with page-table policy that the kernel cannot override on SPTM-protected products (C-145).
- Dependency consequence: kernel-level access and control of the monitor's policy are separate dependencies. The repository states that kernel read and write were not demonstrated on its configuration (C-114). Upstream records state that no publicly usable SPTM or PPL bypass is known for 27.0.1 (C-136).

## 9. Why root access does not automatically imply a complete jailbreak
- Root is a privilege. A bootstrap, a package manager and persistence are separate dependencies. The article's integrity rules apply to exclave code: no code runs unless it shipped with Secure Exclaves, and signatures are checked at boot (summary of S-058).
- Dependency consequence: a complete jailbreak needs each dependency in section 10, not one of them alone.

## 10. Dependency table

| Dependency | What Apple documents | Target status | Records |
|---|---|---|---|
| Sandbox escape (container access) | Not described in the article | Not established. Repository statement for another configuration only | C-165, CMP-016 |
| Exclave-private memory access | Typed for the exclave context; the kernel cannot retype, map or read it | Not established | C-147 |
| Kernel read | Not described for the target | Not established. Exclave-prefixed strings in the target kernelcache are static only | C-161, C-114 |
| Kernel write | Page-table writes are validated by the SPTM | Not established | C-145 |
| Privilege escalation | Not described for the target | Not established | C-146 |
| SPTM bypass | Policy and typing are documented; no bypass recorded | Not established. No publicly usable bypass for 27.0.1 recorded upstream | C-136, C-145, C-147 |
| Bootstrap | Not described | Not established | CMP-010 |
| Package manager | Not described | Not established | CMP-011 |
| Persistence | Not described | Not established | CMP-006, CMP-007 |
| Full jailbreak | Not described | Not established | DIM08 |

See also the [dependency update](../reports/a17pro-jailbreak-dependency-update.md) and the [boundary summary](a17pro-security-boundaries.md).
