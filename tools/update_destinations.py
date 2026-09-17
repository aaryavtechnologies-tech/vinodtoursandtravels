"""Apply destination additions and the owner's supplied traveller photographs."""
from pathlib import Path
from html import escape
import json
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'dist'
DESTINATIONS = [
    ('Char Dham', 'Uttarakhand', 'Pilgrimage', 'Plan your pilgrimage through Yamunotri, Gangotri, Kedarnath and Badrinath.', 'Share the shrines you wish to visit, your travel dates and preferred starting point. We can discuss the road journey and stops for your pilgrimage.'),
    ('Haridwar', 'Uttarakhand', 'Riverside & temples', 'Make time for the Ganga ghats and the spiritual atmosphere of Haridwar.', 'Plan your pickup, riverside visit and onward journey. Haridwar can also be included in an enquiry for Rishikesh or a longer Uttarakhand trip.'),
    ('Rishikesh', 'Uttarakhand', 'River & relaxation', 'Enjoy a journey to the riverside surroundings of Rishikesh.', 'Tell us whether you are planning a quiet stay, sightseeing or onward hill travel, and share your preferred pickup and drop-off points.'),
    ('Mussoorie', 'Uttarakhand', 'Hill getaway', 'Head to Mussoorie for hill views and a relaxed mountain break.', 'Discuss a journey through Dehradun to Mussoorie with time for your preferred local stops. Share your dates and the number of travellers.'),
    ('Nainital', 'Uttarakhand', 'Lakes & hills', 'Plan a lakeside holiday among the hills of Nainital.', 'Enquire about travel to Nainital, local sightseeing and nearby stops you would like to include. Your route can be tailored to the time you have.'),
    ('Jim Corbett', 'Uttarakhand', 'Nature getaway', 'Travel to the forest surroundings of the Jim Corbett region.', 'Discuss transport to your stay, pickup arrangements and onward travel. Include any separately arranged safari times when sharing your itinerary.'),
    ('Shimla', 'Himachal Pradesh', 'Hill station', 'Explore Shimla with a mountain journey shaped around your plans.', 'Share your pickup city, accommodation location and preferred sightseeing stops. You can also enquire about combining Shimla with Manali.'),
    ('Manali', 'Himachal Pradesh', 'Mountain escape', 'Set out for the valley landscapes and mountain atmosphere of Manali.', 'Plan your travel to Manali with time for breaks and the places you wish to visit. Tell us your dates, group size and onward destination.'),
    ('Chandigarh', 'Chandigarh', 'City break', 'Add Chandigarh to your city visit or onward hill journey.', 'Enquire about a city transfer, sightseeing journey or a stop on your route to Himachal Pradesh. Share your arrival details and travel preferences.'),
    ('Amritsar', 'Punjab', 'Heritage & culture', 'Plan a visit to Amritsar and the Golden Temple.', 'Tell us your pickup point and how much time you would like in Amritsar. Discuss city stops and onward travel as part of your personalised enquiry.'),
    ('Lansdowne', 'Uttarakhand', 'Quiet hill retreat', 'Take a peaceful hill break in Lansdowne, starting from Kotdwara or your preferred pickup point.', 'Discuss a short getaway or a longer Uttarakhand route with time in Lansdowne. Share your preferred dates and return arrangements.'),
]

def slug(name):
    return name.lower().replace(' ', '-')

def destination_cards():
    return '<div class="destination-grid">' + ''.join(
        f'<a class="destination-card" href="destination-{slug(name)}.html"><span class="destination-region">{region}</span><h3>{name}</h3><p>{intro}</p><span class="destination-link">Explore {name} <span aria-hidden="true">→</span></span></a>'
        for name, region, style, intro, description in DESTINATIONS) + '</div>'

def destination_section():
    return '<section id="destinations" class="page-content destination-section"><p class="f-family-cursive s-c curs-heading">From our home in Uttarakhand</p><h2 class="heading">Pilgrimages, Hills &amp; North India Getaways</h2><p class="lead-text">Discover Char Dham, riverside towns, quiet hill stations and vibrant cities. Choose your destination and let’s plan the journey.</p>' + destination_cards() + '</section>'

