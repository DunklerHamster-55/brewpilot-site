# -*- coding: utf-8 -*-
"""
BrewPilot Landing Page — Generator
Erzeugt /index.html (de-CH) und /en/index.html (en) aus einer Textquelle.
Design und Texte übernommen aus dem Claude-Design-Entwurf.
"""
import os, html, shutil

SITE = "/home/claude/site"
BASE_URL = "https://brew-pilot.com"

# ── Launch-Schalter ────────────────────────────────────────────────────────────
# "soon"  = Badge grau, Hinweis „Bald verfügbar“
# "store" = Badge verlinkt auf APP_STORE_URL
LAUNCH = "soon"
APP_STORE_URL = "https://apps.apple.com/app/idAPPID"   # nach Freigabe eintragen
APP_ID = ""                                            # für Smart App Banner

def e(s):
    return html.escape(str(s), quote=True)

# ── Texte ─────────────────────────────────────────────────────────────────────
STR = {
"de": dict(
  locale="de_CH", htmllang="de-CH", other="en", other_label="English", other_href="/en/",
  self_href="/",
  title="BrewPilot — Dein persönlicher Kaffee-Coach für iPhone",
  meta_desc="BrewPilot sagt dir nach jedem Espresso, was du an der Mühle ändern sollst — konkret, für deine Mühle. Offline, ohne Konto, ohne Datenerhebung. Gratis für iPhone.",
  skip="Zum Inhalt springen",
  theme_label="Dunkles Design umschalten",
  lang_group="Sprache",
  hero_kicker="Für iPhone · iOS 26 · gratis",
  hero_h1="Dein persönlicher Kaffee-Coach",
  hero_sub="Schluss mit Rätselraten am Siebträger. BrewPilot sagt dir nach jedem Shot, was du ändern sollst — konkret, für deine Mühle.",
  hero_soon="Bald verfügbar",
  hero_soon_note="BrewPilot erscheint in Kürze im App Store.",
  badge1="Laden im", badge2="App Store",
  badge_aria="BrewPilot im App Store laden",
  hero_alt="BrewPilot-Coach nach einem Shot: 40 % Konfidenz, Diagnose „Unterextrahiert — zu sauer“ und die Empfehlung, die Mühle 5 Klicks feiner zu stellen.",
  steps_kicker="So funktioniert es",
  steps_h2="Dial-In in drei Schritten",
  steps=[("1","Shot brühen","Dosis, Zeit und Ausbeute eintragen — der Sweet-Spot-Timer läuft mit."),
         ("2","Sagen, wie er schmeckt","Zu sauer, zu bitter, zu wässrig, fast gut oder perfekt — ein Tap genügt."),
         ("3","Konkrete Anweisung bekommen","Keine Theorie, sondern ein Handgriff an deiner Mühle. Mit Konfidenz-Anzeige, wie nah du dran bist.")],
  steps_quote="„Stelle deine Eureka Mignon auf Mahlgrad 3.3 — 5 Klicks feiner.“",
  steps_quote_cap="Eine typische Empfehlung. Deine Mühle, deine Skala.",
  steps_alt="BrewPilot zeigt den Mahlgrad 3.8 auf der Skala der eigenen Mühle mit grün markierter Zielzone.",
  feat_h2="Was BrewPilot kann",
  feat_sub="Vom ersten Dial-In bis zum Jahresrückblick — alles in einer ruhigen App, alles auf deinem iPhone.",
  features=[
    dict(key="brew", title="Dial-In &amp; Brühen",
         desc="Der Coach führt dich Shot für Shot zum Sweet Spot — und kann auch Filter.",
         img="shot-pourover",
         alt="Geführter V60-Brühplan in BrewPilot: Bloom-Phase mit Timer und Giess-Ziel 30 Gramm.",
         points=["Coach-Engine mit Konfidenz-Anzeige","Sweet-Spot-Timer für die Extraktion",
                 "Geführte Brühpläne für V60, Chemex, AeroPress &amp; French Press","Wetter-adaptiver Mahlgrad"]),
    dict(key="beans", title="Bohnen verwalten",
         desc="Neue Bohne in Sekunden drin — und du weisst immer, wie frisch sie ist und was die Tasse kostet.",
         img="shot-import",
         alt="Bohnen-Import per Shop-Link in BrewPilot: Die Produktseite wird nur auf dem iPhone gelesen.",
         points=["Import per Etiketten-Foto, Shop-Link aus Safari oder von Freunden","Frische-Tracking ab Röstdatum",
                 "Automatischer Vorrats-Abzug","Kosten pro Tasse"]),
    dict(key="stats", title="Dein Fortschritt",
         desc="Sieh dich besser werden — über alle Shots, Bohnen und Länder hinweg.",
         img="shot-statistiken",
         alt="Brew-Statistiken in BrewPilot: Extraktionszeit, Ratio, Sweet-Spot-Quote und Rating-Verlauf.",
         points=["Statistiken zu Zeit, Ratio und Sweet-Spot-Quote","Coffee Passport mit Länder-Stempeln",
                 "Jahresrückblick „Wrapped“","Bestenliste pro Bohne"]),
    dict(key="dash", title="Immer griffbereit",
         desc="Der letzte Shot, die Frische deiner Bohnen und der Coach — ohne die App zu öffnen.",
         img="shot-dashboard",
         alt="BrewPilot-Startseite: letzter Shot mit Rezept, Frische-Status „Aktuell Peak“ und Bohnen-Vorrat.",
         points=["Widgets für Home- und Sperrbildschirm","Live Activity in der Dynamic Island",
                 "Coach-Chat — läuft komplett auf dem Gerät"]),
  ],
  share_h3="Teilen, ohne Konto",
  share_p="Gute Bohnen spricht man weiter. BrewPilot macht daraus eine Datei — kein Account, keine Cloud dazwischen.",
  share_points=["Bohnen und Rezepte per AirDrop an Freunde","Geteilte Dateien öffnen sich direkt in der App",
                "Rezept-Karten zum Posten auf Social Media"],
  priv_kicker="Privatsphäre",
  priv_h2="Deine Daten bleiben bei dir",
  priv_sub="BrewPilot ist ein Werkzeug, kein Datensammler. Es gibt schlicht keinen Server, an den etwas gehen könnte.",
  priv_points=[("Kein Konto","Keine Registrierung, keine Anmeldung. App öffnen, loslegen."),
               ("Keine Cloud","Alles liegt auf deinem iPhone — und in deinem normalen Backup."),
               ("Keine Datenerhebung","Kein Tracking, keine Analytics, keine Werbe-IDs."),
               ("KI auf dem Gerät","Coach-Chat und Textverständnis laufen lokal per Apple Intelligence.")],
  priv_site="Das gilt auch für diese Website: keine Cookies, keine Tracker.",
  roast_kicker="Für Röstereien",
  roast_h2="Eure Bohnen, direkt in der App",
  roast_p1="Wer BrewPilot nutzt, importiert neue Bohnen am liebsten direkt von eurer Website — Name, Herkunft, Röstgrad, Preis und Bild werden automatisch übernommen. Dafür braucht es nur zwei Dinge: strukturierte Produktdaten (Shopify, WooCommerce und die meisten Systeme liefern sie ab Werk mit) und ein lesbares Röstdatum auf der Tüte. Beides habt ihr wahrscheinlich schon.",
  roast_p2="Für Röstereien, die weitergehen möchten, entsteht gerade ein Format, mit dem eine Bohne samt empfohlenem Rezept per Link oder QR-Code direkt in die App wandert — inklusive eurer Empfehlung für Mahlgrad, Dosis und Verhältnis. Interesse? Schreibt uns.",
  faq_h2="Häufige Fragen",
  faq=[("Was kostet BrewPilot?","Die App ist gratis, ohne Werbung und ohne Kaufzwang. Später wird es eine optionale Pro-Version mit Zusatzfunktionen geben; alles, was heute gratis ist, bleibt es auch für alle, die jetzt starten."),
       ("Brauche ich ein Konto?","Nein. Keine Registrierung, keine Anmeldung, kein Cloud-Zwang — nach dem Öffnen kannst du sofort loslegen."),
       ("Welche Geräte werden unterstützt?","iPhone ab iOS 26. Einzelne Funktionen (Textverständnis beim Import, Coach-Chat) nutzen Apple Intelligence und erscheinen nur auf Geräten, die das unterstützen — ohne sie funktioniert die App vollständig, nur diese Extras fehlen. iPad und Apple Watch sind geplant."),
       ("Funktioniert BrewPilot auch für Filterkaffee?","Ja. Neben dem Espresso-Dial-In gibt es geführte Brühpläne für V60, Chemex, AeroPress und French Press — mit Phasen, Zielgewichten und Timer."),
       ("Was passiert mit meinen Daten?","Sie bleiben auf deinem iPhone. BrewPilot hat keinen Server, sammelt nichts und wertet nichts aus. Deine Daten verlassen das Gerät nur, wenn du selbst etwas teilst — und sind Teil deines normalen iPhone-Backups."),
       ("In welchen Sprachen gibt es die App?","Deutsch und Englisch.")],
  foot_tag="Dein persönlicher Kaffee-Coach",
  foot_support="Support", foot_privacy="Datenschutz", foot_imprint="Impressum",
  foot_note="Keine Cookies, kein Tracking — auch hier nicht.",
),
"en": dict(
  locale="en_US", htmllang="en", other="de", other_label="Deutsch", other_href="/",
  self_href="/en/",
  title="BrewPilot — Your personal coffee coach for iPhone",
  meta_desc="After every espresso, BrewPilot tells you exactly what to change on your grinder. Offline, no account, no data collection. Free for iPhone.",
  skip="Skip to content",
  theme_label="Toggle dark mode",
  lang_group="Language",
  hero_kicker="For iPhone · iOS 26 · free",
  hero_h1="Your personal coffee coach",
  hero_sub="No more guesswork at the espresso machine. After every shot, BrewPilot tells you exactly what to change — for your grinder.",
  hero_soon="Coming soon",
  hero_soon_note="BrewPilot is launching on the App Store shortly.",
  badge1="Download on the", badge2="App Store",
  badge_aria="Download BrewPilot on the App Store",
  hero_alt="BrewPilot coach after a shot: 40% confidence, diagnosis “under-extracted — too sour” and a recommendation to grind 5 clicks finer.",
  steps_kicker="How it works",
  steps_h2="Dial in, in three steps",
  steps=[("1","Pull a shot","Log dose, time and yield — the sweet-spot timer runs alongside."),
         ("2","Say how it tastes","Too sour, too bitter, too watery, almost there or perfect — one tap."),
         ("3","Get a concrete instruction","No theory — one adjustment on your grinder, with a confidence score showing how close you are.")],
  steps_quote="“Set your Eureka Mignon to grind setting 3.3 — 5 clicks finer.”",
  steps_quote_cap="A typical recommendation. Your grinder, your scale.",
  steps_alt="BrewPilot showing grind setting 3.8 on your own grinder’s scale with a green target zone.",
  feat_h2="What BrewPilot does",
  feat_sub="From your first dial-in to the year in review — one calm app, everything on your iPhone.",
  features=[
    dict(key="brew", title="Dial-in &amp; brewing",
         desc="The coach walks you to the sweet spot shot by shot — and handles filter too.",
         img="shot-pourover",
         alt="Guided V60 brew plan in BrewPilot: bloom phase with timer and a 30 gram pour target.",
         points=["Coach engine with confidence score","Sweet-spot timer for extraction",
                 "Guided brew plans for V60, Chemex, AeroPress &amp; French press","Weather-adaptive grind size"]),
    dict(key="beans", title="Manage your beans",
         desc="A new bag is in the app in seconds — and you always know how fresh it is and what a cup costs.",
         img="shot-import",
         alt="Bean import via shop link in BrewPilot: the product page is read on your iPhone only.",
         points=["Import via label photo, shop link from Safari, or from friends","Freshness tracking from roast date",
                 "Automatic stock deduction","Cost per cup"]),
    dict(key="stats", title="Your progress",
         desc="Watch yourself get better — across shots, beans and countries.",
         img="shot-statistiken",
         alt="Brew statistics in BrewPilot: extraction time, ratio, sweet-spot rate and rating history.",
         points=["Stats for time, ratio and sweet-spot rate","Coffee Passport with country stamps",
                 "“Wrapped” year in review","Leaderboard per bean"]),
    dict(key="dash", title="Always at hand",
         desc="Your last shot, bean freshness and the coach — without opening the app.",
         img="shot-dashboard",
         alt="BrewPilot home screen: last shot with recipe, freshness status “currently at peak” and bean stock.",
         points=["Widgets for home and lock screen","Live Activity in the Dynamic Island",
                 "Coach chat — runs entirely on device"]),
  ],
  share_h3="Share, no account needed",
  share_p="Good beans deserve to be passed on. BrewPilot turns them into a file — no account, no cloud in between.",
  share_points=["AirDrop beans and recipes to friends","Shared files open straight in the app",
                "Recipe cards for social media"],
  priv_kicker="Privacy",
  priv_h2="Your data stays with you",
  priv_sub="BrewPilot is a tool, not a data collector. There simply is no server anything could be sent to.",
  priv_points=[("No account","No sign-up, no login. Open the app and start."),
               ("No cloud","Everything lives on your iPhone — and in your regular backup."),
               ("No data collection","No tracking, no analytics, no ad IDs."),
               ("On-device AI","Coach chat and text understanding run locally via Apple Intelligence.")],
  priv_site="The same goes for this website: no cookies, no trackers.",
  roast_kicker="For roasters",
  roast_h2="Your beans, straight into the app",
  roast_p1="BrewPilot users love importing new beans directly from your website — name, origin, roast level, price and photo are picked up automatically. All it takes is two things: structured product data (Shopify, WooCommerce and most systems ship it out of the box) and a readable roast date on the bag. You probably have both already.",
  roast_p2="For roasters who want to go further, a format is in the works that sends a bean plus your recommended recipe into the app via link or QR code — including your suggested grind, dose and ratio. Interested? Get in touch.",
  faq_h2="Frequently asked questions",
  faq=[("How much does BrewPilot cost?","The app is free, with no ads and nothing you have to buy. An optional Pro version with extra features will come later; everything that is free today stays free for everyone who starts now."),
       ("Do I need an account?","No. No registration, no login, no forced cloud — open the app and start right away."),
       ("Which devices are supported?","iPhone running iOS 26 or later. Some features (text understanding on import, coach chat) use Apple Intelligence and only appear on devices that support it — the app works fully without them, you just miss those extras. iPad and Apple Watch are planned."),
       ("Does BrewPilot work for filter coffee?","Yes. Besides the espresso dial-in there are guided brew plans for V60, Chemex, AeroPress and French press — with phases, target weights and a timer."),
       ("What happens to my data?","It stays on your iPhone. BrewPilot has no server, collects nothing and analyzes nothing. Your data only leaves the device when you share something yourself — and it is part of your regular iPhone backup."),
       ("Which languages is the app available in?","German and English.")],
  foot_tag="Your personal coffee coach",
  foot_support="Support", foot_privacy="Privacy", foot_imprint="Legal notice",
  foot_note="No cookies, no tracking — not here either.",
),
}

