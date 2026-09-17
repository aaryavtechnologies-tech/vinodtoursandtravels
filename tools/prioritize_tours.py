"""Lead with Delhi, Jaipur and Agra, then hills; keep Uttarakhand last."""
from pathlib import Path
from html import escape
import json
from bs4 import BeautifulSoup
from update_destinations import DESTINATIONS, slug

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'dist'

def prioritize_tours(save, banner):
    photos = json.loads((ROOT/'reference/destination-photos.json').read_text(encoding='utf-8'))
    ordered = sorted(DESTINATIONS, key=lambda d: ['Manali','Shimla','Chandigarh','Amritsar','Char Dham','Haridwar','Rishikesh','Mussoorie','Nainital','Jim Corbett','Lansdowne'].index(d[0]))
    def picture(key, **attrs):
        info = photos[key]
        attributes = ' '.join(f'{k}="{escape(str(v), quote=True)}"' for k,v in attrs.items())
        return f'<img src="{info["image"]}" alt="{escape(info["alt"], quote=True)}" loading="lazy" decoding="async" {attributes}>'
    def card(name, region, intro, href, key):
        return f'<a class="destination-card photo-package" href="{href}">{picture(key)}<div class="destination-card-copy"><span class="destination-region">{region}</span><h3>{name}</h3><p>{intro}</p><span class="destination-link">Explore tour <span aria-hidden="true">→</span></span></div></a>'
    def destinations(items, section_id, eyebrow, title, description):
        cards = ''.join(card(name, region, intro, f'destination-{slug(name)}.html', slug(name)) for name,region,style,intro,desc in items)
        return f'<section id="{section_id}" class="page-content destination-section"><p class="f-family-cursive s-c curs-heading">{eyebrow}</p><h2 class="heading">{title}</h2><p class="lead-text">{description}</p><div class="destination-grid">{cards}</div></section>'
    hills = destinations(ordered[:4], 'mountain-city-tours', 'Your next escape', 'Manali, Shimla &amp; More', 'From mountain valleys to city landmarks, choose the next stop on your journey.')
    uttarakhand = destinations(ordered[4:], 'uttarakhand-tours', 'Closer to nature', 'Uttarakhand Tour Packages', 'Round off your travel plans with sacred rivers, quiet hill towns and Himalayan pilgrimages.')
    heritage_cards = ''.join([
        card('Delhi, Jaipur &amp; Agra', 'Golden Triangle', 'Three iconic cities, one memorable journey. Explore Delhi, Jaipur and Agra with a route planned around you.', 'golden-triangle-tours.html', 'taj-mahal'),
        card('Delhi Sightseeing', 'Delhi', 'Discover India Gate, Qutub Minar and Lotus Temple with time for your preferred stops.', 'delhi-tours.html', 'delhi'),
        card('Taj Mahal &amp; Agra Fort', 'Agra', 'Make time for the Taj Mahal and Agra’s historic fort.', 'agra-tours.html', 'agra-fort'),
        card('Jaipur &amp; Rajasthan', 'Rajasthan', 'Explore the Pink City, grand forts and the colourful cities of Rajasthan.', 'rajasthan-tours.html', 'jaipur'),
    ])
    heritage = f'<section id="heritage-tours" class="page-content destination-section"><p class="f-family-cursive s-c curs-heading">Start with the classics</p><h2 class="heading">Delhi, Jaipur, Agra &amp; Rajasthan</h2><p class="lead-text">Our featured sightseeing journeys, with flexible pickup points and personalised routes.</p><div class="destination-grid heritage-grid">{heritage_cards}</div></section>'
    landmark_keys = [('delhi','India Gate · Delhi'),('jaipur','Hawa Mahal · Jaipur'),('taj-mahal','Taj Mahal · Agra'),('agra-fort','Agra Fort · Agra'),('qutub-minar','Qutub Minar · Delhi'),('lotus-temple','Lotus Temple · Delhi')]
    landmarks = '<section class="page-content landmark-section"><p class="f-family-cursive s-c curs-heading">Places to remember</p><h2 class="heading">The Sights of Delhi, Jaipur &amp; Agra</h2><div class="landmark-grid">' + ''.join(f'<button type="button" class="traveller-photo" data-gallery-src="{photos[key]["image"]}" aria-label="View {label}">{picture(key)}<span>{label} <span aria-hidden="true">↗</span></span></button>' for key,label in landmark_keys) + '</div></section>'
    credits = '<section class="page-content article"><p>Destination photographs are reproduced under the licenses linked below. Owner-supplied vehicle and traveller photographs are provided by Vinod Tour and Travels.</p>'
    for key, info in photos.items():
        credits += f'<h2>{escape(info["alt"])}</h2>{picture(key)}<p>Photo: {escape(info["artist"])} · <a href="{escape(info["source"],quote=True)}">Original photograph</a> · <a href="{escape(info["license_url"],quote=True)}">{escape(info["license"])}</a>. Displayed at responsive sizes; previews may be cropped.</p>'
    save('photo-credits', 'Photo Credits', banner('Photo Credits') + credits + '</section>')
    hero = f'<section class="traveller-hero heritage-hero"><div class="traveller-hero-copy"><p class="hero-eyebrow">VINOD TOUR AND TRAVELS</p><h1>Delhi, Jaipur<br>&amp; Agra Tours</h1><p>Discover the Taj Mahal, Delhi’s landmarks and the royal sights of Rajasthan. Your route, your pace, with our team along the way.</p><a class="button" href="golden-triangle-tours.html">Explore Delhi, Jaipur &amp; Agra →</a><a class="hero-gallery-link" href="rajasthan-tours.html">Discover Jaipur &amp; Rajasthan ↗</a></div><div class="heritage-hero-photos"><figure class="hero-taj">{picture("taj-mahal", fetchpriority="high").replace("loading=\"lazy\"", "loading=\"eager\"")}<figcaption>Taj Mahal · Agra</figcaption></figure><figure>{picture("jaipur")}<figcaption>Hawa Mahal · Jaipur</figcaption></figure><figure>{picture("delhi")}<figcaption>India Gate · Delhi</figcaption></figure></div></section>'
    for path in OUT.glob('*.html'):
        soup = BeautifulSoup(path.read_text(encoding='utf-8'), 'html.parser')
        def fragment(html):
            return BeautifulSoup(html, 'html.parser')
        main = soup.select_one('main')
        # Use the same package order in navigation on every page.
        menus = soup.select('.dropdown-menu')
        if len(menus) >= 2:
            menus[0].clear()
            for href,label in [('golden-triangle-tours.html','Delhi, Jaipur & Agra'),('delhi-tours.html','Delhi Sightseeing'),('agra-tours.html','Agra Tours'),('rajasthan-tours.html','Jaipur & Rajasthan'),('destination-manali.html','Manali'),('destination-shimla.html','Shimla'),('north-india.html','Other North India Tours'),('destinations.html#uttarakhand-tours','Uttarakhand Packages')]:
                menus[0].append(fragment(f'<a class="dropdown-item" href="{href}">{escape(label)}</a>'))
            old_links = [a.extract() for a in menus[1].select('a') if not a.get('href','').startswith(('destination-', 'destinations.'))]
            menus[1].clear()
            menus[1].append(fragment('<a class="dropdown-item" href="destinations.html">All destinations</a><a class="dropdown-item" href="golden-triangle-tours.html">Delhi, Jaipur &amp; Agra</a><a class="dropdown-item" href="rajasthan-tours.html">Jaipur &amp; Rajasthan</a>'))
            for name,*_ in ordered[:4]:
                menus[1].append(fragment(f'<a class="dropdown-item" href="destination-{slug(name)}.html">{name}</a>'))
            for link in old_links:
                if link.get('href') not in ('golden-triangle.html',): menus[1].append(link)
            for name,*_ in ordered[4:]:
                menus[1].append(fragment(f'<a class="dropdown-item" href="destination-{slug(name)}.html">{name}</a>'))
        soup.select_one('.footer-grid>div:nth-child(3)').append(fragment('<a href="photo-credits.html">Photo credits</a>'))
        if path.name == 'index.html':
            sections = main.find_all('section', recursive=False)
            def section_with(text):
                return next(section for section in sections if any(text in h.get_text() for h in section.select('h2')))
            golden = section_with('Golden Triangle India')
            golden.select_one('h2').string = 'Delhi, Jaipur & Agra — Golden Triangle Tours'
            golden['id'] = 'golden-triangle-packages'
            rajasthan = section_with('Rajasthan')
            agra = section_with('Taj Mahal & Agra Tours')
            other_tours = [section_with('Golden Triangle & Varanasi Tours'), section_with('Kerala & South India Journeys')]
            supporting = [s for s in sections if s not in [sections[0], soup.select_one('#destinations'), golden,rajasthan,agra,*other_tours] and not s.select('.home-img-view') and s.select_one('h2') is not None]
            # Explicitly keep the business, fleet and gallery after all package groups.
            supporting = [s for s in supporting if not any('Explore Our Tour Categories' in h.text for h in s.select('h2'))]
            intro = soup.select_one('.intro-strip').extract()
            intro.select_one('span').string = 'Delhi · Jaipur · Agra · Rajasthan · North India'
            dialog = soup.select_one('.photo-dialog').extract()
            for s in [golden,rajasthan,agra,*other_tours,*supporting]: s.extract()
            main.clear()
            main.append(fragment(hero)); main.append(intro)
            main.append(fragment('<nav class="tour-shortcuts" aria-label="Explore tour regions"><a href="#heritage-tours">Delhi, Jaipur &amp; Agra</a><a href="rajasthan-tours.html">Rajasthan</a><a href="#mountain-city-tours">Manali &amp; more</a><a href="#uttarakhand-tours">Uttarakhand</a></nav>'))
            main.append(fragment(heritage)); main.append(golden); main.append(agra); main.append(rajasthan)
            main.append(fragment(hills))
            for s in other_tours: main.append(s)
            main.append(fragment(uttarakhand)); main.append(fragment(landmarks))
            for s in supporting: main.append(s)
            main.append(dialog)
            soup.title.string = 'Delhi, Jaipur & Agra Tours | Vinod Tour and Travels'
            soup.select_one('meta[name="description"]')['content'] = 'Explore Delhi, Jaipur, Agra and Rajasthan with Vinod Tour and Travels. Discover Manali, other North India tours and Uttarakhand packages, with taxi enquiries and personalised routes.'
        elif path.name in ('destinations.html', 'north-india.html'):
            existing = soup.select_one('#destinations')
            if existing: existing.replace_with(fragment(heritage + hills + uttarakhand))
        elif path.stem.startswith('destination-'):
            key = path.stem.removeprefix('destination-')
            details = soup.select_one('.details-body')
            details.insert(0, fragment(f'<figure class="destination-lead-photo">{picture(key)}</figure>'))
        if path.name in ('delhi-tours.html','agra-tours.html','rajasthan-tours.html','golden-triangle-tours.html') or path.stem.startswith('tour-golden-triangle-tour-'):
            main.append(fragment(landmarks))
            if not soup.select_one('.photo-dialog'):
                main.append(fragment('<dialog class="photo-dialog" aria-label="Destination photos"><button class="gallery-close" type="button" aria-label="Close gallery">×</button><button class="gallery-prev" type="button" aria-label="Previous photo">‹</button><img alt="Destination photo"><button class="gallery-next" type="button" aria-label="Next photo">›</button><p class="gallery-caption" aria-live="polite"></p></dialog>'))
        path.write_text(str(soup), encoding='utf-8')
