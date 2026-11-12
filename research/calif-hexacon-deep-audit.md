# Calif.io and Hexacon audit

**Status:** research record, 2026-11-12. Scope: the Calif.io demonstration reported from Hexacon 2026 in Paris on 2026-10-16, the company's published credits, and statements attributed to its team members. Individuals are not named. The upstream file names some of them, and this audit does not repeat those names.

## Directly sourced facts

| Fact | Source | Grade | Records |
|---|---|---|---|
| Hexacon 2026 took place on 16 and 17 October 2026 in Paris | S-011 (hexacon.fr, homepage) | Verified | C-001 (partial) |
| The programme pages for the talk were unavailable to this review | S-011 (requests returned 404) | Not verified | C-001 |
| Press reports an untethered jailbreak shown on an iPhone 18 Pro (A20 Pro) at Hexacon, running iOS 27.0.1 | S-036 (heise English, fetched, dated 2026-10-16); S-037 (heise German, dated 16.10.2026) | Partially verified | C-001, C-002 |
| The vulnerabilities used are not yet known | S-036, S-037 | Verified as the press's statement | C-001 |
| The company's X profile had no further details at the press date | S-036 | Reported | C-001 |
| The press describes the reboot persistence as the first since iOS 9 | S-036 | Press claim, unverified | C-075 |
| t3n reports that AI helped find the exploit chain (dated 18.10.2026) | S-038 (fetched) | Reported; method not confirmed | C-061, C-076 |
| Apple's iOS 27 page credits Calif.io on four entries | S-001 | Verified | C-038 |
| Apple's iOS 27.2 page credits Calif.io on six entries | S-033 | Verified | C-042, C-043 |
| The iOS 27 page's 2026-10-19 and 2026-10-26 entry notes | S-001 | Verified | C-071 |
| The iOS 27 Calif.io entry CVE-2026-28968 is a kernel corruption entry | S-001 | Verified | C-037, C-038 |
| A 2026-11-04 article relays a team member's statement that code and a write-up would follow in about a week | S-029 (PBX Science, fetched) | Reported | C-022 |
| A 2026-11-06 snippet reports no public tool planned | S-019 (snippet only) | Lead only | E-014 |

## Secondary interpretations (not adopted)

- heise's headline says AI helps create the jailbreak (C-061). The article body says the team's method is not known.
- heise says "the first reboot-proof jailbreak since iOS 9" (C-075). The upstream says a 2021 public untethered jailbreak contradicts that framing. This review does not adopt either framing.
- t3n presents an AI-assisted comparison of an iOS 27.2 beta with iOS 27.0.1 as established (C-076). heise's German edition calls the same comparison theoretically possible. No team statement on the method was located.

## Statements attributed to team members (upstream only; not retrieved)

- An interview dated 2026-10-19: no end-user tool is planned, and a proof of concept might follow a patch (C-077). The jailbreak "basically applies to any iPhone running iOS 27.0.1" (C-052). The chain is largely fixed in the 27.2 beta (V11, see [upstream-reconciliation.md](upstream-reconciliation.md)).
- A 2026-11-04 video of a Lockdown Mode device updated over the air to 27.2, with a plugin still working after reboot (C-053). The upstream reports that the update segment was edited.
- Two bare SHA-256 hash posts, one on 2026-10-14 and one on 2026-10-30 (E-027). Their content is unknown.
- An official line that everything "will be released in due time" (upstream V2). Not retrieved.

## A20 Pro demonstration and the A17 Pro target

| Point | Demonstration (press and upstream) | Target |
|---|---|---|
| Chip | A20 Pro (iPhone 18 Pro) (C-002) | A17 Pro (iPhone 15 Pro Max) (C-026) |
| Build | 24A446 (upstream V1) | 24A446 |
| SPTM class | A15 or later (E1 in [sptm-evidence-audit.md](sptm-evidence-audit.md)); the press does not describe the demonstration's SPTM handling | A15 or later (C-014, partially verified) |
| Memory tagging (MIE) | Apple names MIE for A19 and A19 Pro (C-011). The upstream says the chain bypasses MIE on A19 and A20 (V10), which is unverified | Apple does not name the A17 Pro for MIE (C-012) |
| Verified status | Press demonstration (partially verified) | Not established |

The two devices share a build. They differ in chip and, on Apple's text, in memory-protection generation. The demonstration therefore does not establish A17 Pro support. An argument that relies on MIE does not transfer to the A17 Pro either way.

## What is not verified

- Any technical write-up or code for the demonstration.
- The demonstration's vulnerabilities, chain, hardware and firmware beyond the press's statements.
- Whether any entry in Apple's notes belongs to the demonstration's chain. The six Calif.io credits on the 27.2 page are not kernel-memory entries (C-042). The 27.0 entry CVE-2026-28968 is a kernel corruption entry, but its link to the demonstration is not established.

## A demonstration is not a public tool

Even a verified demonstration does not create a public tool. The team's reported plan is not to release an end-user tool (C-077). Press coverage on 2026-11-06 reports no public tool planned (E-014).

## Not reproduced

Personal names, ages, locations and account links about individuals in the upstream file. This follows the repository's privacy rules and METHODOLOGY section 4.7.

## Gaps and next steps

1. If the programme pages become available, record the talk title and abstract, with the access date.
2. Retrieve the original posts only through a primary archive.
3. If a write-up is published, record its device and version scope verbatim.