# ── CSS ───────────────────────────────────────────────────────────────────────
CSS = """
*,*::before,*::after{box-sizing:border-box}
:root{
  --bg:#F5EDE6; --bg2:#EEE1D5; --card:#FFFFFF; --ink:#2A1F1B; --sub:#6B5A50;
  --copper:#8D6E63; --copper-deep:#7A5C50; --line:rgba(42,31,27,.12);
  --band:#2A1F1B; --band-ink:#F5EDE6; --band-sub:#CBB8AC; --band-accent:#BC9A8A;
  --shadow:0 24px 60px -20px rgba(42,31,27,.45);
  --shadow-sm:0 20px 50px -18px rgba(42,31,27,.40);
  --maxw:1060px;
}
html[data-theme="dark"]{
  --bg:#1C1310; --bg2:#241914; --card:#2A1F1B; --ink:#F5EDE6; --sub:#C9B6AB;
  --copper:#A9887A; --copper-deep:#C4A294; --line:rgba(245,237,230,.14);
  --band:#14100E; --band-ink:#F5EDE6; --band-sub:#B8A296; --band-accent:#BC9A8A;
  --shadow:0 24px 60px -20px rgba(0,0,0,.7);
  --shadow-sm:0 20px 50px -18px rgba(0,0,0,.65);
  color-scheme:dark;
}
html{scroll-behavior:smooth;-webkit-text-size-adjust:100%}
body{
  margin:0;background:var(--bg);color:var(--ink);
  font-family:-apple-system,BlinkMacSystemFont,"SF Pro Text","Segoe UI",Roboto,Helvetica,Arial,sans-serif;
  font-size:17px;line-height:1.55;-webkit-font-smoothing:antialiased;
}
img{max-width:100%;height:auto;display:block}
picture{display:contents}
a{color:var(--copper-deep)}
a:hover{color:var(--ink)}
a:focus-visible,button:focus-visible,summary:focus-visible{
  outline:3px solid var(--copper);outline-offset:3px;border-radius:6px}
h1,h2,h3{text-wrap:balance}
p,li{text-wrap:pretty}

.skip{position:absolute;left:-9999px;top:0;z-index:100;background:var(--card);
  color:var(--ink);padding:12px 18px;border-radius:0 0 10px 0;font-weight:600}
.skip:focus{left:0}

.wrap{max-width:var(--maxw);margin:0 auto;padding-left:24px;padding-right:24px}

header{position:sticky;top:0;z-index:50;display:flex;align-items:center;gap:12px;
  padding:10px 20px;background:color-mix(in srgb,var(--bg) 86%,transparent);
  backdrop-filter:blur(14px);-webkit-backdrop-filter:blur(14px);
  border-bottom:1px solid var(--line)}
@supports not (backdrop-filter:blur(1px)){header{background:var(--bg)}}
header .name{font-size:18px;letter-spacing:-.2px;font-weight:700}
header .spacer{flex:1}
.langsw{display:flex;gap:2px;background:var(--bg2);border:1px solid var(--line);
  border-radius:999px;padding:3px}
.langsw a{border-radius:999px;padding:6px 14px;font-size:14px;font-weight:700;
  text-decoration:none;color:var(--sub);line-height:1.2}
.langsw a[aria-current="true"]{background:var(--copper);color:#FFF}
.themebtn{display:flex;align-items:center;justify-content:center;width:38px;height:38px;
  border-radius:999px;border:1px solid var(--line);background:var(--bg2);
  color:var(--ink);cursor:pointer;padding:0}
.themebtn:hover{border-color:var(--copper)}
html[data-theme="dark"] .i-sun{display:block}
html[data-theme="dark"] .i-moon{display:none}
.i-sun{display:none}

.hero{display:flex;flex-wrap:wrap;align-items:center;gap:40px;padding-top:56px;padding-bottom:64px}
.hero .col{flex:1 1 340px;min-width:0}
.hero .shotcol{flex:0 1 300px;margin:0 auto}
.kicker-pill{margin:0 0 14px;display:inline-block;font-size:14px;font-weight:600;
  letter-spacing:.4px;color:var(--copper-deep);border:1px solid var(--line);
  border-radius:999px;padding:5px 12px;background:var(--card)}
h1{margin:0 0 16px;font-size:clamp(38px,6vw,58px);line-height:1.05;
  letter-spacing:-1.5px;font-weight:800}
.hero-sub{margin:0 0 26px;font-size:20px;color:var(--sub);max-width:34ch}
.shot{width:100%;max-width:320px;border-radius:32px;box-shadow:var(--shadow)}

.cta-row{display:flex;flex-wrap:wrap;align-items:center;gap:14px}
.soon-chip{display:inline-flex;align-items:center;gap:8px;background:var(--ink);
  color:var(--bg);border-radius:12px;padding:12px 20px;font-size:16px;font-weight:600}
.soon-dot{width:8px;height:8px;border-radius:99px;background:var(--copper);display:inline-block}
.soon-note{margin:12px 0 0;font-size:14px;color:var(--sub)}
.badge{display:inline-flex;align-items:center;gap:11px;background:#000;color:#FFF;
  border:1px solid rgba(255,255,255,.35);border-radius:11px;padding:9px 18px 9px 14px;
  text-decoration:none}
.badge:hover{color:#FFF}
.badge .b1{font-size:11px;letter-spacing:.2px}
.badge .b2{font-size:20px;font-weight:600;letter-spacing:-.3px;margin-top:1px}
.badge .lines{display:flex;flex-direction:column;line-height:1.15;text-align:left}
.badge-off{opacity:.38;filter:grayscale(1);pointer-events:none}
html:not([data-launch="store"]) .when-store{display:none}
html[data-launch="store"] .when-soon{display:none}

.band-soft{background:var(--bg2);border-top:1px solid var(--line);border-bottom:1px solid var(--line)}
.steps{display:flex;flex-wrap:wrap;align-items:center;gap:48px;padding-top:64px;padding-bottom:64px}
.steps .col{flex:1 1 380px;min-width:0}
.eyebrow{margin:0 0 8px;font-size:14px;font-weight:700;letter-spacing:1.2px;
  text-transform:uppercase;color:var(--copper-deep)}
h2{margin:0 0 28px;font-size:clamp(28px,4vw,40px);letter-spacing:-.8px;line-height:1.1}
ol.steplist{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:22px}
ol.steplist li{display:flex;gap:16px;align-items:flex-start}
.stepnum{flex:none;width:38px;height:38px;border-radius:999px;background:var(--copper);
  color:#FFF;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:17px}
.stepnum+div strong{font-size:19px;display:block;margin-bottom:2px}
.stepnum+div span{color:var(--sub)}
figure.quote{margin:28px 0 0;padding:18px 22px;background:var(--card);
  border-left:4px solid var(--copper);border-radius:0 14px 14px 0;
  box-shadow:0 8px 24px -14px rgba(42,31,27,.3)}
figure.quote blockquote{margin:0;font-size:19px;font-weight:600;letter-spacing:-.2px}
figure.quote figcaption{margin-top:6px;font-size:14px;color:var(--sub)}

.features{padding-top:72px;padding-bottom:8px}
.features>h2{margin-bottom:8px;text-align:center}
.feat-sub{margin:0 auto 24px;color:var(--sub);text-align:center;max-width:52ch}
.feat{display:flex;flex-wrap:wrap;align-items:center;gap:40px;padding:40px 0;
  border-top:1px solid var(--line)}
@media (min-width:820px){.feat.alt{flex-direction:row-reverse}}
.feat .col{flex:1 1 360px;min-width:0}
.feat .shotcol{flex:0 1 270px;margin:0 auto}
.feat h3{margin:0 0 8px;font-size:26px;letter-spacing:-.5px}
.feat p{margin:0 0 18px;color:var(--sub);max-width:48ch}
.feat .shot{max-width:290px;border-radius:28px;box-shadow:var(--shadow-sm)}
ul.ticks{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:10px}
ul.ticks li{display:flex;gap:10px;align-items:flex-start}
ul.ticks svg{flex:none;margin-top:4px}

.share{display:flex;flex-wrap:wrap;gap:28px;align-items:center;margin:0 0 64px;
  padding:34px;background:var(--bg2);border:1px solid var(--line);border-radius:22px}
.share .col{flex:1 1 320px}
.share h3{margin:0 0 8px;font-size:26px;letter-spacing:-.5px}
.share p{margin:0;color:var(--sub);max-width:52ch}
.share ul{flex:1 1 280px}

.privacy{background:var(--band);color:var(--band-ink);padding-top:72px;padding-bottom:72px}
.privacy .eyebrow{color:var(--band-accent)}
.privacy h2{margin-bottom:12px}
.privacy .lead{margin:0 0 32px;color:var(--band-sub);max-width:56ch}
.privgrid{display:grid;grid-template-columns:repeat(auto-fit,minmax(210px,1fr));gap:14px}
.privgrid>div{background:rgba(245,237,230,.06);border:1px solid rgba(245,237,230,.14);
  border-radius:16px;padding:20px}
.privgrid strong{display:block;margin-bottom:4px;font-size:18px}
.privgrid span{color:var(--band-sub);font-size:15px}
.priv-site{margin:26px 0 0;font-size:15px;color:var(--band-sub)}

.roasters{padding-top:72px;padding-bottom:72px}
.roasters .row{display:flex;flex-wrap:wrap;gap:40px}
.roasters .lead-col{flex:1 1 300px}
.roasters .lead-col h2{margin:0;font-size:clamp(26px,3.5vw,36px);letter-spacing:-.7px;
  line-height:1.15;max-width:16ch}
.roasters .body-col{flex:1.4 1 380px;min-width:0}
.roasters .body-col p:first-of-type{margin:0 0 16px}
.roasters .body-col p+p{margin:0 0 22px;color:var(--sub)}
.mailbtn{display:inline-block;background:var(--copper);color:#FFF;text-decoration:none;
  font-weight:600;border-radius:12px;padding:12px 22px}
.mailbtn:hover{background:var(--copper-deep);color:#FFF}

.faq{background:var(--bg2);border-top:1px solid var(--line);padding-top:72px;padding-bottom:72px}
.faq .wrap{max-width:760px}
.faq h2{text-align:center}
.faqlist{display:flex;flex-direction:column;gap:12px}
details{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:0 20px}
summary{cursor:pointer;list-style:none;display:flex;justify-content:space-between;
  align-items:center;gap:12px;padding:16px 0;font-weight:600;font-size:17px}
summary::-webkit-details-marker{display:none}
summary .plus{color:var(--copper);font-size:22px;line-height:1;flex:none;
  transition:transform .18s ease}
details[open] summary .plus{transform:rotate(45deg)}
details>p{margin:0;padding:0 0 18px;color:var(--sub)}

footer{background:var(--band);color:var(--band-sub)}
footer a{color:var(--band-sub);text-decoration:none}
footer a:hover{color:var(--band-ink);text-decoration:underline}
.foot-top{display:flex;flex-wrap:wrap;gap:28px;align-items:flex-start;
  padding-top:44px;padding-bottom:0}
.foot-brand{flex:1 1 260px;display:flex;gap:12px;align-items:center}
.foot-brand strong{color:var(--band-ink);display:block}
.foot-brand span{font-size:14px}
.foot-nav{flex:1 1 180px;display:flex;flex-direction:column;gap:8px;font-size:15px}
.foot-mail{flex:1 1 220px;display:flex;flex-direction:column;gap:8px;font-size:15px}
.foot-bottom{padding-top:26px;padding-bottom:30px;font-size:13px;display:flex;
  flex-wrap:wrap;gap:10px;justify-content:space-between}

html[data-theme="dark"] .only-light{display:none}
html:not([data-theme="dark"]) .only-dark{display:none}

@media (prefers-reduced-motion:reduce){
  html{scroll-behavior:auto}
  *{transition:none!important;animation:none!important}
}
@media (max-width:560px){
  body{font-size:16px}
  .hero{padding-top:40px;padding-bottom:48px}
  .hero-sub{font-size:18px}
  header{padding:8px 14px;gap:8px}
  header .name{font-size:16px}
  .langsw a{padding:6px 11px}
  .share{padding:24px}
}
"""

