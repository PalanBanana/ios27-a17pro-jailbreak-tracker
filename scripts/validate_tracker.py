#!/usr/bin/env python3
"""Validate the tracker's databases, cross-references, privacy rules and links.

Usage:
    python3 scripts/validate_tracker.py              # validate the checkout this file lives in
    python3 scripts/validate_tracker.py --root DIR   # validate another checkout

The script reads local files only. It makes no network requests and never
executes content from the repository. Exit status: 0 = every check passed,
1 = at least one check failed, 2 = environment not ready (jsonschema missing).
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

# Reference date for the "not after the snapshot" checks. It is the date of the research
# snapshot in STATUS.md, so results do not depend on the clock or timezone of the machine or
# CI runner. Bump it with each research update, and never set it earlier than the newest record.
SNAPSHOT_DATE = dt.date(2026, 11, 12)

# The research target. Every compatibility row must match these values.
TARGET = {
    "device_identifier": "iPhone16,2",
    "device_name": "iPhone 15 Pro Max",
    "chipset": "A17 Pro",
    "ios_version": "27.0.1",
    "build_number": "24A446",
}

# dataset file -> (schema file, identifier field)
DATASETS = {
    "claims": ("claim.schema.json", "id"),
    "sources": ("source.schema.json", "id"),
    "timeline": ("timeline.schema.json", "event_id"),
    "compatibility": ("compatibility.schema.json", "id"),
    "firmware": ("firmware.schema.json", "build_number"),
}

REQUIRED_FILES = [
    "README.md", "README_KR.md", "CLAUDE.md", "SKILL.md", "STATUS.md", "CONTEXT.md",
    "CHANGELOG.md", "CONTRIBUTING.md", "CODE_OF_CONDUCT.md", "SECURITY.md",
    "LICENSE", "LICENSE-DOCS", ".gitignore",
    "docs/DEVICE_PROFILE.md", "docs/RESEARCH_METHODOLOGY.md", "docs/SAFETY_POLICY.md",
    "docs/FAQ.md", "docs/RECOVERY_AND_PRESERVATION.md",
    "data/claims.json", "data/sources.json", "data/timeline.json",
    "data/compatibility.json", "data/firmware.json",
    "schemas/claim.schema.json", "schemas/source.schema.json", "schemas/timeline.schema.json",
    "schemas/compatibility.schema.json", "schemas/firmware.schema.json",
    "research/DIM01-event-verification.md", "research/DIM02-a17pro-architecture.md",
    "research/DIM03-sptm-research.md", "research/DIM04-kernel-vulnerability.md",
    "research/DIM05-sandbox-escape.md", "research/DIM06-build-compatibility.md",
    "research/DIM07-exploit-chain.md", "research/DIM08-jailbreak-ecosystem.md",
    "research/DIM09-persistence.md", "research/DIM10-scam-detection.md",
    "research/DIM11-daily-driver-stability.md", "research/DIM12-recovery-safety.md",
    "research/contradictions.md",
    "reports/latest-status.md", "reports/compatibility-report.md",
    "reports/exploit-readiness.md", "reports/firmware-report.md", "reports/evidence-audit.md",
    "scripts/validate_tracker.py",
    ".github/ISSUE_TEMPLATE/new-research.yml", ".github/ISSUE_TEMPLATE/compatibility-report.yml",
    ".github/ISSUE_TEMPLATE/source-verification.yml", ".github/ISSUE_TEMPLATE/incorrect-information.yml",
    ".github/ISSUE_TEMPLATE/research-update.yml", ".github/PULL_REQUEST_TEMPLATE.md",
    ".github/workflows/validate.yml", ".github/workflows/secret-scan.yml",
]

# Level-2 section names required in README.md (English-first).
README_HEADINGS = [
    "Project Introduction", "Project Objectives", "Target Hardware", "Target Firmware",
    "Research Status", "Compatibility Dashboard", "SPTM Research", "Kernel Research",
    "Exploit Chain Status", "Jailbreak Ecosystem", "Daily Driver Readiness",
    "Firmware Preservation", "Research Timeline", "Verified Claims", "Unverified Claims",
    "Source Index", "Contribution Instructions", "Safety Policy", "License", "Disclaimer",
]

# Patterns that must not appear in published text.
PRIVACY_PATTERNS = {
    "email address": re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)+"),
    "device UDID": re.compile(r"\b[0-9A-F]{8}-[0-9A-F]{16}\b"),
    "40-character hex identifier": re.compile(r"(?<![@\w])[0-9a-fA-F]{40}\b"),  # pinned action SHAs follow "@"
    "15-digit identifier (IMEI-like)": re.compile(r"\b\d{15}\b"),
    "absolute Linux home path": re.compile(r"/home/[A-Za-z0-9_.-]+"),
    "absolute Windows user path": re.compile(r"[A-Za-z]:\\Users\\"),
    "GitHub token": re.compile(r"\b(?:ghp|gho|ghu|ghs|ghr)_[A-Za-z0-9]{36}\b|\bgithub_pat_[A-Za-z0-9_]{22,}\b"),
    "AWS access key": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    "private key block": re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
}
ALLOWED_EMAILS = {"noreply@anthropic.com"}
ALLOWED_EMAIL_SUFFIXES = ("users.noreply.github.com",)

TEXT_SUFFIXES = {".md", ".json", ".yml", ".yaml", ".py", ".txt"}
SKIP_DIRS = {".git", ".venv", "venv", "__pycache__"}
DATE_RE = re.compile(r"^(\d{4})-(\d{2})(?:-(\d{2}))?$")
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
VERIFIED_METHODS = {"fetched_full_text", "fetched_partial_text", "api_response"}


def parse_args(argv: list[str] | None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--root", default=str(Path(__file__).resolve().parent.parent),
                        help="repository root to validate (default: the checkout containing this script)")
    return parser.parse_args(argv)


def parse_date(value: str | None, allow_partial: bool) -> dt.date | None:
    """Return a date for YYYY-MM-DD (or YYYY-MM when allowed); None if invalid."""
    if not isinstance(value, str):
        return None
    match = DATE_RE.match(value)
    if not match:
        return None
    if match.group(3) is None and not allow_partial:
        return None
    try:
        return dt.date(int(match.group(1)), int(match.group(2)), int(match.group(3) or 1))
    except ValueError:
        return None


def iter_text_files(root: Path):
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        if any(part in SKIP_DIRS for part in path.relative_to(root).parts):
            continue
        if path.suffix in TEXT_SUFFIXES or path.name == ".gitignore":
            yield path


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace") if path.is_file() else ""


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    root = Path(args.root).resolve()
    try:
        import jsonschema
    except ImportError:
        print("ERROR: the jsonschema package is required. Install it with: pip install jsonschema", file=sys.stderr)
        return 2

    passes: list[str] = []
    failures: list[tuple[str, list[str]]] = []

    def check(name: str, problems: list[str]) -> None:
        if problems:
            failures.append((name, problems))
        else:
            passes.append(name)

    today = SNAPSHOT_DATE

    # 1. Required files exist.
    check("required files present",
          [f"missing: {rel}" for rel in REQUIRED_FILES if not (root / rel).is_file()])

    # 2. JSON parses and matches the schemas.
    data: dict[str, list] = {}
    parse_problems: list[str] = []
    for name in DATASETS:
        path = root / "data" / f"{name}.json"
        try:
            loaded = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            parse_problems.append(f"data/{name}.json: {exc}")
            continue
        if not isinstance(loaded, list):
            parse_problems.append(f"data/{name}.json: top level must be a JSON array")
            continue
        data[name] = loaded
    check("JSON files parse", parse_problems)

    schema_problems: list[str] = []
    for name, (schema_file, _) in DATASETS.items():
        if name not in data:
            continue
        try:
            schema = json.loads((root / "schemas" / schema_file).read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            schema_problems.append(f"schemas/{schema_file}: {exc}")
            continue
        validator = jsonschema.Draft202012Validator(schema)
        for index, record in enumerate(data[name]):
            for error in sorted(validator.iter_errors(record), key=lambda e: list(e.path)):
                location = ".".join(str(part) for part in error.path) or "(record)"
                schema_problems.append(f"data/{name}.json[{index}] {location}: {error.message}")
    check("JSON Schema compliance", schema_problems)

    # 3. Identifiers are unique within each dataset.
    dup_problems: list[str] = []
    for name, (_, key) in DATASETS.items():
        seen: set = set()
        for record in data.get(name, []):
            value = record.get(key)
            if value in seen:
                dup_problems.append(f"data/{name}.json duplicate {key}={value}")
            seen.add(value)
    check("no duplicate IDs", dup_problems)

    claims = data.get("claims", [])
    sources = data.get("sources", [])
    timeline = data.get("timeline", [])
    compatibility = data.get("compatibility", [])
    firmware = data.get("firmware", [])
    source_ids = {s.get("id") for s in sources}
    claim_ids = {c.get("id") for c in claims}

    # 4. Dates are real calendar dates and are not in the future.
    date_problems: list[str] = []

    def check_date(where: str, value, allow_partial: bool = False, allow_null: bool = False) -> None:
        if value is None and allow_null:
            return
        parsed = parse_date(value, allow_partial)
        if parsed is None:
            date_problems.append(f"{where}: '{value}' is not a valid date")
        elif parsed > today:
            date_problems.append(f"{where}: '{value}' is after the snapshot date {SNAPSHOT_DATE.isoformat()}")

    for c in claims:
        check_date(f"claim {c.get('id')} first_observed", c.get("first_observed"))
        check_date(f"claim {c.get('id')} last_checked", c.get("last_checked"))
    for s in sources:
        check_date(f"source {s.get('id')} access_date", s.get("access_date"))
        check_date(f"source {s.get('id')} publication_date", s.get("publication_date"), True, True)
    for e in timeline:
        check_date(f"event {e.get('event_id')} event_date", e.get("event_date"), True)
        check_date(f"event {e.get('event_id')} publication_date", e.get("publication_date"), True, True)
    for row in compatibility:
        check_date(f"compatibility {row.get('id')} last_checked", row.get("last_checked"))
    for f in firmware:
        check_date(f"firmware {f.get('build_number')} release_date", f.get("release_date"))
        check_date(f"firmware {f.get('build_number')} checked_on", (f.get("signing_status") or {}).get("checked_on"))
        check_date(f"firmware {f.get('build_number')} last_checked", f.get("last_checked"))
    check("valid and non-future dates", date_problems)

    # 5. Every reference resolves to a record that exists.
    ref_problems: list[str] = []
    for c in claims:
        for field in ("supporting_source_ids", "contradicting_source_ids"):
            for sid in c.get(field, []):
                if sid not in source_ids:
                    ref_problems.append(f"{c.get('id')}.{field} -> unknown source {sid}")
    for e in timeline:
        for sid in e.get("associated_source_ids", []):
            if sid not in source_ids:
                ref_problems.append(f"{e.get('event_id')} -> unknown source {sid}")
    for row in compatibility:
        for cid in row.get("evidence_claim_ids", []):
            if cid not in claim_ids:
                ref_problems.append(f"{row.get('id')} -> unknown claim {cid}")
    for f in firmware:
        for sid in f.get("source_ids", []):
            if sid not in source_ids:
                ref_problems.append(f"firmware {f.get('build_number')} -> unknown source {sid}")
    for s in sources:
        for cid in s.get("associated_claim_ids", []):
            if cid not in claim_ids:
                ref_problems.append(f"{s.get('id')} -> unknown claim {cid}")
    check("cross-references resolve", ref_problems)

    # 6. Sources list exactly the claims that cite them (both directions).
    recip_problems: list[str] = []
    for s in sources:
        expected = {
            c.get("id") for c in claims
            if s.get("id") in c.get("supporting_source_ids", []) or s.get("id") in c.get("contradicting_source_ids", [])
        }
        actual = set(s.get("associated_claim_ids", []))
        if expected != actual:
            recip_problems.append(
                f"{s.get('id')}: associated_claim_ids {sorted(actual)} but claims citing it are {sorted(expected)}"
            )
    check("sources list the claims that cite them", recip_problems)

    # 7. Verdict and evidence rules.
    rule_problems: list[str] = []
    for c in claims:
        cid = c.get("id")
        supporting = c.get("supporting_source_ids", [])
        if not supporting:
            rule_problems.append(f"{cid}: no supporting source (missing claim evidence)")
        if c.get("verdict") == "verified":
            strong = [
                s for s in sources
                if s.get("id") in supporting
                and (s.get("source_tier") == 1 or s.get("verification_method") in VERIFIED_METHODS)
            ]
            if not strong:
                rule_problems.append(f"{cid}: 'verified' needs a fetched, API or tier-1 supporting source")
            if c.get("confidence") != "high":
                rule_problems.append(f"{cid}: 'verified' claims must have high confidence")
        if c.get("verdict") == "unverified" and c.get("confidence") != "low":
            rule_problems.append(f"{cid}: 'unverified' claims must have low confidence")
    for s in sources:
        if s.get("source_tier") == 1 and s.get("verification_method") == "search_snippet_only":
            rule_problems.append(f"{s.get('id')}: a tier-1 source cannot be search-snippet-only")
    check("verdict and evidence rules", rule_problems)

    # 8. Source URLs are HTTPS and well formed.
    url_problems: list[str] = []
    for s in sources:
        parsed = urlparse(s.get("url", ""))
        if parsed.scheme != "https" or not parsed.netloc:
            url_problems.append(f"{s.get('id')}: url is not an https URL")
    check("source URLs are https", url_problems)

    # 9. Compatibility rows match the target; empty evidence only where allowed.
    compat_problems: list[str] = []
    for row in compatibility:
        target = row.get("target", {})
        for key, expected in TARGET.items():
            if target.get(key) != expected:
                compat_problems.append(f"{row.get('id')}: target.{key} is {target.get(key)!r}, expected {expected!r}")
        if not row.get("evidence_claim_ids") and row.get("status") not in {"not_established", "not_researched"}:
            compat_problems.append(f"{row.get('id')}: status '{row.get('status')}' needs evidence_claim_ids")
    check("compatibility rows match the target profile", compat_problems)

    # 10. Firmware rows use the target device identifier.
    fw_problems = [
        f"firmware {f.get('build_number')}: device_identifier {f.get('device_identifier')!r}"
        for f in firmware if f.get("device_identifier") != TARGET["device_identifier"]
    ]
    check("firmware rows use the target device identifier", fw_problems)

    # 11. Privacy and secret patterns must be absent from every text file.
    privacy_problems: list[str] = []
    for path in iter_text_files(root):
        text = path.read_text(encoding="utf-8", errors="replace")
        for label, pattern in PRIVACY_PATTERNS.items():
            for match in pattern.finditer(text):
                value = match.group(0)
                if label == "email address" and (
                    value in ALLOWED_EMAILS or value.endswith(ALLOWED_EMAIL_SUFFIXES)
                ):
                    continue
                line_no = text.count("\n", 0, match.start()) + 1
                privacy_problems.append(f"{path.relative_to(root)}:{line_no}: {label}")
    check("privacy and secret patterns absent", privacy_problems)

    # 12. Relative Markdown links resolve.
    link_problems: list[str] = []
    for path in root.rglob("*.md"):
        if any(part in SKIP_DIRS for part in path.relative_to(root).parts):
            continue
        for match in LINK_RE.finditer(path.read_text(encoding="utf-8", errors="replace")):
            target = match.group(1)
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            target_path = target.split("#", 1)[0]
            if target_path and not (path.parent / target_path).exists():
                link_problems.append(f"{path.relative_to(root)}: broken link -> {target}")
    check("internal Markdown links resolve", link_problems)

    # 13. README sections exist; Korean README mirrors the structure.
    readme = read_text(root / "README.md")
    readme_kr = read_text(root / "README_KR.md")
    heading_lines = [line for line in readme.splitlines() if line.startswith("#")]
    readme_problems = [
        f"README.md has no heading for '{needed}'"
        for needed in README_HEADINGS
        if not any(needed.lower() in line.lower() for line in heading_lines)
    ]
    en_h2 = sum(1 for line in readme.splitlines() if line.startswith("## "))
    kr_h2 = sum(1 for line in readme_kr.splitlines() if line.startswith("## "))
    if en_h2 != kr_h2:
        readme_problems.append(f"README_KR.md has {kr_h2} level-2 headings; README.md has {en_h2}")
    check("README sections present and mirrored in Korean", readme_problems)

    # 14. Target identity is stated consistently in the primary documents.
    consistency_problems: list[str] = []
    all_tokens = ["iPhone16,2", "iPhone 15 Pro Max", "A17 Pro", "27.0.1", "24A446"]
    for rel in ["README.md", "README_KR.md", "docs/DEVICE_PROFILE.md", "STATUS.md", "reports/firmware-report.md"]:
        text = read_text(root / rel)
        for token in all_tokens:
            if token not in text:
                consistency_problems.append(f"{rel} does not state '{token}'")
    check("target device information is consistent", consistency_problems)

    # 15. .gitignore excludes device artefacts and secrets.
    gitignore = read_text(root / ".gitignore")
    gi_problems = [
        f".gitignore lacks '{pattern}'"
        for pattern in ["*.ipa", "*.ipsw", "*.shsh", "*.shsh2", ".venv/", "*.p12", "*.mobileprovision", ".env"]
        if pattern not in gitignore
    ]
    check(".gitignore covers device artefacts and secrets", gi_problems)

    # Report.
    for name in passes:
        print(f"PASS  {name}")
    for name, problems in failures:
        print(f"FAIL  {name}")
        for problem in problems[:50]:
            print(f"      - {problem}")
        if len(problems) > 50:
            print(f"      ... {len(problems) - 50} more")
    total = len(passes) + len(failures)
    print(f"\n{len(passes)}/{total} checks passed")
    return 0 if not failures else 1


if __name__ == "__main__":
    sys.exit(main())
