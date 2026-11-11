# DIM09: Persistence and deployment

**Status:** Partially researched. Press-reported reboot persistence is recorded. The mechanism is undisclosed, and no reproduction exists.

## Persistence classes used by this project

- **Tethered**: needs a host computer at each boot.
- **Semi-tethered**: boots normally, but a host is needed to re-enable the jailbreak.
- **Semi-untethered**: boots without a host, but the jailbreak is disabled until the user acts.
- **Untethered**: the jailbreak state survives reboot without a host.

Rootless and rootful describe where changes are stored, not how persistence works (see CONTEXT.md).

## Findings

| Item | Finding | Records |
|---|---|---|
| Reported reboot persistence | Press reports root access after the demonstration device was restarted. | C-004, S-010 |
| Reported class | Press describes the demonstration as untethered. Not verified. | C-001, S-010 |
| Stage video | One outlet describes a reboot, passcode unlock and an SSH session as root. The video is not analysed here. | S-010 |
| Cross-version claim | A community reference reports that plugins survived an over-the-air update to 27.2 with Lockdown Mode enabled. This is unverified and has no claim record yet. | S-026 |
| Persistence and restorability | These are different questions. Persistence on one build says nothing about whether that build can be restored (see RECOVERY_AND_PRESERVATION.md). | — |
| Dopamine persistence | The rootless and bootstrap persistence mechanism of the current release is not researched in this pass. | C-017 |

## Verdicts

- Reboot persistence for the reported demonstration: **unverified** (C-004).
- Persistence for the target: **not established** (CMP-012 is reported-unverified and does not apply to the target).

## Gaps and next steps

1. Obtain a primary description of the persistence mechanism, if one is published.
2. Add a claim record for the cross-version report only when a primary source is found.
3. Record the rootless and bootstrap mechanism of Dopamine's current release from its release documentation.
