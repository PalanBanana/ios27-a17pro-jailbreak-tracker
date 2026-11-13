# Cross-generation security matrix: A17 Pro, A18 Pro and A19 Pro (v0.5.0)

**Status:** data as of 2026-11-12. Research target: iPhone 15 Pro Max (A17 Pro, `iPhone16,2`), iOS 27.0.1, build 24A446. **Readiness: LEVEL 0 / NO-GO, unchanged.** This is a metadata-level comparison. It includes no code-level comparison of firmware, no mapping of any binary to an advisory, and no device test. Nothing here transfers a result from one SoC to another.

Companion documents: [manifest reconciliation](exclave-manifest-reconciliation.md), [exclave applicability](../reports/a17pro-exclave-applicability.md), [security matrix](../reports/apple-silicon-security-matrix.md), [architecture map](../reports/secure-exclaves-architecture-map.md) and the data file [analysis/exclave-buildidentity-summary.json](../analysis/exclave-buildidentity-summary.json).

## 1. Method and limits

- Source of the observations: the public BuildManifest of each firmware package, retrieved by range request (S-043 for the target, S-055 for the A19 Pro, S-056 for the A18 Pro). No full package was downloaded, no image was decrypted, and no component was executed.
- Every BuildIdentity of each manifest was enumerated (three per manifest). The earlier analysis used the first identity only, and the complete enumeration supersedes it for exclave purposes (C-157, C-158).
- A component name in a manifest is metadata. It is not evidence that the component runs, is enabled or is used on a device.
- The absence of an exclave-named component from a manifest does not show that the architecture is absent from the device or from the firmware image set.
- Evidence labels used below: **manifest metadata** (verified as a statement of the manifest), **Apple document statement**, **not established** and **unknown**.

## 2. Structured comparison

| Item | A17 Pro (target) | A18 Pro (reference) | A19 Pro (reference) |
|---|---|---|---|
| Device | iPhone 15 Pro Max | iPhone 16 Pro Max | iPhone 17 Pro |
| ProductType | `iPhone16,2` | `iPhone17,2` | `iPhone18,1` |
| SoC (marketing name) | A17 Pro, partially verified (C-026) | A18 Pro | A19 Pro |
| iOS version / build in the manifest | 27.0.1 / 24A446 (also 27.2 / 24B119 and 27.2.1 / 24B156) | 27.2 / 24B119 | 27.0.1 / 24A446 |
| Manifest SHA-256 | `c023bfa8…21e1` (24A446) | `475ddc33…e4` (24B119) | `4e91acd9…052d` (24A446) |
| ApChipID (manifest) | `0x8130` | `0x8140` | `0x8150` |
| Monitor image token | `t8122` | `t8140` | `t8150` |
| Token versus ApChipID | **differ** (C-159) | agree | agree |
| Device class | `d84ap` | `d94ap` | `v53ap` |
| Kernelcache file name | `kernelcache.release.iphone16` | `kernelcache.release.iphone17` | `kernelcache.release.v53` |
| GPU firmware family | `g16p` (C-119) | `g17p` (C-121) | `g18p` (C-120) |
| TXM image file name | `txm.iphoneos.release.im4p` | same name | same name |
| TXM manifest digests | equal to the A19 Pro 24A446 digests; equal to the A18 Pro 24B119 digests for builds 24B119 and 24B156 | equal to the target's 24B119 digests | equal to the target's 24A446 digests |
| BuildIdentity coverage | 3 identities per manifest: Erase (97 components), Update (97), Recovery (24) | 3 identities: Erase (103), Update (103), Recovery (30) | 3 identities: Erase (169), Update (169), Recovery (69) |
| Exclave-named components per identity | **0, 0, 0** in all nine identities of the three target manifests (C-157) | **6, 6, 1** (C-158) | **6, 6, 1** (C-158) |
| Kind of those components | none | four exclaveOS-named and two cL4-named in Erase and Update; one restore cL4-named in Recovery | same as the A18 Pro |
| Static exclave identifiers in the target's images | kernelcache: 702 occurrences, 187 distinct forms; SPTM image: 13, 10 distinct (C-161). Counts only | not examined | not examined |
| Public architecture documentation naming the SoC | none: Apple's article names five products and no chip (C-139) | none | none |
| Independent testing of exclaves on the SoC | none recorded | none recorded | none recorded |
| Confidence | high for the manifest facts; low for any inference about hardware behaviour | high for the manifest facts | high for the manifest facts |

Notes on the table:

- Hashes are shortened here. Full values are in the data file and in the source records.
- TXM digests are manifest digests. The comparison is of listed digests, not of file contents or behaviour. It says nothing about what the monitor does. The earlier record (C-125) compared file names only, and this digest observation is recorded here and in the data file, not as a new claim.
- The identity counts per manifest are all three. Restore paths outside those three identities, if any, are outside the data inspected.
- The exclave-named count for the target is zero in every identity, and it is a statement about names in those manifests only.

## 3. The monitor token and the chip identifier

For the A18 Pro and the A19 Pro, the monitor token equals the ApChipID. For the target, the ApChipID is `0x8130` while the monitor token is `t8122` (C-159).

- The public XNU source groups `T8122` with `T8130` (C-154).
- A community wiki gives `T8130` for the A17 Pro (C-160, partially verified).
- **`t8122` is not recorded as an officially mapped A17 Pro identifier.** No authoritative Apple source states the marketing mapping of the token (C-124, unverified).
- The mismatch is recorded as an unexplained observation. This document offers no explanation for it.

## 4. What the comparison shows, and what it does not

| Statement | Status |
|---|---|
| The A17 Pro manifests for builds 24A446, 24B119 and 24B156 list no exclave-named component | verified as manifest metadata (C-157) |
| The A18 Pro and A19 Pro manifests list exclave-named components in the Erase and Update identities | verified as manifest metadata (C-158) |
| The target's decompressed kernelcache and SPTM image contain exclave-prefixed identifier strings | verified as static string presence (C-161). Not evidence of function |
| The target does not run exclaves | **not established.** Manifest absence is not proof of absence |
| The target runs exclaves, or Secure Exclaves ambient-sensing features apply to it | **not established** (C-162). Apple names no A17 Pro product |
| The reason for the difference between the A17 Pro and later manifests | **not established.** No explanation is offered |
| The token `t8122` is the A17 Pro's official monitor mapping | **not established** (C-124) |
| Shared TXM file names or digests imply shared behaviour or shared exploitability | **not established.** Not inferred |
| Any capability observed on one SoC applies to another | **not applicable.** Results are not transferred between SoCs |

## 5. A17 Pro compatibility assessment

- The comparison establishes a difference in manifest content between the A17 Pro and the two later SoCs. It does not establish a difference in hardware behaviour.
- It gives no support for any compatibility claim for the target. No sandbox escape, kernel access, SPTM bypass, bootstrap or persistence is established for `iPhone16,2` on build 24A446.
- Exclave applicability to the target stays **not established**, and the project does not state that the A17 Pro lacks or has Secure Exclaves.
- Readiness for iPhone 15 Pro Max, iOS 27.0.1 (24A446): **LEVEL 0 / NO-GO, unchanged.**

## 6. Not performed

- No code-level or binary-level comparison against any later build, and no mapping of a binary to an advisory. Both remain declined.
- No decryption, no extraction beyond the manifests and the previously recorded static string counts, and no access to any device.