JS = """
(function(){
  var d=document.documentElement, K='bp-theme';
  function set(t){d.setAttribute('data-theme',t);
    try{localStorage.setItem(K,t)}catch(e){}}
  var b=document.getElementById('theme-toggle');
  if(b)b.addEventListener('click',function(){
    set(d.getAttribute('data-theme')==='dark'?'light':'dark');
  });
})();
"""

# Setzt das Theme vor dem ersten Paint — verhindert Aufblitzen.
JS_HEAD = """
(function(){try{var t=localStorage.getItem('bp-theme');
if(!t)t=matchMedia('(prefers-color-scheme:dark)').matches?'dark':'light';
document.documentElement.setAttribute('data-theme',t);}catch(e){}})();
"""

TICK = ('<svg aria-hidden="true" width="18" height="18" viewBox="0 0 24 24" fill="none" '
        'stroke="var(--copper)" stroke-width="3" stroke-linecap="round" '
        'stroke-linejoin="round"><path d="M4 12.5l5 5L20 6.5"/></svg>')

APPLE_GLYPH = ('<svg width="26" height="30" viewBox="0 0 22 26" fill="#FFF" aria-hidden="true">'
               '<path d="M18.4 13.8c0-3 2.5-4.5 2.6-4.6-1.4-2.1-3.6-2.4-4.4-2.4-1.9-.2-3.6 1.1-4.6 '
               '1.1-1 0-2.4-1.1-4-1.1-2 0-3.9 1.2-5 3-2.1 3.7-.5 9.2 1.5 12.2 1 1.5 2.2 3.1 3.8 3 '
               '1.5-.1 2.1-1 4-1s2.4 1 4 1c1.7 0 2.7-1.5 3.7-3 1.2-1.7 1.7-3.4 1.7-3.5-.1 0-3.3-1.3'
               '-3.3-4.7zM15.3 4.8c.8-1 1.4-2.4 1.2-3.8-1.2.1-2.7.8-3.5 1.8-.8.9-1.5 2.3-1.3 3.7 '
               '1.4.1 2.7-.7 3.6-1.7z"/></svg>')


