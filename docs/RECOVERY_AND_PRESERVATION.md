# Recovery and Firmware Preservation

This document explains what the project records about firmware, signing and recovery, and what it does not know. It contains no device instructions.

## 1. Installed is not the same as restorable

A build can be installed on a device and still be impossible to restore. Restoring requires Apple to sign that build at the time of restore. Apple's signing decisions are not published as a stable list, so the project records third-party observations with their dates and bases (see `data/firmware.json`).

## 2. Current signing picture for the target build

- **Build 24A446 (iOS 27.0.1)**: the third-party index marks it as not signed, last checked 2026-11-12 (ipsw.me, S-014; C-021). A community reference reported it as still signed on 2026-11-02. These reports conflict and neither is confirmed by Apple. Treat the status as unresolved.
- **Build 24B156 (iOS 27.2.1)** and **build 24B119 (iOS 27.2)**: ipsw.me (S-014) marks them as signed, last checked 2026-11-12. This is not verified against Apple.
- Press coverage describes Apple stopping signing of older builds shortly after a newer release (S-020). This is a pattern, not a record for 27.0.1.

## 3. SHSH blobs

SHSH blobs are signed restore tickets. A saved blob does not guarantee a future restore, and the project does not recommend collecting them. Saving blobs is not part of this project's guidance.

## 4. Backups

Before any change to a device, the owner should make and verify a full backup using Apple-supported methods. The project provides no backup tool and stores no backups. Backup files, personal data and device logs must never be committed to this repository (see `.gitignore`).

## 5. Recovery paths

- If a device fails after any change, use Apple's official support channels and Apple's published guidance on restoring a device.
- Do not follow recovery or DFU instructions from unverified websites, videos or private messages. Those are frequent sources of data loss.
- This project does not supply recovery steps. Entering Recovery Mode or DFU mode, restoring firmware and downgrading are outside the project's safety policy for any real device.

## 6. Records the owner may keep (outside this repository)

- The build installed, and the date it was observed.
- The date of the latest verified backup.
- Any Apple support case reference, kept private.

These records should not be placed in this repository, because they may contain identifiers.

## 7. Limits of this document

The project has not checked any signing status against Apple's own systems. The information here may be out of date by the time you read it. Check the date on each record.

## 8. Preservation posture

- Research results are tied to a documented target build, so each result can be checked against the same build.
- The project does not change update settings, configuration profiles or update-deferral configuration of any device, and it does not recommend doing so.
- Public observations about a build's signing status are dated and attributed. They are not a guide to restoring any device.

## 9. What an unsigned build means for preservation

- A firmware version being unsigned does not remove an already-installed copy from a device.
- If a restore becomes necessary, the same build may no longer be available through Apple's ordinary restore process. A restore is therefore not a reliable route back to an unsigned build.
- A failed experiment, or a recovery attempt on any device, could result in a newer firmware being installed. That would change the conditions the research depends on and would make the affected build harder to restore. Anyone performing an operation on a real device must understand this risk before doing so. The project recommends against any operation that carries it.

## 10. Limits of the safeguards

- SHSH blobs do not guarantee restoration. The project does not recommend collecting them.
- Update-deferral settings do not guarantee protection against every update or restore pathway. Updates or restores started by other means may not be covered, and coverage varies by device and version.
- Neither safeguard protects data. Backups made with Apple-supported methods before any change remain the responsibility of the person making the change.
