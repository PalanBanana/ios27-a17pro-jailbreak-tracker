# A17 Pro Secure Exclaves applicability (v0.5.0)

**Status:** applicability assessment for iPhone16,2 (iPhone 15 Pro Max, A17 Pro), iOS 27.0.1, build 24A446. Fields are kept separate, as the project requires. No field reaches "verified" for the target. Readiness: **LEVEL 0 / NO-GO**, unchanged.

## 1. Fields

Verdict terms: verified, partially_verified, not_established, unknown and not_applicable.

| Field | A17 Pro (target, 24A446) | A18 Pro (iPhone17,2, 24B119) | A19 Pro (iPhone18,1, 24A446) | Basis |
|---|---|---|---|---|
| SPTM SUPPORT | partially_verified | partially_verified | partially_verified | Apple's guide states SPTM for A15-or-later (C-013, C-105). The SPTM image is named in each manifest (C-157, C-158, C-159). No runtime evidence |
| EXCLAVES MICROKERNEL PRESENCE | unknown | partially_verified | partially_verified | Target: no cL4 component in any identity (C-157). Target kernelcache and SPTM contain exclave identifiers as strings (C-161). A18 Pro and A19 Pro: cL4 is named in the Erase and Update identities (C-158). Names are not function |
| EXCLAVEOS SUPPORT | not_established | partially_verified | partially_verified | Target: no exclaveOS image component in the manifests. SPTM strings name integrity-catalog and trust-cache concepts (C-163). A18 Pro and A19 Pro: exclaveOS components named (C-158) |
| SECURE EXCLAVES AMBIENT-SENSING FEATURES | not_established | not_established | not_established | Apple names no A17 Pro, A18 Pro or A19 Pro product (C-139). Target strings for camera, audio and sensor proxies (C-161) are not functional evidence |
| HomeView-specific features (person recognition, LED indicator) | not_applicable | not_applicable | not_applicable | Apple names HomeView as a different product (C-139) |
| ANE ISOLATED WORKLOAD SUPPORT | not_established | not_established | not_established | Apple describes isolated queues without naming a Neural Engine generation (C-149). No device evidence |
| SECURE IPC IMPLEMENTATION | unknown | not_established | not_established | The public XNU source contains exclave IPC files (C-153). Use on the target is not established. Apple describes the design (C-143) |
| DEVICE-SPECIFIC VERIFICATION | not_established | not_established | not_established | No independent reproduction or device result is recorded for any of the three |

## 2. Outcome labels

- **VERIFIED AS AN APPLE DOCUMENT STATEMENT.** Applies to Apple's architecture statements (C-138 to C-151, C-168, C-169). It does not apply to the target device.
- **VERIFIED AS AN IMPLEMENTATION ON A SPECIFIC DEVICE.** None recorded.
- **INDEPENDENTLY VERIFIED ON THE EXACT TARGET.** None recorded.
- **Manifest metadata and static string presence** (C-157 to C-159, C-161, C-163) are separate from all three outcomes. They are not device results.

## 3. Reasoning for the target

1. Apple's article does not name the A17 Pro or the iPhone 15 Pro Max. It names five products and no chip (C-139).
2. Apple's SPTM and exclave statements are general or name other products (C-144, C-145, C-146, C-169).
3. The A17 Pro manifests list no exclave-named component in any identity (C-157). The A18 Pro and A19 Pro manifests do (C-158). The A17 Pro manifests therefore do not show that the target runs an exclave runtime.
4. The target's decompressed kernelcache and SPTM contain exclave identifiers as static strings (C-161). The strings show that exclave-related names exist in the target build's images. They do not show that any feature runs or is enabled.
5. Absence of an exclaveOS image from the manifests is not proof that the A17 Pro lacks exclaveOS. Nor is the presence of strings proof that it has exclaveOS (see [the reconciliation](../research/exclave-manifest-reconciliation.md)).
6. The chip identifier (0x8130) differs from the monitor token (t8122). The marketing mapping is partially verified (C-160).

## 4. Conclusion

- Exclave applicability to the A17 Pro is **not established**. The project records it as an open question (C-162).
- The project does not state that the A17 Pro lacks Secure Exclaves, and it does not state that the A17 Pro has them.
- Readiness: LEVEL 0 / NO-GO, unchanged.

## 5. What would change the status

- An Apple statement that names the A17 Pro, the iPhone 15 Pro Max or build 24A446 for an exclave feature, or that lists the products that load exclaveOS.
- A public firmware package for the target that lists exclaveOS components, with the packaging location explained.
- An independent, public reproduction on the exact target. The project does not perform device tests.

## 6. Sources and dates

- Apple article, published and accessed 2026-11-12 (S-058).
- Manifests: S-043 (A17 Pro 24A446), S-044 (24B119) and S-045 (24B156), all for iPhone16,2; S-055 (A19 Pro, 24A446); S-056 (A18 Pro, 24B119).
- Public XNU source search, accessed 2026-11-12 (S-057).
- Community wiki lead for the chip identifier (S-061, search snippet only).
- Press reports (S-060): reported, not verified (C-155, C-156).
