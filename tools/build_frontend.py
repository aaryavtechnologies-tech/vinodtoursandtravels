"""Build a portable, frontend-only English adaptation of the reference."""
from pathlib import Path
from bs4 import BeautifulSoup, Comment
from urllib.parse import urlsplit, quote
from html import escape
import json, re, copy

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'dist'
source=BeautifulSoup((ROOT/'reference/home.html').read_text(encoding='utf-8'),'html.parser')
assets=json.loads((ROOT/'reference/assets.json').read_text())
BASE='https://www.tourporlaindia.com'
BRAND='Vinod Tour and Travels'
PHONE='+91 80760 69722'
ADDRESS='Near UGB Bank, East, Jhandichour, Kotdwara, Uttarakhand 246149'
WA='https://wa.me/918076069722'
MAP='https://www.google.com/maps/search/?api=1&query='+quote(BRAND+' '+ADDRESS)

# All homepage text is replaced; the original frontend markup is retained.
for el in source.select('script,style'): el.decompose()
texts=list(dict.fromkeys(source.stripped_strings))
en={
0:'Taxi Service in Uttarakhand | Vinod Tour and Travels',1:'Call us:',2:PHONE,3:'Kotdwara, Uttarakhand',4:'Let’s plan your trip',
5:'About us',6:'Tour packages',7:'in Agra',8:'in Delhi',9:'in Rajasthan',10:'Golden Triangle',11:'Tours',12:'Explore India',13:'Festival of Colours –',14:'Holi',15:'Group Travel',16:'Golden Triangle',17:'Varanasi',18:'South India',19:'North India',20:'Same-Day Tours',21:'Travel Blog',22:'Contact',23:'Plan My Trip',
24:'Discover India with Vinod Tour and Travels',25:'Golden Triangle India – Unforgettable Journeys',
26:'Discover Delhi, Agra and Jaipur on India’s classic Golden Triangle route. From historic streets and grand forts to the beauty of the Taj Mahal, explore a journey filled with culture and memorable sights. Contact Vinod Tour and Travels in Kotdwara to discuss your route, travel dates and transport requirements.',
28:'Golden Triangle Tour – 3 Days',29:'3 days',30:'View tour',31:'Golden Triangle Tour – 4 Days',32:'4 days',33:'Golden Triangle Tour – 5 Days',34:'5 days',35:'Golden Triangle Tour – 6 Days',36:'6 days',37:'Golden Triangle & Varanasi Tours',39:'Golden Triangle with Varanasi – 6 Days',40:'Delhi – Varanasi – Delhi',41:'Delhi to Varanasi – 5-Day Rail Journey',43:'Golden Triangle with Khajuraho & Varanasi',44:'13 days',46:'Golden Triangle with Varanasi',47:'10 days',48:'Discover the timeless beauty of Agra',49:'Taj Mahal & Agra Tours',
50:'Discover the Taj Mahal, the white-marble monument on the banks of the Yamuna in Agra. Explore its gardens and architecture, then make time for the city’s remarkable heritage. Browse these suggested day trips and overnight journeys, and speak with us to plan the travel arrangements that suit you.',
52:'Same-Day Agra Tour from Delhi by Train',53:'1 day',54:'Same-Day Agra Tour from Delhi by Car',56:'Same-Day Agra Tour from Jaipur by Car',58:'Overnight Taj Mahal & Agra Tour from Delhi',59:'Festival of Colours',60:'Golden Triangle & Varanasi',61:'Find your next journey',62:'Explore Our Tour Categories',
63:'Choose a journey that matches your interests, from the palaces of Rajasthan and the Golden Triangle to the landscapes of South India. These routes are travel ideas: contact us for availability, a personalised itinerary and a quote before making plans.',64:'Taj Mahal Tours',65:'Rajasthan – Palaces, Forts & Colour',
66:'Explore Rajasthan’s royal heritage through Jaipur, Bikaner, Udaipur, Jaisalmer and Jodhpur. Discover hilltop forts, ornate palaces and vibrant streets on a route shaped around your interests. Whether you are planning a family holiday or a longer journey, share your preferred destinations with Vinod Tour and Travels to discuss your transport and itinerary.',
68:'Rajasthan with the Taj Mahal – 12 Days',70:'Golden Triangle with Amritsar – 10 Days',71:'10 days',73:'Royal & Classic Rajasthan Tour',74:'15 days',76:'Delhi, Bikaner & Jaisalmer – 15 Days',77:'Kerala & South India Journeys',
78:'Discover the green hills, tranquil backwaters and coastal landscapes of South India. Kerala’s tea-growing hills and waterways offer a different pace of travel, while historic temples and lively cities add variety to a longer route. Browse the suggested journeys below and get in touch to discuss your plans.',
80:'A Week in Kerala',81:'7 days',83:'South India with Goa & Delhi',85:'South India with Mumbai',86:'14 days',88:'Wonders of South India',89:'Vinod Tour and Travels – Travel Your Way',
90:'Vinod Tour and Travels is a taxi service based in Kotdwara, Uttarakhand. Find us near UGB Bank, East, Jhandichour. Whether you need a local taxi, want to discuss an outstation journey or are planning a holiday, contact us directly with your pickup point, destination and travel dates. We will help you discuss the route and confirm the fare and availability before you book.',
91:'Local taxi enquiries',92:'Personalised trip quotes',93:'Flexible route planning',94:'Direct phone & WhatsApp support',95:'Why travel with us',96:'Your Journey Begins with a Conversation',97:'Tell us where you want to go. We will help you work out the travel details before you confirm your trip.',98:'Your choice of route',99:'Share your destinations and preferred stops so we can discuss a route that suits your trip.',100:'Easy enquiries',101:'Call or send us a WhatsApp message with your travel dates and pickup location.',102:'A local point of contact',103:'Speak directly with Vinod Tour and Travels in Kotdwara about your taxi and travel requirements.',104:'Personalised planning',105:'Travel inspiration',106:'Stories & Guides from India',107:'Travel guide',108:'Read',109:'Ranthambore: Beyond the Safari',110:'Photographing Wildlife & Nature in Ranthambore',111:'Varanasi: Life Along the Ganga',112:'Need help? Get in touch',113:'Near UGB Bank, East,',114:'Jhandichour, Kotdwara,',115:'Uttarakhand 246149, India',116:PHONE,117:'Agra Tour Packages',118:'Delhi Tour Packages',119:'Rajasthan Tour Packages',120:'Golden Triangle Tours',121:'Privacy',122:'Booking Information',123:'Frequently Asked Questions',124:'Plan your next journey',125:'Tell us your pickup point, destination and travel dates. Ask for a personalised quote on WhatsApp.',126:'Copyright © 2026',127:BRAND,128:'. All rights reserved.',129:'',130:'.'}
translations={texts[i]:v for i,v in en.items()}
for node in list(source.find_all(string=True)):
    if isinstance(node,Comment):node.extract();continue
    t=node.strip()
    if t in translations:node.replace_with(translations[t])

