// ── HERO VIDEO ──────────────────────────────────
// Click-to-load YouTube embed (Zwei-Klick-Lösung).
//
// Nothing is requested from Google until the visitor clicks: the poster is
// served from this domain and the iframe is created on demand, pointed at
// youtube-nocookie.com. Without JavaScript the facade stays a plain link to
// YouTube, so the video is always reachable.

const HERO_VIDEOS = {
  de: {
    id:     'HjNTXOYGww4',
    poster: 'images/video/intro-de.jpg',
    label:  'Intro-Video ansehen — 90 Sekunden',
  },
  en: {
    id:     'AMyBZBL3nUE',
    poster: 'images/video/intro-en.jpg',
    label:  'Watch the intro video — 90 seconds',
  },
};

const EMBED_PARAMS = 'autoplay=1&rel=0&modestbranding=1&playsinline=1';

function heroVideoFrame() {
  return document.getElementById('hero-video');
}

// Swap the facade for a live player. Only ever called from a click.
function playHeroVideo(lang) {
  const frame = heroVideoFrame();
  const cfg = HERO_VIDEOS[lang];
  if (!frame || !cfg) return;

  const iframe = document.createElement('iframe');
  iframe.src = 'https://www.youtube-nocookie.com/embed/' + cfg.id + '?' + EMBED_PARAMS;
  iframe.title = cfg.label;
  iframe.allow = 'accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture';
  iframe.referrerPolicy = 'strict-origin-when-cross-origin';
  iframe.allowFullscreen = true;
  iframe.className = 'hv-player';

  frame.classList.add('is-playing');
  frame.replaceChildren(iframe);
}

// Return the frame to its poster state — also stops playback, which is what
// we want when the visitor switches language mid-video.
function resetHeroVideo(lang) {
  const frame = heroVideoFrame();
  const cfg = HERO_VIDEOS[lang];
  if (!frame || !cfg) return;

  const link = document.createElement('a');
  link.className = 'hv-facade';
  link.href = 'https://youtu.be/' + cfg.id;
  link.target = '_blank';
  link.rel = 'noopener';
  link.setAttribute('aria-label', cfg.label);

  const poster = document.createElement('img');
  poster.className = 'hv-poster';
  poster.src = cfg.poster;
  poster.alt = '';
  poster.loading = 'lazy';
  poster.width = 1280;
  poster.height = 720;
  // A missing poster must not show a broken image — the panel colour stands in.
  poster.addEventListener('error', () => poster.remove());

  const play = document.createElement('span');
  play.className = 'hv-play';
  play.setAttribute('aria-hidden', 'true');

  const caption = document.createElement('span');
  caption.className = 'hv-caption';
  caption.textContent = cfg.label;

  link.append(poster, play, caption);
  link.addEventListener('click', (ev) => {
    ev.preventDefault();
    playHeroVideo(lang);
  });

  frame.classList.remove('is-playing');
  frame.replaceChildren(link);
}

document.addEventListener('langchange', (ev) => resetHeroVideo(ev.detail.lang));
