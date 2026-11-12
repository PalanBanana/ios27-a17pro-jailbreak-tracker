# Safety Policy

Real devices, including devices in daily use, are treated as non-disposable. Research permission is not permission to run anything on a real device.

## 1. Operations this project never performs or recommends on any real device

- Jailbreak installation or any jailbreak attempt.
- Kernel exploit or SPTM bypass execution on the device.
- Bootloader modification, firmware flashing, IPSW restore, DFU or Recovery Mode operation.
- Firmware downgrade, firmware update, factory reset.
- NVRAM modification, root filesystem modification.
- Bootstrap, package-manager or tweak installation.
- Installing unknown IPA files, unknown configuration profiles, or experimental builds.
- Unrequested device reboots, or any operation that could compromise normal daily use.

Permission to research a jailbreak is not permission to execute one. Permission to read source code is not permission to run exploit code.

## 2. Environments

- **Environment A, real devices**: any device a person uses in daily life. The project never connects to, inspects, or modifies any such device.
- **Environment B, research workspace**: repository inspection, static reading, documentation, version comparison, data validation. No exploit code is run here.
- **Environment C, isolated test environment**: optional, for reviewed tools only. Emulators do not reproduce A17 Pro hardware behaviour, so emulator results are not compatibility evidence.

Experimental code is never moved onto a real device.

## 3. Third-party code

- Maintainers do not execute code from pull requests or from downloads.
- The validator reads local data files only. It makes no network requests.
- Downloads advertising iOS 27.0.1 jailbreaks are not verified to relate to any public research. Treat them as untrusted and potentially malicious.

## 4. Data protection

Never collect or publish:

- Serial numbers, UDIDs, ECIDs, IMEI or EID values.
- Apple Account information, authentication tokens or passwords.
- Personal backups, personal application data, or private device logs.
- Real names of private individuals connected to handles, unless a primary source confirms the link and the publication is necessary.

Run the privacy and secret checks before any commit (`scripts/validate_tracker.py` and the secret-scanning workflow).

## 5. Scam and malware awareness

- Treat installation packages, profiles and "jailbreak" tools from unverified sources as malware until shown otherwise.
- Do not pay for jailbreak access. Verify any claim against the sources in `data/sources.json`.
- Report suspected scams using the new-research issue template, choosing 'Scam or fake-tool report'.

## 6. Responsibility

This project is an information resource. It is not legal advice. Owners are responsible for complying with the law where they live and with the terms of their device, operating system and service agreements.

## 7. Real devices

- The project does not connect to, inspect, or modify any maintainer-owned device.
- Research in this repository never requires operating on a real device. Compatibility is assessed from public sources, and recorded only with evidence for the exact device and build.
- Any operation on a real device needs explicit, separate authorization from that device's owner for that specific operation. Publishing this repository does not provide that authorization.
- A device in daily use is not a research device. A failed experiment is not an acceptable cost of research.
