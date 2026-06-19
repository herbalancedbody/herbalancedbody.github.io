# Default Format Rules for HerBalancedBody Articles and Category Pages

## Canonical Article Page Requirements
Each new article must match `blog/home-workout-plan-for-women.html` exactly in structure and features. Mandatory components:
- Complete head with charset, viewport, author, theme-color
- Google Analytics and AdSense scripts
- Exact page title and meta description
- Robots meta: `index, follow, max-image-preview:large`
- Canonical URL, Open Graph tags, Twitter Card tags, Pinterest rich pin
- OG/Twitter image assets and alt text
- Stylesheet reference `/assets/style.css`
- Two JSON-LD schema blocks: Article + BreadcrumbList
- Post meta row with Published/Updated/Reading time
- Lead intro paragraph(s)
- In-content ad zones with `.ad-zone` markup
- Internal links to related articles
- Structured H2/H3 section hierarchy with semantic IDs
- Related Reading links section
- FAQ section with at least one question
- Editorial Transparency section
- Author bio section
- Table of Contents sidebar (MANDATORY):
  - `<aside class="post-sidebar">` with sticky widget
  - `<h4>Table of Contents</h4>`
  - `<ul class="toc-list">` with links matching actual H2/H3 IDs
- Active scroll-highlight script (MANDATORY):
  - `const sections = document.querySelectorAll(".post-body h2[id], .post-body h3[id]");`
  - `const navLinks = document.querySelectorAll(".toc-list a");`
  - scroll handler that adds/removes `.active` on TOC links
- 3000+ word minimum before publishing

## Canonical Category Page Requirements
Each new category page must match `blog/category/weight-loss-after-40.html` exactly in structure and features. Mandatory components:
- Complete head with GA, AdSense, meta, OG, Twitter, schema
- CollectionPage + BreadcrumbList JSON-LD
- Hero section with category title and description
- Category intro section
- Blog grid with article cards or placeholder cards
- Related topics section with category links
- Footer with site links
- No "Coming Soon" placeholders; use real article cards

## Enforcement Rule
Every new article or category page created by Hermes must be verified against these rules before commit. Missing features must be patched immediately.
