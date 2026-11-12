# DIM03: SPTM research

**Status:** Researched for this pass. Apple's SPTM statements, an independent academic analysis and Dopamine's release notes are checked. No public SPTM bypass for the A17 Pro or iOS 27.0.1 is verified. The full graded audit is in [sptm-evidence-audit.md](sptm-evidence-audit.md).

## Questions and answers

| Question | Answer | Records |
|---|---|---|
| Does a public A17 Pro SPTM bypass exist? | **Not verified.** | C-051, C-066 |
| Has an SPTM bypass been privately demonstrated? | Reported only, second-hand. The primary PSA was not retrieved. | C-051, C-050, S-026 |
| Do technical disclosures exist? | Apple's architecture statements (SPTM on A15 and later) and an independent paper about iOS 18.4 on an iPhone 16. None covers the A17 Pro or iOS 27. | C-013, C-059, C-060 |
| Is a public PoC known? | None for an SPTM bypass applicable to the target. Dopamine's public bypass covers iOS 16.5.1 to 17.3.1. | C-065, C-066 |
| Has independent reproduction occurred? | None found. | CMP-002 |
| Is it compatible with iOS 27.0.1? | **Not established.** | C-051, CMP-002 |
| Does an actual jailbreak chain integrate the research? | **Not established.** No complete chain is verified for the target. | C-027 |

## Verified related facts

- SPTM is supported on A15-or-later and M2-or-later SoCs and replaces PPL on supported platforms (C-013).
- The A17 Pro is in that class. The grade stays partially verified, because the guide does not name the device (C-014).
- PPL and SPTM enforce execution of signed and trusted code on all platforms except macOS (C-032).
- Dopamine 3.0 includes a Titan PPL/SPTM bypass for all devices on iOS 16.5.1 to 17.3.1 (C-065). Its notes state that real-device SPTM support ends at 17.3.1 because no bypass is known for iOS 17.4 and later (C-066).
- Apple's iOS 27 and 27.2 advisory text has no SPTM, TXM, PPL, AGX or IOGPU term (C-073).
- The arXiv analysis covers an iPhone 16 on iOS 18.4 and 18.5 and does not mention the A17 Pro (C-060).

## Community and upstream claims recorded but not verified

The community reference (S-026) reports, without a primary source, that:

- an SPTM bypass exists and is valid through iOS 27.0.1, reportedly patched in a 27.2 beta (C-051);
- the bypass would be used for devices from A14 onward, which would still need a further n-day step (C-050);
- the existing kernel bugs cover iOS only up to 26.0.1 (C-054).

These are leads only. They remain unverified until a primary technical source appears.

## Gaps and next steps

1. Retrieve the 2026-10-17 opa334 PSA from a primary archive, if one exists. Record its date and access method.
2. Look for a primary technical SPTM publication that names device families and iOS versions.
3. Re-check Dopamine's release notes at each update (C-065 to C-068).
4. Record any Apple statement that names SPTM or TXM with affected versions.
