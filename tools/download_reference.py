from pathlib import Path
from urllib.request import Request, urlopen
from urllib.parse import urljoin, urlsplit, quote
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup
import json, re

ROOT=Path(__file__).resolve().parents[1]
CACHE=ROOT/'reference'
OUT=ROOT/'dist'
CACHE.mkdir(exist_ok=True)
(OUT/'assets').mkdir(parents=True,exist_ok=True)
BASE='https://www.tourporlaindia.com/'
home=(ROOT/'reference.html').read_text(encoding='utf-8')
(CACHE/'home.html').write_text(home,encoding='utf-8')
pages=['sobre-nosotros','contacto','planificar-mi-recorrido','preguntas-frecuentes','tour/tour-triangulo-dorado-3-dias','paquetes-turisticos-de-agra','blog/aventuras-inesperadas-en-ranthambore-mas-alla-del-safar']
def get(url):
    return urlopen(Request(quote(url,safe=':/?=&%+'),headers={'User-Agent':'Mozilla/5.0'}),timeout=40).read()
def page(p):
    try:
        data=get(BASE+p)
        (CACHE/(p.replace('/','__')+'.html')).write_bytes(data)
        return p,len(data)
    except Exception as e: return p,str(e)
with ThreadPoolExecutor(max_workers=6) as ex: print(list(ex.map(page,pages)))
s=BeautifulSoup(home,'html.parser')
urls={x.get('src') for x in s.select('img[src]')}
urls.update(BASE+'assets/css/'+x for x in ['bootstrap.min.css','style.css'])
urls.add('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css')
urls.add('https://fonts.googleapis.com/css2?family=Heebo:wght@400;500;600&family=Nunito:wght@600;700;800&display=swap')
for f in CACHE.glob('*.html'):
    soup=BeautifulSoup(f.read_text(encoding='utf-8'),'html.parser')
    urls.update(urljoin(BASE,x['src']) for x in soup.select('img[src]'))
mapping={}
def asset(url):
    if not url or url.startswith('data:'):return
    import hashlib
    suffix=Path(urlsplit(url).path).suffix or '.css'
    name=hashlib.sha1(url.encode()).hexdigest()[:10]+suffix
    path=OUT/'assets'/name
    try:
        if not path.exists():path.write_bytes(get(url))
        mapping[url]='assets/'+name
        return url,path
    except Exception as e: print('FAILED',url,str(e))
with ThreadPoolExecutor(max_workers=8) as ex: results=list(ex.map(asset,urls))
for result in results:
    if not result or result[1].suffix!='.css':continue
    url,path=result
    css=path.read_text(encoding='utf-8')
    for dep in re.findall(r'url\([\"\']?([^\)\"\']+)',css):
        if dep.startswith('data:'):continue
        depurl=urljoin(url,dep.split('#')[0])
        res=asset(depurl)
        if res:css=css.replace(dep,res[1].name)
    path.write_text(css,encoding='utf-8')
(CACHE/'assets.json').write_text(json.dumps(mapping,indent=2),encoding='utf-8')
print('Downloaded',len(mapping),'assets')
