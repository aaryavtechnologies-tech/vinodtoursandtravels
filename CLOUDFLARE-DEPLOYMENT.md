# Deploy Vinod Tour and Travels on Cloudflare Pages

This project is a ready-made static website. The live website files are in `dist/`, including `dist/index.html`. No npm install, build, API keys, database or server is required.

Repository: https://github.com/aaryavtechnologies-tech/vinodtoursandtravels

## 1. Connect GitHub

1. Sign in at https://dash.cloudflare.com/ and select your account.
2. Open **Workers & Pages**, then **Create application**.
3. Select **Pages**, then **Import an existing Git repository**.
4. Connect GitHub. Select the `aaryavtechnologies-tech` account or organization and grant Cloudflare access to `vinodtoursandtravels`.
5. Select that repository and click **Begin setup**.

If the repository is missing, update the Cloudflare GitHub application's repository access. An organization administrator may need to approve access.

Cloudflare's [Git integration guide](https://developers.cloudflare.com/pages/get-started/git-integration/) describes this connection and setup process.

## 2. Enter these exact deployment settings

| Setting | Value |
| --- | --- |
| Project name | `vinodtoursandtravels` (or another available name) |
| Production branch | `main` |
| Framework preset | `None` |
| Build command | `exit 0` |
| Build output directory | `dist` |
| Root directory (advanced) | Leave blank; use the repository root |
| Environment variables | None |

Publish only `dist/`. The reference downloads, development tools, ZIP and documentation remain in GitHub but are outside the website's published folder.

These settings follow Cloudflare's [static HTML deployment guide](https://developers.cloudflare.com/pages/framework-guides/deploy-anything/).

## 3. Deploy and check the website

1. Click **Save and Deploy**.
2. Wait for a successful deployment and open the URL Cloudflare displays. It will be a `pages.dev` address based on the available project name.
3. Check the homepage, images, menu and tour pages on desktop and mobile.
4. Open Contact and Plan My Trip. Complete a sample enquiry and confirm the prepared WhatsApp message contains the entered details and uses **+91 80760 69722**. You can inspect it without sending it.
5. Check a tour page directly and refresh it to confirm the URL loads correctly.

Forms prepare WhatsApp messages for visitors to review and send. They do not automatically send enquiries, accept payment or create reservations.

## 4. Optional: connect your own domain

1. Open **Workers & Pages > your Pages project > Custom domains**.
2. Select **Set up a domain**, enter the domain you own and follow the prompts.
3. For a root domain such as `example.com`, add it as a website/zone in the same Cloudflare account and point its registrar nameservers to the two Cloudflare provides. Preserve existing email and other service DNS records when moving DNS.
4. For a subdomain such as `www.example.com` using another DNS provider, first add it in the Pages project's Custom domains panel, then add the CNAME Cloudflare requests at that provider, targeting your actual `pages.dev` hostname.
5. Wait until Cloudflare shows the domain as active, then test its HTTPS URL.

Use your actual domain in place of the examples. Follow Cloudflare's [custom domain guide](https://developers.cloudflare.com/pages/configuration/custom-domains/) for DNS details. Adding a CNAME alone, without registering the domain in the Pages project, is insufficient.

## 5. Publish later changes

Edit files in `dist/`, then commit and push to `main`. With Git integration enabled, Cloudflare automatically deploys changes pushed to the production branch.

```powershell
git add dist
git commit -m "Update website content"
git push origin main
```

The optional Python utilities are for development and are not run by Cloudflare with these settings.

## Troubleshooting

| Symptom | What to check |
| --- | --- |
| Homepage shows 404 | Output directory must be `dist`; `dist/index.html` must be committed. |
| Build reports missing package.json | Choose framework `None` and build command `exit 0`. |
| Setup requests a Worker entry point or deploy command | Return to Create application and choose the Pages flow. |
| Repository does not appear | Confirm the GitHub account/organization and Cloudflare application's repository access. |
| Images or styles are missing | Confirm `dist/assets/`, `dist/styles.css` and `dist/app.js` are in GitHub; use exact filename casing. |
| Latest changes are missing | Check that the Pages production deployment matches the latest `main` commit, then refresh the browser. |
| Custom domain does not load | Confirm it was added in Pages, DNS matches the setup instructions, and its status is active. |

Documentation checked on 17 September 2026.