def shot(base, alt, cls="shot", sizes="320px", lazy=True, dark_variant=None):
    """<picture> mit WebP und PNG-Fallback."""
    lz = ' loading="lazy" decoding="async"' if lazy else ' fetchpriority="high" decoding="async"'
    def one(b, extra=""):
        return (f'<picture{extra}>'
                f'<source srcset="{A}{b}.webp" type="image/webp">'
                f'<img src="{A}{b}.png" alt="{e(alt)}" width="640" height="1380" '
                f'class="{cls}" sizes="{sizes}"{lz}></picture>')
    if dark_variant:
        return one(base, ' class="only-light"') + one(dark_variant, ' class="only-dark"')
    return one(base)


def build(lang):
    t = STR[lang]
    global A
    A = "assets/" if lang == "de" else "../assets/"
    other = STR[t["other"]]
    canonical = BASE_URL + t["self_href"]

    # ---- CTA-Block (soon / store) ----
    badge_inner = (f'{APPLE_GLYPH}<span class="lines"><span class="b1">{e(t["badge1"])}</span>'
                   f'<span class="b2">{e(t["badge2"])}</span></span>')
    cta = f'''
      <div class="when-soon">
        <div class="cta-row">
          <span class="soon-chip"><span class="soon-dot"></span>{e(t["hero_soon"])}</span>
          <span class="badge badge-off" aria-hidden="true">{badge_inner}</span>
        </div>
        <p class="soon-note">{e(t["hero_soon_note"])}</p>
      </div>
      <div class="when-store">
        <a class="badge" href="{e(APP_STORE_URL)}" aria-label="{e(t["badge_aria"])}">{badge_inner}</a>
      </div>'''

    # ---- Schritte ----
    steps = "".join(
        f'<li><span class="stepnum" aria-hidden="true">{n}</span>'
        f'<div><strong>{e(ti)}</strong><span>{e(d)}</span></div></li>'
        for n, ti, d in t["steps"])

    # ---- Features ----
    feats = []
    for i, f in enumerate(t["features"]):
        pts = "".join(f'<li>{TICK}<span>{p}</span></li>' for p in f["points"])
        dark = "shot-dashboard-dark" if f["key"] == "dash" else None
        img = shot(f["img"], f["alt"], cls="shot", sizes="290px", dark_variant=dark)
        feats.append(f'''
      <article class="feat{' alt' if i % 2 else ''}">
        <div class="col">
          <h3>{f["title"]}</h3>
          <p>{e(f["desc"])}</p>
          <ul class="ticks">{pts}</ul>
        </div>
        <div class="shotcol">{img}</div>
      </article>''')

    share_pts = "".join(f'<li>{TICK}<span>{e(p)}</span></li>' for p in t["share_points"])
    priv = "".join(f'<div><strong>{e(a)}</strong><span>{e(b)}</span></div>'
                   for a, b in t["priv_points"])
    faq = "".join(
        f'<details><summary>{e(q)}<span class="plus" aria-hidden="true">+</span></summary>'
        f'<p>{e(a)}</p></details>' for q, a in t["faq"])

    # ---- Strukturierte Daten ----
    ld = f'''{{
  "@context":"https://schema.org","@type":"SoftwareApplication",
  "name":"BrewPilot","applicationCategory":"LifestyleApplication",
  "operatingSystem":"iOS 26","inLanguage":["de-CH","en"],
  "description":{t["meta_desc"]!r},
  "url":"{canonical}","image":"{BASE_URL}/assets/og-{lang}.png",
  "offers":{{"@type":"Offer","price":"0","priceCurrency":"CHF"}},
  "author":{{"@type":"Organization","name":"BrewPilot","url":"{BASE_URL}",
    "email":"info@brew-pilot.com"}}
}}'''.replace("'", '"')

    faq_ld_items = ",".join(
        '{"@type":"Question","name":%s,"acceptedAnswer":{"@type":"Answer","text":%s}}'
        % (repr(q).replace("'", '"'), repr(a).replace("'", '"'))
        for q, a in t["faq"])
    faq_ld = ('{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[%s]}'
              % faq_ld_items)

    banner = (f'\n  <meta name="apple-itunes-app" content="app-id={APP_ID}">'
              if APP_ID else
              '\n  <!-- Nach der Freigabe eintragen (Smart App Banner):\n'
              '       <meta name="apple-itunes-app" content="app-id=1234567890"> -->')

    return f'''<!DOCTYPE html>
<html lang="{t["htmllang"]}" data-theme="light" data-launch="{LAUNCH}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(t["title"])}</title>
<meta name="description" content="{e(t["meta_desc"])}">
<link rel="canonical" href="{canonical}">
<link rel="alternate" hreflang="de-CH" href="{BASE_URL}/">
<link rel="alternate" hreflang="en" href="{BASE_URL}/en/">
<link rel="alternate" hreflang="x-default" href="{BASE_URL}/">
<meta name="theme-color" content="#F5EDE6" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#1C1310" media="(prefers-color-scheme: dark)">
<meta name="color-scheme" content="light dark">{banner}

<meta property="og:type" content="website">
<meta property="og:site_name" content="BrewPilot">
<meta property="og:locale" content="{t["locale"]}">
<meta property="og:title" content="{e(t["title"])}">
<meta property="og:description" content="{e(t["meta_desc"])}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{BASE_URL}/assets/og-{lang}.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{e(t["hero_h1"])} — BrewPilot">
<meta name="twitter:card" content="summary_large_image">

<link rel="icon" href="{A}favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="{A}favicon-32.png">
<link rel="apple-touch-icon" href="{A}apple-touch-icon.png">

<link rel="preload" as="image" href="{A}shot-coach.webp" type="image/webp" fetchpriority="high">
<script>{JS_HEAD.strip()}</script>
<style>{CSS.strip()}</style>
<script type="application/ld+json">{ld}</script>
<script type="application/ld+json">{faq_ld}</script>
</head>
<body>
<a class="skip" href="#main">{e(t["skip"])}</a>

<header>
  <img src="{A}icon-96.png" alt="" width="34" height="34" style="border-radius:8px">
  <span class="name">BrewPilot</span>
  <span class="spacer"></span>
  <nav class="langsw" aria-label="{e(t["lang_group"])}">
    <a href="{t["self_href"]}" aria-current="true" lang="{t["htmllang"]}">{"DE" if lang=="de" else "EN"}</a>
    <a href="{t["other_href"]}" lang="{other["htmllang"]}" hreflang="{other["htmllang"]}">{"EN" if lang=="de" else "DE"}</a>
  </nav>
  <button class="themebtn" id="theme-toggle" type="button" aria-label="{e(t["theme_label"])}">
    <svg class="i-sun" width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="4.5"/><path d="M12 2v3M12 19v3M2 12h3M19 12h3M4.5 4.5l2 2M17.5 17.5l2 2M19.5 4.5l-2 2M6.5 17.5l-2 2"/></svg>
    <svg class="i-moon" width="17" height="17" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M20.4 14.2A8.5 8.5 0 0 1 9.8 3.6 8.5 8.5 0 1 0 20.4 14.2z"/></svg>
  </button>
</header>

<main id="main">

  <section class="wrap hero" aria-labelledby="hero-h">
    <div class="col">
      <p class="kicker-pill">{e(t["hero_kicker"])}</p>
      <h1 id="hero-h">{e(t["hero_h1"])}</h1>
      <p class="hero-sub">{e(t["hero_sub"])}</p>
      {cta}
    </div>
    <div class="shotcol">{shot("shot-coach", t["hero_alt"], lazy=False, dark_variant="shot-coach-dark")}</div>
  </section>

  <section class="band-soft" aria-labelledby="steps-h">
    <div class="wrap steps">
      <div class="col">
        <p class="eyebrow">{e(t["steps_kicker"])}</p>
        <h2 id="steps-h">{e(t["steps_h2"])}</h2>
        <ol class="steplist">{steps}</ol>
        <figure class="quote">
          <blockquote>{e(t["steps_quote"])}</blockquote>
          <figcaption>{e(t["steps_quote_cap"])}</figcaption>
        </figure>
      </div>
      <div class="shotcol">{shot("shot-empfehlung", t["steps_alt"])}</div>
    </div>
  </section>

  <section class="wrap features" aria-labelledby="feat-h">
    <h2 id="feat-h">{e(t["feat_h2"])}</h2>
    <p class="feat-sub">{e(t["feat_sub"])}</p>
    {"".join(feats)}
    <article class="share">
      <div class="col">
        <h3>{e(t["share_h3"])}</h3>
        <p>{e(t["share_p"])}</p>
      </div>
      <ul class="ticks">{share_pts}</ul>
    </article>
  </section>

  <section class="privacy" aria-labelledby="priv-h">
    <div class="wrap">
      <p class="eyebrow">{e(t["priv_kicker"])}</p>
      <h2 id="priv-h">{e(t["priv_h2"])}</h2>
      <p class="lead">{e(t["priv_sub"])}</p>
      <div class="privgrid">{priv}</div>
      <p class="priv-site">{e(t["priv_site"])}</p>
    </div>
  </section>

  <section class="wrap roasters" aria-labelledby="roast-h">
    <div class="row">
      <div class="lead-col">
        <p class="eyebrow">{e(t["roast_kicker"])}</p>
        <h2 id="roast-h">{e(t["roast_h2"])}</h2>
      </div>
      <div class="body-col">
        <p>{e(t["roast_p1"])}</p>
        <p>{e(t["roast_p2"])}</p>
        <a class="mailbtn" href="mailto:info@brew-pilot.com">info@brew-pilot.com</a>
      </div>
    </div>
  </section>

  <section class="faq" aria-labelledby="faq-h">
    <div class="wrap">
      <h2 id="faq-h">{e(t["faq_h2"])}</h2>
      <div class="faqlist">{faq}</div>
    </div>
  </section>

</main>

<footer>
  <div class="wrap foot-top">
    <div class="foot-brand">
      <img src="{A}icon-96.png" alt="" width="40" height="40" style="border-radius:10px">
      <div><strong>BrewPilot</strong><span>{e(t["foot_tag"])}</span></div>
    </div>
    <nav class="foot-nav" aria-label="Footer">
      <a href="/support/">{e(t["foot_support"])}</a>
      <a href="/privacy/">{e(t["foot_privacy"])}</a>
      <!-- Impressum: in DE/AT gesetzlich verpflichtend, Seite anlegen und Zeile aktivieren
      <a href="/impressum/">{e(t["foot_imprint"])}</a> -->
    </nav>
    <div class="foot-mail">
      <a href="mailto:support@brew-pilot.com">support@brew-pilot.com</a>
      <a href="mailto:info@brew-pilot.com">info@brew-pilot.com</a>
    </div>
  </div>
  <div class="wrap foot-bottom">
    <span>© 2026 BrewPilot</span>
    <span>{e(t["foot_note"])}</span>
  </div>
</footer>
<script>{JS.strip()}</script>
</body>
</html>
'''


