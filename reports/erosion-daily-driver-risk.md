# Erosion: generic daily-driver risk assessment (v0.4.0)

**Status:** generic public assessment, based only on Erosion's public documentation and metadata at commit `585a24a` (2026-11-10). No device was used. No real-device status is recorded here, and none is implied. Data as of 2026-11-12.

**Verdict in one line:** no meaningful evidence supports using Erosion, or any tool of this class, on a device that holds data its owner depends on. Erosion does not claim to be safe for daily use, and this assessment does not describe it as safe.

## 1. Scope

This assessment is generic. It covers the risks that any iOS customisation tool of this kind carries, and the specific risks its documents describe. It is not a recommendation to install anything, and it does not describe any particular device or owner. Full evidence is in [research/erosion-compatibility-audit.md](../research/erosion-compatibility-audit.md).

## 2. Risk factors

| Risk | What the project documents | Evidence strength | Generic assessment |
|---|---|---|---|
| **Data loss** | The README warns that data may be lost, and asks for a backup before use | Documented by the project | High. A backup is a precondition, not an option |
| **Container modification** | The file browser "can browse and modify app containers" (release 0.2) | Documented by the project | High. Modifying another app's data can corrupt it |
| **Device-identity edits** | MobileGestalt tweaks are a feature. A commit adds device-model entries for "ai spoofing" | Documented feature; effects not evaluated | Medium to high. Apps and services that read device-identity values may misbehave |
| **Version support** | The README lists supported versions and says unlisted versions are unsupported. A commit says the version check was disabled | Developer statements; the shipped effect was not verified | Medium. The tool may run on versions it does not list |
| **Exact build and device evidence** | None. No device or SoC list; no issues in the repository | Absent | High. Any run would be untested on the device in question |
| **Persistence behaviour** | Not documented. Release 0.3.1 describes App Group signing limits and sideloading advice | Partly documented | Unknown. Certificate and signing behaviour can change how long an installation lasts |
| **Recovery requirements** | Not documented. The project refuses support when a tweak does not work | Documented refusal | High. Recovery would be the owner's responsibility |
| **Firmware signing and distribution** | Releases are IPA files, sideloaded with the owner's own certificate. The website asks users to avoid mirrors | Documented | Medium. Sideloading adds trust and provenance risk |
| **Reboot and respring** | Auto-respring is a documented toggle. No reboot is documented | Documented | Low to medium. A respring interrupts the interface |
| **Face ID, passcode, cellular, eSIM** | Not mentioned | Absent | Not evaluated. No evidence either way |
| **Banking and authentication apps** | Not mentioned | Absent | Not evaluated. A customisation tool that edits app data may affect these apps. No evidence either way |
| **Battery and system stability** | Not evaluated. Tweaks "depend on your device cooperating" | Disclaimer only | Not evaluated |

## 3. Why compatibility and safety are separate questions

A tool can claim a version range and still be unsafe for a particular device. The declared range is a developer statement about versions. It is not evidence about the device, its build, its configuration or its data. The project declares no device list and has no reports from users in its repository. Both questions are open.

## 4. Position of the tracker

- No device or SoC evidence supports using Erosion on an A17 Pro device with iOS 27.0.1.
- The tracker does not describe Erosion as safe for any primary device.
- Erosion is not a jailbreak in the tracker's readiness scale (see [a17pro-compatibility-matrix.md](a17pro-compatibility-matrix.md)). Its documented capabilities do not include kernel access, bootstrap, or persistence.
- Installing, signing or running the tool is outside this project's scope. This assessment does not authorise it, and it does not describe how to do it.

## 5. What would change the assessment

- An independent, dated report of Erosion's behaviour on the exact device and build, from a source the tracker can verify.
- The project stating the device models it supports, with evidence for them.
- A documented data-protection behaviour, such as containers that the tool cannot modify without confirmation, and a reliable recovery path.
- An explanation of the version-check change in the shipped build, and of the 26.6.2 and 26.7.2 discrepancy.
