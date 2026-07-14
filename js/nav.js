// ── NAV SCROLL BEHAVIOUR ──────────────────────────
const nav = document.getElementById('main-nav');

window.addEventListener('scroll', () => {
  nav.classList.toggle('scrolled', window.scrollY > 10);
}, { passive: true });

// ── MOBILE MENU (hamburger) ───────────────────────
const navToggle = nav.querySelector('.nav-toggle');

if (navToggle) {
  const closeMenu = () => {
    nav.classList.remove('menu-open');
    navToggle.setAttribute('aria-expanded', 'false');
  };

  navToggle.addEventListener('click', () => {
    const open = nav.classList.toggle('menu-open');
    navToggle.setAttribute('aria-expanded', String(open));
  });

  // close after choosing a link
  nav.querySelectorAll('ul a').forEach((link) => {
    link.addEventListener('click', closeMenu);
  });

  // close on Escape
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') closeMenu();
  });

  // close if the viewport grows back to the desktop nav
  window.addEventListener('resize', () => {
    if (window.innerWidth > 1200) closeMenu();
  }, { passive: true });
}
// ──────────────────────────────────────────────────