route_names={
'sobre-nosotros':'about','contacto':'contact','planificar-mi-recorrido':'plan-my-trip','preguntas-frecuentes':'faq','politica-de-privacidad':'privacy','terminos-y-condiciones':'booking-information',
'paquetes-turisticos-de-agra':'agra-tours','paquetes-turisticos-de-delhi':'delhi-tours','paquetes-turisticos-de-rajastan':'rajasthan-tours','tour-del-triangulo-dorado':'golden-triangle-tours','festival-de-los-colores':'holi-tours','viaje-en-grupo':'group-travel','triangulo-de-oro':'golden-triangle','triangulo-de-oro-varanasi':'golden-triangle-varanasi','sur-de-la-india':'south-india','norte-de-la-india':'north-india','recorridos-el-mismo-dia':'same-day-tours','blog':'blog'}
route_names['festival-de-colores']='holi-tours'
route_names['tour/holi-el-festival-del-color-en-la-india-2024']='holi-tours'
def slug(text):return re.sub(r'[^a-z0-9]+','-',text.lower()).strip('-')

tours=[]
for a in source.select('a.package-anchor'):
    item={'title':a.select_one('.pkg-title').get_text(strip=True),'source':a['href'],'route':a.select('.pkg-loc')[0].get_text(' ',strip=True),'duration':a.select('.pkg-loc')[1].get_text(' ',strip=True),'image':assets[a.img['src']],'card':str(a)}
    item['slug']=slug(item['title'])
    # Correct two inconsistent duration labels in the reference cards.
    if '12 Days' in item['title']:item['duration']='12 days'; a.select('.pkg-loc')[1].clear();a.select('.pkg-loc')[1].append('12 days')
    if 'Overnight' in item['title']:item['duration']='2 days'; a.select('.pkg-loc')[1].clear();a.select('.pkg-loc')[1].append('2 days')
    route_names[urlsplit(a['href']).path.strip('/')]='tour-'+item['slug']
    tours.append(item)

