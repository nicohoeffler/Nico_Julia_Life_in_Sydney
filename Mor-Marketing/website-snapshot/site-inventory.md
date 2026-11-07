# mor-marketing.com – Seiten-Inventar (Stand 7.11.2026)

Bauplan für den Nachbau: Struktur, Überschriften, Buttons, Links und alle Medien-URLs. Fließtexte sind hier nur sinngemäß zusammengefasst. Den Originaltext, die Bilder und Videos holt `scrape.sh` (siehe README).

**Technik:** Next.js auf Vercel. 16 Seiten, alle erreichbar (HTTP 200).

## Seitenstruktur

```
/                         Startseite (Hero-Video, Case Studies, Expertise)
/contact                  Kontaktformular
/legal-notice             Impressum
/privacy-policy           Datenschutz
/services/
  content-creation
  social-media-campaigns
  event-launch-coverage
  hospitality-venue-content
  fashion-campaign-shoots
  editing-post-production
/work/
  badlambs  mix-deli  poke-mix  554  pirlos-pizza  riada-concept
```

## Auf jeder Seite gleich

- **Navigation:** Work (/#work) · About (/#about) · Services (/#services) · Contact (/contact). Logo `/logo_transparent.png`
- **Footer-Block:** H2 „Work with Me.“, „Let's bring your brand to life through content.“, „Ready to collaborate?“, Button „Start a Project“ → /contact, „or email“ info@mor-marketing.com
- **Social:** Instagram @j.ulz.i.e (Julia Mor), @_mormarketing (Portfolio)
- **Footer:** Legal Notice, Privacy Policy, „© 2026 MOR MARKETING. Based in Sydney, AUS.“, „MADE WITH ❤ BY HWM AGENTUR“
- **SEO-Fehler:** Alle Seiten außer den beiden Rechtsseiten haben denselben Titel („Mor Marketing | Social Media Marketing & Creative Direction“) und dieselbe Description. og:url bzw. canonical zeigt auf `https://mormarketing.com`.
- Service- und Work-Seiten haben eine Breadcrumb: Home / Bereich / Seitenname.

## Startseite `/`

- Hero-Video `/hero-video.mp4`
- H1 „Social Media Content & Brand Direction“, Untertitel „Visual content created to reflect the character and quality of your brand.“
- Intro: Sie arbeitet in Sydney für Hospitality-, Fashion- und Lifestyle-Marken und übernimmt alles vom Shoot bis zum fertigen Schnitt. Link „Explore daily insights on Instagram“.
- H2 „Selected Case Studies“ (horizontal scrollbar), 6 Karten:

| Titel | Tags | Link |
|---|---|---|
| BADLAMBS (Hero Campaign Video) | Event Coverage, Brand Visuals, Hero Campaign Video | /work/badlambs |
| MIX DELI | Food Videography, Menu Content, Social Campaign Assets | /work/mix-deli |
| POKÉ MIX | Social Media Content, Reels, In-Venue Photography | /work/poke-mix |
| 554 | Venue Content, Cocktail Videography, Nightlife Campaign Visuals | /work/554 |
| PIRLOS PIZZA x MIX DELI (Pop-up Collaboration) | Event Coverage, Atmosphere Content, Social Media Assets | /work/pirlos-pizza |
| RIADA CONCEPT | Fashion Content, Visual Identity, Social & Digital Platforms | /work/riada-concept |

- H2 „Expertise“, 6 Service-Karten:

| # | Service | Medium | Bildunterschrift |
|---|---|---|---|
| 01 | Content Creation (Photo & Video) | /poke_mix.mp4 | Poké Mix |
| 02 | Social Media Campaigns | /MIXDELI_PIRLOSPIZZA.jpg | Mix Deli × Pirlos Pizza |
| 03 | Event & Launch Coverage | /BADLAMBS(4).jpg | Badlambs |
| 04 | Hospitality & Venue Content | /554.mov | 554 |
| 05 | Fashion Campaign Shoots | /RIADA CONCEPT.mp4 | Riada Concept |
| 06 | Editing & Post-Production | /MIX DELI.mp4 | Mix Deli |

## Kontakt `/contact`

- H1 „Let’s create something.“
- Formularfelder: Name*, Email*, Company / Brand, Estimated Budget, „What are you looking for?“ (Social Media Management, Creative Direction, Content Creation, Consulting, Other), „Tell me about your project*“. Button „Send Message“
- **Für Analytics wichtig:** Das Absenden des Formulars ist das wichtigste Lead-Ereignis und sollte als Event gezählt werden.

## Service-Seiten `/services/*`

Jede Seite hat eine H1, einen kurzen Text, einen CTA-Button zu /contact und 3 Karten zu passenden Case Studies („View case study →“).

| Seite | CTA | Verlinkte Case Studies |
|---|---|---|
| content-creation | Start your project | poke-mix, mix-deli, riada-concept |
| social-media-campaigns | Start your campaign | pirlos-pizza, mix-deli, poke-mix |
| event-launch-coverage | Plan your coverage | badlambs, pirlos-pizza, 554 |
| hospitality-venue-content | Start your project | 554, badlambs, mix-deli |
| fashion-campaign-shoots | Start your campaign | riada-concept, pirlos-pizza, poke-mix |
| editing-post-production | Plan your post-production | mix-deli, badlambs, poke-mix |

## Case Studies `/work/*`

| Seite | Inhalt | Videos | Bilder |
|---|---|---|---|
| badlambs | Event-Fotos und -Videos | badlamps.mp4 (Dateiname mit Tippfehler) | BADLAMBS.jpg/.png, BADLAMBS(1–4).jpg, BADLAMBS(1–2).png |
| mix-deli | Pop-ups mit KEF und Pirlos Pizza | MIX DELI.mp4, MIXDELI_KEF.mov | Updated image for Mix Deli slide.jpg, MIXDELI_PIRLOSPIZZA(.jpg/(1).jpg), MIX DELI.jpg, MIXDELI(.jpg/(1)/(2)) |
| poke-mix | Food-Visuals für Social Media | poke_mix.mp4, POKEMIX.mov, POKEMIX(1).mov | – |
| 554 | Interview mit Head Chef Anton | 554.mov, 554.mp4, 554(1).mp4, 554(2).mp4 | – |
| pirlos-pizza | Pop-up Mix Deli × Pirlos Pizza | PIRLOS&MIXDELI.mov | MIXDELI_PIRLOSPIZZA.jpg, (1).jpg |
| riada-concept | Fashion-Content | RIADA CONCEPT.mp4, (1).mp4, (2).mp4 | – |

## Rechtsseiten

- **Impressum:** Julia Josephine Mor, Solo Trader, ABN 66701137801, 19/78 Curlewis Street, Bondi Beach NSW 2026, info@mor-marketing.com, +61493567242, Hosting bei Vercel Inc., Stand 25.3.2026. Enthält außerdem einen Credit-Block für HWM.
- **Datenschutz:** Hosting bei Vercel, Server-Logs (30 Tage), Kontaktanfragen, nur notwendige Cookies, Datentransfer in die USA, Betroffenenrechte. Beim Umzug muss der Abschnitt zum Hosting angepasst werden, und Cloudflare Web Analytics muss ergänzt werden (cookielos, trotzdem erwähnen).

## Was beim Nachbau verbessert werden sollte

1. Jede Seite bekommt einen eigenen Titel und eine eigene Description, und canonical zeigt auf `https://www.mor-marketing.com`.
2. Cloudflare Web Analytics einbauen, dazu Events für Formular-Absendung, Klick auf die E-Mail und Instagram-Klicks.
3. Die .mov-Videos in MP4/WebM umwandeln. .mov läuft nicht in allen Browsern (Chrome/Android teilweise nicht), außerdem sind die Dateien kleiner.
4. Bilder mit sprechenden Dateinamen ablegen, zum Beispiel `badlambs-event-sydney-1.jpg` statt `BADLAMBS(1).jpg`.
5. Ohne Hosting bei HWM fallen der HWM-Credit und der Designer-Block im Impressum weg.
