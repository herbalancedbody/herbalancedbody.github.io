# HerBalancedBody default format rules

Read this before creating or normalising HerBalancedBody pages. It encodes the exact structure used by the current repo so future articles and categories are generated consistently.

## Article-page rules
- Path: `/blog/<slug>.html`; slugs are lowercase words with hyphens
- Head: UTF-8, viewport set, author meta set
- Include Google Analytics gtag snippet already used on this site
- Include Google AdSense snippet already used on this site
- Title format: `<Topic> | Her Balanced Body`
- Meta description: concise benefit-focused sentence
- Robots: `index, follow, max-image-preview:large`
- Canonical: `https://herbalancedbody.github.io/blog/<slug>.html`
- OpenGraph type: `article`; image: `https://herbalancedbody.github.io/assets/<slug-without-blog-prefix>300.png`
- Twitter card: `summary_large_image`; same image as OG
- Stylesheet: `/assets/style.css`
- JSON-LD: `Article` + `BreadcrumbList`
- Body: skip-nav link; nav with Blog active; main content; optional sticky TOC
- Images: present whenever possible; use `300.png` naming
- Schema image URL: matches OpenGraph image
- Internal links: at least 3 relevant existing posts/categories

## Category-page rules
- Path: `/blog/category/<slug>.html`
- Intro: two short paragraphs explaining the category focus
- Cards: tag, title link, short description
- Bottom section: Related Topics with 3 category cards
- Include the same shared analytics/AdSense snippets as article pages
- Avoid Coming Soon placeholders whenever possible