blogs=[]
for card in source.select('.blog-card'):
    title=card.select_one('.fw-bold').get_text(strip=True)
    key='blog/'+urlsplit(card.a['href']).path.split('/')[-1]
    route_names[key]='guide-'+slug(title)
    blogs.append({'title':title,'slug':route_names[key],'image':assets[card.img['src']]})

def rewrite(soup):
    for img in soup.select('img'):
        src=img.get('src','').strip()
        if src in assets:img['src']=assets[src]
        if not img.get('alt'):img['alt']='India travel destination'
        img['loading']='lazy';img['decoding']='async'
    for a in soup.select('a[href]'):
        href=a['href']
        if href.startswith(BASE):a['href']=route_names.get(urlsplit(href).path.strip('/'),'index')+'.html'
        elif href.startswith('tel:'):a['href']='tel:+918076069722'
        elif href.startswith('mailto:'):a['href']=MAP;a.string='Kotdwara, Uttarakhand'
        elif 'wa.me' in href:a['href']=WA+'?text='+quote('Hello Vinod Tour and Travels, I would like to enquire about a trip.')
    for el in soup.select('[data-wow-delay]'):del el['data-wow-delay']
rewrite(source)
source.select_one('#spinner').decompose()
top=source.body.find('section')
top.clear()
top.append(BeautifulSoup(f'<div class="topline"><a href="tel:+918076069722"><i class="fa-solid fa-phone-volume"></i> Call us: <strong>{PHONE}</strong></a><a href="{MAP}" target="_blank" rel="noopener"><i class="fa-solid fa-location-dot"></i> Kotdwara, Uttarakhand</a><span class="top-rating"><span class="stars">★★★★★</span> 4.9 · 177 Google reviews</span></div>','html.parser'))
nav=source.select_one('nav')
nav.select_one('.navbar-brand').clear()
nav.select_one('.navbar-brand').append(BeautifulSoup('<img src="assets/vinod-logo.svg" alt="Vinod Tour and Travels" width="230" height="76">','html.parser'))
nav.select_one('.navbar-toggler')['aria-label']='Open navigation'
nav.select_one('.navbar-toggler')['aria-expanded']='false'
for a in nav.select('.dropdown-toggle'):a['role']='button';a['aria-expanded']='false'
nav.select_one('.navbar-nav').insert(0,BeautifulSoup('<a class="nav-item nav-link" href="index.html">Home</a>','html.parser'))
header=str(top)+str(nav.parent)
hero=source.select_one('img[src="'+assets[BASE+'/assets/img/carousel/slider.jpg']+'"]')
hero['loading']='eager';hero['fetchpriority']='high';hero['alt']='A collage of travellers visiting India’s historic landmarks'

footer=f'''<footer class="site-footer"><div class="footer-grid"><div><h3>NEED HELP? CALL US</h3><p>{BRAND}<br>Taxi service in Uttarakhand</p><p>{ADDRESS}</p><a href="tel:+918076069722"><i class="fa-solid fa-phone"></i> {PHONE}</a><br><a href="{MAP}" target="_blank" rel="noopener">Get directions ↗</a></div><div><h3>TOUR PACKAGES</h3><a href="agra-tours.html">Agra Tours</a><a href="delhi-tours.html">Delhi Tours</a><a href="rajasthan-tours.html">Rajasthan Tours</a><a href="golden-triangle-tours.html">Golden Triangle</a><a href="golden-triangle-varanasi.html">Golden Triangle & Varanasi</a></div><div><h3>EXPLORE & PLAN</h3><a href="about.html">About us</a><a href="blog.html">Travel blog</a><a href="contact.html">Contact us</a><a href="faq.html">Frequently asked questions</a><a href="privacy.html">Privacy</a><a href="booking-information.html">Booking information</a></div><div><h3>PLAN YOUR NEXT JOURNEY</h3><p>Share your destination, pickup point and travel dates. Let’s start planning your trip.</p><a class="button navy" href="{WA}?text=Hello%20Vinod%20Tour%20and%20Travels%2C%20I%20would%20like%20a%20trip%20quote." target="_blank" rel="noopener"><i class="fa-brands fa-whatsapp"></i> WhatsApp us</a><p class="review-footer"><span class="stars">★★★★★</span><br>4.9 / 5 · 177 Google reviews</p></div></div><div class="copyright">© 2026 {BRAND}. All rights reserved.</div></footer><a class="whatsapp-float" href="{WA}?text=Hello%20Vinod%20Tour%20and%20Travels%2C%20I%20would%20like%20to%20plan%20a%20trip." target="_blank" rel="noopener" aria-label="Chat with Vinod Tour and Travels on WhatsApp"><i class="fa-brands fa-whatsapp"></i><span>WhatsApp us</span></a>'''

