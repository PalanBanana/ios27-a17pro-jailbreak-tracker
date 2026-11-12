# Firmware metadata comparison: iOS 27.0.1 (24A446) and iOS 27.2 (24B119), iPhone16,2

**Status:** metadata-level comparison complete. Data as of 2026-11-12. Offline analysis of retrieved artifacts. No device
was contacted and no firmware was installed, restored or updated.

**Scope.** This page compares build metadata only: manifest structure and digests, container metadata, kernel version
strings, and KEXT inventory counts. No code-level or binary-level comparison was made. A binary diff against a later
build would locate changed code in a build that a device may still run, which is n-day vulnerability discovery; that
work was declined.

**Interpretation.** A difference on this page is a difference in metadata. It is not evidence of a security fix, and
it is not evidence that 24A446 contained a vulnerability. No difference is interpreted here.

Claims: C-089 and C-090 (27.2 manifest and containers), C-093 (monitor containers), C-094 (kernel version strings),
C-095 (KEXT inventory counts).

## 1. Artifacts

| Item | 24A446 (27.0.1) | 24B119 (27.2) |
|---|---|---|
| BuildManifest SHA-256 | c023bfa8dff4b299aa140699817e53f44fac4ad07cc3a19791d2c39a858021e1 | 4acab4a08dea01522f9de6c7a7a75a1d8911b8403896896f4f9b6b1b59ede379 |
| Kernelcache IM4P SHA-256 | 33606c425d5b9ebc9db16f1e7cf5197e8437c0df09ff061c9bd16596547c4d96 | 7fd4e6d38acbdbcef27ff40d0ee8d0601def62abe4114807ba83eaf22cc0eedf |
| SPTM IM4P SHA-256 | e9d428a985d885d1b93d549f942e79b2bffa6f011d8f3064291e15e03e1521f5 | 1976658c6b7eeef3ed969e1da2ca0f040aba2d56fd84f06b24b3ea7ead8684e7 |
| TXM IM4P SHA-256 | b81fb0c2db25d77055639bfdf8d1dc4610f31cde914f77d873e757c7405c65ff | 284e5413dfd447dc81c8840e92748dc8a390b474142f390c1fddee1ac1c716b6 |

- The 27.2 BuildManifest and the kernelcache, SPTM and TXM containers were retrieved by HTTP range request from the
  Apple CDN object for the build (S-044). The complete package was not downloaded.
- Part of the remote extraction (the AppOS disk image step) failed because the tool needs a FUSE driver that is not
  installed. That step runs after the requested files are written and does not affect these results.
- Decompression was performed without keys. Each decompressed size equals the container's declared uncompressed size.

## 2. Manifest structure

- Both builds list the same three build identities, with 97, 97 and 24 components.
- The component keys match 24A446 in every identity.
- 32 component paths differ from 24A446. They are artifact identifiers (disk-image file names and one firmware version
  string). Their names are not listed here.
- Digests were compared component by component over the variants both builds share. Of 206 components compared, **78
  digests are identical and 128 differ**.

## 3. Container verification

| Container | Normal manifest entry | Retrieved container | Restore entry |
|---|---|---|---|
| Kernelcache | KernelCache | SHA-384 matches | does not match (unresolved) |
| SPTM | Ap,SecurePageTableMonitor | SHA-384 matches | does not match (unresolved) |
| TXM | Ap,TrustedExecutionMonitor | SHA-384 matches | does not match (unresolved) |

The restore-entry mismatch is recorded in C-090. Its cause is unresolved. The complete package was not hashed, so no
full-file verification is claimed for this build.

## 4. Container metadata

| Container | 24A446 | 24B119 |
|---|---|---|
| Kernelcache: type, compression, encryption | krnl, LZFSE, not encrypted, no key bag | krnl, LZFSE, not encrypted, no key bag |
| Kernelcache: uncompressed size | 73,023,488 bytes | 73,351,168 bytes (+327,680) |
| Kernelcache: IM4P version string | KernelManagement_host-514.2.2 | KernelManagement_host-514.40.8 |
| SPTM: type, compression, uncompressed size | sptm, LZFSE, 1,212,448 bytes | sptm, LZFSE, 1,212,448 bytes (same) |
| TXM: type, compression, uncompressed size | trxm, LZFSE, 557,088 bytes | trxm, LZFSE, 557,088 bytes (same) |

The SPTM and TXM containers are different files in the two builds, and their decompressed sizes are the same (C-093).

## 5. Kernel version strings

| Build | Darwin | XNU | Kernel build date | CPU field |
|---|---|---|---|---|
| 24A446 | 27.0.0 | 13432.2.10~2 | 2026-08-13 | T8122 |
| 24B119 | 27.2.0 | 13432.42.3~28 | 2026-10-13 | T8122 |

The CPU field is recorded by the kernel. No cited source maps it to the A17 Pro (C-094).

## 6. KEXT inventory (counts only)

- Both builds contain 281 KEXT records. None was added and none was removed.
- **48** records have a different short version string, and **47** have a different bundle version (the field the
  ipsw KEXT diff reports). One record changed its short version and kept its bundle version.
- The kernel-programming-interface records follow the kernel version (27.0.0 to 27.2.0).
- Component identifiers and version values are not published here (C-095).

## 7. What this comparison does not show

- Any change inside any function or any code path.
- Whether any difference is a security fix. Metadata differences do not establish this.
- Whether 24A446 contained any vulnerability, or whether a later build addresses one.
- The applicability of any build to the A17 Pro beyond the device identifier in the manifest.

## 8. Status

| Question | Status |
|---|---|
| 27.2 manifest and three containers retrieved by range request | Verified (S-044) |
| Normal manifest digests match the retrieved containers | Verified (C-089) |
| Restore-entry digests match the retrieved containers | Do not match; unresolved (C-090) |
| Component keys identical to 24A446 | Verified |
| Component paths and digests that differ | Verified (counts) |
| KEXT inventory differences | Verified as counts (C-095) |
| Interpretation as security fixes | **Not made** |
| Code-level or binary-level differences | **Declined** |

Readiness is unchanged: LEVEL 0, NO-GO.
