# KRW release audit

**Status:** research record, 2026-11-12. KRW means a kernel read/write primitive. It is not a tool. This audit records the announced release, the checks made and the current status. It records no exploit steps.

## Timeline

Reported items are marked as reported. Event IDs refer to `data/timeline.json`.

| Date | Event | Basis | Records |
|---|---|---|---|
| 2026-10-16 | Calif.io demonstration reported at Hexacon 2026 (iPhone 18 Pro, iOS 27.0.1). The press says the vulnerabilities are not yet known | S-036 (fetched); S-037 | C-001, C-061 |
| 2026-10-17 | opa334 PSA warning of an SPTM bypass (reported) | Upstream only | C-051, E-019 |
| 2026-11-04 | A Calif.io team member said on X that kernel read/write exploit code and a write-up would follow in roughly a week (reported) | PBX Science (S-029, fetched); upstream V30 | C-022, E-013 |
| 2026-11-04 | opa334 comment (reported): a kernel exploit is expected within the week; A12 and A13 support could follow with momentarius; A14 and later still need an SPTM bypass | Upstream V31 (reprints) | C-050, E-020 |
| 2026-11-06 | Press snippet: no public tool planned | S-019 (snippet) | E-014 |
| 2026-11-11 | The one-week window lapses | Calendar arithmetic | E-022 |
| 2026-11-12 | No write-up, release or repository found. The team member's public GitHub account lists no matching repository | GitHub API (S-013) | C-049 |

## What is verified

- The announcement appears in secondary press (S-029, fetched) and in the upstream reference. The X post itself was not retrieved, so the statement is partially verified.
- Apple's iOS 27.2 notes credit the handle "pwnlambda" with a Calif.io affiliation on two entries (C-043). That is Apple's own statement.
- No KRW write-up or release for the target or any other build was found on 2026-11-12.

## What is not verified

- Which iOS versions or chips a KRW would support. The press and the upstream say the version was not stated (C-022). The upstream places the announcement in the 27.0.1 or 27.1 window, but that is not a primary statement.
- Whether any entry in Apple's notes is the bug a KRW would use. No mapping exists (see [apple-27x-cve-mapping.md](apple-27x-cve-mapping.md)).
- Whether a KRW would work on the A17 Pro. No reproduction exists (CMP-014).

## What a KRW would and would not establish

- A kernel read/write primitive is one component. It does not give a complete chain, a route to code execution on the target, persistence or a package manager (see [dependency-matrix.md](../reports/dependency-matrix.md)).
- The upstream reports opa334's tier vocabulary (V33). On that vocabulary a KRW alone would not reach a full jailbreak on A14 and later. This is second-hand and is not recorded as a claim.
- For A12 and A13, the momentarius route is already listed in Dopamine 3.0 (C-067). The A17 Pro is not in that group.

## Status and re-check triggers

- KRW status for the target: **not established**. The release is announced and was unpublished on 2026-11-12. Readiness is unchanged (LEVEL 0).
- Re-check triggers: a primary post or repository by the team member or the project; a write-up that names the iOS versions and devices; an independent reproduction. Each would be recorded as a new source and claim.
- The project does not download, run or test any code that claims to be a KRW or an exploit.

## Gaps

1. Retrieve the 2026-11-04 X post from a primary archive, if one exists.
2. Re-check the team member's GitHub account and the company's public pages at each update.
3. When a write-up exists, record its device and version scope verbatim.
