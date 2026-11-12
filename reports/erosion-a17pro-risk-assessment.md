# Erosion A17 Pro risk assessment (v0.5.0)

**Status:** risk assessment from public documents only. It applies to any device, not to a named device. No installation is authorised, and this document does not describe Erosion as safe for any device. Readiness: **LEVEL 0 / NO-GO**, unchanged.

## 1. Basis

- Declared versions: 27.0 to 27.2.1, and 26.0 to 26.6.2 with limited functionality, per the README (C-126). Build 24A446 (27.0.1) falls within the declared 27.0 to 27.2.1 range. That is a version statement only.
- Declared devices: none (C-128). Exact-build evidence: none. Exact-hardware evidence: none. Open issues: zero (C-132).
- The developer's patch-status statement is dated 2026-11-08 and is not verified (C-130).

## 2. Risk factors

| Factor | Assessment | Basis |
|---|---|---|
| Exact-build compatibility evidence | None. Not established | C-126, C-128, C-132 |
| Exact hardware evidence | None. Not established | C-128 |
| Data loss | The developer warns that data may be lost. The risk is not evaluated here | C-129 |
| Container modification | A documented capability. Effect on user data not evaluated | Release 0.2 |
| Device-identity edits (MobileGestalt) | A documented capability. The version split on iOS 26 is recorded | C-166 |
| Version support | The developer declares it. The README excludes requests for extended version support | README |
| Exact-build evidence of worse_query status | Absent. The developer's statement is dated and not verified | C-130 |
| Persistence | Not documented | Full-text search |
| Reboot behaviour | Not documented | Full-text search |
| Recovery limitations | Not documented. The backup warning applies | C-129 |
| Firmware signing consequences | App Group limits for enterprise and paid certificates (release 0.3.1). The signing path is not evaluated | Release 0.3.1 |
| Banking application compatibility | No evidence. Not evaluated | None |
| Authentication compatibility | No evidence. Not evaluated | None |
| Face ID | No evidence. Not evaluated | None |
| Cellular service and eSIM | No evidence. Not evaluated | None |
| System stability | Not documented. The tool modifies containers and device-identity values by design | Documented capabilities |
| Battery consumption | No evidence. Not evaluated | None |

## 3. Assessment

- Erosion's public documents support no conclusion that it is safe to install on a device that holds data the owner depends on.
- The project does not authorise installation, testing or any device work.
- The developer states that data may be lost. The project cannot evaluate that risk without testing, and testing is out of scope.
- The version statement covers build 24A446 only as a range statement.

## 4. What would change the assessment

- An independent, dated report on the exact device and build, from a source other than the developer, describing observed behaviour.
- Documented recovery and reboot behaviour from the developer.
- Documented signing and persistence behaviour for the build.

None of these is recorded in this release.

See the [current status](../research/erosion-current-status.md) and the [daily-driver risk note for 0.3.1](erosion-daily-driver-risk.md).
