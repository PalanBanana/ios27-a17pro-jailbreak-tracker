# Exclave manifest reconciliation (v0.5.0)

**Status:** metadata-level reconciliation of the firmware BuildManifests for three device families. The inspected files are the manifests of public firmware packages, read locally. No image was decrypted, no device-derived key was used, and nothing was installed or connected. Nothing here is a device result. Target: iPhone16,2 (A17 Pro) at build 24A446. Readiness: **LEVEL 0 / NO-GO**, unchanged.

Machine-readable record: [analysis/exclave-buildidentity-summary.json](../analysis/exclave-buildidentity-summary.json). It holds the full SHA-256 of each manifest, the component paths, and the SHA-384 digests of the exclave, SPTM, TXM and kernelcache entries. This document shows the first 12 hex characters of each hash.

## 1. Inventory

Each manifest was parsed as a complete property list. Each lists three BuildIdentities: a customer Erase identity, a customer Update identity and a Recovery identity.

| Manifest | Family | Product type | Build | Device class | ApChipID | Monitor token | Components (Erase / Update / Recovery) | Exclave-named (Erase / Update / Recovery) | SHA-256, first 12 hex |
|---|---|---|---|---|---|---|---|---|---|
| M1 | A17 Pro (target) | iPhone16,2 | 24A446 | d84ap | 0x8130 | t8122 | 97 / 97 / 24 | 0 / 0 / 0 | c023bfa8dff4 |
| M2 | A17 Pro | iPhone16,2 | 24B119 | d84ap | 0x8130 | t8122 | 97 / 97 / 24 | 0 / 0 / 0 | 4acab4a08dea |
| M3 | A17 Pro | iPhone16,2 | 24B156 | d84ap | 0x8130 | t8122 | 97 / 97 / 24 | 0 / 0 / 0 | 643eeb99dc82 |
| M4 | A18 Pro | iPhone17,2 | 24B119 | d94ap | 0x8140 | t8140 | 103 / 103 / 30 | 6 / 6 / 1 | 475ddc333732 |
| M5 | A19 Pro | iPhone18,1 | 24A446 | v53ap | 0x8150 | t8150 | 169 / 169 / 69 | 6 / 6 / 1 | 4e91acd9a28c |

- Identity variants: "Customer Erase Install (IPSW)" (Erase), "Customer Upgrade Install (IPSW)" (Update) and "Recovery Customer Install" (Erase).
- Consistency checks passed for every identity: the BuildNumber matches the manifest build, and the manifest's product type appears in its supported-types list.
- File sizes are 411,725 to 411,742 bytes for the A17 Pro manifests, 468,701 bytes for M4 and 816,945 bytes for M5.

## 2. Findings

- **F1. The A17 Pro has no exclave-named component in any identity.** None of the nine identities of M1, M2 and M3 lists a component whose name or path contains "exclave" (C-157).
- **F2. The A18 Pro and A19 Pro have six exclave-named components in the Erase and Update identities.** The names are Ap,ExclaveOS, Ap,ExclaveOSIntegrityCatalog, Ap,ExclaveOSTrustCache, Ap,ExclaveOSVolume, Ap,cL4 and Ap,RestorecL4. The Recovery identity lists Ap,RestorecL4 only (C-158).
- **F3. The Recovery identity is a different class.** It has fewer components and fewer device-tree and coprocessor entries. The Erase and Update identities of each manifest have the same exclave count. The earlier record used only the first identity; the complete enumeration shows that identity 0 is not representative of the Recovery identity.
- **F4. The A17 Pro monitor token and chip identifier differ.** The SPTM image name carries t8122. The BuildIdentity ApChipID is 0x8130. For the A18 Pro and A19 Pro the token equals the ApChipID value (t8140 with 0x8140; t8150 with 0x8150). See C-159.
- **F5. Component names differ between families (names only).** Erase identity, as recorded in the JSON:
  - A17 Pro against A18 Pro: 92 names shared. Eleven names occur only in the A18 Pro manifest: six exclave names, AOP2, ApplePMCFirmware, GFX1Firmware, RestoreSecureM3Firmware and SecureM3Firmware. Five occur only in the A17 Pro manifest: Ap,HapticAssets and four Savage patch names.
  - A17 Pro against A19 Pro: 82 names shared. Fifteen occur only in the A17 Pro manifest (fourteen Savage patch names and USBPortController1,USBFirmware). Eighty-seven occur only in the A19 Pro manifest.
  - A18 Pro against A19 Pro: 92 names shared. Eleven occur only in the A18 Pro manifest (ten Savage patch names and USBPortController1,USBFirmware). Seventy-seven occur only in the A19 Pro manifest.
  The meaning of these differences is not inferred.
- **F6. Coprocessor-type names.** The Erase identity lists 27 coprocessor-type names for the A17 Pro and the A18 Pro, and 26 for the A19 Pro. Names were classified by rule (see the JSON). The classification is naming only.
- **F7. The exclave-related names correspond to article terms by name only.** See section 4.

## 3. Absence analysis