head=f'''<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="theme-color" content="#002248"><link rel="icon" type="image/svg+xml" href="assets/favicon.svg"><link rel="stylesheet" href="{assets[BASE+'/assets/css/bootstrap.min.css']}"><link rel="stylesheet" href="{assets['https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css']}"><link rel="stylesheet" href="{assets[BASE+'/assets/css/style.css']}"><link rel="stylesheet" href="styles.css">'''
def save(name,title,body):
    html=f'<!doctype html><html lang="en"><head>{head}<title>{escape(title)} | {BRAND}</title><meta name="description" content="{escape(title)}. Taxi and travel enquiries with Vinod Tour and Travels, Kotdwara, Uttarakhand. Call {PHONE}."></head><body><a class="skip-link" href="#main">Skip to content</a>{header}<main id="main">{body}</main>{footer}<script src="app.js" defer></script></body></html>'
    (OUT/(name+'.html')).write_text(html,encoding='utf-8')

sections=source.body.find_all('section',recursive=False)[1:]
body=''
for section in sections:
    if section.select_one('.partener'):
        body+=f'<section class="rating-band"><div><span class="stars">★★★★★</span><h2>4.9 out of 5</h2><p>177 Google reviews</p></div><div><h2>Your local travel contact in Kotdwara</h2><p>Vinod Tour and Travels · Taxi service in Uttarakhand</p><a class="button navy" href="contact.html">Get in touch <span>→</span></a></div></section>'
        continue
    iframe=section.select_one('iframe')
    if iframe:
        # The source video advertises another company; retain the visual panel using local photography.
        iframe.replace_with(BeautifulSoup(f'<a href="plan-my-trip.html" class="travel-panel"><img src="{assets[BASE+"/assets/img/others/animate_home_view-5/img_001.webp"]}" alt="Explore India with a personalised journey"><span>Let’s plan your next journey <b>→</b></span></a>','html.parser'))
    body+=str(section)
    if section is sections[0]:
        body+=f'<section class="intro-strip"><div><strong>{BRAND}</strong><span>Taxi service in Uttarakhand · Based in Kotdwara</span></div><a class="button" href="plan-my-trip.html">Plan your trip <i class="fa-solid fa-arrow-right"></i></a><a class="button outline" href="{WA}" target="_blank" rel="noopener"><i class="fa-brands fa-whatsapp"></i> Get a quote</a></section>'
save('index','Taxi Service in Uttarakhand',body)
(ROOT/'reference/tours.json').write_text(json.dumps(tours,indent=2),encoding='utf-8')
(ROOT/'reference/routes.json').write_text(json.dumps(route_names,indent=2),encoding='utf-8')
print('Homepage created with',len(tours),'tour cards and',len(blogs),'articles.')

# Detail and category pages are generated below using the same local components.
def banner(title):
    return f'<section class="page-banner"><h1>{escape(title)}</h1><p><a href="index.html">Home</a> <span aria-hidden="true">›</span> {escape(title)}</p></section>'

def form(destination='',full=False):
    return f'''<form class="form-card enquiry-form"><h2>{'Plan Your Journey' if full else 'Enquire About This Trip'}</h2><p>Tell us a little about your plans.</p><div class="form-grid"><div class="field"><label for="name">Your name *</label><input id="name" name="name" autocomplete="name" required maxlength="100" placeholder="Full name"></div><div class="field"><label for="phone">Phone number *</label><input id="phone" name="phone" type="tel" autocomplete="tel" required pattern="[+0-9() -]{{7,20}}" maxlength="20" placeholder="+91"></div></div><div class="field"><label for="pickup">Pickup location *</label><input id="pickup" name="pickup" required maxlength="150" placeholder="City, hotel or pickup point"></div><div class="field"><label for="destination">Destination or tour *</label><input id="destination" name="destination" value="{escape(destination,quote=True)}" required maxlength="160" placeholder="Where would you like to go?"></div><div class="form-grid"><div class="field"><label for="date">Travel date *</label><input type="date" id="date" name="date" required></div><div class="field"><label for="travellers">Travellers *</label><input type="number" id="travellers" name="travellers" value="2" min="1" max="100" required></div></div><div class="field"><label for="service">Travel requirement</label><select id="service" name="service"><option>Taxi / outstation travel</option><option>Local taxi in Uttarakhand</option><option>Airport or railway transfer enquiry</option><option>Tour planning</option><option>Group travel enquiry</option></select></div><div class="field"><label for="message">Anything else we should know?</label><textarea id="message" name="message" rows="3" maxlength="2000" placeholder="Preferred stops, return date or other requests"></textarea></div><button class="button" type="submit"><i class="fa-brands fa-whatsapp"></i> Prepare WhatsApp enquiry</button><p class="form-note">Review your message in WhatsApp before sending. This form does not store your details or confirm a booking.</p><div class="success-message" role="status" tabindex="-1" hidden></div></form>'''

