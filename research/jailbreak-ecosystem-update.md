# Jailbreak ecosystem update (v0.4.0)

**Status:** dated update to [DIM08](DIM08-jailbreak-ecosystem.md), checked on 2026-11-12. This page records only what changed or was newly checked. Everything not listed here stands as recorded in DIM08. No product is shown to support iOS 27.0.1 on the A17 Pro. Readiness remains **LEVEL 0 / NO-GO**.

## 1. What changed since DIM08

| Item | DIM08 recorded | Checked on 2026-11-12 | Effect |
|---|---|---|---|
| Dopamine README (default branch `3.x`) | "Describes an early rootless arm64e release for iOS 15.0 to 15.4.1. It has no current support matrix" (S-008, 2026-11-11) | The README describes "a rootless semi-untethered jailbreak" for iOS 15.0 to 17.3.1 on arm64e devices, iOS 15.0 to 18.7.1 on arm64 devices, and 26.0 to 26.0.1 on A12 and A13 devices. It says "More details will follow here soon" and "all issues related to version support will be deleted without response" | **Superseded.** The earlier reading is replaced by the current text. Nothing in the current README is an iOS 27 range |
| Dopamine repository description | Not recorded | "semi-untethered jailbreak for iOS 15 to 26(.0.1)" | Consistent with the README. No iOS 27 entry |
| Dopamine latest release | 3.0.13, published 2026-11-03 (C-017) | Unchanged. Releases 3.0.8 to 3.0.13 are dated 2026-08-22 to 2026-11-03 | No change |
| Dopamine default branch | `3.x` (C-033) | `3.x`; last push 2026-11-03; head is the 3.0.13 commit | No change |
| ElleKit official repository | Not recorded | `dhinakg/ellekit-official`: "Official ElleKit repo/website". Its README says it hosts official ElleKit builds and names its maintainers. It states **no iOS version range**. It has **no GitHub release** and no licence field | C-057 (an upstream claim that ElleKit 1.2 covers iOS 15 to 27) is **not supported by the official repository**. C-057 stays unverified |
| ElleKit former repository | Last pushed 2026-07-31; BSD-3-Clause is not recorded; no release | Unchanged: last push 2026-07-31; BSD-3-Clause; no release | No change |
| Procursus (bootstrap) | Not recorded | `ProcursusTeam/Procursus`: a cross-compiled "*OS bootstrap" with a BSD Zero Clause licence; last push 2026-11-12. The README gives no iOS version range and names no device. It has no GitHub release | Bootstrap compatibility for iOS 27.0.1 is **not established** (CMP-010) |
| Sileo | Latest release 2.5.1, 2024-10-08 (C-030) | Unchanged | No change |
| momentarius | Repository metadata; A12 and A13 only (C-058) | Not re-checked in this pass | No change recorded |
| Upstream tracker (iMaxTomas) | Reconciled claim by claim (S-026) | Last push 2026-11-06, head `038b9f090564`. Its chip-status table states that no publicly usable PPL or SPTM bypass is known for 27.0.1 | Consistent with the tracker's record. Its own claims remain statements of that repository |
| Other public iOS 27 project | Not recorded | A community repository created 2026-11-09, with no licence and no stars, whose description claims "IOSurface kernel surface exploitation" on "iPhone 13 Pro / 17 Pro" | Recorded as an **unverified community claim about other devices**. The "17 Pro" there is the A19 Pro iPhone 17 Pro, not the A17 Pro target. Not analysed; no compatibility inference |
| Erosion | Not recorded | An iOS customisation toolbox using the worse_query sandbox escape. See the [audit](erosion-compatibility-audit.md) | Recorded. It makes no kernel, bootstrap, package-manager or jailbreak claim |
| SKVLENT research | Not recorded | Documented in the [audit](skvlent-a19pro-research-audit.md) | Recorded as repository statements. No jailbreak claim |

## 2. Dopamine: what the current documents say

- **Rootless:** the current README describes a rootless project. Rootful status is not stated in the README and is not claimed here.
- **Supported ranges:** arm64e devices to iOS 17.3.1; arm64 devices to 18.7.1; A12 and A13 devices 26.0 to 26.0.1. No iOS 27 range is stated, and the A17 Pro is not named.
- **SPTM dependency:** the 3.0 release notes state that real-device SPTM support ends at iOS 17.3.1 (C-066).
- **Kernel dependency:** the 3.0 release notes name workarounds for two exploits without an iOS range (C-068). The names are recorded, and no mechanism is described here.
- **Support requests:** the README says that version-support issues are deleted without response.

## 3. Bootstrap, package managers and rootless environments

- **Bootstrap:** no bootstrap is recorded as supporting iOS 27.0.1 on the A17 Pro. The official Procursus repository gives no version range.
- **Package managers:** Sileo's latest release predates iOS 27 and makes no iOS 27 statement (C-030). ElleKit's official repository states no version range (above).
- **A package manager is not a jailbreak.** A package manager is not supported on iOS 27.0.1 for the A17 Pro without a complete compatible environment (CMP-011). No claim of support is made.

## 4. Claims recorded in this update

Claims C-133 to C-137 in `data/claims.json` record the Dopamine README reading (C-133), the ElleKit official repository statement (C-134), the Procursus repository statement (C-135), the upstream chip-status statement (C-136) and the community repository claim (C-137). Compatibility rows CMP-010 and CMP-011 are updated with these statements. Their statuses are unchanged.

## 5. Verdict vocabulary

Repository statements are recorded as statements. A technical result is not recorded as verified because a project says so. For upstream claims the tracker keeps two distinctions:

- **Verified as a repository statement:** the repository says this at the recorded commit.
- **Verified as a technical result:** the tracker has checked that the result holds. No upstream result for iOS 27.0.1 on the A17 Pro has been verified in this way.

## 6. What this update does not establish

- That any product works on iPhone16,2, the A17 Pro, iOS 27.0.1 or build 24A446.
- That any bootstrap or package manager is available for the target.
- That any community claim about any device is accurate.

Readiness is unchanged: LEVEL 0, NO-GO.
