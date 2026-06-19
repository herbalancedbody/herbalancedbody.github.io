#!/bin/bash
set -euo pipefail
REPO="C:/Users/prana/herbalancedbody-repo"
cd "$REPO"

echo "[audit] $(date +%Y-%m-%d_%H%M)"
echo "[git] status"
git status -b

echo "[assets] missing asset references"
python - <<'PY'
from pathlib import Path
repos = Path('C:/Users/prana/herbalancedbody-repo')
assets = repos / 'assets'
htmls = list(repos.rglob('*.html'))
asset_paths = {p.name for p in assets.iterdir() if p.is_file()} if assets.exists() else set()
missing = []
for path in htmls:
    text = path.read_text(encoding='utf-8', errors='ignore')
    for raw in text.split('"'):
        s = raw.strip()
        if s.startswith('/assets/'):
            fname = Path(s.split('?')[0]).name
            if fname not in asset_paths:
                missing.append((str(path.relative_to(repos)), s, fname))
for item in missing[:20]:
    print(item)
print('missing_count=' + str(len(missing)))
PY

echo "[adsense] slot placeholders"
grep -RIn "data-ad-slot=\"0000000000\"" blog || true

echo "[done]"
