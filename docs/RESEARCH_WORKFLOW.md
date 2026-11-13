# Research workflow

A practical checklist for a research session. The evidence rules, tiers and readiness levels are defined in [RESEARCH_METHODOLOGY.md](RESEARCH_METHODOLOGY.md), and the safety rules in [SAFETY_POLICY.md](SAFETY_POLICY.md). This page does not repeat them. It orders the work.

All research uses public information and authorised local static-analysis artifacts. No physical device is involved at any step, except the optional, separately authorised identification in section 4.

## 1. Bounded process for each question

1. Define **one concrete question**, with the device, SoC, build and date it concerns.
2. Read the **original source** first (Apple documentation, the project's own repository, a primary publication).
3. Check **up to two** useful independent sources. Stop adding sources when they become repetitive.
4. Record **source dates**, the version or build each statement covers, and its limitations.
5. Resolve a material contradiction by recording both statements and their sources. Do not choose silently.
6. **Stop** when sources are repetitive or unavailable. If a primary source cannot be retrieved after two reasonable attempts, record `SOURCE_UNAVAILABLE`. If a finding stays unsupported, record `unverified` or `UNRESOLVED`. If nothing material changed, record `NO MATERIAL CHANGE`.

A failed technical operation is attempted at most three times. After that, take a different route or record the limitation.

## 2. Steps of a session

| # | Step | Practical notes |
|---|---|---|
| 1 | Repository inspection | `git status`, `git log`, `git fetch origin --prune`, tag list. Confirm the branch and that origin has no unseen commits. Read `STATUS.md` and `CHANGELOG.md` first |
| 2 | Existing evidence review | Search before reading: `rg` for a claim ID or term, `jq` for a record. Do not re-read whole reports or databases |
| 3 | Primary-source identification | Prefer the vendor or project's own page, repository or API at a fixed commit. Record the URL and the access date |
| 4 | Secondary corroboration | At most two independent sources. A community post is never the sole evidence of a vulnerability |
| 5 | Device and firmware scope | Write the exact device, product type, SoC, version and build for every statement. Never infer exact-build compatibility from another SoC or from a version list |
| 6 | Evidence classification | Tier 1 to 4, verification method and verdict, as in the methodology. Separate an official architectural description from device-specific implementation evidence |
| 7 | Claim creation and update | Update an existing claim when one covers the point. Supersede, do not delete. Never turn a hypothesis into a verified claim. `verified` needs high confidence and a fetched, API or tier-1 source |
| 8 | Source database maintenance | One record per source, with the method used. A search snippet is a lead only. Keep each source's `associated_claim_ids` equal to the claims that cite it |
| 9 | Timeline maintenance | Add dated events only for things that happened and are sourced. Dates are ISO 8601 and not after the validator's snapshot date |
| 10 | Compatibility matrix updates | Change a row only on exact-device evidence. Keep the readiness level unless the methodology's criteria are met |
| 11 | Report generation | Regenerate the derived documents from the data where a generator exists. Keep English and Korean README files structurally parallel |
| 12 | Technical review | The main agent re-checks every high-impact finding independently, including anything a subagent returned. See [AGENT_CONFIGURATION.md](AGENT_CONFIGURATION.md) |
| 13 | Validation | `python3 scripts/validate_tracker.py`. Fix failures. Never weaken a check |
| 14 | Secret and privacy scan | Run the secret scanner and search the staged diff for identifiers, personal paths and device state. See `CLAUDE.md` rules 5 and 10 |
| 15 | GitHub publication | Review `git diff`, stage only intended files, commit normally, push as a fast-forward, then check the CI run and the published files. No force-push, no history rewrite, no tag moves |

## 3. Rules that apply at every step

- Separate **a statement in a source** from **a verified technical result**. A repository statement is not an independent reproduction.
- Static string presence, a manifest component name or a function count is not evidence of a running feature.
- Quote only short, verified phrases, and check each quotation against the fetched text. Summarise everything else with attribution.
- Do not write or link exploit steps, offsets, selectors or bypass code. Do not run, build or install a third-party exploit or tool.
- Code-level comparison against later builds and mapping of binaries to advisories remain declined. Metadata-level comparison is allowed.
- Never record a maintainer's personal device state. The target is described only as a profile. Results of the optional identification in section 4 stay local.
- Do not create a release unless the owner asks. Clarification and correction go to `main` with a normal commit.

## 4. Optional device identification phase

This phase is optional and runs only when the user has explicitly authorised it for the session. Public source analysis and static reverse engineering never need it.

- The conditions, the stop rule and the handling of results are in [SAFETY_POLICY.md](SAFETY_POLICY.md) section 8. Only the main agent performs it.
- It is limited to six metadata fields: ProductType, ProductVersion, BuildVersion, DeviceClass, HardwareModel and CPUArchitecture.
- If it would need a new pairing or trust relationship, stop and record the limitation. Continue with public sources.
- Device identification does not establish jailbreak compatibility or vulnerability status. It leaves the evidence levels, the readiness level and every verdict unchanged.
- Diagnostic collection, backups and any broader device access need a separate approval from the user.
