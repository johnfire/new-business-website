// ── NAV / PHOTO-STRIP SCROLL BEHAVIOUR ──────────
const strip = document.getElementById('photo-strip');
const nav   = document.getElementById('main-nav');
const hero  = document.getElementById('hero');
const MAXH  = 110;
const NAV_H = 64;

function onScroll() {
  const sy      = window.scrollY;
  const newH    = Math.max(0, MAXH - sy);
  const opacity = newH / MAXH;

  strip.style.height  = newH + 'px';
  strip.style.opacity = opacity;
  nav.style.top       = newH + 'px';
  hero.style.paddingTop = (newH + NAV_H) + 'px';

  nav.classList.toggle('scrolled', sy > MAXH);
}

window.addEventListener('scroll', onScroll, { passive: true });
// ────────────────────────────────────────────────