def card(t):
    return f'''<article data-tour data-days="{re.search(r'\d+',t['duration']).group()}"><a href="tour-{t['slug']}.html" class="package-anchor"><div class="package-item"><img src="{t['image']}" alt="{escape(t['title'])}" loading="lazy" width="400" height="290"><div class="package-content-area"><p class="t-c pkg-loc mb-1"><i class="fa-solid fa-location-dot me-1"></i>{escape(t['route'])}</p><h2 class="pkg-title" style="font-size:18px">{escape(t['title'])}</h2><p class="t-c pkg-loc"><i class="fa-solid fa-clock-rotate-left me-1"></i>{t['duration']}</p><hr><p class="p-c pkg-botm-info mb-0">View tour <i class="fa-solid fa-circle-chevron-right ms-2"></i></p></div></div></a></article>'''

category_data=[
('agra-tours','Agra & Taj Mahal Tours',tours[8:12],'Discover Agra’s marble monuments and historic streets. Choose a day-trip or overnight travel idea and ask us about transport arrangements.'),
('delhi-tours','Delhi Tour Packages',tours[:8],'Start with India’s capital and explore routes that connect Delhi with Agra, Jaipur and Varanasi. Share your pickup point and available travel time.'),
('rajasthan-tours','Rajasthan Tour Packages',tours[12:16],'Explore Rajasthan’s forts, palaces and desert cities. These suggested journeys can help you decide which destinations to include.'),
('golden-triangle-tours','Golden Triangle Tours',tours[:4],'Discover the classic Delhi–Agra–Jaipur route. Compare different trip lengths and ask about a journey tailored to your dates.'),
('golden-triangle','Explore the Golden Triangle',tours[:4],'A journey through Delhi, Agra and Jaipur brings together the historic architecture and vibrant streets of North India.'),
('golden-triangle-varanasi','Golden Triangle & Varanasi',tours[4:8],'Combine the heritage of Delhi, Agra and Jaipur with time beside the Ganga in Varanasi.'),
('south-india','South India Tours',tours[16:20],'Discover Kerala’s landscapes and the cities and temples of South India. Tell us the places you would like to visit.'),
('north-india','North India Tours',tours[:16],'Explore North India’s landmarks, royal cities and spiritual destinations. Contact our Kotdwara team to discuss your travel requirements.'),
('same-day-tours','Same-Day Tours',tours[8:11],'Make time for a day of discovery. Discuss pickup times, driving distances and sightseeing stops before confirming your trip.'),
('group-travel','Group Travel',tours,'Planning a journey with family or friends? Tell us your group size, luggage requirements and destinations so we can discuss suitable transport.'),
('holi-tours','Holi – The Festival of Colours',tours[:4],'Bring a festival experience into your North India itinerary. Ask about dates, local arrangements and availability before making your travel plans.')]
for name,title,items,desc in category_data:
    content=banner(title)+f'<section class="page-content"><p class="f-family-cursive s-c curs-heading">Find your next journey</p><h2 class="heading">{title}</h2><p class="lead-text">{desc}</p><p>Suggested itineraries · Availability, transport and inclusions are confirmed by enquiry.</p><div class="filter-bar"><label class="visually-hidden" for="tour-search">Search journeys</label><input type="search" id="tour-search" placeholder="Search by tour or destination…"><label class="visually-hidden" for="duration-filter">Filter by duration</label><select id="duration-filter"><option value="all">All durations</option><option value="short">1–3 days</option><option value="medium">4–7 days</option><option value="long">8+ days</option></select></div><p id="result-count" aria-live="polite">{len(items)} journeys</p><div class="cards-grid">'+''.join(card(t) for t in items)+'</div><p class="no-results" hidden>No journeys match your search. Try another destination or duration.</p></section>'
    save(name,title,content)

