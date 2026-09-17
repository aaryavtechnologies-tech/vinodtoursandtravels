from pathlib import Path
from bs4 import BeautifulSoup
from urllib.parse import urlsplit
import re, json

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'dist'
errors=[]
pages=list(OUT.glob('*.html'))
for file in pages:
    html=file.read_text(encoding='utf-8')
    soup=BeautifulSoup(html,'html.parser')
    if soup.html.get('lang')!='en': errors.append(f'{file.name}: incorrect language')
    if len(soup.select('h1'))!=1:errors.append(f'{file.name}: expected one main heading')
    if re.search(r'tourporla|9536973121|8439031573|tawk|Llámenos|Más información|Días|paquetes',html,re.I):errors.append(f'{file.name}: old company or Spanish content')
    if soup.select('iframe,form[action],script[src^="http"]'):errors.append(f'{file.name}: backend / embed dependency')
    for tag in soup.select('[src],[href]'):
        link=tag.get('src') or tag.get('href')
        if link.startswith(('https:','http:','tel:','data:','#')):
            if tag.name in ('img','script','link','iframe') and not link.startswith('data:'):errors.append(f'{file.name}: external render asset {link}')
            if 'wa.me/' in link and 'wa.me/918076069722' not in link:errors.append(f'{file.name}: wrong WhatsApp number')
            continue
        if not (OUT/urlsplit(link).path).is_file():errors.append(f'{file.name}: missing {link}')
    ids=[el['id'] for el in soup.select('[id]')]
    if len(ids)!=len(set(ids)):errors.append(f'{file.name}: duplicate ids')
for file in OUT.rglob('*.css'):
    css=file.read_text(encoding='utf-8')
    for url in re.findall(r'url\([\"\']?([^\)\"\']+)',css):
        if url.startswith('data:'):continue
        if url.startswith(('http:','https:')):errors.append(f'{file.name}: remote CSS asset')
        elif not (file.parent/url.split('#')[0]).is_file():errors.append(f'{file.name}: missing CSS dependency {url}')
print(json.dumps({'pages_checked':len(pages),'errors':errors},indent=2))
raise SystemExit(bool(errors))
