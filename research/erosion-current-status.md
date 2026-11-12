# Erosion current status (v0.5.0)

**Status:** review of Erosion's public documents and metadata at its latest commit on 2026-11-12. Erosion was not installed, its IPA was not downloaded, no signing certificate or profile was generated, and worse_query was not run. Readiness: **LEVEL 0 / NO-GO**, unchanged.

## 1. Snapshot

| Item | Value |
|---|---|
| Repository | jailbreakdotparty/Erosion |
| Latest commit at the access date | 585a24a973d1, committed 2026-11-10T04:44:43Z ("pretty sure 27.2.1 is supported") |
| Repository description | iOS 26.0 to 26.7.2; iOS 27.0 to 27.2.1; 27.3b1 |
| Licence | GPL-3.0 (repository metadata and LICENSE file) |
| Open issues | 0 |
| Latest release | 0.3.1, published 2026-11-10 (an IPA asset is named; not downloaded) |
| Releases since v0.4.0 | None |
| Website | jailbreak.party/erosion. HTTP 200; a short page; contains the version strings 26.0, 26.7.2, 27.0 and 27.2.1 |

The head commit is the same as the v0.4.0 snapshot. No new release was published after 0.3.1.

## 2. Declared support (README at 585a24a973d1)

- The header states iOS 26.0 to 26.7.2 and iOS 27.0 to 27.2.1 (C-127).
- The supported list states iOS/iPadOS 26.0 to 26.6.2, "limited functionality, e.g. no gestalt tweaks"; iOS/iPadOS 27.0 to 27.2.1; and iOS/iPadOS 27.3 beta 1 (24C5037i) (C-126).
- The README says that a version not on the list means the device is not supported, and asks users not to request support for extending version support.
- The README says that at the time of writing (dated 2026-11-08) worse_query "has not been patched in any new software releases by Apple" (C-130). This is a dated statement by the developer. It is not verified.
- Build 24A446 (27.0.1) falls within the declared 27.0 to 27.2.1 range. That is a version statement only.

## 3. Contradictions and differences (unresolved)

1. The header (26.7.2) and the supported list (26.6.2) disagree on the iOS 26 upper bound (C-127).
2. Release 0.3.1 says "Allow Config Tweaks on iOS/iPadOS 26", while the README FAQ says MobileGestalt tweaks do not work on iOS 26. The statements may refer to different tweak classes (C-166).
3. The latest commit says "pretty sure 27.2.1 is supported", while the README lists 27.2.1 as supported.
4. A commit of 2026-11-08 is titled "disable version support check for now". Its effect on the shipped build was not verified, because the source was not reviewed.
5. The release 0.1 warning about iOS 26 tweaks is superseded by later notes.
6. The description says "27.3b1" and the README says "27.3 beta 1 (24C5037i)". This is naming only.

## 4. Capabilities: documented, claimed or not documented

| Capability | Status in the project's documents | Source |
|---|---|---|
| Sandbox escape | Documented: the app is built on the worse_query escape | README; release 0.3 |
| Container enumeration | Documented: release 0.3.1 changes the enumeration method (named in the notes) | Release 0.3.1 |
| Container browsing and modification | Documented: release 0.2 says the file browser can browse and modify app containers | Release 0.2 |
| System customisation | Documented: dialer themes, wallpapers and config tweaks | Release notes; FAQ |
| MobileGestalt changes | Documented with a version split: the FAQ says they do not work on iOS 26; release 0.3.1 allows config tweaks on iOS 26 (C-166) | README FAQ; release 0.3.1 |
| Bootstrap | Not documented | Full-text search |
| Root | Not documented | Full-text search |
| Kernel read and write | Not documented | Full-text search |
| SPTM bypass | Not documented | Full-text search |
| Full jailbreak | Not claimed. The README describes a customisation toolbox | README |
| Persistence | Not documented. Release 0.3.1 describes App Group signing limits and recommends sideloading with one's own Apple ID | Release 0.3.1 |

## 5. Attribution and licence

- The README credits forcequitOS for worse_query and 0xjohnny for the sandbox escape. worse_query is GPL-3.0 in repository metadata.
- Release 0.3.1 adds the GPLv3 licence and an acknowledgments view, which GPLv3 requires.
- This project does not copy, adapt or run Erosion code or worse_query.

## 6. Data-loss and safety warnings (preserved)

- The README says to back up the device before use and warns that data may be lost (C-129).
- The README and release 0.1 say that tweaks depend on the device and sometimes on Apple's servers, and that users should not request support for tweaks that do not work.
- Release 0.3.1 warns that enterprise or paid certificates can cause App Group problems, and recommends SideStore, Impactor or sideloading with one's own Apple ID.

## 7. Device and SoC evidence

- The README, release notes and website name no iPhone model, SoC or device list (C-128).
- The repository has no open issues (C-132). No device report for iPhone16,2, the A17 Pro, 27.0.1 or 24A446 was found.
- No compatibility with the target is verified.

## 8. Not checked

- The IPA contents, the source of the latest commits (only commit subjects were read), and any runtime behaviour.

See the [risk assessment](../reports/erosion-a17pro-risk-assessment.md).