The A17 Pro absence is recorded as an open question. The table lists each explanation the project considered. No explanation is adopted.

| Explanation | Evidence for | Evidence against or limit | Status |
|---|---|---|---|
| Genuinely absent from the A17 Pro firmware package | No exclave-named entry in any identity of three builds; no exclaveOS image entry | Target SPTM and kernelcache contain exclave-prefixed identifiers as strings (C-161, C-163); public XNU source has exclave code (C-153) | Not established |
| Packaged elsewhere, inside another component | Strings naming the exclaveOS integrity catalog and trust cache appear in the target SPTM image (C-163) | No packaged exclaveOS image was found. This review did not extract further components | Possible; not established |
| Device-specific omission (device class d84ap) | The manifests are device-class specific | No evidence either way | Possible; not established |
| BuildIdentity-specific omission | Ruled out for the three identities of each A17 Pro build, which cover Erase, Update and Recovery | Only the identities that each manifest lists were considered | Ruled out for the listed identities |
| Naming difference | No A17 Pro identity contains a name with "exclave" or "cL4", and none contains "L4" | Names are consistent across families (Ap, prefixes) | Not supported |
| Manifest representation difference | The A17 Pro manifests use the same key scheme as the A18 Pro and A19 Pro manifests | Component counts differ (97, 103 and 169) | Not supported as an explanation |
| Insufficient metadata | A manifest lists the components the restore uses; it cannot show components it does not reference | Each file parses completely and has the identity structure of the other families, so there is no sign of truncation | Limit of this method; not established |

Extraction failure is distinguished from absence on this evidence. Each A17 Pro file parses completely, has three identities and matches its build fields. An absent entry is therefore a property of the manifest, not a parsing failure of the local copy.

## 4. Naming correspondence (names only)

| Manifest name | Term in the article or guide | Note |
|---|---|---|
| Ap,ExclaveOS | exclaveOS | Name-level correspondence only |
| Ap,ExclaveOSVolume | Not named | Volume of the exclaveOS image (name only) |
| Ap,ExclaveOSIntegrityCatalog | Integrity catalog | The article describes an integrity catalog for read-only exclave files |
| Ap,ExclaveOSTrustCache | Not named | Name only |
| Ap,cL4 | "Apple-customized version of the L4 microkernel" | Name suggests the L4-derived microkernel. Function not established |
| Ap,RestorecL4 | Not named | Restore variant of cL4 (name only) |
| SecurePageTableMonitor (and Restore variant) | Secure Page Table Monitor (S-058, S-004) | Same term in both sources |
| TrustedExecutionMonitor (and Restore variant) | Trusted Execution Monitor (S-004 title) | TXM |
| SEP, RestoreSEP, SepStage1 | Secure Enclave Processor (S-058) | The article names SEP; processor class not stated |
| AOP, AOP2 | Always-On Processor (S-058) | AOP2 is not defined in the article |
| ANE | Apple Neural Engine (S-058) | The article names ANE |
| GFX, GFX1Firmware | Not discussed in the article | Naming only |
| DCP, RestoreDCP | Display subsystem (S-058) | The article describes a display subsystem; DCP is not defined there |

**Terminology mismatches recorded:**
1. The monitor token and the ApChipID differ for the A17 Pro. This is a value mismatch inside one package, not a naming variant.
2. Capitalisation: "ExclaveOS" in manifests against "exclaveOS" in the article.
3. The L4 spelling: "cL4" in manifests against "L4" in the article and in the guide.
4. The public XNU source uses identifiers beginning "exclaves", while the article uses "Secure Exclaves" for the architecture.

## 5. Chip-identifier observations

- ApChipID values: 0x8130 (A17 Pro), 0x8140 (A18 Pro), 0x8150 (A19 Pro).
- Monitor tokens in SPTM file names: t8122, t8140 and t8150.
- Public XNU source: T8122 and T8130 appear in one board configuration. T8140 and T8150 returned no search hits (C-154).
- Community wiki: T8130 for the A17 Pro, read as a search snippet (tier 3; C-160, S-061).
- Result: for the A17 Pro, the manifest chip identifier (0x8130, matching T8130) and the monitor token (t8122) differ, while the XNU source groups the two. The reason is not established. The token is not treated as the chip identifier. The marketing mapping of t8122 is not verified (C-124 remains unverified).

## 6. Limits

- Metadata only. A component name is not functional evidence.
- Three identities per manifest. Restore paths outside the manifest were not considered.
- The string checks (C-161, C-163) use decompressed local copies of the target payloads. Identifier names are not published.
- The XNU search is a search-index snapshot (C-153, C-154).
- No device, runtime or independent verification.

## 7. Relationship to earlier records

- C-119 to C-125 remain true. C-122 and C-123 are now backed by the complete identity enumeration (C-157, C-158).
- The earlier A17 Pro record used the component list of identity 0 only. The enumeration in this document covers every identity, which the earlier record did not.
- C-124 remains unverified. C-159 and C-160 record the observed values and the pairing that is partially verified.
