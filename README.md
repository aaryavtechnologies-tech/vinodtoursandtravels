# Vinod Tour and Travels — English frontend

The finished website is in `dist/`. Open `dist/index.html` directly, or serve the directory with any static web server. No build step, installation, API key or backend is required.

## Included

- 43 English HTML pages, local CSS, JavaScript, photographs, icons and fonts.
- Reference homepage layout, navigation menus, destination grids, tour cards, company section, feature sections, blog cards and footer.
- Tour category search and duration filters, 20 tour detail pages, photo galleries and route accordions.
- About, contact, trip planning, FAQs, privacy and booking information pages.
- Phone links: **+91 80760 69722**.
- WhatsApp links: **https://wa.me/918076069722**.
- Address: **Near UGB Bank, East, Jhandichour, Kotdwara, Uttarakhand 246149**.
- Rating displayed as **4.9 / 5 from 177 Google reviews**, interpreting the business information provided in the request. This is a static supplied value, not a live Google integration.

The frontend is adapted from https://www.tourporlaindia.com/. The homepage preserves the reference structure and photographs. Inner pages use the same visual language and recreated components, with new English content for Vinod Tour and Travels; this is not a verbatim translation of every source article or a crawl of every tour available on the original site.

No chatbot, original company social accounts, analytics, payment processing, booking database or backend scripts are included. Original company awards, affiliations, customer testimonials and promotional video have been omitted. Tour routes are presented as suggested itineraries with services confirmed by enquiry.

## Enquiry flow

Forms validate locally and prepare a WhatsApp link containing the entered details. The visitor opens WhatsApp, reviews the message and sends it themselves. No message is sent automatically and no reservation is created.

## Editing

Edit the HTML files, `dist/styles.css`, `dist/app.js` and `dist/assets/vinod-logo.svg` directly. The `tools/` directory contains optional development utilities for rebuilding and checking the files; these are not website backend code and are not needed for deployment. Reference downloads are kept separately in `reference/`.

Serve **only `dist/`** or upload the contents of the supplied frontend ZIP to static hosting. Do not upload the reference or tools directories.

## Cloudflare deployment

Use Cloudflare Pages with production branch `main`, framework `None`, build command `exit 0`, build output directory `dist`, and the root directory left blank. No environment variables are required. Follow [the step-by-step Cloudflare deployment guide](CLOUDFLARE-DEPLOYMENT.md) for GitHub connection, deployment, custom domains and future updates.

## Validation commands

`python tools/verify_frontend.py` checks all pages for broken local links, missing assets, old branding, Spanish remnants, duplicate IDs and remote rendering dependencies. `node --check dist/app.js` checks JavaScript syntax. Browser checks cover desktop and mobile navigation, search, empty results, WhatsApp enquiry preparation, gallery controls and FAQ accordions.
