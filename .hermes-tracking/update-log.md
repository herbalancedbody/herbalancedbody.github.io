# Her Balanced Body — Update Log

## 2026-06-19

### Refresh category pages with article portfolio and planned sections
- Patched category pages with article grids and planned section coverage
- Commit: `4222116`

### Expand category coverage and post support sections
- Expanded 8 original short posts to 3000+ words
- Commit: `3753bb0`

### Maintenance backlog and tracking refresh
- Created `.hermes-tracking/maintenance-backlog.md`
- Refreshed `.hermes-tracking/todo-tracker.md`
- Commit: `eb678b1`

### Create maintenance backlog and refresh tracker
- Added maintenance audit script `.hermes-tracking/maintenance-audit.sh`
- Commit: prior to `ed17484`

### Format standardization for new and existing pages
- Extracted canonical article format from `blog/home-workout-plan-for-women.html`
- Extracted canonical category format from `blog/category/weight-loss-after-40.html`
- Stored rules in `.hermes-tracking/default-format-rules.md`
- Normalized and expanded 12 new category articles to 3000+ words
- Replaced remaining “Coming Soon” placeholders in category pages where needed
- Commit: `968ec76`

### Format new articles and link category pages
- Reformatted all new article pages to match existing published article format
- Verified word counts, metadata, schema, related reading, FAQ, and disclaimer coverage
- Updated category page `blog/category/healthy-habits-metabolism.html` with real article card
- Commit: `f2dea48`

### Add missing article and resolve 404
- Created `blog/simple-meal-prep-strategies-for-busy-women.html` with canonical article format, schema, and 3000+ word content
- Replaced missing-link cause for `https://herbalancedbody.github.io/blog/simple-meal-prep-strategies-for-busy-women.html`
- Commits: `c392a61`, `a8723b5`

### Normalize new article TOC/schema/footer and lock format rules
- Fixed missing/wrong Table of Contents sidebar on new articles
- Fixed duplicate FAQ blocks across new articles
- Fixed stray orphaned footer/markup between `</main>` and `<footer>`
- Updated `.hermes-tracking/default-format-rules.md`
- Commit: `a5bc40f`

### Fix broken TOC and footer on daily-stress article and all new articles
- Corrected wrong canonical TOC links on `daily-stress-management-habits-for-women.html`
- Removed stray content/broken footer after `</html>` across new articles
- Commit: pending push

## Pending
- AdSense slot-ID replacement remains pending user approval
- Windows scheduled task creation blocked by quoting/runtime issues
