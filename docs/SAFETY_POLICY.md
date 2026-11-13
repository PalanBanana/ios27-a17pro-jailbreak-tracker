# Safety Policy

Real devices, including devices in daily use, are treated as non-disposable. Research permission is not permission to run anything on a real device.

## 1. Operations this project never performs or recommends on any real device

The default is no device access. The only exception is the read-only identification in section 8, which does not cover any operation in this list.

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

- **Environment A, real devices**: any device a person uses in daily life. By default the project never connects to, inspects, or modifies any such device. The only exception is the read-only identification in section 8.
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

- By default the project does not connect to, inspect, or modify any maintainer-owned device. The only exception is the read-only identification in section 8, and it needs a separate authorisation from the user.
- Research in this repository never requires operating on a real device. Compatibility is assessed from public sources, and recorded only with evidence for the exact device and build.
- Any operation on a real device needs explicit, separate authorization from that device's owner for that specific operation. Publishing this repository does not provide that authorization.
- A device in daily use is not a research device. A failed experiment is not an acceptable cost of research.

## 8. Explicitly Authorized Read-Only Device Identification

This is a narrow exception to the default in sections 1, 2 and 7. It is not general permission to operate on a physical device. It applies only when the user separately authorizes it for their own device, for one session, and it must be requested again for any later session.

**Permitted fields.** ProductType, ProductVersion, BuildVersion, DeviceClass, HardwareModel and CPUArchitecture. No other device information may be collected.

**Required conditions.**

- USB connection only, to the research host.
- An existing trusted pairing only. No new pairing.
- No automatic approval of a "Trust This Computer" prompt.
- No device reboot.
- No configuration modification.
- No firmware operation of any kind.
- No application data access.
- No filesystem mounting.
- No memory extraction.
- No Sysdiagnose.
- No backup creation.

**Stop rule.** If identification would need a new trust relationship, stop immediately. Do not retry or work around it.

**Separate approval.** The user must separately approve diagnostic collection, backup operations, or any broader device access. This section does not grant any of them.

**Handling of results.** The results stay local. They are never committed, pushed or quoted in published text, and a published statement must not confirm the state of a private device. The public record keeps only the research target profile in [DEVICE_PROFILE.md](DEVICE_PROFILE.md). Device identifiers listed in section 4 are never collected.

**Who may perform it.** Only the main agent. Subagents never access a device. See [AGENT_CONFIGURATION.md](AGENT_CONFIGURATION.md).

**Meaning of the result.** Identification does not establish jailbreak compatibility, vulnerability status or readiness. The five evidence levels in [DEVICE_PROFILE.md](DEVICE_PROFILE.md) are unchanged by it.
