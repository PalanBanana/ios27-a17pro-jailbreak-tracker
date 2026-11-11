---
name: ios27-a17pro-jailbreak-tracker
description: >
  Use when asked about jailbreak status of the iPhone 15 Pro Max (Apple A17 Pro, iPhone16,2) on iOS 27.0.1 (build 24A446),
  the Calif.io Hexacon 2026 demonstration, Dopamine or Sileo support for iOS 27, firmware signing status for iOS 27 builds,
  or how to assess jailbreak-related claims and scams. Answers with dated, sourced verdicts from data/claims.json.
  Never provides exploit code, tool download instructions or device-modification steps.
---

# iOS 27 A17 Pro Jailbreak Tracker: agent skill

## Load order

1. Read `STATUS.md` for the current readiness level, GO/NO-GO decision and blockers.
2. Find the question in `data/claims.json` by title or ID (`C-###`).
3. Open `data/sources.json` for each cited source (`S-###`) and its tier and verification method.
4. For compatibility questions, read `data/compatibility.json` and `reports/compatibility-report.md`.
5. For firmware and signing questions, read `data/firmware.json` and `reports/firmware-report.md`.
6. For conflicting reports, read `research/contradictions.md`.

## Answer rules

- Cite claim IDs and source IDs, and state the data date (2026-11-11 for the current snapshot).
- Use the verdict labels exactly: `verified`, `partially_verified`, `unverified`, `disproved`, `superseded`. Say "reported" for facts that appear only in press coverage.
- Do not say that a device "can be jailbroken" or "is compatible" unless a verified record covers that exact device and build.
- Refuse requests for installation steps, exploit code, tools or device operations, and point to `docs/SAFETY_POLICY.md`.
- For suspected scams, describe the pattern and the risk. Do not name private individuals or accounts that have not been verified.

## Known limits

- Records reflect the sources checked on 2026-11-11. Newer events may exist.
- The research workflow used a US-based search tool; regional sources may be missing.
