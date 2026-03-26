# BlackOrigin Inc. — Official Company Website

## Overview
This is the official BlackOrigin Inc. company website — a static site originally exported from Webflow and fully adapted to serve as the home of BlackOrigin, a technology company that builds and scales one product at a time.

## Company
**BlackOrigin Inc.** is a parent technology company. Its first product is **Campus Music**, a platform for student creators, music culture, and campus engagement. OriginOS is the second product in the portfolio.

## Project Structure
- `index.html` — Homepage (entry point, fully redesigned)
- `about.html` — About page
- `contact.html` — Contact page
- `work.html` — Products / portfolio page
- `services.html` — Platform page
- `career.html` — Careers page
- `pricing.html` — Plans page
- `legal.html` — Legal & Privacy page
- `detail_news.html`, `detail_news-category.html` — Insights detail pages
- `detail_works.html`, `detail_services.html` — Product/platform detail pages
- `401.html`, `404.html` — Error pages
- `css/` — Stylesheets (blackorigin.webflow.css, webflow.css, normalize.css)
- `js/` — JavaScript files (GSAP, ScrollTrigger, SplitText, jQuery, webflow.js — all local)
- `images/` — Image assets (includes symlinks for Webflow filename quirks + product images)
- `fonts/` — Font files
- `videos/` — Video assets (hero background)
- `server.py` — Custom Python HTTP server with no-cache headers

## Running the Site
**Workflow:** `Start application`  
**Command:** `python3 server.py`  
**Port:** 5000

## Homepage Sections (index.html)
1. **Hero** — Video background, "BLACK ORIGIN" display type, H1: "One company. One product at a time. Built to last.", CTAs: "Discover Campus Music" + "Partner with us"
2. **About BlackOrigin** — Company philosophy and mission
3. **Products** — Two-column grid: Campus Music (2026) + OriginOS (2025)
4. **How We Build** — Three pillars: One Product at a Time / Technology First / Built to Scale Independently
5. **Insights** — Article teaser section
6. **Vision** — "From first product to lasting platforms."
7. **Footer** — Newsletter, Navigate links, Company links, © BlackOrigin Inc. 2026

## Navigation (all pages)
- **Products** (dropdown: Campus Music, OriginOS, Coming Soon)
- **About**
- **Platform**
- **Insights**
- **Contact** (CTA button)

## Technical Fixes Applied

### 1. Webflow IX3 Visibility Fix
Removed blocking `visibility: hidden` CSS that required GSAP animations to complete before content was visible. Added CSS override forcing all animated elements to be immediately visible. Applied to all 14 HTML pages.

### 2. Template Popup Removed
The Webflow "Sitemap / Buy" template popup is hidden via `display: none !important` across all pages.

### 3. Scripts Made Local
All CDN-hosted scripts are now served locally:
- `js/jquery-3.5.1.min.js`
- `js/gsap.min.js`
- `js/ScrollTrigger.min.js`
- `js/SplitText.min.js`

### 4. Script Loading Order Fixed
GSAP loads before `webflow.js` in all HTML files.

### 5. Broken Image Symlinks Fixed
Webflow exports use spaces in filenames but HTML references use hyphens. 16 symlinks created in `images/` to bridge the gap.

### 6. Product Images Added
- `images/campus-music.png` — Campus Music product visual
- `images/originos.png` — OriginOS product visual

### 7. Brand Identity Updated (All Pages)
- Page titles updated to BlackOrigin across all 13 inner pages
- "OSCAR®" brand logo replaced with `BO_Logo.svg` in fixed navbars
- Nav labels updated: Services→Products, Work→Products, Team→About, News→Insights
- Dropdown items updated: Creative Direction/Development/Brand Strategy → Campus Music/OriginOS/Coming Soon
- Copyright updated: "Oscar 2026" → "© BlackOrigin Inc. 2026"
- Footer newsletter and privacy text updated to BlackOrigin branding
- Meta descriptions updated across all pages

### 8. No-Cache Server
`server.py` serves all files with `Cache-Control: no-cache` headers to prevent stale browser caching.

## Notes
- GSAP "target not found" warnings in console are expected — they reference Webflow CMS dynamic elements not present in the static export
- Scroll-triggered animations still work as progressive enhancement
- The preloader intro sequence is disabled for static export compatibility
