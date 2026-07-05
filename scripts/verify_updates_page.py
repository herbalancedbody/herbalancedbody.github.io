#!/usr/bin/env python3
"""Verification for HBB page template consistency."

Validates that `updates.html` matches the structural template used by
canonical content pages such as `about.html` and `contact.html`, and that
`sitemap.xml` includes the updates page.

Run locally or in CI:
    python scripts/verify_updates_page.py
"""
from __future__ import annotations

import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable

REPO_ROOT = Path(__file__).resolve().parent.parent
UPDATES_PATH = REPO_ROOT / "updates.html"
SITEMAP_PATH = REPO_ROOT / "sitemap.xml"
REFERENCE_PATHS = [
    REPO_ROOT / "about.html",
    REPO_ROOT / "contact.html",
]


@dataclass
class Check:
    name: str
    ok: bool = True
    details: list[str] = field(default_factory=list)

    def fail(self, detail: str) -> None:
        self.ok = False
        self.details.append(detail)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def contains_all(text: str, fragments: Iterable[str]) -> bool:
    return all(fragment in text for fragment in fragments)


def first_missing(text: str, fragments: Iterable[str]) -> str | None:
    for fragment in fragments:
        if fragment not in text:
            return fragment
    return None


def check_required_blocks(text: str) -> Check:
    result = Check(name="required_blocks")
    required = [
        '<link rel="stylesheet" href="/assets/style.css"',
        '<link rel="stylesheet" href="/assets/cookie-consent.css"',
        '<script src="/assets/cookie-consent.js"></script>',
        '<nav class="nav" aria-label="Main navigation">',
        '<footer class="footer">',
        '<main id="main">',
    ]
    missing = [fragment for fragment in required if fragment not in text]
    if missing:
        result.fail(f"Missing required fragments: {missing}")
    return result


def check_nav_links(text: str) -> Check:
    result = Check(name="nav_links")
    required_links = ["/", "/blog/", "/about.html", "/contact.html"]
    missing = [link for link in required_links if f'href="{link}"' not in text]
    if missing:
        result.fail(f"Missing nav links: {missing}")
    return result


def check_footer_links(text: str) -> Check:
    result = Check(name="footer_links")
    required_links = [
        "/updates.html",
        "/about.html",
        "/contact.html",
        "/privacy-policy.html",
        "/terms-and-conditions.html",
        "/affiliate-disclosure.html",
        "/medical-disclaimer.html",
        "/editorial-transparency.html",
    ]
    missing = [link for link in required_links if f'href="{link}"' not in text]
    if missing:
        result.fail(f"Missing footer links: {missing}")
    return result


def check_analytics_presence(text: str) -> Check:
    result = Check(name="analytics_presence")
    fragments = [
        "www.googletagmanager.com/gtag/js?id=G-P5N3NDE5R4",
        "pagead2.googlesyndication.com/pagead/js/adsbygoogle.js",
        'client="ca-pub-7940751159869157"',
    ]
    missing = [fragment for fragment in fragments if fragment not in text]
    if missing:
        result.fail(f"Missing analytics/adsense fragments: {missing}")
    return result


def check_sitemap_includes_updates() -> Check:
    result = Check(name="sitemap_includes_updates")
    text = read_text(SITEMAP_PATH)
    if "https://herbalancedbody.github.io/updates.html" not in text:
        result.fail("sitemap.xml missing updates.html loc")
    return result


def check_reference_parity(reference_texts: list[str], updates_text: str) -> Check:
    result = Check(name="reference_parity")
    expected = [
        '<nav class="nav" aria-label="Main navigation">',
        '<footer class="footer">',
        '<link rel="stylesheet" href="/assets/style.css"',
        '<link rel="stylesheet" href="/assets/cookie-consent.css"',
        '<script src="/assets/cookie-consent.js"></script>',
    ]
    present_in_references = all(fragment in "".join(reference_texts) for fragment in expected)
    present_in_updates = all(fragment in updates_text for fragment in expected)
    if present_in_references and not present_in_updates:
        result.fail("updates.html is missing template fragments present in reference pages")
    return result


def run_local_checks() -> list[Check]:
    if not UPDATES_PATH.exists():
        return [Check(name="updates_exists", ok=False, details=[f"{UPDATES_PATH} missing"])]

    updates_text = read_text(UPDATES_PATH)
    reference_texts = [read_text(path) for path in REFERENCE_PATHS if path.exists()]

    return [
        check_required_blocks(updates_text),
        check_nav_links(updates_text),
        check_footer_links(updates_text),
        check_analytics_presence(updates_text),
        check_sitemap_includes_updates(),
        check_reference_parity(reference_texts, updates_text),
    ]


def summarize(checks: Iterable[Check]) -> bool:
    all_ok = True
    for check in checks:
        status = "PASS" if check.ok else "FAIL"
        print(f"[{status}] {check.name}")
        for detail in check.details:
            print(f"       - {detail}")
        if not check.ok:
            all_ok = False
    return all_ok


def main() -> int:
    checks = run_local_checks()
    ok = summarize(checks)
    if not ok:
        print("\nVerification failed.")
        return 1
    print("\nVerification passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
