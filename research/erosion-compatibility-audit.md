# Erosion compatibility audit (v0.4.0)

**Status:** static review of public documentation and metadata. Erosion was **not installed**, its IPA was **not downloaded**, no signing certificate or profile was generated, nothing was run, and no device was used. Data as of 2026-11-12. For the target, **compatibility is not established** and readiness remains **LEVEL 0 / NO-GO**.

## 1. Identity

| Item | Value |
|---|---|
| Project | Erosion, `jailbreakdotparty/Erosion` |
| Repository | [github.com/jailbreakdotparty/Erosion](https://github.com/jailbreakdotparty/Erosion), commit reviewed [`585a24a973d1`](https://github.com/jailbreakdotparty/Erosion/tree/585a24a973d1) (2026-11-10) |
| Created / last pushed | 2026-08-23 / 2026-11-10 |
| Commits | 42 |
| Releases | 0.1 (2026-08-25), 0.2 (2026-09-15), 0.2.1 (2026-09-18), 0.3 (2026-11-09), 0.3.1 (2026-11-10). Each release has an IPA asset. Asset names and sizes were read; no asset was downloaded |
| Issues | None recorded (zero open or closed at review), so no public user reports exist in the repository |
| Licence | GNU General Public License v3.0 (LICENSE file; repository metadata). The v0.3.1 notes say the acknowledgments view was added because GPLv3 requires it |
| Official website | jailbreak.party/erosion (static fetch; partial text). The site says it is "the only official site" and asks users to avoid third-party download mirrors |
| Attribution form used | Erosion (jailbreakdotparty), GPL-3.0; upstream technique: worse_query (forcequitOS), GPL-3.0 |

## 2. What the project declares

- **Purpose.** "iOS customization toolbox using the worse_query sandbox escape" (README; repository description; website).
- **Declared iOS range.** The README lists iOS/iPadOS **26.0 to 26.6.2** ("limited functionality, e.g. no gestalt tweaks"), **27.0 to 27.2.1**, and **27.3 beta 1 (24C5037i)**. It also says that a version not on the list means the device "is not supported".
- **Declared device scope.** None. The README, the release notes and the website contain no iPhone model, SoC or device list (checked for "iPhone", "SoC" and "model": no occurrences).
- **Range is not device proof.** 24A446 (27.0.1) falls inside the declared 27.0 to 27.2.1 range. That is a statement about versions only. It does not establish that the tool works on iPhone16,2 or on the A17 Pro.

## 3. Contradictions within the project's own surfaces

| # | Statement A | Statement B | Note |
|---|---|---|---|
| 1 | README: 26.0 to **26.6.2** | Repository description, website and release 0.3: 26.0 to **26.7.2** | Not reconciled. Both cannot be current |
| 2 | README: "27.3 beta 1 (24C5037i)" | Repository description: "27.3b1" | Naming only |
| 3 | README and website: 27.0 to 27.2.1 supported | Latest commit message (2026-11-10): "pretty sure 27.2.1 is supported" | The project's own uncertainty about one version it lists |
| 4 | README: devices not on the list are not supported | Commit 4dc0fc8 (2026-11-08): "disable version support check for now" | A commit message stating the in-app check was disabled. Its effect on the shipped build was not verified (the source was not reviewed) |
| 5 | Release 0.1: iOS 26 "cannot use most of the tweaks" | README (current): iOS 26 supported with limited functionality, and tweaks re-enabled in 0.3.1 | Later release notes supersede the earlier warning |

## 4. Capabilities: documented, claimed, or not documented

| Capability | Status in the project's documents | Source |
|---|---|---|
| 1. Sandbox escape | **Documented.** The app is built on the worse_query escape. Release 0.3 "replaced bad_query with worse_query" | README; release 0.3 |
| 2. Application-container access | **Documented.** The file browser can "browse and modify app containers" (release 0.2). Container enumeration uses pathleak (release 0.3.1) | Release notes |
| 3. System customization | **Documented.** Dialer themes, PosterBoard and MercuryPoster wallpapers, auto-respring, and config tweaks | Release notes; FAQ |
| 4. MobileGestalt changes | **Documented.** MobileGestalt tweaks are a feature, limited on iOS 26. A commit adds device-model entries for "ai spoofing" (commit subject only; code not reviewed) | README FAQ; release 0.1; commit 4a865b9 |
| 5. Bootstrap | **Not documented.** No package manager or bootstrap is described | Full text search |
| 6. Root access | **Not documented.** The word appears only as part of a contributor's handle | Full text search |
| 7. Kernel read and write | **Not documented** | Full text search |
| 8. SPTM bypass | **Not documented** | Full text search |
| 9. Full jailbreak | **Not claimed.** The name and website use "jailbreak", but the README describes a customisation toolbox | README |
| 10. Persistence | **Not documented.** The release notes describe App Group signing limits and recommend SideStore, Impactor or sideloading with one's own Apple ID. Renewal and expiry are not described | Release 0.3.1 |

## 5. Verification of exact compatibility

| Test | Result |
|---|---|
| Does the official documentation name iPhone16,2, the A17 Pro, or build 24A446? | **No.** None of these appears in the README, the release notes or the website |
| Does the repository record independent device reports? | **No.** Zero issues; no device-report search matched "iPhone16,2", "15 Pro Max", "A17" or "24A446" |
| Is the declared range independently verified? | **No.** The range is the developer's statement |
| Is the claim that worse_query has not been patched verified? | **No.** The README gives a date of 2026-11-08 and says "expect that to change in the short future". It is a dated statement |

**Conclusion.** Exact hardware support for iPhone16,2, the A17 Pro, iOS 27.0.1 and build 24A446 has **not been verified**. A supported version range is not sufficient to establish exact hardware support, and this project declares no hardware support at all.

## 6. Data-loss and safety warnings (included in the assessment)

- The README warns: "Please create a backup of your device before usage! While Erosion has been extensively tested, there is still a possibility that you could lose your data by using this tool."
- The README and release 0.1 say that tweaks depend on the device and sometimes on Apple's servers, and that users should not ask for support when a tweak does not work.
- Release 0.1 says "Use all of these own tweaks at your own risk, and have a backup please!"
- Release 0.3.1 warns that enterprise or paid certificates can cause App Group problems, and recommends sideloading with one's own Apple ID.

## 7. Licence and attribution

- GPL-3.0 applies to the project. This tracker does not copy any code, asset or documentation from Erosion.
- The worse_query escape is credited by its author (forcequitOS) and is GPL-3.0 in its repository metadata. This tracker does not reproduce or adapt it.

## 8. Distribution

Releases are distributed as IPA files. The website asks users to avoid third-party mirrors. This review did not download, install or sideload any file. The IPA route is noted here because installing an IPA is an operation this project does not authorise on the primary device.

## 9. What this audit does not establish

- Whether Erosion works on iPhone16,2 with iOS 27.0.1 (24A446), or on any A17 Pro device.
- Whether the worse_query escape is available on 24A446. The developer states it has not been patched as of 2026-11-08. That is not verified.
- Whether any of Erosion's documented capabilities has been independently verified on any device.
- Any behaviour of the tool's code. The source was not reviewed beyond the documents and commit subjects listed here.

## 10. Status for the tracker

| Question | Status |
|---|---|
| Declared iOS range includes 27.0.1 | Repository statement (declared range only) |
| Declared device or SoC compatibility | **None declared** |
| Independent verification on the target | **None found** |
| Documented capabilities | Sandbox escape, container access, customisation, MobileGestalt changes (see section 4) |
| Not documented | Bootstrap, root, kernel read and write, SPTM bypass, full jailbreak, persistence |
| A17 Pro compatibility | **Not established**; readiness LEVEL 0 / NO-GO |

Claims: C-126 to C-132 (Erosion). Sources: S-048 (repository), S-049 (website). Compatibility row: CMP-017. The daily-driver assessment is in [reports/erosion-daily-driver-risk.md](../reports/erosion-daily-driver-risk.md).
