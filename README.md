# Vinod Tour and Travels — English frontend

The finished website is in `dist/`. Open `dist/index.html` directly, or serve the directory with any static web server. No build step, installation, API key or backend is required.

## Included

- 57 English HTML pages, local CSS, JavaScript, photographs, icons and fonts.
- Delhi–Jaipur–Agra and Rajasthan lead the homepage and package menus, followed by Manali and other tours. Uttarakhand is the final package group.
- Every destination card and individual destination enquiry page includes a relevant photograph. The homepage and city tour pages feature India Gate, Hawa Mahal, Taj Mahal, Agra Fort, Qutub Minar and Lotus Temple. Photo credits and license links are included in `dist/photo-credits.html`.
- Added Char Dham, Haridwar, Rishikesh, Mussoorie, Nainital, Jim Corbett, Shimla, Manali, Chandigarh, Amritsar and Lansdowne with individual enquiry pages.
- All 43 owner-supplied photos from `images.zip` and the additional WhatsApp ZIP files appear in the homepage and traveller gallery, with full-size viewing. The latest four vehicle photos appear in the fleet section on the homepage, contact and trip-planning pages, preserving the complete photos.
- The 16 additional photos appear in the full gallery, with vehicle photos on the homepage and taxi enquiry pages, guest welcomes on About Us, and Taj Mahal photos on relevant Agra and Golden Triangle pages.
- Reference homepage layout, navigation menus, destination grids, tour cards, company section, feature sections, blog cards and footer.
- Tour category search and duration filters, 20 tour detail pages, photo galleries and route accordions.
- About, contact, trip planning, FAQs, privacy and booking information pages.
- Phone links: **+91 80760 69722**.
- WhatsApp links: **https://wa.me/918076069722**.
- Address: **Near UGB Bank, East, Jhandichour, Kotdwara, Uttarakhand 246149**.
- Rating displayed as **4.9 / 5 from 177 Google reviews**, interpreting the business information provided in the request. This is a static supplied value, not a live Google integration.

The frontend is adapted from https://www.tourporlaindia.com/. The homepage combines the reference components with a new hero, destination listings and owner-supplied traveller photographs. Destination scenery is retained where appropriate. Inner pages use the same visual language and recreated components, with new English content for Vinod Tour and Travels; this is not a verbatim translation of every source article or a crawl of every tour available on the original site.

No chatbot, original company social accounts, analytics, payment processing, booking database or backend scripts are included. Original company awards, affiliations, customer testimonials and promotional video have been omitted. Tour routes are presented as suggested itineraries with services confirmed by enquiry.

## Enquiry flow

Forms validate locally and prepare a WhatsApp link containing the entered details. The visitor opens WhatsApp, reviews the message and sends it themselves. No message is sent automatically and no reservation is created.

## Editing

Edit the HTML files, `dist/styles.css`, `dist/app.js` and `dist/assets/vinod-logo.svg` directly. For repeatable content changes, edit `tools/build_frontend.py`, `tools/update_destinations.py` and `tools/prioritize_tours.py`, then run `python tools/build_frontend.py`. The photo manifests are `reference/traveller-photos.json` and `reference/destination-photos.json`; supplied JPEG files are in `dist/assets/traveller-photos/`. Destination photographs are already downloaded in `dist/assets/destinations/`, so rebuilding does not require network access. The `tools/` directory contains optional development utilities, not website backend code. Reference downloads are kept separately in `reference/`.

Serve **only `dist/`** or upload the contents of the supplied frontend ZIP to static hosting. Do not upload the reference or tools directories.

## Cloudflare deployment

Use Cloudflare Pages with production branch `main`, framework `None`, build command `exit 0`, build output directory `dist`, and the root directory left blank. No environment variables are required. Follow [the step-by-step Cloudflare deployment guide](CLOUDFLARE-DEPLOYMENT.md) for GitHub connection, deployment, custom domains and future updates.

## Validation commands

The responsive layout pass in `tools/refine_layout.py` runs after content generation. It keeps the company and journey sections within their columns and reserves the correct image dimensions. Photo frames preserve complete traveller images, with consistent sizing across mobile, tablet and desktop.

`node tools/verify_layout.cjs` (with Playwright available and `dist/` served at `http://127.0.0.1:8765`) checks all pages at 320, 390, 768, 1024 and 1440 pixels, plus package order, full vehicle photos, mobile navigation, photo viewing, FAQ and enquiry interactions. Screenshots and results are saved locally under `reference/`.

`python tools/verify_frontend.py` checks all pages for broken local links, missing assets, old branding, Spanish remnants, duplicate IDs and remote rendering dependencies. `node --check dist/app.js` checks JavaScript syntax. Browser checks cover desktop and mobile navigation, search, empty results, WhatsApp enquiry preparation, gallery controls and FAQ accordions.
