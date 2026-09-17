"""Download attributed destination photographs from Wikimedia Commons."""
from pathlib import Path
from urllib.parse import urlsplit, unquote
import json
import requests
import time
import warnings
from bs4 import MarkupResemblesLocatorWarning
warnings.filterwarnings('ignore', category=MarkupResemblesLocatorWarning)
from bs4 import BeautifulSoup
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'dist/assets/destinations'
OUT.mkdir(parents=True, exist_ok=True)
PAGES = {
    'manali': 'Manali, Himachal Pradesh', 'shimla': 'Shimla',
    'chandigarh': 'Chandigarh', 'amritsar': 'Golden Temple',
    'char-dham': 'Kedarnath Temple', 'haridwar': 'Har Ki Pauri',
    'rishikesh': 'Rishikesh', 'mussoorie': 'Mussoorie', 'nainital': 'Nainital',
    'jim-corbett': 'Jim Corbett National Park', 'lansdowne': 'Lansdowne, India',
    'delhi': 'India Gate', 'jaipur': 'Hawa Mahal', 'agra-fort': 'Agra Fort',
    'qutub-minar': 'Qutb Minar', 'lotus-temple': 'Lotus Temple', 'taj-mahal': 'Taj Mahal',
}

def fetch(item):
    slug, title = item
    session = requests.Session()
    session.headers['User-Agent'] = 'VinodTravelWebsite/1.0 (destination photography with attribution)'
    data = session.get('https://en.wikipedia.org/w/api.php', params={
        'action': 'query', 'format': 'json', 'prop': 'pageimages',
        'titles': title, 'redirects': 1, 'pithumbsize': 1280, 'pilicense': 'free'}, timeout=40).json()
    page = next(iter(data['query']['pages'].values()))
    url = page['thumbnail']['source']
    filename = page['pageimage']
    meta = session.get('https://commons.wikimedia.org/w/api.php', params={
        'action': 'query', 'format': 'json', 'prop': 'imageinfo',
        'titles': 'File:' + filename, 'iiprop': 'extmetadata|url'}, timeout=40).json()
    info = next(iter(meta['query']['pages'].values()))['imageinfo'][0]
    ext = info['extmetadata']
    clean = lambda key: BeautifulSoup(ext.get(key, {}).get('value', ''), 'html.parser').get_text(' ', strip=True)
    response = session.get(url, timeout=60)
    response.raise_for_status()
    path = OUT / (slug + Path(unquote(urlsplit(url).path)).suffix.lower())
    path.write_bytes(response.content)
    with Image.open(path) as img:
        img.verify()
    return slug, {'image': path.relative_to(ROOT/'dist').as_posix(), 'alt': title,
        'source': info['descriptionurl'], 'artist': clean('Artist'),
        'license': clean('LicenseShortName'), 'license_url': clean('LicenseUrl')}

if __name__ == '__main__':
    manifest_path = ROOT/'reference/destination-photos.json'
    manifest = json.loads(manifest_path.read_text()) if manifest_path.exists() else {}
    for item in PAGES.items():
        if item[0] in manifest:
            continue
        for attempt in range(4):
            try:
                slug, info = fetch(item)
                break
            except Exception as error:
                print(item[0], str(error)[:160], flush=True)
                if attempt == 3:
                    raise
                time.sleep(2)
        if info:
            manifest[slug] = info
            print(slug, info['license'], flush=True)
            manifest_path.write_text(json.dumps(manifest, indent=2), encoding='utf-8')
