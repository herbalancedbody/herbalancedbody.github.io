# Her Balanced Body — AdSense “Low Value Content” Recovery Plan

Current AdSense state (2026-07-03/04):  
Site: https://herbalancedbody.github.io  
Status: Needs attention — Low value content  
Ads.txt: Authorized

This repository already has strong foundations: 30+ article pages, structured data, medical disclaimer, editorial transparency page, GA4 tracking, and substantive body content (~4,000–5,000 words in many posts).  
The “Low value content” flag is almost never about raw word count. It is about **originality, authorship, expertise signals, editorial transparency, and perceived value beyond template text**.

---

## Phase 1 — Fix hard failures / obvious red flags

### 1.1 Remove or replace the template stub `post-slug.html`
Status: `noindex, follow` + placeholder text. AdSense crawlers may still visit it and treat it as thin / low-value site content.

Action: Delete it now.

Permanent protection:  
Add a build-time guard so the template cannot exist in deployed output:
- If template lives in `/blog/post-slug.html`, remove it before publish.
- If it lives in `/assets/templates/`, keep it there with `X-Robots-Tag: noindex`.

### 1.2 Tighten canonical + robots hygiene
- `blog/index.html` already has non-canonical category pages — ensure they are either `noindex` or have real unique intro text above the link list.
- `sitemap.xml` should not list template stubs, tag pages, or dead slots.

### 1.3 Audit page-value distribution
AdSense reviewers scan for pages that feel “thin” or low-signal.

Do these checks before moving to Phase 2:
- Category pages should each have at least 2–3 sentences of unique, original intro text (not a generic tagline).
- Author/author-box area is currently missing in article layout; add it.
- Article metadata must match actual content: wordCount / timeRequired should be accurate after rewrites.

---

## Phase 2 — Strengthen E-E-A-T and authorship

### 2.1 Adopt named, human-byline authorship
Current byline:  
- `<meta name="author" content="Her Balanced Body Editorial Team">`  
- JSON-LD author: “Her Balanced Body Editorial Team”

Risk: “Editorial Team” is an anonymous/non-human entity. AdSense/Quality Raters want named individuals.

Minimum lift (no identity change needed):  
- Change author meta to a real person + role.
- Add visible byline and author bio on each post.
- Populate `/about.html` with bio, photo, and a stated focus area.

Example mapping:
- Hormones / perimenopause → named byline with relevant framing
- Strength training / workouts → named byline with relevant framing
- Nutrition / balanced plate / protein → named byline with relevant framing

Format:
```json
"author": {
  "@type": "Person",
  "name": "Caroline Doe",
  "jobTitle": "Wellness Writer, Her Balanced Body",
  "url": "https://herbalancedbody.github.io/about.html"
}
```

If you prefer pseudonymity, at minimum use a consistent named persona with an about page explanation.

### 2.2 Publish the About/Editor pages in human-readable form
`about.html` exists, but strengthen it:
- Mission statement
- Editorial process (“How articles are researched, reviewed, and updated”)
- Who is responsible for medical boundaries
- Contact email visible in footer and about page
- Author headshot + credentials/experience framing
- Last updated date on About/Editorial pages

### 2.3 Add inline “Reviewed by / Sources” signals
Current signal: generic medical disclaimer.  
Better signal: article-level credibility.

At the bottom of each post:
```
Last medically reviewed: June 2026  
Sources: [NIH / PubMed-style references or named material]  
Reviewed for accuracy by: [Name or role]
```

Even simplified, this is stronger than a global disclaimer alone.

---

## Phase 3 — Improve originality and first-party value

### 3.1 Original graphics > generic placeholders
AdSense reviewers associate stock-only imagery with low-value content.

Priority assets:
- Real author photos
- Custom simple diagrams: hormone timeline, plate method visual, strength routine layout
- Data-presentation style images: cited studies in table form, before/after framework charts
- Infographics showing balanced plate proportions, protein timing, cortisol curve

Use `/assets/` in repo. Compress to reasonable sizes.

### 3.2 Add personal / case-style framing without promising outcomes
- opening “what this is for” paragraphs are good, but add 1–2 short real-world scenarios per article
- include specific audience segments: “If you’re restarting after a long break…” / “If you’re in early perimenopause…” / “If you prefer short home workouts…”

This raises semantic uniqueness and reader-specific value.

### 3.3 Internal linking density and hub-and-spoke structure
Current state: articles link to related posts via text anchors.  
Strengthen this:
- Each article should link to 3–5 other HBB articles naturally.
- Add “Next article in this series” or related reading cards.
- Category pages should be actual hubs, not just link lists.

Better structure helps crawlers understand topical depth, which correlates with perceived value.

### 3.4 Add a real non-generic FAQ block per article (not boilerplate)
Remove generic `Question one? → Answer this question clearly` placeholders across the template set.  
Replace with real, high-search-intent questions for each topic, answered in actual paragraphs.

---

## Phase 4 — Ad experience and site maturity signals

### 4.1 Ad density / placement hygiene
AdSense reviewers sometimes associate thin content with aggressive ad layouts.  
Check realism:
- Total visible ad units per page should be proportional to content depth.
- Above-the-fold ads should not dominate the viewport.
- Keep “Advertisement” labels visible and consistent.

### 4.2 Navigation maturity
Add these UX signals if missing:
- Homepage has a visible newsletter / email capture path with real benefit statement
- Contact page has reply-capable email, not just a form that may be `mailto` lazy
- Legal/editorial pages include effective dates and last-updated lines
- Search works or is replaced with a “Browse topics” index page

### 4.3 Increase crawl-passive content signals
- `sitemap.xml` dates should reflect real publish/update dates.
- Add `/humans.txt` with simple contact info and repo/origin note.
- Consistent brand mentions / social profiles in structured data.

---

## Phase 5 — Verification loop before resubmission

1. Local audit checklist:
   - [ ] No template stub pages in `/blog/`
   - [ ] Every article `<title>` and `<meta description>` is unique and non-boilerplate
   - [ ] Every `wordCount` in JSON-LD matches actual rendered text length
   - [ ] Every article has visible byline + author bio block
   - [ ] Every article has sources / reviewed-by block
   - [ ] About page has real description, photo, process statement, date
   - [ ] Category pages have unique intro text
   - [ ] All OG images load successfully
   - [ ] No blank ad placeholders that could appear as low-value ad clutter

2. Live crawl sanity check:
   - fetch home + 5 random article URLs
   - confirm no template text slips
   - confirm structured data parses
   - confirm canonical resolves to intended URL

3. AdSense resubmission readiness:
   - Keep the site exactly as-is after the live crawl passes.
   - In AdSense, request a site review after changes are live and stable.
   - Do not add new ad units during review; reviewers want to see normal site behavior.

---

## Recommended execution order

1. Delete `/blog/post-slug.html`
2. Replace generic byline with named authors + author-box block in layout
3. Add real author bio/credential block in `/about.html`
4. Add sources/reviewed metadata to each post footer
5. Replace template FAQ placeholders
6. Add category-page unique intros
7. Add 3–5 original simple graphics
8. Tighten sitemap + robots + canonical handling
9. Do local audit
10. Request AdSense review

---

If you want, I can directly:
- remove the template stub,
- patch the article layout to include author + sources blocks, and
- update the byline across posts to a named persona.
