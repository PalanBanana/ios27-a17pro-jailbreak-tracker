# DIM05: Sandbox escape and privilege escalation

**Status:** Not researched in depth in this pass. The claims and rows below are placeholders with reasons, not findings.

## What is recorded

| Item | Status | Records |
|---|---|---|
| Sandbox escape for the target | Not established. No verified public sandbox escape for the A17 Pro on iOS 27.0.1. | CMP-006 |
| Privilege escalation for the target | Not established. No verified public privilege escalation for the target. | CMP-007 |
| AMFI (code-signing enforcement) | Not researched. | CMP-008 |
| Apple-credited entry on protected files | Apple's text for CVE-2026-86886 says an app may be able to modify protected system files. Its relevance to sandbox and privilege boundaries is not assessed here, and the fixed-in release is not established. | C-005 |
| Community chain description | A community reference describes a chain that includes a sandbox escape. Not verified. | S-026 |

## Related verified context

- Apple states that PPL and SPTM enforce execution of signed and trusted code on all platforms except macOS (C-032). This is related to AMFI's role, but the AMFI-specific text was not found in this pass.
- Apple's iOS 27 security notes contain many CVE entries. This pass did not classify them by component for sandbox, AMFI or privilege-escalation issues.

## Why this dimension is incomplete

The sandbox and AMFI sections of Apple's documentation, and the component breakdown of Apple's iOS 27 notes, were not reviewed in full. No conclusion about these components should be drawn from this file yet.

## Next steps

1. Classify the iOS 27 CVE entries by component (sandbox, AMFI, CoreTrust, kernel) from Apple's fetched pages, with fixed-in releases where stated.
2. Read Apple's platform security guide sections on code-signing enforcement and record them as separate claims.
3. Only after primary entries are recorded, update CMP-006 to CMP-008.
