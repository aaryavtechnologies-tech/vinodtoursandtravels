'use strict';
const toggle = document.querySelector('.navbar-toggler');
const navigation = document.querySelector('#navbarCollapse');
toggle?.addEventListener('click', () => {
  const open = navigation.classList.toggle('show');
  toggle.setAttribute('aria-expanded', String(open));
  toggle.setAttribute('aria-label', open ? 'Close navigation' : 'Open navigation');
});
document.querySelectorAll('.dropdown-toggle').forEach(button => {
  button.addEventListener('click', event => {
    event.preventDefault();
    const open = button.nextElementSibling.classList.toggle('show');
    button.setAttribute('aria-expanded', String(open));
  });
  button.addEventListener('keydown', event => {
    if (event.key === ' ') { event.preventDefault(); button.click(); }
  });
});
document.addEventListener('keydown', event => {
  if (event.key !== 'Escape') return;
  document.querySelectorAll('.dropdown-menu.show').forEach(menu => {
    menu.classList.remove('show');
    menu.previousElementSibling.setAttribute('aria-expanded', 'false');
    menu.previousElementSibling.blur();
  });
  navigation?.classList.remove('show');
  toggle?.setAttribute('aria-expanded', 'false');
});
const localToday = new Date();
localToday.setMinutes(localToday.getMinutes() - localToday.getTimezoneOffset());
document.querySelectorAll('input[type="date"]').forEach(input => { input.min = localToday.toISOString().slice(0, 10); });
document.querySelectorAll('.enquiry-form').forEach(form => {
  form.addEventListener('submit', event => {
    event.preventDefault();
    if (!form.reportValidity()) return;
    const fields = new FormData(form);
    const lines = ['Hello Vinod Tour and Travels, I would like to enquire about a trip.'];
    const labels = {name:'Name',phone:'Phone',pickup:'Pickup',destination:'Destination / tour',date:'Travel date',travellers:'Travellers',service:'Service',message:'Additional details'};
    Object.entries(labels).forEach(([key,label]) => { const value = String(fields.get(key) || '').trim(); if (value) lines.push(`${label}: ${value}`); });
    const url = 'https://wa.me/918076069722?text=' + encodeURIComponent(lines.join('\n'));
    const result = form.querySelector('.success-message');
    result.hidden = false;
    result.replaceChildren();
    const message = document.createElement('p');
    message.textContent = 'Your enquiry is ready. Open WhatsApp to review it and press Send. Your booking is confirmed only after speaking with our team.';
    const link = document.createElement('a');
    link.href = url; link.target = '_blank'; link.rel = 'noopener'; link.textContent = 'Open enquiry in WhatsApp →';
    result.append(message, link);
    result.focus();
  });
});
const search = document.querySelector('#tour-search');
const duration = document.querySelector('#duration-filter');
function filterTours() {
  let visible = 0;
  document.querySelectorAll('[data-tour]').forEach(card => {
    const matchesText = card.textContent.toLowerCase().includes((search?.value || '').trim().toLowerCase());
    const days = Number(card.dataset.days);
    const filter = duration?.value || 'all';
    const matchesDuration = filter === 'all' || (filter === 'short' ? days <= 3 : filter === 'medium' ? days >= 4 && days <= 7 : days >= 8);
    card.hidden = !(matchesText && matchesDuration); if (!card.hidden) visible++;
  });
  const count = document.querySelector('#result-count');
  if (count) count.textContent = `${visible} ${visible === 1 ? 'journey' : 'journeys'}`;
  const empty = document.querySelector('.no-results');
  if (empty) empty.hidden = visible !== 0;
}
search?.addEventListener('input', filterTours);
duration?.addEventListener('change', filterTours);
const gallery = document.querySelector('.photo-dialog');
const photos = Array.from(document.querySelectorAll('[data-gallery-src]'));
let currentPhoto = 0;
function showPhoto(index) {
  currentPhoto = (index + photos.length) % photos.length;
  gallery.querySelector('img').src = photos[currentPhoto].dataset.gallerySrc;
  gallery.querySelector('img').alt = photos[currentPhoto].querySelector('img').alt;
  gallery.querySelector('.gallery-caption').textContent = `Photo ${currentPhoto + 1} of ${photos.length}`;
}
photos.forEach((photo,index) => photo.addEventListener('click', () => { showPhoto(index); gallery.showModal(); }));
gallery?.querySelector('.gallery-close').addEventListener('click', () => gallery.close());
gallery?.querySelector('.gallery-prev').addEventListener('click', () => showPhoto(currentPhoto - 1));
gallery?.querySelector('.gallery-next').addEventListener('click', () => showPhoto(currentPhoto + 1));
gallery?.addEventListener('keydown', event => {
  if (event.key === 'ArrowLeft') { event.preventDefault(); showPhoto(currentPhoto - 1); }
  if (event.key === 'ArrowRight') { event.preventDefault(); showPhoto(currentPhoto + 1); }
});
