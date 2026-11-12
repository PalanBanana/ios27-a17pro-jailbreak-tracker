# FAQ

**Is there a jailbreak for my iPhone 15 Pro Max on iOS 27.0.1?**
No verified public jailbreak for this device and build has been found. Calif.io reportedly demonstrated an untethered iOS 27.0.1 jailbreak on an iPhone 18 Pro at Hexacon 2026 (C-001, partially verified). That demonstration used an A20 Pro device, so it is not evidence for the A17 Pro (C-002). No public write-up or tool was found (C-027, C-028). The project's decision is NO-GO.

**Did Calif.io really demonstrate it?**
Press outlets reported a live demonstration on 2026-10-16. Hexacon 2026 took place on 16 and 17 October 2026 in Paris (S-011). Apple's own security notes credit Calif.io researchers for four CVE entries (C-005). The talk listing and any primary Calif.io material were not located, so the demonstration itself is partially verified.

**Why does the project say "reported" so often?**
Because most of what is known about the demonstration comes from press coverage. A reported fact is not a verified fact, and the records say which is which.

**Which firmware does the research target use?**
The research target profile is iPhone 15 Pro Max (A17 Pro, `iPhone16,2`) running iOS 27.0.1 (build 24A446). The project does not check the installed state of any individual device. See [DEVICE_PROFILE.md](DEVICE_PROFILE.md).

**Is the iOS 27.0.1 build still signed?**
Unresolved. A third-party index marked build 24A446 as not signed on 2026-11-12 (ipsw.me, S-014; C-021). A community reference reported it as still signed on 2026-11-02, and that report is not verified. Apple has not published a signing record that this project could check. Do not assume that a restore to 27.0.1 is possible. See `docs/RECOVERY_AND_PRESERVATION.md`.

**Should I update or downgrade?**
This project does not recommend either. Those decisions belong to the device owner, who should weigh backups, signing status and the project's safety policy. The project does not change update settings or perform updates.

**Can you give me the tool or the exploit?**
No. The project does not publish, link to or explain exploit code or jailbreak tools, and it never runs them.

**Is this project affiliated with Apple, Calif.io, Hexacon or the Dopamine project?**
No. It is an independent research and compatibility tracker.

**Did an AI write this?**
Drafting and research assistance was provided by Claude, an AI model made by Anthropic. The maintainer reviews the work. Apple's security notes name "Claude and Anthropic Research" alongside Calif.io for two CVE entries (C-006). The project quotes Apple's wording and does not infer anything about how that collaboration worked.

**How do I report a scam or a bad claim?**
Use the new-research template (choose 'Scam or fake-tool report') or the incorrect-information template. Include the URL, the date you saw it, and why you think it is wrong. Do not include any personal data or device identifiers.

**How often is the data updated?**
When the maintainer runs an update, following the procedure in `docs/RESEARCH_METHODOLOGY.md`. Every record carries a `last_checked` date.

**Where do I start reading?**
`STATUS.md` for the current position, `data/claims.json` for the claims, and `research/contradictions.md` for conflicting reports.