for t in tours:
    route=t['route'].replace('...','').strip('- ')
    stops=[x.strip() for x in re.split(r'\s*[-–]\s*',route) if x.strip()]
    segments=[]
    for i,stop in enumerate(stops):
        if i==0:desc=f'Start your journey in {stop.title()}. Confirm your pickup point, arrival time and onward travel arrangements with us.'
        elif i==len(stops)-1:desc=f'Continue to {stop.title()} for the final part of your suggested route. Confirm your drop-off point and allow time for any onward connections.'
        else:desc=f'Include time in {stop.title()} for the places that interest you. The sightseeing stops and time spent here can be discussed when planning your itinerary.'
        segments.append(f'<details{(" open" if i==0 else "")}><summary>Stop {i+1} · {escape(stop.title())}</summary><p>{escape(desc)}</p></details>')
    detail=f'''<section class="page-content"><p><a href="index.html">Home</a> › <a href="north-india.html">Explore tours</a> › {escape(t['title'])}</p><div class="two-column"><div class="details-body"><img class="content-photo" src="{t['image']}" alt="{escape(t['title'])}"><p class="mt-4"><i class="fa-solid fa-location-dot s-c"></i> {escape(route)}</p><h1 class="heading">{escape(t['title'])}</h1><div class="facts"><div><small>Suggested duration</small><strong>{t['duration']}</strong></div><div><small>Travel style</small><strong>Personalised journey</strong></div><div><small>Availability</small><strong>Enquire directly</strong></div></div><h2>About this journey</h2><p>Explore {escape(route)} with a travel plan built around your interests. This suggested {t['duration']} route is a starting point for your enquiry. Share your dates, pickup location and preferred stops with Vinod Tour and Travels to discuss transport, timing and a personalised quote.</p><h2>Journey highlights</h2><ul><li>Explore the destinations along your chosen route.</li><li>Discuss sightseeing stops and time for local experiences.</li><li>Choose pickup and drop-off points that suit your plans.</li><li>Speak directly with our Kotdwara team before confirming.</li></ul><h2>Your travel arrangements</h2><p>Ask for a written quote covering the vehicle, driver, route, travel dates and agreed inclusions. Confirm tolls, parking, accommodation, guides and entrance fees before booking; these are not automatically included.</p><h2>Suggested route</h2><p>The stops below outline the route, rather than a confirmed daily schedule. Exact timing and arrangements are agreed during your enquiry.</p><div class="itinerary">{''.join(segments)}</div><div class="review-box"><span class="stars">★★★★★</span><h2>4.9 / 5 · 177 Google reviews</h2><p>Vinod Tour and Travels · Taxi service in Uttarakhand</p><a href="{MAP}" target="_blank" rel="noopener">Find our business on Google Maps ↗</a></div></div><aside>{form(t['title'])}<div class="map-panel"><h2 style="font-size:22px">Prefer to call?</h2><p>Discuss your plans directly with us.</p><a class="button navy" href="tel:+918076069722">{PHONE}</a></div></aside></div></section>'''
    image_paths=[t['image']]
    if t in tours[:4]:
        image_paths += [assets[url] for url in assets if '/tour-triangulo-dorado-3-dias/img' in url][:3]
    else:
        group=tours[4:8] if t in tours[4:8] else tours[8:12] if t in tours[8:12] else tours[12:16] if t in tours[12:16] else tours[16:20]
        image_paths += [x['image'] for x in group if x['image']!=t['image']][:3]
    gallery='<div class="hero-gallery">'+''.join(f'<button class="gallery-image" type="button" data-gallery-src="{path}" aria-label="View destination photo {i+1}"><img src="{path}" alt="{escape(t["title"])} – destination inspiration {i+1}" loading="{("eager" if i==0 else "lazy")}"></button>' for i,path in enumerate(image_paths))+'</div>'
    dialog='<dialog class="photo-dialog" aria-label="Destination photo gallery"><button class="gallery-close" type="button" aria-label="Close gallery">×</button><button class="gallery-prev" type="button" aria-label="Previous photo">‹</button><img alt="Destination photo"><button class="gallery-next" type="button" aria-label="Next photo">›</button><p class="gallery-caption" aria-live="polite"></p></dialog>'
    original=f'<img class="content-photo" src="{t["image"]}" alt="{escape(t["title"])}">'
    detail=detail.replace(original,gallery)+dialog
    save('tour-'+t['slug'],t['title'],detail)

