# BlackOrigin – Static Webflow Export

## Overview
This is a static website exported from Webflow. No build step is required — all assets (HTML, CSS, JS, images, fonts, videos) are pre-built.

## Project Structure
- `index.html` — Homepage (entry point)
- `about.html`, `career.html`, `contact.html`, `legal.html`, `pricing.html`, `services.html`, `work.html` — Main pages
- `detail_news.html`, `detail_works.html`, `detail_services.html`, `detail_news-category.html` — Detail/template pages
- `401.html`, `404.html` — Error pages
- `css/` — Stylesheets
- `js/` — JavaScript files (includes GSAP animations)
- `images/` — Image assets
- `fonts/` — Font files
- `videos/` — Video assets
- `template/` — Template files

## Running the Site
The site is served with Python's built-in HTTP server on port 5000.

**Workflow:** `Start application`
**Command:** `python3 -m http.server 5000`
**Port:** 5000 (webview)

## Notes
- The homepage includes a GSAP-powered intro/preloader animation — this is expected Webflow behavior.
- No backend, database, or build step needed.
- Do not modify HTML/CSS/JS unless redesigning — this is an exported Webflow site.
