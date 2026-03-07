// ── NAV SCROLL BEHAVIOUR ──────────────────────────
const nav = document.getElementById('main-nav');

window.addEventListener('scroll', () => {
  nav.classList.toggle('scrolled', window.scrollY > 10);
}, { passive: true });
// ──────────────────────────────────────────────────