features=[('fa-route','Your choice of route','Tell us your destinations, travel dates and preferred stops.'),('fa-comments','Easy enquiries','Call or prepare a WhatsApp enquiry in a few simple steps.'),('fa-location-dot','Based in Kotdwara','Find us near UGB Bank, East, Jhandichour, Uttarakhand.'),('fa-car','Taxi & travel planning','Discuss local taxi and outstation travel requirements directly.')]
features_html='<div class="feature-grid">'+''.join(f'<div class="feature"><i class="fa-solid {icon}"></i><h3>{title}</h3><p>{desc}</p></div>' for icon,title,desc in features)+'</div>'
about_img=assets[BASE+'/assets/img/about/tourist-img.webp']
save('about','About Us',banner('About Vinod Tour and Travels')+f'<section class="page-content"><div class="two-column"><div><p class="f-family-cursive s-c curs-heading">Explore, enjoy, experience</p><h2 class="heading">Your Travel Contact in Kotdwara</h2><p class="lead-text">{en[90]}</p><a class="button" href="plan-my-trip.html">Plan your trip →</a></div><img class="content-photo" src="{about_img}" alt="Travel experiences across India"></div>{features_html}<div class="review-box"><span class="stars">★★★★★</span><h2>4.9 / 5 from 177 Google reviews</h2><p>Visit our business listing to find Vinod Tour and Travels in Kotdwara.</p><a href="{MAP}" target="_blank" rel="noopener">Find us on Google Maps ↗</a></div></section>')

contact=f'''<div><p class="f-family-cursive s-c curs-heading">Let’s talk travel</p><h2 class="heading">Get in Touch</h2><p>For taxi availability, route planning or a trip quote, contact Vinod Tour and Travels directly.</p><div class="contact-card"><h3><i class="fa-solid fa-phone"></i>Call us</h3><a href="tel:+918076069722">{PHONE}</a></div><div class="contact-card"><h3><i class="fa-brands fa-whatsapp"></i>WhatsApp</h3><a href="{WA}" target="_blank" rel="noopener">Start a conversation →</a></div><div class="contact-card"><h3><i class="fa-solid fa-location-dot"></i>Visit us</h3><p>{ADDRESS}</p><a href="{MAP}" target="_blank" rel="noopener">Open directions in Google Maps ↗</a></div><div class="map-panel"><span class="stars">★★★★★</span><h3>4.9 · 177 Google reviews</h3><p>Taxi service in Uttarakhand</p></div></div>'''
save('contact','Contact Us',banner('Contact Us')+'<section class="page-content two-column">'+contact+form(full=True)+'</section>')
save('plan-my-trip','Plan My Trip',banner('Plan Your Journey')+'<section class="page-content two-column"><div><p class="f-family-cursive s-c curs-heading">A trip that starts with you</p><h2 class="heading">Where Would You Like to Go?</h2><p class="lead-text">Share your travel dates, pickup location and destination. We will discuss your requirements and confirm the next steps directly.</p>'+features_html+f'<p>Prefer a quick conversation? <a href="tel:+918076069722">Call {PHONE}</a>.</p></div>'+form(full=True)+'</section>')

faqs=[('How do I enquire about a taxi or tour?',f'Call {PHONE} or use the enquiry form to prepare a WhatsApp message. Include your pickup point, destination, travel date and number of travellers.'),('Where is Vinod Tour and Travels located?',ADDRESS+'.'),('Does submitting the form confirm my booking?','No. The form prepares a message for you to review and send in WhatsApp. Confirm availability, the fare and the travel arrangements directly with our team.'),('Can I request a customised route?','Yes. Send your preferred destinations and stops as an enquiry. Route feasibility, vehicle availability and costs will be discussed before confirmation.'),('What is included in the price?','Ask for a written quote that lists the agreed inclusions. Confirm vehicle and driver charges, tolls, parking, accommodation, guide fees and entrance tickets as applicable.'),('What are the payment and cancellation terms?','Please request the applicable payment, cancellation and refund terms directly before confirming a booking. These depend on the arrangements agreed for your trip.'),('Are the tour itineraries fixed?','The routes shown are suggested journeys. Final timing, stops and services are confirmed after discussing your requirements.'),('Does this website collect my enquiry details?','The form processes your details in your browser to prepare a WhatsApp link. There is no booking database on this website. WhatsApp receives the details when you open the prepared link.')]
save('faq','Frequently Asked Questions',banner('Frequently Asked Questions')+'<section class="page-content article faq">'+''.join(f'<details><summary>{q}</summary><p>{escape(a)}</p></details>' for q,a in faqs)+'</section>')
save('privacy','Privacy',banner('Privacy')+f'''<article class="page-content article"><h2>Using this website</h2><p>This frontend website does not include an account system, chatbot, analytics tracking or a booking database. Enquiry forms prepare a message locally in your browser.</p><h2>WhatsApp enquiries</h2><p>When you open a prepared WhatsApp link, the information you entered is passed to WhatsApp as part of that link. You can review the message before sending it. Use only the contact and trip information you wish to share.</p><h2>External services</h2><p>WhatsApp and Google Maps are external services and have their own privacy practices. The site’s hosting provider may process ordinary request information to deliver the website.</p><h2>Questions</h2><p>For enquiries about information shared with {BRAND}, call <a href="tel:+918076069722">{PHONE}</a>.</p></article>''')
save('booking-information','Booking Information',banner('Booking Information')+f'''<article class="page-content article"><h2>Enquire before confirming</h2><p>The tour pages provide suggested travel routes. The website does not take payment or confirm reservations. Contact {BRAND} to check availability and agree the details of your journey.</p><h2>Confirm your quote</h2><p>Before booking, confirm the pickup and drop-off points, dates, vehicle, passenger count, itinerary, total fare and any additional charges. Ask which services and expenses are included.</p><h2>Payment, changes and cancellation</h2><p>Request the applicable payment, change, cancellation and refund terms directly before you agree to a booking. No universal cancellation or refund promise is made on this website.</p><h2>Contact</h2><p>Call <a href="tel:+918076069722">{PHONE}</a> or <a href="{WA}" target="_blank" rel="noopener">contact us on WhatsApp</a>.</p></article>''')

