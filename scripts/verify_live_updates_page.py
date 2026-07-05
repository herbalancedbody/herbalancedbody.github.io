#!/usr/bin/env python3
"""Live verification for the rendered updates.html page.

Fetches the live page and asserts it contains the same template blocks as
the local reference/canonical pages.
"""
from __future__ import annotations

import sys

try:
    from urllib.request import urlopen
except ImportError:  # pragma: no cover - very old Pythons
    print("urlopen unavailable; run this on Python 3.8+.")
    raise SystemExit(2)

URL = "https://herbalancedbody.github.io/updates.html"
TIMEOUT_SECONDS = 30


def _fetch(url: str) -> str:
    with urlopen(url, timeout=TIMEOUT_SECONDS) as response:
        return response.read().decode("utf-8", errors="replace")


def check_required_blocks(text: str) -> bool:
    required = [
        'href="/assets/style.css"',
        'href="/assets/cookie-consent.css"',
        'src="/assets/cookie-consent.js"',
        'aria-label="Main navigation"',
        'class="footer"',
        'id="main"',
    ]
    missing = [item for item in required if item not in text]
    if missing:
        print(f"FAIL: missing fragments in live page: {missing}")
        return False
    return True


def check_nav_links(text: str) -> bool:
    required = ["/", "/blog/", "/about.html", "/contact.html"]
    missing = [link for link in required if f'href="{link}"' not in text]
    if missing:
        print(f"FAIL: missing nav links in live page: {missing}")
        return False
    return True


def check_footer_links(text: str) -> bool:
    required = [
        "/updates.html",
        "/about.html",
        "/contact.html",
        "/privacy-policy.html",
        "/terms-and-conditions.html",
        "/affiliate-disclosure.html",
        "/medical-disclaimer.html",
        "/editorial-transparency.html",
    ]
    missing = [link for link in required if f'href="{link}"' not in text]
    if missing:
        print(f"FAIL: missing footer links in live page: {missing}")
        return False
    return True


def main() -> int:
    print(f"Fetching {URL}")
    try:
        text = _fetch(URL)
    except Exception as exc:
        print(f"FAIL: could not fetch live page: {exc}")
        return 1

    checks = [
        check_required_blocks(text),
        check_nav_links(text),
        check_footer_links(text),
    ]
    if all(checks):
        print("PASS: live updates.html template verification")
        return 0
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
