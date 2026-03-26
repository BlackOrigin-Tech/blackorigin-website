# BlackOrigin Inc. — Official Company Website

## Overview
This is the official BlackOrigin Inc. company website — a static site originally exported from Webflow and fully adapted to serve as the home of BlackOrigin, a technology company that builds and scales one product at a time. The Webflow CSS design system is fully intact; only copy, content, and branding have been changed.

## Company
**BlackOrigin Inc.** is a parent technology company. Its first product is **Campus Music**, a music streaming and discovery platform designed for student creators and listeners. **OriginOS** is an AI-powered personal life operating system, currently in development.

## Navigation Structure (all pages)
- **About ▾** (dropdown: About → about.html / How We Build → services.html / Vision → about.html#vision)
- **Products** → work.html
- **Careers** → career.html
- **Investors** (CTA button) → contact.html

## Page Index
| File | Page Title | Purpose |
|------|-----------|---------|
| `index.html` | BlackOrigin Inc. | Homepage |
| `about.html` | About BlackOrigin Inc. | Company story, vision, values |
| `services.html` | How We Build | Build methodology (Mission, Vision, Story) |
| `work.html` | Products | Campus Music + OriginOS product cards |
| `contact.html` | Investors | Investor inquiry form + FAQs |
| `career.html` | Careers | Job listings (3 real tech roles) |
| `pricing.html` | Plans | Pricing (not in nav) |
| `legal.html` | Legal & Privacy | Privacy policy |
| `detail_news.html` | Insights | Article detail (not in nav) |
| `detail_news-category.html` | Insights | Category view (not in nav) |
| `detail_works.html` | Work Detail | Product detail (not in nav) |
| `detail_services.html` | Service Detail | (not in nav) |
| `401.html`, `404.html` | Error pages | Standard error pages |

## Footer Structure (all pages)
- **Col 1**: Newsletter signup + brand tagline
- **Navigate**: Home / About / How We Build / Products / Investors / Careers
- **Company**: Legal & Privacy

## Key Content Changes Made
1. **Nav restructure** — All pages: About dropdown, Products, Careers, Investors CTA. Removed Platform, Insights from nav.
2. **about.html** — "ABOUT" hero, company story intro, 6 differentiator cards (Focused Execution, Long-term Vision, Technology at the Core, Creator-First, Speed Through Discipline, Equity-Driven Impact), "What We Believe" section with 3 BlackOrigin principles, Vision section (id="vision").
3. **services.html** — "HOW WE BUILD" hero, methodology intro, 3 service blocks (01 Our Mission / 02 Our Vision / 03 Our Story).
4. **work.html** — "PRODUCTS" hero, static product grid: Campus Music (Active) + OriginOS (In Development).
5. **contact.html** — "INVESTORS" hero, "Investor inquiries" label, investor inquiry form.
6. **career.html** — 3 real tech roles: Full-Stack Software Engineer, Product Designer, Growth Lead (all Remote).
7. **All footers** — Navigate column: Home/About/How We Build/Products/Investors/Careers. Company column: Legal & Privacy.

## Running the Site
**Workflow:** `Start application`
**Command:** `python3 server.py`
**Port:** 5000

## Technical Fixes Applied
1. **Webflow IX3 Visibility Fix** — Removed blocking `visibility: hidden` CSS; added CSS override for all animated elements.
2. **Template Popup Hidden** — Webflow "Sitemap / Buy" popup hidden via `display: none !important`.
3. **Scripts Made Local** — All CDN-hosted scripts served locally (GSAP, ScrollTrigger, SplitText, jQuery).
4. **Script Loading Order Fixed** — GSAP loads before `webflow.js` in all HTML files.
5. **Broken Image Symlinks Fixed** — Webflow uses spaces in filenames; 16 symlinks bridge the gap.
6. **Product Images** — `images/campus-music.png`, `images/originos.png` added.
7. **No-Cache Server** — `server.py` serves all files with `Cache-Control: no-cache`.

## Notes
- GSAP "target not found" warnings in console are expected — they reference Webflow CMS dynamic elements not present in the static export.
- Scroll-triggered animations work as progressive enhancement.
- `detail_news-category.html` is not linked from the nav (Insights removed from navigation).
