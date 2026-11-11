# DIM03: SPTM research

**Status:** Partially researched. Apple's SPTM statements are checked. No public A17 Pro SPTM bypass has been verified.

## Questions and answers

| Question | Answer | Records |
|---|---|---|
| Does public A17 Pro SPTM bypass research exist? | **Not verified.** | C-015 |
| Has research been privately demonstrated? | Only reported, in a community reference. No primary evidence. | C-015, S-026 |
| Do technical disclosures exist? | None found for an A17 Pro bypass. Apple's SPTM description exists. | C-013, S-004 |
| Does a public PoC exist? | None verified. The project does not list or execute PoC code. | — |
| Has independent reproduction occurred? | None found. | CMP-002 |
| Is it compatible with iOS 27.0.1? | **Not established.** | C-015, CMP-002 |
| Does an actual jailbreak chain integrate the research? | **Not established.** No complete chain is verified for the target. | C-027 |

## Related verified facts

- SPTM is supported on A15-or-later and M2-or-later SoCs (C-013). The A17 Pro falls in that class (C-014, partially verified).
- Dopamine's documented range for A15, A16 and A17 devices ends at iOS 17.3.1 (C-016, partially verified). That range does not cover iOS 27.0.1, so it is not an SPTM bypass for the target (C-018).
- The official Dopamine commit subject lines do not mention iOS 27 (C-033).

## Community claims recorded but not verified

The community reference (S-026) reports, without primary evidence, that:

- an SPTM bypass exists, and is valid through iOS 27.0.1 (C-015);
- a kernel component is missing for that bypass to be useful;
- a 27.2 beta reportedly patched the bypass.

These are leads only. They should be treated as unverified until a primary technical source appears.

## Gaps and next steps

1. Search Apple's iOS 27 security notes for SPTM- and kernel-memory-related entries, and record their fixed-in versions where Apple states them.
2. Look for a primary technical publication on SPTM bypass. Record its date and access method before citing it.
3. Re-check Dopamine's release notes and default-branch activity on each update (C-017, C-033).
