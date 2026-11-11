# Firmware report

**Device:** iPhone 15 Pro Max (A17 Pro), device identifier `iPhone16,2`. **Target:** iOS 27.0.1, build `24A446`. **Snapshot:** 2026-11-11.

This report preserves firmware facts for the research record. It does not recommend any update, downgrade or restore. Those decisions belong to the device owner. See [docs/RECOVERY_AND_PRESERVATION.md](../docs/RECOVERY_AND_PRESERVATION.md).

## Builds recorded

| Version | Build | Released | Signing (as recorded) | Apple CVE status |
|---|---|---|---|---|
| 27.0 | 24A437 | 2026-09-14 | not signed (third-party index), 2026-11-12 | listed on Apple page |
| 27.0.1 | 24A446 | 2026-09-28 | not signed (third-party index), 2026-11-12 | none published |
| 27.2 | 24B119 | 2026-10-26 | signed (third-party index), 2026-11-12 | not located |
| 27.2.1 | 24B156 | 2026-11-09 | signed (third-party index), 2026-11-12 | not located |

## What is known

- **Installed firmware (owner-reported):** iOS 27.0.1, build 24A446. The owner reports this as the installed build. The project has not verified it and does not connect to the device.
- **Release date of 27.0.1:** 2026-09-28 (C-024).
- **Apple CVE entries for 27.0.1:** none published (C-007).
- **Latest recorded build for this device family:** 27.2.1 (build 24B156), released 2026-11-09 (C-009). Latest is not the same as recommended.

## Signing

- Build 24A446 is marked **not signed** by a third-party index on 2026-11-12 (re-checked; unchanged from 2026-11-11) (C-021). A community reference reports it was still signed on 2026-11-02. The conflict is unresolved, and no Apple-hosted signing record was checked. The owner reports the installed build as unsigned, which is consistent with the index; this is not verified against Apple.
- An installed build is not the same as a restorable build. If a build is no longer signed, restoring to it is not possible, whatever the device's state.
- SHSH blobs do not guarantee a restore (see [RECOVERY_AND_PRESERVATION.md](../docs/RECOVERY_AND_PRESERVATION.md)).

## Owner-reported preservation settings

The owner reports that over-the-air update blocking is enabled. This report does not change that setting. Its mechanism and coverage are not verified, and it does not guarantee protection against every update or restore pathway.

## Restore availability

Not established for build 24A446. The project cannot check device-specific restore eligibility without device identifiers, and it does not collect them.

## Backups and recovery limits

- Backups are the owner's responsibility, made through Apple-supported methods before any change to a device.
- This project stores no backups, backup tools or device logs.
- Recovery guidance is limited to Apple's official channels.

## Items to track

- Apple statements about signing windows for 24A446 and 24B119 (signing for 24B119 is recorded as reported).
- Apple's 27.2 advisory (not located) and the per-CVE fixed-in releases.
- Any primary source on whether iOS 27.0.1 is affected by Calif.io-credited entries.
- The owner's decision on any non-invasive confirmation of the installed build.
