# BlackOrigin — Static Webflow Export

## Overview
This is a static website exported from Webflow. No build step is required — all assets (HTML, CSS, JS, images, fonts, videos) are pre-built.

## Project Structure
- `index.html` — Homepage (entry point)
- `about.html`, `career.html`, `contact.html`, `legal.html`, `pricing.html`, `services.html`, `work.html` — Main pages
- `detail_news.html`, `detail_works.html`, `detail_services.html`, `detail_news-category.html` — Detail/template pages
- `401.html`, `404.html` — Error pages
- `css/` — Stylesheets
- `js/` — JavaScript files (GSAP animations + jQuery, all local copies)
- `images/` — Image assets (includes symlinks mapping hyphenated names to space-named originals)
- `fonts/` — Font files
- `videos/` — Video assets
- `template/` — Template files
- `server.py` — Custom Python HTTP server with no-cache headers

## Running the Site
The site is served with a custom Python HTTP server with no-cache headers on port 5000.

**Workflow:** `Start application`
**Command:** `python3 server.py`
**Port:** 5000 (webview)

## Fixes Applied

### 1. Broken Image Paths (symlinks)
Webflow exports image files with spaces in the display-name portion of filenames (e.g., `Team-member-1_1Team member-1.avif`), but HTML references them with hyphens (e.g., `Team-member-1_1Team-member-1.avif`). Created 16 symlinks in `images/` to resolve all mismatches.

### 2. Scripts Made Local
All CDN-hosted scripts downloaded locally to eliminate network dependencies:
- `js/jquery-3.5.1.min.js` (from cloudfront)
- `js/gsap.min.js` (from Webflow CDN)
- `js/ScrollTrigger.min.js` (from Webflow CDN)
- `js/SplitText.min.js` (from Webflow CDN)

### 3. Script Loading Order Fixed
GSAP scripts moved to load **before** `webflow.js` in all HTML files so Webflow's IX3 animation system can access GSAP when it initializes.

### 4. Webflow IX3 Animation Compatibility Fix
Webflow exports include a CSS rule that hides all page content with `visibility: hidden !important` until a `w-mod-ix3` class is added by GSAP. In a static export environment, the GSAP animations don't fully initialize so content stays hidden.

**Fix applied to all 14 HTML files:**
- Removed the blocking `visibility: hidden` CSS rule
- Added CSS override forcing all animated elements (`[homepage-load]`, `[innerpage-load]`, `.navbar`, `.footer`, etc.) to `opacity: 1; visibility: visible; transform: none`
- Added `w-mod-ix3` alongside `w-mod-js` in the initialization script
- Set `.preloader { display: none !important }` to prevent the loading overlay from blocking content

### 5. CDN Image References Fixed
Replaced external Webflow CDN image references with local files:
- `Two men looking at Laptop.png` → `images/Two-men-looking-at-Laptop_1Two-men-looking-at-Laptop.avif`
- `About Header.png` → `images/About-Header_1About-Header.avif`

### 6. Video Poster URL Cleaned
Removed CDN-hosted video poster URL (was only used as a fallback background for the video element).

## Notes
- GSAP "target not found" warnings are expected and harmless — they occur because the Webflow CMS dynamic content elements referenced in animations don't exist in the static export
- Scroll-triggered GSAP animations (fade-ins, parallax effects) still work as progressive enhancement
- The preloader intro animation is disabled for static export compatibility; content is immediately visible
