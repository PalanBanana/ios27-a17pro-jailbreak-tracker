# DIM12: Recovery and safety

**Status:** Partially researched. Signing status is recorded with its conflict. Recovery limits and the safety policy are documented. The project has not verified restorability for the owner's device, and cannot without device-level checks, which it does not perform.

## Findings

| Item | Finding | Records |
|---|---|---|
| Signing of build 24A446 | Conflicting: not signed per the third-party index (2026-11-11), reported as signed on 2026-11-02 by a community reference. | C-021 |
| Installed vs restorable | An installed build is not necessarily restorable. Restore depends on Apple's signing at restore time. | RECOVERY_AND_PRESERVATION.md |
| Pattern of older builds losing signing | Press reports Apple stopped signing older builds shortly after a newer iOS 27 release. This is a pattern, not a record for 27.0.1. | S-020 |
| SHSH blobs | Not a guarantee of restore. | RECOVERY_AND_PRESERVATION.md |
| Backups | Owner responsibility, through Apple-supported methods. The project stores no backups. | RECOVERY_AND_PRESERVATION.md |
| Device-level restorability | Not verified. The project cannot check it without device identifiers, which it never collects. | DEVICE_PROFILE.md |
| Owner-reported baseline | Installed build iOS 27.0.1 (24A446) and over-the-air update blocking, as reported by the owner. Not verified by the project. | DEVICE_PROFILE.md |
| OTA update blocking | Does not guarantee protection against every update or restore pathway. Coverage is not verified. | RECOVERY_AND_PRESERVATION.md |

## Safety position

- The project performs no operation on any iPhone.
- The owner's installed firmware and over-the-air update blocking are preserved as reported. The project changes neither.
- The project recommends no jailbreak, downgrade, restore or firmware change for the owner's device.
- Packages, profiles and tools from unverified sources are treated as malware until shown otherwise (SAFETY_POLICY.md).

## Gaps and next steps

1. Track any Apple statement about signing and the restore window for build 24A446.
2. Keep the signing record dated and sourced at every update, and mark it as unresolved while the sources conflict.
3. Keep recovery guidance limited to Apple's official channels.
