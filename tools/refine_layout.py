"""Keep the responsive layout repairs reproducible after a content rebuild."""
from pathlib import Path
from bs4 import BeautifulSoup
from PIL import Image
import re

OUT = Path(__file__).resolve().parents[1] / 'dist'


def refine_layout():
    for path in OUT.glob('*.html'):
        soup = BeautifulSoup(path.read_text(encoding='utf-8'), 'html.parser')
        # Reserve the correct space before photos load, including replaced assets.
        for img in soup.select('img[src]'):
            asset = OUT / img['src']
            if asset.suffix.lower() in ('.jpg', '.jpeg', '.png', '.webp') and asset.exists():
                with Image.open(asset) as source:
                    img['width'], img['height'] = map(str, source.size)
        if path.name == 'index.html':
            heading = next(h for h in soup.select('h2') if 'Travel Your Way' in h.text)
            section = heading.find_parent('section')
            if 'company-section' not in section.get('class', []):
                copy = heading.parent
                copy['class'] = ['company-copy']
                photo = section.select_one('img').extract()
                photo['class'] = ['company-photo']
                frame = soup.new_tag('button', attrs={'type': 'button', 'class': 'company-photo-frame', 'data-gallery-src': photo['src'], 'aria-label': 'View our travellers photo'})
                frame.append(photo)
                grid = soup.new_tag('div', attrs={'class': 'company-grid'})
                grid.append(copy.extract())
                grid.append(frame)
                section.clear()
                section['class'] = ['page-content', 'company-section']
                section.append(grid)
            panel = soup.select_one('.travel-panel')
            if panel:
                section = panel.find_parent('section')
                # The inherited overlapping photo collage escaped its column.
                copy = panel.parent
                panel.extract()
                copy['class'] = ['journey-copy']
                features = copy.select_one('.row')
                features['class'] = ['journey-features']
                for item in features.find_all('div', recursive=False):
                    item['class'] = ['journey-feature']
                    item.select_one('img').decompose()
                photo = section.select_one('.video-sec img').extract()
                photo['class'] = ['journey-photo']
                frame = soup.new_tag('a', href='plan-my-trip.html', attrs={'class': 'journey-photo-frame', 'aria-label': 'Plan your next journey'})
                frame.append(photo)
                grid = soup.new_tag('div', attrs={'class': 'journey-grid'})
                grid.append(frame)
                grid.append(copy.extract())
                section.clear()
                section['class'] = ['page-content', 'journey-section']
                section.append(grid)
        output = re.sub(r'<!DOCTYPE html>\s*', '<!DOCTYPE html>\n', str(soup), count=1)
        path.write_text(output, encoding='utf-8')


if __name__ == '__main__':
    refine_layout()
