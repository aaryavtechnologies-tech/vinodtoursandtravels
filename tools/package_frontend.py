from pathlib import Path
from urllib.parse import urlsplit
from bs4 import BeautifulSoup
from PIL import Image
import re, json, zipfile

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'dist'
included=set(OUT.glob('*.html'))|{OUT/'styles.css',OUT/'app.js'}
for file in OUT.glob('*.html'):
    soup=BeautifulSoup(file.read_text(encoding='utf-8'),'html.parser')
    for tag in soup.select('[src],[href]'):
        url=tag.get('src') or tag.get('href')
        if url.startswith(('https:','http:','tel:','data:','#')):continue
        included.add(OUT/urlsplit(url).path)
processed=set()
while True:
    css_files=[f for f in included if f.suffix=='.css' and f not in processed]
    if not css_files:break
    for file in css_files:
        processed.add(file)
        for url in re.findall(r'url\([\"\']?([^\)\"\']+)',file.read_text(encoding='utf-8')):
            if not url.startswith('data:'):included.add(file.parent/url.split('#')[0])
image_count=0
for file in included:
    if file.suffix.lower() in ['.jpg','.png','.webp','.jpeg']:
        with Image.open(file) as img:img.verify()
        image_count+=1
mapping=json.loads((ROOT/'reference/assets.json').read_text())
sources='# Asset provenance\n\nReference layout and photographs: https://www.tourporlaindia.com/\n\nBrand mark and favicon: created for Vinod Tour and Travels.\n\nLocal asset | Original source\n--- | ---\n'
for url,path in sorted(mapping.items()):
    if OUT/path in included:sources+=f'{path} | {url}\n'
photos=json.loads((ROOT/'reference/traveller-photos.json').read_text())
sources+=f'\n## Owner-supplied traveller photographs\n\nAll {len(photos)} owner-supplied photos from images.zip and the additional WhatsApp ZIP files are included in the traveller gallery.\n\nLocal asset | Supplied filename\n--- | ---\n'
for photo in photos:
    sources+=f'{photo["image"]} | {photo["source"]}\n'
sources+='\n## Destination photographs\n\nSee photo-credits.html for visible credits and original license links.\n\n'
for photo in json.loads((ROOT/'reference/destination-photos.json').read_text(encoding='utf-8')).values():
    sources+=f'{photo["image"]} | {photo["artist"]} | {photo["license"]} | {photo["source"]} | {photo["license_url"]}\n'
readme=f'''VINOD TOUR AND TRAVELS — FRONTEND WEBSITE

Open index.html in your browser, or upload this folder to static hosting.
No installation, build process or backend is required.

{len(list(OUT.glob('*.html')))} English pages with local styles, JavaScript, photographs and fonts.
Includes 11 added destinations and all {len(photos)} owner-supplied traveller photos.
Business phone and WhatsApp: +91 80760 69722
Address: Near UGB Bank, East, Jhandichour, Kotdwara, Uttarakhand 246149
The supplied rating is interpreted as 4.9 / 5 from 177 Google reviews.

Enquiry forms prepare a WhatsApp message for the visitor to review and send.
They do not automatically send messages or confirm reservations.
No chatbot, analytics, payment processing, backend or database is included.

The reference layout is adapted and rebranded, with owner-supplied tourist
photography, a full traveller gallery and Uttarakhand / North India destinations.
Inner pages recreate the reference components with English business copy;
they are not a verbatim archive of every page on the original website.

Edit the HTML files for content, styles.css for custom styling, app.js for
interactions and assets/vinod-logo.svg for the brand mark.
'''
archive=ROOT/'vinod-tour-and-travels-frontend.zip'
with zipfile.ZipFile(archive,'w',zipfile.ZIP_DEFLATED) as z:
    for file in sorted(included):z.write(file,file.relative_to(OUT))
    z.writestr('README.txt',readme)
    z.writestr('ASSET-SOURCES.md',sources)
with zipfile.ZipFile(archive) as z:assert z.testzip() is None
print(json.dumps({'archive':str(archive),'size_mb':round(archive.stat().st_size/1024**2,2),'frontend_files':len(included),'verified_photos':image_count},indent=2))
