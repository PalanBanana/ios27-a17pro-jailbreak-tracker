# SKVLENT latest update audit (v0.5.0)

**Status:** audit of the public documentation of the SKVLENT iOS 27 research repository at its latest commit on 2026-11-12. Repository statements are recorded as statements. No result was reproduced. The exploit-development folders were not inspected, Bench27 was not built or run, and the open-work steps were not followed. Readiness: **LEVEL 0 / NO-GO**, unchanged.

## 1. Snapshot

| Item | Value |
|---|---|
| Repository | SKVLENT/iOS27-Research-Exploits |
| Default branch | main |
| Latest commit at the access date | 73f7a579ce91, committed 2026-11-12T00:50:18Z |
| Comparison with the v0.4.0 snapshot | Identical: no commits ahead or behind (C-164) |
| Repository created | 2026-10-30 |
| Licence metadata | NOASSERTION. The v0.4.0 audit recorded the LICENSE file's educational-use terms |
| Releases and tags | None recorded in the v0.4.0 audit |

The latest public state is the same as the v0.4.0 snapshot. Nothing in the repository changed after the v0.4.0 audit.

## 2. Recent history

The last twelve commits on the default branch were made between 2026-11-11 23:20 and 2026-11-12 00:50 (UTC). Their titles concern a network-process denial-of-service path, a brotli decoder status check and its measurement, a ring-buffer condition, an MTE-related result, the removal of a second CI system, and the closure of an IOSurface size-validation direction. These are the author's own statements. They are summarised here and not quoted.

## 3. Direction 10: exact status

- The README table labels direction 10 "Sandbox escape to other containers" and gives its status as demonstrated (C-165).
- The README body says the escape "crosses a container boundary in userland; it is not kernel code execution" (C-165).
- The README also says "Kernel read/write and a jailbreak were not demonstrated on this configuration" (C-114).
- The repository names the result as a container boundary. It does not name a process boundary, a kernel boundary or a privilege boundary.
- The table label "Sandbox escape" is the author's term. This project uses the body wording, a container boundary in userland.
- The v0.4.0 audit described the result as a "sandbox boundary crossing into other apps' containers and shared groups". That wording describes the reach that the repository states. The boundary itself is recorded here as a container boundary.

## 4. Configurations and results, as stated

- Primary configuration: A19 Pro (iPhone18,1), iOS 27.0.1, build 24A446 (C-109).
- Second configuration: A18 Pro (iPhone17,2), iOS 27.2. The build is given in two forms, 24B115 and 24B119 (C-110, C-116).
- The STATUS table names "27.0.1 / A19 Pro" for its verdicts.
- Results stated as demonstrated include direction 07 (container path disclosure with contents denied) and direction 10 (container boundary in userland). Other results are recorded in C-111 to C-113.
- Results stated as not demonstrated include kernel read and write, kernel code execution, root and a jailbreak (C-114, C-115).

## 5. Corrections and superseded statements

Carried from v0.4.0 and present at the head commit:

- The direction 08 entitlement reading is withdrawn (2026-11-10), as the STATUS table states.
- The direction 17 figure recorded earlier is withdrawn.
- The HID correction and the F1OOB corrections in the credits remain.
- The open-work page's inference that CVE-2026-112705 is open on 27.0.1 (C-117) is recorded as an inference. Apple gives no affected-version ranges (C-047).

## 6. Limits

- These are repository statements. None was reproduced or verified by this project.
- The API and search results are snapshots at the access date.
- The exploit-development folders and the open-work steps were not reviewed, by design.

Records: C-108 to C-118 (existing), C-164 and C-165 (new). Reconciliation: [SKVLENT evidence reconciliation](../reports/skvlent-evidence-reconciliation.md).
