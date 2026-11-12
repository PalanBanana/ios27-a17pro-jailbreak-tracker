# DIM09: Persistence and deployment

**Status:** Researched for this pass. Press-reported reboot persistence and an upstream-reported over-the-air persistence claim are recorded. Neither mechanism is disclosed, and no reproduction exists.

## Persistence classes used by this project

- **Tethered:** needs a host computer at each boot.
- **Semi-tethered:** boots normally, but a host is needed to re-enable the jailbreak.
- **Semi-untethered:** boots without a host, but the jailbreak is disabled until the user acts.
- **Untethered:** the jailbreak state survives reboot without a host.

Rootless and rootful describe where changes are stored, not how persistence works (see CONTEXT.md).

## Findings

| Item | Finding | Records |
|---|---|---|
| Reported reboot persistence | Press reports root access after the demonstration device was restarted. | C-004, S-036, S-037 |
| Reported class | The press calls the demonstration untethered. Not verified. | C-001, S-036 |
| Stage video | One outlet describes a reboot, a passcode unlock and an SSH session as root. The video was not analysed here. | S-010 |
| Over-the-air persistence | The upstream reports that a plugin survived an over-the-air update to 27.2 with Lockdown Mode enabled. The update segment is reported as edited. | C-053 |
| Update-time reboots | Dopamine's 3.0 notes say a jbupdate from an earlier version triggers a full reboot by design. That is a tool behaviour during updates, not evidence for the target. | S-007 |
| Persistence and restorability | These are separate questions. Persistence on one build says nothing about whether that build can be restored (see RECOVERY_AND_PRESERVATION.md). | C-021 |

## Verdicts

- Reboot persistence for the reported demonstration: **unverified** (C-004).
- Over-the-air persistence on 27.2: **unverified** (C-053).
- Persistence for the target: **not established.** CMP-012 is reported and unverified, and does not apply to the target.

## Gaps and next steps

1. Obtain a primary description of the persistence mechanism, if one is published.
2. Record the mechanism of Dopamine's current release from its release documentation, without operating on any device.
3. Add a claim record for any primary source that describes persistence on iOS 27.0.1 or the A17 Pro.
