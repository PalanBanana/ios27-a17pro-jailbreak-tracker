# CLAUDE.md: instructions for AI agents in this repository

This file applies to every AI model that works in this repository, including Claude. Read it before editing anything.

## Purpose

This is an independent research and compatibility tracker for an iPhone 15 Pro Max (Apple A17 Pro, device identifier iPhone16,2) running iOS 27.0.1, build 24A446. It is not a jailbreak tool. The target profile is fixed in `docs/DEVICE_PROFILE.md`.

## Non-negotiable rules

1. Never write, link to or describe working exploit steps, exploit code or jailbreak tools. Summarise public reporting only.
2. Never instruct anyone to connect to, modify, update, restore, downgrade or jailbreak an iPhone. The project never operates on devices.
3. Never claim compatibility for the exact device without evidence. Use the five evidence levels in `docs/DEVICE_PROFILE.md`.
4. Never invent sources, dates, build numbers, verdicts or quotations. If evidence is missing, record `unverified`, `not_established` or `not_researched`.
5. Never publish personal data: no device identifiers (UDID, ECID, serial number, IMEI, EID), no Apple Account details, no tokens, no personal filesystem paths and no real names of private individuals.
6. Do not copy substantial third-party text. The reference repository (S-026) is CC BY 4.0 for its own content: cite it, do not reproduce it.
7. Keep `README.md` and `README_KR.md` structurally parallel. English is the source of truth.
8. Before finishing any change, run `python3 scripts/validate_tracker.py` and fix every failure. Never weaken a check to make it pass.
9. Never force-push, rewrite history or delete existing evidence. Supersede an earlier verdict with a new record instead.
10. Never record a maintainer's personal device state (installed build, update or configuration settings, usage, or any device identifier) in this repository. The research target profile in `docs/DEVICE_PROFILE.md` is the only device description published here.

## Data conventions

- IDs: `C-###` claims, `S-###` sources, `E-###` timeline events, `CMP-###` compatibility rows. Firmware rows are keyed by build number.
- Reciprocity: a source's `associated_claim_ids` must equal the claims that cite that source.
- `verified` requires high confidence and a fetched, API or tier-1 source. `unverified` requires low confidence.
- Search-snippet-only sources are leads. They cannot support a `verified` verdict.
- Dates use ISO 8601 (`YYYY-MM-DD`) and may not be after `SNAPSHOT_DATE` in `scripts/validate_tracker.py`. Bump that constant with each research update, and only after the update's records are dated.

## Research updates

Follow the update procedure in `docs/RESEARCH_METHODOLOGY.md`. If nothing material changed, record `NO MATERIAL CHANGE` in `CHANGELOG.md`. Do not invent changes.

## Tone

Plain, precise and appropriately hedged. Use "reported" for facts that appear only in press coverage.
