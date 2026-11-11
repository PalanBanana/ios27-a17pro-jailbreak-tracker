# Contributing

Thank you for helping keep this record accurate. This project values checkable evidence over speed: a contribution is a proposal until a maintainer has reviewed its sources.

## What we accept

- New research leads, with at least one source that can be checked.
- Official announcements from vendors, developers and conference organisers, with a URL and an access date.
- Compatibility evidence, clearly labelled with the exact device, chip, iOS version and build it concerns, and how it was verified.
- Source verification: confirming, qualifying or disproving an existing source.
- Technical corrections, timeline updates and reports of incorrect claims.

## What we do not accept

- Exploit code, proof-of-concept binaries, jailbreak tools, IPA files, configuration profiles, or links to any of them.
- Step-by-step instructions for jailbreaking, bypassing protections, or modifying, updating, restoring or downgrading a device.
- Device identifiers or personal data: UDID, ECID, serial numbers, IMEI, EID, Apple Account details, authentication tokens, backups, logs, or screenshots that show any of them.
- Claims with no source, and claims supported only by rumours, paid promotion, or unverifiable video.
- Naming private individuals as suspects or as the source of a claim.

## How to change the data

1. Choose the file: `data/claims.json`, `data/sources.json`, `data/timeline.json`, `data/compatibility.json` or `data/firmware.json`.
2. Follow the matching schema in `schemas/`. Identifiers are sequential: `C-###` (claims), `S-###` (sources), `E-###` (timeline events), `CMP-###` (compatibility rows); firmware rows are keyed by build number.
3. Every claim needs at least one supporting source. Each source must list the claims that cite it (`associated_claim_ids`); the validator checks both directions.
4. Verdicts follow `docs/RESEARCH_METHODOLOGY.md`. A `verified` verdict needs a fetched, API or tier-1 source and high confidence. Do not raise a verdict because a site or post says something works.
5. Run the validator: `python3 scripts/validate_tracker.py` (requires the `jsonschema` package).
6. Add an entry under `[Unreleased]` in `CHANGELOG.md`.
7. Open a pull request using the template.

## Review

- Every contribution stays unverified until a maintainer has checked its sources.
- Maintainers do not run code from pull requests. The validator reads local data files only and makes no network requests.
- Automated checks validate structure, privacy patterns and links. They never grant technical credibility to a claim.
- External pull requests are never merged automatically.
- Disclose any AI assistance in your pull request.

## Conduct and security

This project follows the [Code of Conduct](CODE_OF_CONDUCT.md). For security issues, including accidental publication of personal data, see [SECURITY.md](SECURITY.md).

## Licensing of contributions

Code contributions are licensed under the MIT License (see `LICENSE`). Documentation and research text is licensed under CC BY 4.0 (see `LICENSE-DOCS`). By submitting a contribution you agree to these terms. Third-party material keeps its own licence: do not submit copied text, figures or code that you do not have the right to share.
