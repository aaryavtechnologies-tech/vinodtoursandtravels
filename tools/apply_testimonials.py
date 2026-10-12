# -*- coding: utf-8 -*-
"""Generate and apply Google Reviews testimonial slider to every page before footer."""
import json
from pathlib import Path
from html import escape

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / 'dist'
REVIEWS_FILE = DIST / 'reviews.json'

with open(REVIEWS_FILE, 'r', encoding='utf-8') as f:
    reviews = json.load(f)

print(f"Loaded {len(reviews)} reviews from reviews.json")

# Google palette colors
AVATAR_COLORS = [
    '#1a73e8', '#c2185b', '#7b1fa2', '#00897b',
    '#388e3c', '#e65100', '#5c6bc0', '#0097a7',
    '#d32f2f', '#689f38'
]

def get_avatar_color(name):
    h = 0
    for ch in name:
        h = ord(ch) + ((h << 5) - h)
    return AVATAR_COLORS[abs(h) % len(AVATAR_COLORS)]

def build_card_html(r):
    name = escape(r['name'])
    url = escape(r['url'])
    date = escape(r['date'])
    text = escape(r['text'])
    initial = (r['name'].strip()[:1] or 'U').upper()
    color = get_avatar_color(r['name'])
    is_long = len(r['text']) > 120
    read_more_btn = '<button type="button" class="testimonial-read-more" aria-expanded="false">Read more</button>' if is_long else ''
    
    return f'''<div class="testimonial-card">
  <div class="testimonial-card-header">
    <div class="testimonial-profile">
      <div class="testimonial-avatar" style="background-color: {color};">{initial}</div>
      <div class="testimonial-meta">
        <a class="testimonial-name" href="{url}" target="_blank" rel="noopener">{name}</a>
        <span class="testimonial-date">{date}</span>
      </div>
    </div>
    <div class="testimonial-google-logo">
      <img src="assets/google-g-logo.svg" alt="Google review" width="24" height="24" loading="lazy" decoding="async">
    </div>
  </div>
  <div class="testimonial-stars" aria-label="5 out of 5 stars">★★★★★</div>
  <div class="testimonial-body">
    <p class="testimonial-text">{text}</p>
    {read_more_btn}
  </div>
</div>'''

# Pre-render first 3 cards for static HTML fallback (zero CLS)
first_3_cards = "\n".join(build_card_html(r) for r in reviews[:3])

testimonials_section = f'''<section class="testimonials-section" aria-label="Customer Testimonials">
  <div class="testimonials-container">
    <div class="testimonials-header">
      <span class="testimonials-subtitle">OUR TESTIMONIALS</span>
      <h2 class="testimonials-title">What They Say</h2>
    </div>
    <div class="testimonials-carousel" aria-roledescription="carousel">
      <button class="carousel-arrow carousel-arrow-prev" type="button" aria-label="Previous review">
        <svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="15 18 9 12 15 6"></polyline></svg>
      </button>
      <div class="carousel-viewport">
        <div class="carousel-track">
{first_3_cards}
        </div>
      </div>
      <button class="carousel-arrow carousel-arrow-next" type="button" aria-label="Next review">
        <svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="9 18 15 12 9 6"></polyline></svg>
      </button>
    </div>
    <div class="testimonials-footer-score">
      <strong>Google</strong> rating score: <strong>5.0</strong> of 5, based on <strong>{len(reviews)} reviews</strong>
    </div>
  </div>
</section>'''

# Apply to all 57 HTML pages in dist/
html_pages = list(DIST.glob('*.html'))
updated_pages = 0

for page in html_pages:
    content = page.read_text(encoding='utf-8')
    # If already applied, remove old testimonials section first
    if '<section class="testimonials-section"' in content:
        import re
        content = re.sub(r'<section class="testimonials-section".*?</section>', '', content, flags=re.DOTALL)
    
    if '</main><footer class="site-footer">' in content:
        content = content.replace('</main><footer class="site-footer">', f'</main>{testimonials_section}<footer class="site-footer">')
        page.write_text(content, encoding='utf-8')
        updated_pages += 1
    else:
        print(f"Warning: footer boundary not found in {page.name}")

print(f"Successfully applied testimonials section to {updated_pages} of {len(html_pages)} pages.")

# Now update dist/app.js to include reviews array and slider engine
app_js_path = DIST / 'app.js'
app_js = app_js_path.read_text(encoding='utf-8')

# Remove any previous reviews code if present
if '/* GOOGLE_REVIEWS_START */' in app_js:
    app_js = app_js.split('/* GOOGLE_REVIEWS_START */')[0].strip() + '\n'

reviews_json_compact = json.dumps(reviews, ensure_ascii=False)

