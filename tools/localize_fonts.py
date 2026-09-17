from pathlib import Path
from urllib.request import Request, urlopen
from urllib.parse import urljoin
import json, re, hashlib
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'dist'
mapping=json.loads((ROOT/'reference/assets.json').read_text())
done=set()
while True:
    pending=[(url,path) for url,path in mapping.items() if path.endswith('.css') and url not in done]
    if not pending:break
    for url,path in pending:
        done.add(url)
        css=(OUT/path).read_text(encoding='utf-8')
        for raw in re.findall(r'url\([\"\']?([^\)\"\']+)',css):
            if raw.startswith('data:'):continue
            if (OUT/'assets'/raw).is_file():continue
            target=urljoin(url,raw)
            suffix=Path(target.split('?')[0]).suffix or '.css'
            name=hashlib.sha1(target.encode()).hexdigest()[:10]+suffix
            file=OUT/'assets'/name
            if not file.exists():file.write_bytes(urlopen(Request(target,headers={'User-Agent':'Mozilla/5.0'}),timeout=30).read())
            mapping[target]='assets/'+name
            css=css.replace(raw,name)
        (OUT/path).write_text(css,encoding='utf-8')
(ROOT/'reference/assets.json').write_text(json.dumps(mapping,indent=2),encoding='utf-8')
print('Stylesheets and font dependencies are local:',len(mapping),'assets.')