def apply_updates(save, banner, form):
    photos = json.loads((ROOT / 'reference/traveller-photos.json').read_text())
    def photo(number):
        return photos[number - 1]['image']

    def photo_tiles(numbers):
        tiles = '<div class="context-photos">'
        for number in numbers:
            item = photos[number - 1]
            caption = escape(item.get('caption', f'Travel memory {number}'))
            width, height = item['size']
            tiles += f'<button type="button" class="traveller-photo" data-gallery-src="{item["image"]}" aria-label="Open photo: {caption}"><img src="{item["image"]}" alt="{caption}" width="{width}" height="{height}" loading="lazy" decoding="async"><span>{caption} <span aria-hidden="true">↗</span></span></button>'
        return tiles + '</div>'

    vehicle_section = '<section class="page-content vehicle-section"><p class="f-family-cursive s-c curs-heading">On the road with us</p><h2 class="heading">Our Cars, Ready for Your Journey</h2><p class="lead-text">See our vehicles from the front, side and rear. Tap any photo to view it full size, then share your route, group size and luggage needs to check availability.</p>' + photo_tiles([40, 41, 42, 43, 24, 26]) + '<a class="button" href="plan-my-trip.html">Enquire about a taxi →</a></section>'
    agra_section = '<section class="page-content"><p class="f-family-cursive s-c curs-heading">Memories from Agra</p><h2 class="heading">Our Travellers at the Taj Mahal</h2><p class="lead-text">A few moments from visits to Agra, shared by Vinod Tour and Travels.</p>' + photo_tiles([31, 32, 33]) + '</section>'

    save('destinations', 'Our Destinations', banner('Our Destinations') + destination_section())
    for name, region, style, intro, description in DESTINATIONS:
        body = banner(name) + f'<section class="page-content two-column"><div class="details-body"><p class="destination-region">{region} · {style}</p><h2 class="heading">Your Journey to {name}</h2><p class="lead-text">{intro}</p><p>{description}</p><div class="map-panel"><h2>A journey planned around you</h2><p>Choose your pickup point, travel dates, preferred stops and return arrangements. Contact our Kotdwara team for vehicle availability and a personalised quote.</p></div><h2>Plan your travel</h2><ul><li>Share your pickup and drop-off locations.</li><li>Tell us your group size and luggage requirements.</li><li>Include the stops and overnight stays you have in mind.</li></ul><p>Final routes, timing, fares and inclusions are agreed when you enquire.</p><a href="destinations.html" class="button outline">Browse all destinations →</a></div><aside>{form(name)}</aside></section>'
        save('destination-' + slug(name), name + ' Taxi & Tour Enquiry', body)

    gallery = '<section id="travel-memories" class="page-content"><p class="f-family-cursive s-c curs-heading">Moments from the journey</p><h2 class="heading">Our Traveller Photo Gallery</h2><p class="lead-text">Welcomes, shared journeys and memories along the way with Vinod Tour and Travels.</p><div class="traveller-gallery">'
    for index, item in enumerate(photos, 1):
        width, height = item['size']
        caption = escape(item.get('caption', f'Travel memory {index:02} shared by Vinod Tour and Travels'))
        gallery += f'<button type="button" class="traveller-photo" data-gallery-src="{item["image"]}" aria-label="Open photo: {caption}"><img src="{item["image"]}" alt="{caption}" width="{width}" height="{height}" loading="lazy" decoding="async"><span>{caption} <span aria-hidden="true">↗</span></span></button>'
    gallery += '</div></section>'
    dialog = '<dialog class="photo-dialog" aria-label="Traveller photo gallery"><button class="gallery-close" type="button" aria-label="Close gallery">×</button><button class="gallery-prev" type="button" aria-label="Previous photo">‹</button><img alt="Travel memory"><button class="gallery-next" type="button" aria-label="Next photo">›</button><p class="gallery-caption" aria-live="polite"></p></dialog>'
    save('traveller-gallery', 'Traveller Photo Gallery', banner('Traveller Photo Gallery') + gallery + dialog)

    replacements = {'assets/841e157383.webp': photo(7), 'assets/22ca898b49.webp': photo(8), 'assets/795cd877bb.webp': photo(3), 'assets/98bc735f79.jpg': photo(17)}
    for path in OUT.glob('*.html'):
        soup = BeautifulSoup(path.read_text(encoding='utf-8'), 'html.parser')
        if path.name.startswith('destination') or path.name == 'traveller-gallery.html':
            soup.body['class'] = soup.body.get('class', []) + ['new-destination-page']
        for img in soup.select('img[src]'):
            if img['src'] in replacements:
                img['src'] = replacements[img['src']]
                img['alt'] = 'Traveller memories with Vinod Tour and Travels'
        menu = soup.select('.dropdown-menu')[1]
        links = '<a class="dropdown-item" href="destinations.html">All destinations</a>' + ''.join(f'<a class="dropdown-item" href="destination-{slug(name)}.html">{name}</a>' for name, *_ in DESTINATIONS)
        menu.insert(0, BeautifulSoup(links, 'html.parser'))
        menu['class'] = menu.get('class', []) + ['destination-menu']
        package_menu = soup.select('.dropdown-menu')[0]
        package_menu.insert(0, BeautifulSoup('<a class="dropdown-item" href="destinations.html">Uttarakhand &amp; North India</a>', 'html.parser'))
        footer_column = soup.select('.footer-grid>div')[2]
        footer_column.append(BeautifulSoup('<a href="destinations.html">Our destinations</a><a href="traveller-gallery.html">Traveller photo gallery</a>', 'html.parser'))
        if path.name == 'index.html':
            main = soup.select_one('main')
            hero = main.find('section')
            hero.replace_with(BeautifulSoup(f'<section class="traveller-hero"><div class="traveller-hero-copy"><p class="hero-eyebrow">VINOD TOUR AND TRAVELS · KOTDWARA</p><h1>Your Journey.<br>Our Local Touch.</h1><p>From Char Dham pilgrimages to mountain escapes and city discoveries, travel your way with us.</p><a class="button" href="destinations.html">Explore destinations →</a><a class="hero-gallery-link" href="traveller-gallery.html">Meet our travellers ↗</a></div><div class="traveller-hero-photos"><img src="{photo(7)}" alt="Travellers enjoying their journey" width="720" height="720" fetchpriority="high"><img src="{photo(3)}" alt="Travellers beside their taxi" width="1204" height="1599"></div></section>', 'html.parser'))
            for old_heading in main.select('h1')[1:]:
                old_heading.name = 'h2'
            main.select_one('.intro-strip').insert_after(BeautifulSoup(destination_section(), 'html.parser'))
            main.select_one('#destinations').insert_after(BeautifulSoup(vehicle_section, 'html.parser'))
            main.append(BeautifulSoup(gallery + dialog, 'html.parser'))
        elif path.name == 'north-india.html':
            soup.select_one('main').append(BeautifulSoup(destination_section(), 'html.parser'))
        elif path.name == 'about.html':
            soup.select_one('main').append(BeautifulSoup('<section class="page-content"><h2 class="heading">A Warm Welcome to Every Journey</h2><p>Shared welcomes and pickup memories with Vinod Tour and Travels.</p>' + photo_tiles([27, 29, 30]) + f'<a class="button" href="traveller-gallery.html">View all {len(photos)} photos →</a></section>', 'html.parser'))
        elif path.name in ('contact.html', 'plan-my-trip.html'):
            soup.select_one('main').append(BeautifulSoup(vehicle_section, 'html.parser'))
        if path.name in ('agra-tours.html', 'golden-triangle-tours.html') or path.stem.startswith(('tour-same-day-agra-', 'tour-overnight-taj-mahal-', 'tour-golden-triangle-tour-')):
            soup.select_one('main').append(BeautifulSoup(agra_section, 'html.parser'))
        if soup.select_one('[data-gallery-src]') and not soup.select_one('.photo-dialog'):
            soup.select_one('main').append(BeautifulSoup(dialog, 'html.parser'))
        path.write_text(str(soup), encoding='utf-8')
    print(f'Added {len(DESTINATIONS)} destinations and {len(photos)} traveller photographs.')
