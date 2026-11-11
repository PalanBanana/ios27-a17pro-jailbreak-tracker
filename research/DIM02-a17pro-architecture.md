# DIM02: A17 Pro security architecture

**Status:** Partially researched. Apple's statements on SPTM, PPL and Memory Integrity Enforcement (MIE) are checked against Apple's own pages. Other mechanisms are listed below as not yet researched.

## Apple statements checked

| Mechanism | What Apple states | Records |
|---|---|---|
| SPTM | Supported on A15-or-later and M2-or-later SoCs. Replaces the Page Protection Layer (PPL) on supported platforms. | C-013, S-004 |
| PPL and SPTM | Enforce execution of signed and trusted code on all platforms except macOS. Page-table protection is present across all supported platforms. | C-032, S-004 |
| MIE | Built into all iPhone 17 and iPhone Air models. Names the A19 and A19 Pro chips as designed to support it. Uses the Enhanced Memory Tagging Extension (EMTE) on Apple silicon. | C-011, S-003 |
| SPTM's role in MIE | Protects the kernel allocator backing store and tag storage. | S-003 |
| TXM | Works with SPTM. Apple's guide describes the two as designed to work together. | S-004 |

## What this means for the A17 Pro

- The A17 Pro is later than the A15, so Apple's SPTM statement covers it by ordering (C-014, partially verified). The chip identity relies on Wikipedia (C-026), because Apple's product page did not expose the chip name in this check.
- Apple names A19 and A19 Pro for MIE and does not name the A17 Pro (C-012, partially verified). Treat the A17 Pro as an SPTM-class device rather than an MIE-class device, unless Apple states otherwise.
- Apple's platform guide groups A15 through A18 in one column of its feature table. The extracted text does not allow reliable reading of each cell, so feature-by-feature support for the A17 Pro is **not established** in this pass.
- The reported demonstration device uses the A20 Pro (C-002). Apple's MIE text does not name the A20 Pro, so whether that device has MIE is **not verified**. The demonstration is not evidence for the A17 Pro either way.

## Mechanisms not yet researched in this pass

- Pointer Authentication Codes: named in Apple's feature table; per-generation support not decoded.
- Kernel Integrity Protection, Fast Permission Restrictions and System Coprocessor Integrity Protection: named as table rows; not described in this pass.
- Secure Enclave: named in Apple's guide; not reviewed in depth.
- Kernel address space layout randomisation, the Secure Boot chain, AMFI, CoreTrust and trust caches: the guide sections describing these were not located in the extracted text.

These are the next research tasks for DIM02. Each will need an Apple source and a claim record before it is cited.
