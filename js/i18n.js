// ── TRANSLATIONS ────────────────────────────────
const TRANSLATIONS = {
  de: {
    // NAV
    nav_about:          'Über mich',
    nav_services:       'Leistungen',
    nav_impressum:      'Impressum',
    nav_contact:        'Kontakt',
    nav_blog:           'Aktuelles gibt es hier',
    // HERO
    availability:       'Verfügbar für neue Projekte · Bayern · Remote',
    h1_line1:           'Engineering das denkt.',
    h1_line2_pre:       'Software die\u00a0',
    h1_line2_ships:     'liefert.',
    subline:            'Senior-Ingenieur & Architekt mit tiefen Wurzeln in Hardware, Full-Stack-Entwicklung und KI-Werkzeugen. Ich bringe Präzision in komplexe Systeme und ein kreatives Auge für jedes Interface.',
    btn_primary:        'Projekt starten',
    btn_see_work:       'Meine Arbeiten',
    scroll_hint:        'Scrollen zum Entdecken',
    card_label:         'Was ich baue',
    svc1:               'Individuelle Anwendungen',
    svc2:               'Prozessautomatisierung & KI-Agenten',
    svc3:               'Sicherheitsprüfungen',
    svc4:               'Individuelle Schulungen',
    svc5:               'Ein Problem? Ich finde eine Lösung.',
    quote:              '„Ich habe Netzwerkprozessoren bei Intel gebaut und Aquarelle in Bayern gemalt.<br>Beide Denkweisen bringe ich in Ihr Projekt."',
    // ABOUT
    about_label:        'Über mich',
    about_h2_light:     'Ingenieur.',
    about_h2_bold:      'Architekt. Künstler.',
    about_bio:          'Ich begann meine künstlerische Laufbahn im Alter von 7 Jahren in Key West, Florida. Nach dem Armeedienst und ausgedehnten Reisen zog ich vor 19 Jahren nach Europa — heute lebe ich in Klosterlechfeld, Bayern.',
    about_bio2:         'Als Design-Ingenieur bei Intel entwickelte ich Netzwerkprozessoren in VHDL. Seit über 6 Jahren baue ich Web-Applikationen mit React, Node.js, TypeScript und MongoDB. Ingenieurswesen und Kunst sind meine beiden Leidenschaften — ich bringe all meine Erfahrungen mit, was Ihrem Projekt den entscheidenden Vorteil verschafft.',
    about_cta:          'Projekt starten',
    bio_fact1_title:    'Intel — Design-Ingenieur',
    bio_fact1_desc:     'VHDL, Netzwerkprozessoren',
    bio_fact2_title:    'Full-Stack-Entwicklung',
    bio_fact2_desc:     '6+ Jahre · React, Node, TypeScript, MongoDB',
    bio_fact2b_title:   'Python, C, C++ & Assembler',
    bio_fact2b_desc:    '20+ Jahre Erfahrung',
    bio_fact2c_title:   'MBA — Purdue University',
    bio_fact2c_desc:    '2007',
    bio_fact2d_title:   'Computer Systems Engineer — University of Arkansas',
    bio_fact2d_desc:    '2001',
    bio_fact3_title:    'Bildender Künstler',
    bio_fact3_desc:     'Öl, Aquarell, Holzschnitt, Fotografie',
    bio_fact4_title:    'Galerie Auxburg, Augsburg',
    bio_fact4_desc:     'Professionell ausstellender Künstler',
    bio_fact5_title:    'Va Tech — Architektur & Design',
    bio_fact5_desc:     'School of Architecture and Design',
    // SERVICES
    services_label:     'Leistungen',
    services_h2_light:  'Was ich',
    services_h2_bold:   'für Sie baue.',
    svc_title1:         'KI-Agenten & Prozessautomatisierung',
    svc_desc1:          'Wiederkehrende Abläufe übernimmt eine Maschine: LLM-Integration, RAG-Systeme, autonome Pipelines und Werkzeuge, die echte Aufgaben erledigen statt nur Vorschläge zu machen.',
    svc_title2:         'Architektur & Technische Beratung',
    svc_desc2:          'Systemdesign und technische Führung für skalierbare, wartbare Software. Von der ersten Skizze bis zur Implementierung — klar und umsetzbar.',
    svc_title3:         'Full-Stack-Webentwicklung',
    svc_desc3:          'Moderne Web-Apps mit React, Node.js, TypeScript und MongoDB. Schnell, sauber, wartbar — und gut anzusehen.',
    svc_title4:         'Komplexe Probleme lösen',
    svc_desc4:          'Wenn die Anforderung ungewöhnlich ist, bin ich besonders interessiert. Ich denke quer und finde Lösungen, die andere übersehen.',
    svc_title5:         'Sicherheitsprüfungen',
    svc_desc5:          'Ich prüfe Websites, Anwendungen und jede Art von Datenspeicher auf Schwachstellen — bevor es jemand anderes tut. Zugriffsrechte und DSGVO-Technik inklusive.',
    svc_title6:         'Individuelle Schulungen',
    svc_desc6:          'Maßgeschneiderte Kurse für Ihr Team: KI im Arbeitsalltag, KI-gestütztes Programmieren und die Arbeit mit KI-Agenten. Danach kommen Sie allein weiter.',
    // PRODUCTS
    products_label:     'Eigene Produkte',
    products_h2_light:  'Produkte,',
    products_h2_bold:   'die ich gebaut habe.',
    // CONTACT
    contact_label:      'Kontakt',
    contact_h2_light:   'Bereit,',
    contact_h2_bold:    'loszulegen?',
    contact_tagline:    'Erzählen Sie mir von Ihrem Projekt. Ich melde mich innerhalb von 24 Stunden.',
    contact_cta:        'E-Mail senden',
    contact_avail:      'Verfügbar für neue Projekte',
    contact_loc_label:  'Standort',
    contact_loc:        'Klosterlechfeld, Bayern',
    contact_remote:     'Weltweit verfügbar',
    // PORTFOLIO
    nav_chats:          'KI-Gespräche',
    nav_tools:          'Tools',
    nav_portfolio:      'Portfolio',
    nav_certs:          'Certifications',
    pf_label:           'Meine Arbeiten',
    pf_h1_light:        'Mein',
    pf_h1_bold:         ' Portfolio',
    pf_intro1:          'Eine Sammlung von Websites und Projekten, an denen ich gearbeitet habe. Alle wurden mit Claude Code und den Modellen Sonnet 4.6 oder Opus gebaut.',
    pf_intro2:          'Alle haben MCP-Anbindungen und sind so optimiert, dass Ihr KI-Agent direkt mit den verschiedenen Werkzeugen arbeiten kann, um zu erreichen, was auch immer Sie erreichen möchten. Meine gesamte Software ist in hohem Maße KI-freundlich. Wenn ich etwas tun kann, um sie noch freundlicher zu machen, sagen Sie mir Bescheid. Ich stelle es gern bereit, solange es kein Sicherheitsrisiko darstellt. Schreiben Sie mir für weitere Details.',
    pf_soon_h:          'In Arbeit, kurz vor der Veröffentlichung',
    pf_soon_note:       'Demnächst verfügbar — noch nicht öffentlich zugänglich.',
    pf_badge:           'Demnächst',
    pf_flash_desc:      'Eine Web- und Android-App, mit der man Karteikarten-Stapel erstellt und per Spaced Repetition lernt.',
    pf_notes_desc:      'Eine Notiz-App für das Web und Ihr Android-Handy.',
    pf_leguilde_desc:   'Eine Website, auf der Künstler ihr Portfolio online präsentieren und mit ihren Fans in Kontakt treten können. Dazu gibt es zwei Android-Apps: eine für Künstler zur Verwaltung ihres Portfolios und eine für Sammler und Fans, um die Werke der Künstler anzuschauen und sie direkt zu kontaktieren.',
    pf_crm_desc:        'Ein allgemeines Customer-Relationship-Management- und Lead-Finding-System aus Agenten für Marketingprojekte und Unternehmen.',
    pf_pa_desc:         'Eine Methode, um die Schritte in einem Geschäftsprozess zu finden, die es gar nicht geben sollte, statt sie nur zu beschleunigen. Sie zeigt, wie die Arbeit wirklich fließt, deckt die Wartezeiten zwischen den Schritten auf und streicht Schritte, die nur aus Gewohnheit existieren. KI kommt erst dann zum Einsatz, wo sie wirklich etwas bringt, nicht an jedem Schritt.',
    pf_cl_desc:         'Eine Plattform für den Elektronikentwurf, auf der Ihre eigene KI mitbaut, was auch immer Sie entwickeln. Schaltungen werden mit echter SPICE-Simulation geprüft (ngspice-Kurven statt Schätzungen), analog wie digital, vom RC-Filter bis zum Logikgatter. Gedacht ist sie auch für Embedded-Projekte wie den Raspberry Pi.',
    pf_back:            '← Zurück',
    // IMPRESSUM
    impressum_label:    'Rechtliches',
    impressum_heading:  'Impressum',
  },

  en: {
    // NAV
    nav_about:          'About',
    nav_services:       'Services',
    nav_impressum:      'Impressum',
    nav_contact:        'Get in Touch',
    nav_blog:           'All the latest can be found here',
    // HERO
    availability:       'Available for new projects · Bavaria · Remote',
    h1_line1:           'Engineering that thinks.',
    h1_line2_pre:       'Software that\u00a0',
    h1_line2_ships:     'ships.',
    subline:            'Senior engineer & architect with deep roots in hardware, full stack development, and AI tooling. I bring precision to complex systems and a creative eye to every interface.',
    btn_primary:        'Start a project',
    btn_see_work:       'See my work',
    scroll_hint:        'Scroll to explore',
    card_label:         'What I build',
    svc1:               'Custom Applications',
    svc2:               'Process Automation & AI Agents',
    svc3:               'Security Testing',
    svc4:               'Custom Training Courses',
    svc5:               'Have a problem? I can find a solution.',
    quote:              '"I\'ve built network processors at Intel and watercolors in Bavaria.<br>I bring both kinds of thinking to your project."',
    // ABOUT
    about_label:        'About',
    about_h2_light:     'Engineer.',
    about_h2_bold:      'Architect. Artist.',
    about_bio:          'I started my artistic journey at age 7 in Key West, Florida. After Army service and extensive travel, I moved to Europe 19 years ago — today I live in Klosterlechfeld, Bavaria.',
    about_bio2:         'As a design engineer at Intel I built network processors in VHDL. For 6+ years I\'ve been building web applications in React, Node.js, TypeScript, and MongoDB. Engineering and art are both passions of mine — I bring all of my experience with me, giving your project the winning advantage.',
    about_cta:          'Start a project',
    bio_fact1_title:    'Intel — Design Engineer',
    bio_fact1_desc:     'VHDL, network processors',
    bio_fact2_title:    'Full Stack Development',
    bio_fact2_desc:     '6+ years · React, Node, TypeScript, MongoDB',
    bio_fact2b_title:   'Python, C, C++ & Assembler',
    bio_fact2b_desc:    '20+ years experience',
    bio_fact2c_title:   'MBA — Purdue University',
    bio_fact2c_desc:    '2007',
    bio_fact2d_title:   'Computer Systems Engineer — University of Arkansas',
    bio_fact2d_desc:    '2001',
    bio_fact3_title:    'Visual Artist',
    bio_fact3_desc:     'Oil, watercolour, woodblock printing, photography',
    bio_fact4_title:    'Gallery Auxburg, Augsburg',
    bio_fact4_desc:     'Professional exhibiting artist',
    bio_fact5_title:    'Va Tech — Architecture & Design',
    bio_fact5_desc:     'School of Architecture and Design',
    // SERVICES
    services_label:     'Services',
    services_h2_light:  'What I',
    services_h2_bold:   'build for you.',
    svc_title1:         'AI Agents & Process Automation',
    svc_desc1:          'A machine takes over the jobs that come back every week: LLM integration, RAG systems, autonomous pipelines, and tools that do real work instead of only making suggestions.',
    svc_title2:         'Architecture & Technical Consulting',
    svc_desc2:          'System design and technical leadership for scalable, maintainable software. From the first sketch to implementation — clear and actionable.',
    svc_title3:         'Full Stack Web Development',
    svc_desc3:          'Modern web apps with React, Node.js, TypeScript, and MongoDB. Fast, clean, maintainable — and good-looking.',
    svc_title4:         'Complex Problem Solving',
    svc_desc4:          'When the requirement is unusual, I\'m most interested. I think laterally and find solutions others miss.',
    svc_title5:         'Security Testing',
    svc_desc5:          'I test websites, applications and any kind of data storage for vulnerabilities — before someone else does. Access control and GDPR technical checks included.',
    svc_title6:         'Custom Training Courses',
    svc_desc6:          'Tailored courses for your team: using AI day to day, AI-assisted coding, and working with AI agents. Afterwards you can carry on without me.',
    // PRODUCTS
    products_label:     'Products I\'ve Built',
    products_h2_light:  'Products',
    products_h2_bold:   'I\'ve built.',
    // CONTACT
    contact_label:      'Contact',
    contact_h2_light:   'Ready to',
    contact_h2_bold:    'get started?',
    contact_tagline:    'Tell me about your project. I\'ll get back to you within 24 hours.',
    contact_cta:        'Send an email',
    contact_avail:      'Available for new projects',
    contact_loc_label:  'Location',
    contact_loc:        'Klosterlechfeld, Bavaria',
    contact_remote:     'Available worldwide',
    // PORTFOLIO
    nav_chats:          'AI Chats',
    nav_tools:          'Tools',
    nav_portfolio:      'Portfolio',
    nav_certs:          'Certifications',
    pf_label:           'My Work',
    pf_h1_light:        'My',
    pf_h1_bold:         ' Portfolio',
    pf_intro1:          'A collection of websites and projects I have worked on, these were all built using Claude Code, and the Sonnet 4.6 or Opus models.',
    pf_intro2:          'All of these have MCP connections and are optimized so that your AI agent can interface directly with the various tools and work with them to accomplish whatever you wish to accomplish. All of my software is highly AI-friendly, and if there is anything I can do to make it friendlier, let me know. I will be happy to provide it, as long as it is not a security risk. Email me for more details.',
    pf_soon_h:          'Currently underway, nearing public deployment',
    pf_soon_note:       'Coming soon — not yet available to the public.',
    pf_badge:           'Coming soon',
    pf_flash_desc:      'A web and Android app that allows the user to create decks of flashcards and use them for spaced repetition learning.',
    pf_notes_desc:      'A note taking app that runs on the web and on your Android phone.',
    pf_leguilde_desc:   'A website that allows artists to set up their portfolio on the web for public viewing and contact with their fans. There are also two Android apps: one for artists to manage their portfolio, and one for collectors and fans to look at artists\' works and contact the artists directly.',
    pf_crm_desc:        'A general customer relationship management and lead finding system of agents for marketing projects and businesses.',
    pf_pa_desc:         'A method for finding the steps in a business process that shouldn\'t exist, rather than just making them faster. It maps how work really flows, finds the waiting time between steps, and removes the steps that only exist out of habit. AI is then added only at the points where it actually helps, not bolted onto every step.',
    pf_cl_desc:         'An electronics design platform where your own AI helps you build whatever you are building. Circuits are checked with real SPICE simulation (ngspice waveforms, not guesses), for analog and digital designs from RC filters to logic gates. It\'s built with embedded projects such as the Raspberry Pi in mind.',
    pf_back:            '← Back',
    // IMPRESSUM (legal notice stays in German by law — label only translates)
    impressum_label:    'Legal',
    impressum_heading:  'Impressum',
  },

  // ── ADD NEW LANGUAGES HERE ──
  // fr: { ... }  copy 'en' block as template
};

let currentLang = 'de';

function setLang(lang) {
  if (!TRANSLATIONS[lang]) return;
  currentLang = lang;
  const t = TRANSLATIONS[lang];

  document.querySelectorAll('[data-i18n]').forEach(el => {
    const key = el.getAttribute('data-i18n');
    if (t[key] !== null && t[key] !== undefined) {
      el.innerHTML = t[key];
    }
  });

  // Feature-flagged element — translate even if hidden
  const btnWork = document.getElementById('btn-see-work');
  if (btnWork) btnWork.textContent = t.btn_see_work;

  document.querySelectorAll('.lang-btn').forEach(btn => {
    btn.classList.toggle('active', btn.getAttribute('onclick').includes("'" + lang + "'"));
  });

  document.documentElement.lang = lang;

  // Announce the change so language-aware widgets (hero video) can react
  // without i18n needing to know they exist.
  document.dispatchEvent(new CustomEvent('langchange', { detail: { lang } }));
}
// ────────────────────────────────────────────────
