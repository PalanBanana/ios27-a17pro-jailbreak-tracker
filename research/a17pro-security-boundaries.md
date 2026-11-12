# A17 Pro security boundaries (v0.5.0)

**Status:** boundary-by-boundary summary for the target (iPhone16,2, A17 Pro, iOS 27.0.1, build 24A446). Each row states what Apple documents, what target evidence exists, and what would be needed. A boundary crossed in one layer is not evidence for another. Readiness: **LEVEL 0 / NO-GO**, unchanged.

| Boundary | What Apple documents | Target evidence (24A446) | Evidence grade | What would change the status |
|---|---|---|---|---|
| Application sandbox and container access | Not described by the Secure Exclaves article. The project's container records are repository statements about other configurations (SKVLENT direction 10, C-165) | None for the target | Repository statement; not reproduced | An independent result on the target. Out of scope for this project |
| Process boundary (XNU and Darwin user space) | XNU, Darwin user space and exclaveOS all execute on the application-processor cores (C-142) | None | Apple statement | Not a tracker result; the boundary is documented as shared hardware |
| Kernel boundary (XNU and SPTM) | The SPTM runs at a higher privilege level, is loaded separately, and shares no code or data with the main OS (C-146). On SPTM-protected products the kernel cannot write page-table entries (C-145) | SPTM image present (C-157); the article does not name the target as SPTM-protected | Apple statement; target applicability partially verified | An Apple statement that names the product, or target evidence |
| Physical-page typing | Every page has a type; retyping follows an allow-list and security policy (S-058) | None | Apple statement | Target evidence |
| Exclave-private memory | Typed for the exclave context only. The kernel cannot retype, map or read it, and the SPTM keeps no mapping (C-147) | No exclave runtime evidence for the target | Apple statement | Target evidence of exclave memory on the target |
| Capability boundary in the microkernel | Capabilities restrict each component's resources (C-140) | The microkernel component is absent from the target's manifests (C-157) | Apple statement; target presence unknown | Target evidence of the component |
| Secure IPC | Explicit capabilities; no default communication (C-143) | Public XNU source contains IPC files (C-153); target use is not established | Apple statement; source presence | Target evidence of use |
| Indicator and sensor-data gate | The Exclave Indicator Controller gates sensor data after the indicator check (C-144). The display exclave checks pixels on screen-indicator products (C-169) | None for the target. The products Apple names do not include the target | Apple statement for other products | Target evidence |
| Memory filters | Configurable only by the SPTM (C-148) | None | Apple statement | Target evidence |
| Coprocessor and accelerator queues | An AOP compartment and isolated Neural Engine queues (C-149) | Coprocessor and Neural Engine component names are present (C-157); no isolation evidence | Apple statement; names only | Target evidence |
| Integrity of exclave code | No code runs unless it shipped with Secure Exclaves; the integrity catalog is checked at boot (S-058 summary) | Integrity-catalog names appear as strings in the target SPTM (C-163); no target exclave image | Apple statement; static string presence | Target evidence of a packaged exclave image |

## Rules for reading this table

- A statement about one boundary does not establish another. A container-level result does not establish a kernel result (SKVLENT direction 10 states this itself; C-165).
- A component name in a manifest does not establish that the component is enabled.
- A static string does not establish that code runs.
- Apple's statements apply to the products and configurations that Apple names. For the target, none is named.

See the [applicability assessment](../reports/a17pro-exclave-applicability.md) and the [matrix](../reports/apple-silicon-security-matrix.md).
