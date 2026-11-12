# Cross-device compatibility: A17 Pro, A18 Pro and A19 Pro (v0.4.0)

**Status:** metadata comparison complete. No result is transferred between devices. The A17 Pro compatibility of every reported research result is **not established**. Data as of 2026-11-12. Readiness remains **LEVEL 0 / NO-GO**.

## 1. Question and rules

- **Target:** iPhone16,2 (iPhone 15 Pro Max), A17 Pro, iOS 27.0.1, build 24A446.
- **Reference B:** iPhone18,1 (iPhone 17 Pro), A19 Pro, iOS 27.0.1, build 24A446. This is the repository's primary configuration ([audit](skvlent-a19pro-research-audit.md)).
- **Reference C:** iPhone17,2 (iPhone 16 Pro Max), A18 Pro, iOS 27.2, build 24B119. The repository reports reproduction of directions 01–07 on this configuration.

Rules applied:

1. A result on one SoC is not evidence for another SoC.
2. An identical build number does not establish identical kernel or driver binaries across devices. The same build number on different devices names different package contents, and this comparison checks the names.
3. Exact device metadata is used wherever it is available. Here it is the BuildManifest of each device's public firmware package, retrieved by HTTP range request. Only the manifests were read. No package was downloaded, and no binary was compared.
4. No code-level or binary-level differencing is performed, consistent with the earlier decision.

## 2. Exact device metadata

| Field | A17 Pro (iPhone16,2) | A19 Pro (iPhone18,1) | A18 Pro (iPhone17,2) |
|---|---|---|---|
| Build | 24A446 (27.0.1) | 24A446 (27.0.1) | 24B119 (27.2) |
| Device class | d84ap | v53ap | d94ap |
| Secure page-table monitor image | `sptm.t8122.release.im4p` | `sptm.t8150.release.im4p` | `sptm.t8140.release.im4p` |
| Trusted execution monitor image | `txm.iphoneos.release.im4p` | `txm.iphoneos.release.im4p` | `txm.iphoneos.release.im4p` |
| Kernelcache file | `kernelcache.release.iphone16` | `kernelcache.release.v53` | `kernelcache.release.iphone17` |
| GPU firmware (main) | `agx/armfw_g16p.im4p` | `agx/armfw_g18p.im4p` | `agx/armfw_g17p.im4p` |
| Neural engine firmware | `ane/h16x_ane_fw_iaso_d8x.im4p` | `ane/h18_ane_fw_apollo_v5x.im4p` | `ane/h17_ane_fw_theia_d9x.im4p` |
| Secure enclave firmware | `all_flash/sep-firmware.d84` | `all_flash/sep-firmware.v53` | `all_flash/sep-firmware.d94` |
| Components, erase identity | 97 | 169 | 103 |
| Exclave-related components, erase identity | **0** | **6** | **6** |
| Exclave-related components, recovery identity | 0 | 1 | 1 |

Sources: the BuildManifest of each build (see the Records in section 6). The chip token in each monitor image name is recorded as it appears. Section 4 explains why it is not mapped to a marketing name.

## 3. What the metadata shows and does not show

**GPU generation.** The main GPU firmware name follows the generation: G16P on the A17 Pro, G17P on the A18 Pro and G18P on the A19 Pro. The repository's names agree with this: it reports the A18 Pro GPU service as `AGXAcceleratorG17P`, and a credited upstream reference names the A19 Pro service as `AGXAcceleratorG18P`. The 24A446 kernelcache inventory of the A17 Pro contains G16-family driver components. *What this does not show:* any difference in GPU behaviour, memory mapping or driver logic. The GPU results reported by the repository were measured on a G18-family device and cannot be transferred to G16.

**Neural engine.** The firmware family changes with the generation: h16 on the A17 Pro, h17 on the A18 Pro and h18 on the A19 Pro. The repository's ANE research names a kernel service class with a different prefix. The A17 Pro inventory contains the H16-family ANE interface and no component with the name the repository uses. The two naming schemes are not established to be equivalent. *What this does not show:* any reachability or behaviour.

