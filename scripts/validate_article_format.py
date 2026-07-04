from pathlib import Path

blog_dir = Path(__file__).parent.parent / "blog"
files = sorted([f for f in blog_dir.glob("*.html") if f.name not in ["index.html", "post-slug.html"]])

broken = []
for f in files:
    text = f.read_text(encoding="utf-8")
    has_body = '<article class="post-body">' in text
    has_script = 'querySelectorAll' in text
    if not has_body or not has_script:
        broken.append((f.name, has_body, has_script))

if broken:
    print(f"BROKEN: {len(broken)} articles missing required format")
    for name, has_body, has_script in broken:
        print(f"  {name}: post-body={has_body}, scroll-script={has_script}")
    exit(1)
else:
    print("OK: All article files match universal format")
