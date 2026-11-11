# DIM01: Event verification

**Status:** Partially researched. The event's existence and press coverage are checked. The primary talk material has not been located.

**Question:** Did the reported iOS 27.0.1 demonstration happen? On which device and build? What has been published?

## Findings

| Item | Finding | Records |
|---|---|---|
| Event | Hexacon 2026 took place on 16 and 17 October 2026 in Paris, according to the official conference site. | S-011 |
| Presenter | Press names Calif.io, a security company, as the presenter. Its homepage describes an AI-security business and does not mention Hexacon. Individual presenters are not named in this repository. | S-010, S-012 |
| Date | Press places the demonstration on 2026-10-16. | C-001, S-010 |
| Device | Press reports an iPhone 18 Pro. Apple's iPhone 18 Pro specification page lists the A20 Pro chip. | C-001, C-002, S-005 |
| Firmware | Press reports iOS 27.0.1. No build number is stated in the reports reviewed. | C-001 |
| Reboot | Press reports root access after a restart. One outlet describes stage video of a reboot, passcode unlock and an SSH session as root. Accounts of reboot behaviour differ. | C-004, S-010 |
| Publication | No technical write-up or tool was found. Press reports the firm would publish later. | S-010, S-019 |
| Conflicting plans | A 2026-11-04 article reported exploit code and a write-up within about a week. A later article (coverage through about 2026-11-06) reported no public tool planned. | C-022, S-029, S-019 |
| Independent reproduction | None found. | CMP-014 |
| Apple's security notes | Apple credits Calif.io researchers for four CVE entries: CVE-2026-65409, CVE-2026-65410, CVE-2026-28968 and CVE-2026-86886. Apple's text does not link these entries to the stage demonstration. | C-005, S-001 |

## Verdicts

- Reported demonstration on 2026-10-16: **partially verified** (C-001). Event and venue are confirmed; the demonstration itself is press-reported.
- The demonstration device uses A20 Pro: **verified** as a statement about the iPhone 18 Pro model (C-002).
- Reboot persistence: **unverified** (C-004).
- Publication plans: **conflicting, unverified** (C-022).

## Gaps and next steps

1. Find the official Hexacon 2026 programme page. Four likely paths on the official site returned HTTP 404 in this pass.
2. Find a primary Calif.io statement or post. The company homepage did not mention the talk.
3. If a technical write-up is published, add it as a new source with its date before changing any claim.
4. Do not assess individual presenters beyond what primary sources state.