articles=[
[('A different side of Ranthambore','Ranthambore is often associated with wildlife, but a thoughtful visit can also make room for the surrounding landscape and local atmosphere. Leave space in your itinerary to slow down, enjoy the views and appreciate the setting beyond a single activity.'),('Plan your travel carefully','Agree your pickup point and travel schedule before you set off. If a safari is part of your plans, check the current booking arrangements, entry requirements and availability with the appropriate provider. A taxi enquiry does not include a safari reservation.'),('Make time for the journey','Avoid fitting too many stops into one day. Discuss driving time and your preferred breaks when planning the route. Carry the essentials you need and respect local guidance at every stop.')],
[('Let nature set the pace','Wildlife photography calls for patience. Observe quietly, give animals space and follow the instructions of your guide or park staff. The best travel memories often come from taking the time to notice the landscape around you.'),('Prepare your equipment','Pack the camera equipment you are comfortable carrying, along with spare batteries and memory cards. Protect equipment from dust and keep it secure while travelling. Check any current photography rules with the destination before your visit.'),('Travel responsibly','Stay in permitted areas and avoid disturbing wildlife for a photograph. Plan transport with enough time for the activities you have booked, and confirm pickup and return arrangements before departure.')],
[('A city shaped by the river','A visit to Varanasi offers a chance to spend time along the Ganga and observe the rhythms of the riverside. Walk at your own pace, allow time for the lanes and viewpoints, and approach places of worship with care and respect.'),('Respect local life','Ask before photographing people and respect requests not to take photographs. Follow local guidance around ceremonies and religious spaces. Quiet observation can be more rewarding than trying to capture every moment.'),('Plan your riverside visit','If you would like to take a boat ride, check conditions and arrangements directly with a local provider. Agree the route, price and safety arrangements before boarding. Share your onward travel plans when arranging transport to or from the city.')]]
save('blog','Travel Blog',banner('Travel Stories & Guides')+'<section class="page-content"><p class="f-family-cursive s-c curs-heading">A little inspiration for your next trip</p><h2 class="heading">Discover More of India</h2><div class="article-list mt-4">'+''.join(f'<article><img src="{b["image"]}" alt="{b["title"]}" loading="lazy"><div class="article-summary"><p>Travel guide</p><h2>{b["title"]}</h2><a class="button navy" href="{b["slug"]}.html">Read guide →</a></div></article>' for b in blogs)+'</div></section>')
for b,paragraphs in zip(blogs,articles):
    content=banner(b['title'])+f'<article class="page-content article"><img class="content-photo" src="{b["image"]}" alt="{b["title"]}"><p class="s-c">Travel guide · {BRAND}</p>'+''.join(f'<h2>{heading}</h2><p>{paragraph}</p>' for heading,paragraph in paragraphs)+f'<div class="map-panel"><h2>Planning a journey?</h2><p>Share your travel requirements with Vinod Tour and Travels.</p><a class="button" href="plan-my-trip.html">Plan my trip →</a></div></article>'
    save(b['slug'],b['title'],content)

save('404','Page Not Found',banner('Page Not Found')+'<section class="page-content"><h2>Let’s get you back on your journey.</h2><p>The page you are looking for could not be found.</p><a class="button" href="index.html">Return home →</a></section>')
from update_destinations import apply_updates
apply_updates(save, banner, form)
from prioritize_tours import prioritize_tours
prioritize_tours(save, banner)
from refine_layout import refine_layout
refine_layout()
print('Created',len(list(OUT.glob('*.html'))),'English frontend pages.')