**Exclave components.** The A18 Pro and A19 Pro manifests list exclave-related components (core bundles and an exclave trust cache) in each erase identity. The A17 Pro manifest lists none in any identity. The repository's own A19 Pro study mentions a "Secure-Kernel 'exclave' world". *What this shows:* the firmware packages for the three devices differ in what they list. *What it does not show:* whether exclave hardware or code is present on the A17 Pro, or why the list differs. Metadata is not behaviour. (C-122.)

**Secure page-table monitor generation.** The monitor image token differs on each device: t8122 on the A17 Pro, t8140 on the A18 Pro and t8150 on the A19 Pro. *What this shows:* each device uses its own monitor image. *What it does not show:* any difference in the monitor's logic, interfaces or enforcement. No monitor code was compared.

**Trusted execution monitor interfaces.** The TXM image file name is the same on all three devices. The file contents were not compared. *Not established:* any interface difference.

**Kernel configuration and driver implementation.** No kernel or driver binary was compared across devices. The inventory comparison is limited to names. *Not established:* any difference in configuration or implementation.

**Device-specific hardware interfaces.** The A17 Pro inventory contains a chip-specific driver identifier with the token T8130, and its kernel records a CPU field of T8122. These tokens are recorded as they appear. *Not established:* their mapping to marketing names (section 4).

**Security policy and memory protection.** Apple's Platform Security guide states that SPTM is supported on A15-or-later and M2-or-later SoCs, and that SPTM with TXM replaces the page protection layer there (C-105). It states that Memory Integrity Enforcement is available on A19 and M5 processors or later (C-106). The A17 family is not named in the MIE passage, and no text states that MIE is off on the A17 Pro. This difference is documented; activation on the target is **not established** (C-084, C-107).

**Tag checking.** The repository reports a tag-check failure in a networking process on the A19 Pro. Whether tagging is active on the A17 Pro is not established.

## 4. Chip token mapping: unresolved

The three monitor images use the tokens t8122, t8140 and t8150, the A17 Pro's kernel records T8122, and its inventory contains T8130. No source checked here maps these tokens to marketing names with certainty. The repository's own README gives T8150 for the A19 Pro, which is consistent with the monitor token but is one source. **Unresolved.** No device-to-token claim is made beyond what the manifests show.

## 5. Build identifiers

- **24A446** is the same build number on the A17 Pro and on the A19 Pro. The packages name different kernelcaches, monitors, GPU and neural engine firmware, so the build number does not establish identical binaries.
- **24B119** is the A18 Pro build used by the repository. It is not the tracker's target build.
- **24B156** is the build used by the tracker's static comparisons. It is not a device configuration in this comparison.

## 6. Records

Claims: C-119 to C-125 (metadata facts), with sources S-043 (target manifest), S-055 (A19 Pro manifest) and S-056 (A18 Pro manifest). Repository statements are in C-108 to C-118.

## 7. Result by SoC

| SoC | Reported results (repository) | Reproduction statement | A17 Pro status |
|---|---|---|---|
| A19 Pro (27.0.1, 24A446) | Directions 01–04, 07, 10–13 and 15–17 demonstrated, partially demonstrated or static, per the repository's verdict column; directions 05, 06, 08, 09 and 14 not demonstrated | Author's own measurements | Not transferred |
| A18 Pro (27.2, 24B119) | Directions 01–07 stated to reproduce; direction 04 trigger fixed | Same author, second device | Not transferred |
| A17 Pro (27.0.1, 24A446) | None tested | None | Not established |

The detailed matrix, with evidence type and verdict per finding, is in [reports/a17pro-compatibility-matrix.md](../reports/a17pro-compatibility-matrix.md).

## 8. Conclusion

- No reported result is accepted as applicable to the A17 Pro.
- The metadata differences are real and documented. They show that the three SoC packages differ in monitor images, GPU and neural engine firmware, secure enclave firmware, and exclave components. They do not show behaviour.
- The A17 Pro compatibility status for every reported sandbox, kernel, monitor and GPU result is **not established**.

## 9. Limits

- Only manifests were compared. No package content, kernelcache, monitor image, GPU firmware or driver binary was examined on the reference devices.
- The reference manifests are from single builds; they do not cover the device's other builds.
- The chip token mapping is unresolved (section 4).
- The A17 Pro data comes from the tracker's own retrieval of build 24A446. The other two devices' data comes from range requests to public packages in the same way.
