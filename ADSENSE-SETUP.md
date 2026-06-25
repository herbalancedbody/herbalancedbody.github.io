# Her Balanced Body — AdSense Ad Unit Setup

## Current status
- AdSense client: `ca-pub-7940751159869157`
- Site in AdSense: `herbalbalancedbody.github.io`
- Status: **Getting ready** (approved but still being reviewed for ad serving)
- ads.txt: **Authorized**
- Existing ads: using placeholder slot IDs (`0000000000`–`0000000075`) and empty placeholders
- **No real ads will serve until real ad unit slot IDs replace these placeholders**

## Slot IDs received
- `home`: `8455436014` ✅ applied
- `blog-top`: `5110674689` ✅ applied to all blog posts
- `blog-mid`: `2384851686` ✅ applied to all blog posts
- `blog-sidebar`: `9448953484` ✅ applied to all blog posts
- `static`: `7689149251` ✅ applied to About and Contact pages

## What needs to happen
1. You create ad units in Google AdSense
2. You give me the real slot IDs
3. I replace every placeholder across the whole repo automatically
4. I push the changes live

---

## Step 1 — Create these 5 ad units in AdSense

Go to **Google AdSense → Sites → Get code → Create ad unit** for each of these:

### Ad Unit A — Home Page
- Name: `HBB - Home`
- Type: **Display ads** (responsive)
- Placement: main content area

### Ad Unit B — Blog Post In-Content Top
- Name: `HBB - Blog In-Content Top`
- Type: **Display ads** (responsive)
- Placement: after intro paragraph

### Ad Unit C — Blog Post In-Content Mid
- Name: `HBB - Blog In-Content Mid`
- Type: **In-article ads** (in-feed / in-article responsive)
- Placement: between paragraphs mid-article

### Ad Unit D — Blog Post Sidebar
- Name: `HBB - Blog Sidebar`
- Type: **Display ads** (responsive, vertical)
- Placement: sidebar widget

### Ad Unit E — Static Pages
- Name: `HBB - Static Pages`
- Type: **Display ads** (responsive)
- Placement: About / Contact / Privacy / Terms / Disclaimer pages

After creating each unit, copy its **Slot ID** (looks like `1234567890`).

---

## Step 2 — Send me the slot IDs

Send me the 5 slot IDs in this format:
```
home: <slot-id>
blog-top: <slot-id>
blog-mid: <slot-id>
blog-sidebar: <slot-id>
static: <slot-id>
```

---

## Step 3 — I’ll finish it
Once you send the IDs, I will:
- Replace every placeholder/empty ad slot across the entire repo
- Run the preflight validator
- Commit and push to GitHub
- Confirm live

---

## Notes
- Do **not** create more than 5 ad units unless you want a different layout
- If AdSense shows the site as "Getting ready", ads may still not serve immediately even after real IDs are added — that’s normal; it usually clears after final review
- Only the pages listed in AdSense (`herbalbalancedbody.github.io`) can show ads
