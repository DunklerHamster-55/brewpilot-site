# BrewPilot Landing Page — Einbau

Statische Seite, kein Build-Schritt, keine Abhängigkeiten. Läuft auf GitHub Pages so wie sie ist.

## Inhalt

```
index.html            Deutsch (de-CH)
en/index.html         Englisch
assets/               Screenshots (WebP + PNG-Fallback), Icons, Open-Graph-Bilder
robots.txt
sitemap.xml
build_site.py         Generator — erzeugt beide HTML-Dateien aus einer Textquelle
```

`build_site.py` ist optional. Für einzelne Textänderungen kannst du die HTML-Dateien direkt bearbeiten. Für alles, was in **beiden** Sprachen gleich aussehen soll — Struktur, CSS, neue Abschnitte — ist der Generator der sichere Weg, weil DE und EN sonst auseinanderlaufen.

## Einbau

1. `index.html`, `en/`, `assets/`, `robots.txt`, `sitemap.xml` ins Repo-Root kopieren.
2. **`/support/` und `/privacy/` nicht überschreiben** — die Seite verlinkt darauf und sie sind live.
3. Eine vorhandene `CNAME` bleibt unberührt.
4. Commit, push, fertig.

## Nach der App-Store-Freigabe

Drei Werte oben in `build_site.py`, dann `python3 build_site.py`:

```python
LAUNCH = "store"                                       # statt "soon"
APP_STORE_URL = "https://apps.apple.com/app/id……"      # echte URL
APP_ID = "……"                                          # nur die Ziffern
```

Damit passiert dreierlei: aus „Bald verfügbar" wird der verlinkte Badge, der graue Badge wird aktiv, und der Smart App Banner erscheint auf iPhones, die die Seite besuchen.

Ohne Generator geht es auch von Hand: in beiden HTML-Dateien `data-launch="soon"` auf `"store"` setzen, die `href` im `.badge`-Link eintragen und die auskommentierte `apple-itunes-app`-Zeile aktivieren.

## Was noch offen ist

**App-Store-Badge ersetzen — vor dem Livegang.**
Der Badge in `index.html` ist nachgezeichnet, inklusive Apple-Logo. Apples Marketing-Richtlinien verlangen das unveränderte Original-Artwork; ein selbst gezeichnetes Apple-Logo ist markenrechtlich angreifbar. Das offizielle SVG gibt es unter *Apple Identity Guidelines / Marketing Resources*. Die Klasse `.badge` im CSS kann danach entfallen.

**Impressum anlegen.**
Für DE und AT ist ein Impressum auf einer geschäftsmässigen Website vorgeschrieben, in der Schweiz greift UWG Art. 3 Abs. 1 lit. s. Die Footer-Zeile ist in beiden HTML-Dateien schon vorhanden, nur auskommentiert — sie zeigt auf `/impressum/`. Welche Angaben konkret nötig sind, hängt von deiner Rechtsform ab; im Zweifel kurz abklären lassen.

## Technische Entscheidungen

**Zwei Seiten statt Sprachumschalter.**
Der Design-Entwurf schaltet DE/EN per JavaScript um. Für einen Prototyp richtig, für die Live-Seite nicht: Suchmaschinen sehen dann nur eine Sprache, und in App Store Connect lässt sich keine eigene englische Marketing-URL hinterlegen. Jetzt sind es zwei echte Seiten mit `hreflang`, eigenen Titeln, Beschreibungen und Open-Graph-Bildern. Die Umschaltung ist ein normaler Link und funktioniert ohne JavaScript.

**Dark Mode.**
Voreinstellung folgt dem System, die manuelle Wahl bleibt in `localStorage`. Das Theme wird vor dem ersten Rendern gesetzt, damit beim Laden nichts aufblitzt. Hero und Dashboard zeigen im dunklen Modus dunkle App-Screenshots.

**Bilder.**
WebP als Primärformat mit PNG-Fallback über `<picture>`, feste `width`/`height` gegen Layout-Sprünge, alles ausser dem Hero lazy. Gesamtgewicht rund 300 KB statt 1,6 MB.

**Zugänglichkeit.**
Sprungmarke zum Inhalt, sichtbarer Fokusrahmen, korrekte Überschriftenhierarchie (eine H1 je Seite), beschreibende Alt-Texte, `prefers-reduced-motion` respektiert. Alle Farbpaare erreichen mindestens WCAG AA.

**Datenschutz.**
Keine externen Ressourcen, keine Schriften von fremden Servern, keine Cookies, kein Tracking. Die Seite lädt ausschliesslich aus der eigenen Domain — passend zum Versprechen im Privacy-Abschnitt.
