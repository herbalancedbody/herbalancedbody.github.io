#!/usr/bin/env python3
import os, re, json, sys
from pathlib import Path

repo = Path('.')

articles = list((repo / 'blog').glob('*.html'))
pages = [p for p in repo.glob('*.html') if p.name not in ('index.html',)]

errors = []
warnings = []

for f in sorted(articles + pages):
    rel = f.relative_to(repo)
    txt = f.read_text(encoding='utf-8')
    
    # 1) JSON-LD parse + duplicate keys
    blocks = re.findall(r'<script type="application/ld\+json">(.*?)</script>', txt, re.DOTALL)
    for i, s in enumerate(blocks):
        try:
            json.loads(s)
        except json.JSONDecodeError as e:
            errors.append((str(rel), f'JSON-LD block {i} parse error: {e}'))
        def scan(obj, path=''):
            if isinstance(obj, dict):
                keys = list(obj.keys())
                if len(keys) != len(set(keys)):
                    errors.append((str(rel), f'Duplicate key(s) at {path}: {[k for k in keys if keys.count(k)>1]}'))
                for k, v in obj.items():
                    scan(v, f'{path}.{k}')
            elif isinstance(obj, list):
                for idx, v in enumerate(obj):
                    scan(v, f'{path}[{idx}]')
        try:
            scan(json.loads(s))
        except Exception:
            pass
    
    # 2) Title check
    m = re.search(r'<title>(.*?)</title>', txt, re.IGNORECASE)
    title = m.group(1).strip() if m else ''
    if not title or title in ('#', 'Her Balanced Body'):
        warnings.append((str(rel), 'Missing or generic <title>'))
    
    # 3) Canonical href
    m = re.search(r'<link rel="canonical" href="([^"]+)"', txt, re.IGNORECASE)
    if not m:
        errors.append((str(rel), 'Missing canonical href'))
    else:
        canonical = m.group(1)
        expected_slug = f.name if f.name != 'index.html' else ''
        if expected_slug and expected_slug not in canonical:
            warnings.append((str(rel), f'Canonical may be mismatched: {canonical}'))
    
    # 4) H2/H3 unique IDs
    h_ids = re.findall(r'<h[23][^>]*id="([^"]+)"', txt, re.IGNORECASE)
    dups = [hid for hid in h_ids if h_ids.count(hid) > 1]
    if dups:
        errors.append((str(rel), f'Duplicate heading IDs: {list(set(dups))}'))
    
    # 5) Empty/placeholder links
    bad_links = re.findall(r'href="#"|href=""|href="javascript:void\(0\)"', txt, re.IGNORECASE)
    if bad_links:
        warnings.append((str(rel), f'Placeholder links found: {len(bad_links)}'))
    
    # 6) wordCount/timeRequired in JSON-LD Article
    for s in blocks:
        try:
            j = json.loads(s)
        except Exception:
            continue
        if j.get('@type') == 'Article':
            if not j.get('wordCount'):
                warnings.append((str(rel), 'Article JSON-LD missing wordCount'))
            if not j.get('timeRequired'):
                warnings.append((str(rel), 'Article JSON-LD missing timeRequired'))

# 7) ads.txt presence
if not (repo / 'ads.txt').exists():
    errors.append(('ads.txt', 'Missing at repo root'))

print('\n=== HBB PREFLIGHT REPORT ===\n')
if not errors and not warnings:
    print('ALL CLEAR — no issues found.\n')
else:
    if errors:
        print('ERRORS:')
        for rel, msg in errors:
            print(f'  {rel}: {msg}')
        print()
    if warnings:
        print('WARNINGS:')
        for rel, msg in warnings:
            print(f'  {rel}: {msg}')
        print()

sys.exit(0 if not errors else 1)