app_js_extension = f'''
/* GOOGLE_REVIEWS_START */
const REVIEWS_DATA = {reviews_json_compact};

(function initReviewsSlider() {{
  const carousel = document.querySelector('.testimonials-carousel');
  if (!carousel) return;
  const track = carousel.querySelector('.carousel-track');
  const prevBtn = carousel.querySelector('.carousel-arrow-prev');
  const nextBtn = carousel.querySelector('.carousel-arrow-next');
  const viewport = carousel.querySelector('.carousel-viewport');
  if (!track || !viewport) return;

  const AVATAR_COLORS = [
    '#1a73e8', '#c2185b', '#7b1fa2', '#00897b',
    '#388e3c', '#e65100', '#5c6bc0', '#0097a7',
    '#d32f2f', '#689f38'
  ];

  function getAvatarColor(name) {{
    let h = 0;
    for (let i = 0; i < name.length; i++) {{
      h = name.charCodeAt(i) + ((h << 5) - h);
    }}
    return AVATAR_COLORS[Math.abs(h) % AVATAR_COLORS.length];
  }}

  function escapeHTML(str) {{
    return str
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;');
  }}

  // Append remaining reviews starting from current count in track
  const currentCount = track.children.length;
  if (currentCount < REVIEWS_DATA.length) {{
    const frag = document.createDocumentFragment();
    for (let i = currentCount; i < REVIEWS_DATA.length; i++) {{
      const r = REVIEWS_DATA[i];
      const initial = (r.name.trim().charAt(0) || 'U').toUpperCase();
      const color = getAvatarColor(r.name);
      const isLong = r.text.length > 120;
      const card = document.createElement('div');
      card.className = 'testimonial-card';
      card.innerHTML = `
        <div class="testimonial-card-header">
          <div class="testimonial-profile">
            <div class="testimonial-avatar" style="background-color: ${{color}};">${{initial}}</div>
            <div class="testimonial-meta">
              <a class="testimonial-name" href="${{escapeHTML(r.url)}}" target="_blank" rel="noopener">${{escapeHTML(r.name)}}</a>
              <span class="testimonial-date">${{escapeHTML(r.date)}}</span>
            </div>
          </div>
          <div class="testimonial-google-logo">
            <img src="assets/google-g-logo.svg" alt="Google review" width="24" height="24" loading="lazy" decoding="async">
          </div>
        </div>
        <div class="testimonial-stars" aria-label="5 out of 5 stars">★★★★★</div>
        <div class="testimonial-body">
          <p class="testimonial-text">${{escapeHTML(r.text)}}</p>
          ${{isLong ? '<button type="button" class="testimonial-read-more" aria-expanded="false">Read more</button>' : ''}}
        </div>
      `;
      frag.appendChild(card);
    }}
    track.appendChild(frag);
  }}

  let currentIndex = 0;
  let autoSlideTimer = null;
  let isHovered = false;
  let isDragging = false;
  let startX = 0;

  function getCardsPerView() {{
    if (window.innerWidth > 991) return 3;
    if (window.innerWidth > 639) return 2;
    return 1;
  }}

  function getCardStep() {{
    const firstCard = track.querySelector('.testimonial-card');
    if (!firstCard) return 0;
    const cardWidth = firstCard.getBoundingClientRect().width;
    const gap = parseFloat(window.getComputedStyle(track).gap) || 22;
    return cardWidth + gap;
  }}

  function getMaxIndex() {{
    const total = track.children.length;
    const perView = getCardsPerView();
    return Math.max(0, total - perView);
  }}

  function updateSlider(animate = true) {{
    track.style.transition = animate ? 'transform 0.45s cubic-bezier(0.25, 1, 0.5, 1)' : 'none';
    const step = getCardStep();
    const offset = currentIndex * step;
    track.style.transform = `translateX(-${{offset}}px)`;
  }}

  function nextSlide() {{
    const max = getMaxIndex();
    if (currentIndex >= max) {{
      currentIndex = 0;
    }} else {{
      currentIndex++;
    }}
    updateSlider(true);
  }}

  function prevSlide() {{
    const max = getMaxIndex();
    if (currentIndex <= 0) {{
      currentIndex = max;
    }} else {{
      currentIndex--;
    }}
    updateSlider(true);
  }}

  function startAutoSlide() {{
    stopAutoSlide();
    autoSlideTimer = setInterval(() => {{
      if (!isHovered && !isDragging) {{
        nextSlide();
      }}
    }}, 3600);
  }}

  function stopAutoSlide() {{
    if (autoSlideTimer) {{
      clearInterval(autoSlideTimer);
      autoSlideTimer = null;
    }}
  }}

  function resetAutoSlide() {{
    stopAutoSlide();
    startAutoSlide();
  }}

  prevBtn?.addEventListener('click', () => {{
    prevSlide();
    resetAutoSlide();
  }});

  nextBtn?.addEventListener('click', () => {{
    nextSlide();
    resetAutoSlide();
  }});

  carousel.addEventListener('mouseenter', () => {{ isHovered = true; }});
  carousel.addEventListener('mouseleave', () => {{ isHovered = false; }});
  carousel.addEventListener('focusin', () => {{ isHovered = true; }});
  carousel.addEventListener('focusout', () => {{ isHovered = false; }});

  // Swipe gesture for touch devices
  viewport.addEventListener('touchstart', (e) => {{
    isDragging = true;
    startX = e.touches[0].clientX;
    stopAutoSlide();
  }}, {{ passive: true }});

  viewport.addEventListener('touchend', (e) => {{
    if (!isDragging) return;
    isDragging = false;
    const endX = e.changedTouches[0].clientX;
    const diff = endX - startX;
    if (diff > 40) {{
      prevSlide();
    }} else if (diff < -40) {{
      nextSlide();
    }}
    resetAutoSlide();
  }}, {{ passive: true }});

  // Read more / Read less delegation
  track.addEventListener('click', (e) => {{
    const btn = e.target.closest('.testimonial-read-more');
    if (btn) {{
      const card = btn.closest('.testimonial-card');
      const text = card?.querySelector('.testimonial-text');
      if (text) {{
        const isExpanded = text.classList.toggle('expanded');
        btn.textContent = isExpanded ? 'Read less' : 'Read more';
        btn.setAttribute('aria-expanded', String(isExpanded));
      }}
    }}
  }});

  let resizeTimer;
  window.addEventListener('resize', () => {{
    clearTimeout(resizeTimer);
    resizeTimer = setTimeout(() => {{
      const max = getMaxIndex();
      if (currentIndex > max) currentIndex = max;
      updateSlider(false);
    }}, 120);
  }});

  startAutoSlide();
}})();
'''

app_js_path.write_text(app_js.strip() + '\n' + app_js_extension, encoding='utf-8')
print("Updated dist/app.js successfully.")