os.makedirs(f"{SITE}/en", exist_ok=True)
open(f"{SITE}/index.html", "w", encoding="utf-8").write(build("de"))
open(f"{SITE}/en/index.html", "w", encoding="utf-8").write(build("en"))

open(f"{SITE}/robots.txt", "w").write(
    f"User-agent: *\nAllow: /\n\nSitemap: {BASE_URL}/sitemap.xml\n")

open(f"{SITE}/sitemap.xml", "w", encoding="utf-8").write(
    '<?xml version="1.0" encoding="UTF-8"?>\n'
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
    'xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
    + "".join(
        f'  <url>\n    <loc>{BASE_URL}{p}</loc>\n'
        f'    <xhtml:link rel="alternate" hreflang="de-CH" href="{BASE_URL}/"/>\n'
        f'    <xhtml:link rel="alternate" hreflang="en" href="{BASE_URL}/en/"/>\n'
        f'    <xhtml:link rel="alternate" hreflang="x-default" href="{BASE_URL}/"/>\n'
        f'  </url>\n' for p in ("/", "/en/"))
    + "</urlset>\n")

for f in ("index.html", "en/index.html"):
    print(f"{f:18s} {os.path.getsize(f'{SITE}/{f}')/1024:6.1f} KB")
print("ok")
