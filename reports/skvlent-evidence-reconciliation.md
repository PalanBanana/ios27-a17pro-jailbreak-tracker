# SKVLENT evidence reconciliation (v0.5.0)

**Status:** reconciles SKVLENT's repository statements, at commit 73f7a579ce91, with the evidence grades the project uses. Repository statements are not technical results. Readiness: **LEVEL 0 / NO-GO**, unchanged.

## 1. Reconciliation table

| Item | Repository statement | Evidence grade in this project | Reconciliation | Status |
|---|---|---|---|---|
| Direction 10: container boundary in userland | Demonstrated, per the README table; the body says "container boundary in userland" (C-111, C-165) | Repository statement | Consistent with Apple's architecture, which does not describe container access or claim exclave access | Statement only; not reproduced |
| Kernel code execution | Not demonstrated; the escape "is not kernel code execution" (C-114, C-165) | Repository statement | No conflict found. Not tested | Statement only |
| Kernel read/write and jailbreak | Not demonstrated on the configuration (C-114, C-115) | Repository statement | No conflict found | Statement only |
| Build of the second device | 24B115 in one document; 24B119 in others (C-116) | Contradiction recorded | Apple's manifest for the A18 Pro lists 24B119 (manifest S-056). No manifest for 24B115 was found | Unresolved in SKVLENT's documents |
| Direction 03 on 27.2 | The README says directions 01 to 07 reproduce on 27.2 (C-110). Apple's bulletin lists the CVE behind direction 03 as fixed in 27.2 (C-047) | Contradiction recorded | Whether the 27.2 result reproduces the fixed behaviour is not stated | Unresolved |
| "Open on 27.0.1" inference | The open-work page infers that the CVE is open on 27.0.1 because the fix is listed in 27.2 (C-117) | Inference, not established | Apple gives no affected-version ranges (C-047) | Not established |
| Decoder status check in two builds | A static claim about two builds (C-118) | Repository statement; not verified here | This project did no code-level differencing and does not adopt the claim | Statement only |
| Chip identifier for the A18 Pro | Not in dispute | Manifest metadata: ApChipID 0x8140 for iPhone17,2 (C-159) | No conflict | Consistent |

## 2. Terminology reconciliation

| Term | Used by the repository | Used by this project | Note |
|---|---|---|---|
| "Sandbox escape" | Table label for direction 10 | Not adopted as the boundary name | The body's "container boundary in userland" is adopted |
| Container boundary | Body text for direction 10 | Yes | The boundary recorded for direction 10 |
| Process boundary | Not claimed | Not claimed | No cross-process compromise is recorded (see the rule in the reconciliation of direction 10) |
| Kernel boundary | Not crossed, per the repository | Not claimed | No kernel result is recorded |
| Privilege boundary | Not claimed | Not claimed | No privilege escalation is recorded |

## 3. Evidence limits

- Every SKVLENT result is a repository statement. No result was reproduced by this project.
- No SKVLENT result is recorded as a verified technical result.
- The reconciliation does not run or request any probe.

## 4. What would change the status

- An independent, public reproduction of a stated result on a named configuration.
- A dated correction in the repository, or a corrected document that the author publishes.
- A dated primary source that resolves one of the contradictions above.

Records: C-108 to C-118 (existing), C-164 and C-165 (new). See the [audit](../research/skvlent-latest-update-audit.md).
