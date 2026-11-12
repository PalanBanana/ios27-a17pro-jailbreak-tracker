# DIM10: Scam detection and community verification

**Status:** Researched for this pass. Patterns are recorded in general terms. No individuals or accounts are named, because none has been verified against a primary source for this purpose.

## Findings

| Item | Finding | Records |
|---|---|---|
| No installable package from the firm | Press reports that no installable package has come from the demonstration's firm. Downloads that advertise iOS 27.0.1 jailbreaks are not verified to relate to that demonstration. | C-028, S-036, S-019 |
| A project with a date-bound promise | A project announced in November 2026 claimed a release in one to two weeks, with a test-device claim. The upstream reports no proof of concept or third-party validation. It is recorded as unverified and high risk. | C-064, E-029 |
| Hash posts without content | Two bare SHA-256 posts reported by the upstream carry no explanation. A hash cannot be checked until its preimage is published. | E-027 |
| Single-party demonstrations | A company-branded root-shell claim on iOS 27.2 has only image or video evidence and no CVE. | C-063, E-028 |
| Tutorial pages | A tutorial page claims a complete iOS 27 jailbreak built on a BootROM issue. It has no verifiable author, makes broad claims and is not used as evidence. | C-020, S-025 |
| Press-reported AI claims | Press reports that AI found an exploit chain are not tool evidence. The method was not confirmed by the team. | C-076 |

## Warning signs used by this project

These are indicators, not proof. Any one of them is a reason to hold a claim as unverified:

- A new account, or an account with no track record in the field.
- No reproducible evidence, only screenshots, cropped logs or unverifiable video.
- Promised dates for a complete tool or a full jailbreak.
- A bare hash or other commitment without any content.
- Requests to move the conversation to private messages or a paid channel.
- A claim that does not match the author's public record.
- Packages (IPA files, profiles, installers) offered for download from an unknown source.

## Rules

1. Treat installation packages, profiles and "jailbreak" tools from unverified sources as malware until shown otherwise (SAFETY_POLICY.md).
2. Do not pay for access to a jailbreak. Verify any claim against the sources in `data/sources.json`.
3. A credit in Apple's security notes is a credit for a reported vulnerability. It is not an endorsement of any tool.
4. Name no individual or account in this repository unless a primary source confirms the link and the publication is necessary (METHODOLOGY section 4.7).
5. Report suspected scams with the new-research issue template, choosing 'Scam or fake-tool report'.

## Gaps and next steps

1. Track any official statement from the firm or from Apple about impersonation or fake tools.
2. Keep the warning-sign list current, with dated and sourced examples and no names.
