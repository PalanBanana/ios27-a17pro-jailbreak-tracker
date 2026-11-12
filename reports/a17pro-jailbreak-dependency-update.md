# A17 Pro jailbreak dependency update (v0.5.0)

**Status:** dependency status for the target after the Secure Exclaves review. No capability reaches "verified" for the target. The analysis describes dependencies, not methods. Readiness: **LEVEL 0 / NO-GO**, unchanged.

| Capability | What it depends on (architecture level) | Status for the target | What changed in v0.5.0 | Records |
|---|---|---|---|---|
| Sandbox escape | Container isolation and the app sandbox | Not established. Repository statement for another configuration (A19 Pro) | Terminology fixed to the repository's container-boundary wording | C-165, C-164 |
| Cross-application access | Container and shared-group boundaries | Not established | As above | C-165 |
| Kernel read | Kernel memory access under SPTM policy | Not established | Exclave-prefixed strings in the target kernelcache are recorded as static only | C-161, C-114 |
| Kernel write | Kernel mappings, which the SPTM validates on SPTM-protected products | Not established | Kernel write is recorded as separate from monitor policy | C-145, C-146 |
| Privilege escalation | Privilege levels and exclave memory typing | Not established | Exclave-private memory typing recorded as a separate dependency | C-146, C-147 |
| SPTM bypass | Monitor policy and typed pages | Not established. No publicly usable bypass for 27.0.1 recorded upstream | Apple does not state that the target is SPTM-protected | C-136, C-145, C-162 |
| AMFI compatibility | Code-signing enforcement; the integrity catalog for exclave code | Not researched for the target (CMP-008) | Integrity-catalog names recorded in the manifests and strings | C-163 |
| Bootstrap | Root filesystem layout and bootstrap packages | Not established (CMP-010) | Ecosystem re-check unchanged | C-167 |
| Package manager | Bootstrap and package tooling | Not established (CMP-011) | Ecosystem re-check unchanged; a standalone release is not a support statement | C-167 |
| Complete jailbreak | The combination of the dependencies above, on a named device and build | Not established | No change | DIM08, C-167 |
| Persistence | Survival across reboot and relaunch | Not established (CMP-006, CMP-007) | No change | CMP-006, CMP-007 |
| Daily-driver stability | Stability over ordinary use | Not established. No target evidence | No change | DIM11 |

## Reading the table

- Each row is a separate dependency. A result in one row is not evidence for another.
- A boundary described by Apple for other products is not a boundary result for the target.
- Repository statements are recorded as statements. They are not verified technical results.
- Nothing in this update changes the readiness level. LEVEL 0 / NO-GO stands.

See the [dependency reasoning](../research/exclave-security-implications-for-jailbreak.md) and the [architecture map](secure-exclaves-architecture-map.md).
