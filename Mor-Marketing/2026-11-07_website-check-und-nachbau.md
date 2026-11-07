# mor-marketing.com – Check & Plan zum Selbst-Hosten (Stand 7.11.2026)

## 1. Was die Website heute ist

- **Domain:** https://mor-marketing.com (mit Bindestrich). Gebaut von HWM Agentur (Sven Heynhold), Footer: "Made with ❤ by HWM Agentur".
- **Technik:** Next.js-Seite, gehostet auf **Vercel** (steht so im Impressum/Datenschutz). Also kein eigener Server bei HWM – die 8 €/Monat bezahlen faktisch Domain, E-Mail-Postfach (info@mor-marketing.com) und Wartung.
- **Inhalt:** Startseite mit Leistungen (Content Creation, Social Media Campaigns, Event & Launch Coverage, Hospitality & Venue Content, Fashion Campaign Shoots, Editing & Post-Production), 6 Case Studies (Badlambs, Mix Deli, Poké Mix, 554, Pirlos Pizza, Riada Concept), Kontaktformular (Name, E-Mail, Firma, Budget, Bedarf, Nachricht), Instagram-Links (@_mormarketing, @j.ulz.i.e), Impressum, Datenschutz.
- **Analytics:** Kein Hinweis auf Google Analytics, Plausible, Meta Pixel o. Ä. Die Datenschutzerklärung erwähnt nur "technisch notwendige Cookies". Einschätzung: **~85 %, dass es aktuell null Tracking gibt.** (Roh-HTML konnte ich nicht prüfen, nur gerenderten Inhalt.)

## 2. Gefundene Probleme

| # | Problem | Wirkung | Fix |
|---|---|---|---|
| 1 | **Canonical-Tag und og:url zeigen auf `mormarketing.com` (ohne Bindestrich)** – das ist eine geparkte GoDaddy-"Domain zu verkaufen"-Seite | Google kann die echte Seite als Duplikat werten, Link-Vorschauen (WhatsApp, LinkedIn) zeigen evtl. falsche URL. **Größter SEO-Fehler.** | 1 Zeile Code, Sven kann das sofort ändern |
| 2 | Alle Unterseiten haben denselben Title/Meta-Description | Google zeigt für Service-Seiten keine passenden Snippets | Pro Seite eigener Title/Description |
| 3 | Kein Analytics, keine Google Search Console | Niemand weiß, wie viele Besucher kommen und woher | siehe Abschnitt 4 |
| 4 | Kein Google Business Profile verlinkt | Für lokale Sydney-Suchen ("content creator Bondi") der stärkste kostenlose Lead-Kanal | Profil anlegen, Website verlinken |
| 5 | Kleinkram: Tippfehler in der Datenschutzerklärung ("contact use directly") | gering | korrigieren |

## 3. Was Julia beim Ausstieg aus HWM braucht (wichtig!)

Der Vertrag (§ 6) gibt nur ein Recht auf "Daten" binnen 14 Tagen nach Vertragsende. Ob das den **Quellcode** und die **Domain** umfasst, steht nicht drin.

Vor dem Kündigungsversand (spätestens im Januar) klären:
1. **Domain:** Auf wen ist mor-marketing.com registriert? Wenn auf HWM → Auth-Code/Transfer an Julia anfordern. Ohne Domain ist die Seite weg.
2. **Quellcode:** Zugriff auf das Git-Repository (GitHub) oder ein ZIP des Next.js-Projekts. Wahrscheinlichkeit, dass Sven das ohne Diskussion herausgibt: **~60 %**. Falls nicht: Nachbau (siehe unten), Inhalte/Bilder gehören ohnehin Julia.
3. **E-Mail:** Alle Mails aus info@mor-marketing.com exportieren, bevor das Postfach abgeschaltet wird.

## 4. Selbst betreiben – Kosten

| Baustein | Empfehlung | Kosten |
|---|---|---|
| Domain .com | Cloudflare Registrar (Selbstkosten) | ~US$10–11/Jahr (~A$17) |
| Hosting | Cloudflare Pages oder Netlify (kostenlos, auch kommerziell erlaubt). Vercel Hobby ist laut AGB nur nicht-kommerziell, Vercel Pro wäre US$20/Monat → nicht sinnvoll | 0 |
| E-Mail info@ | Variante A: Cloudflare Email Routing (kostenlos) → leitet an Julias Gmail weiter, Antworten per Gmail "Senden als". Variante B: Zoho Mail Free. Variante C: Google Workspace (~A$10/Monat) nur wenn sie es professionell will | 0 (A/B) |
| Kontaktformular | Web3Forms oder Formspree Free | 0 |
| Analytics | **Cloudflare Web Analytics** (kostenlos, ohne Cookies) + **Google Search Console** (kostenlos, zeigt Suchbegriffe) + optional GA4 für Conversion-Events | 0 |
| **Summe** | | **~A$17/Jahr ≈ 1,40 A$/Monat** statt 8 €/Monat (~A$170/Jahr) |

Ersparnis ~A$150/Jahr. Ehrlich: Das Geld ist nicht der Punkt (wie du sagst) – der Mehrwert ist die **Kontrolle + Messbarkeit**.

## 5. Was Julia mit Analytics tatsächlich sehen würde

- Besucher pro Tag/Monat, Herkunft (Instagram, Google, direkt, WhatsApp-Link)
- Welche Case Studies/Services angeschaut werden
- **Leads:** Formular-Absendungen, Klicks auf E-Mail und Instagram (als Events)
- Google Search Console: Für welche Suchbegriffe sie bei Google auftaucht und wie oft geklickt wird

Realistische Erwartung (Einschätzung, ~70 %): Eine Portfolio-Seite einer Solo-Creatorin in Sydney hat **unter 100–300 Besuche/Monat**, fast alles aus Instagram-Bio und direkten Links. Die Seite ist eher **Glaubwürdigkeitsnachweis** als Lead-Maschine. Leads entstehen über Instagram, Empfehlungen und Google Business Profile. Analytics macht genau das sichtbar – und zeigt, ob sich Investitionen in SEO überhaupt lohnen.

## 6. Vorschlag Reihenfolge

1. **Jetzt (Nov):** Sven bitten, den Canonical-Fehler zu fixen (kostet ihn 5 Min, ist im Vertrag "Wartung"). Optional gleich Cloudflare Web Analytics einbauen lassen → bis März echte Zahlen.
2. **Jetzt:** Google Search Console + Google Business Profile für Julia anlegen (geht ohne HWM, Domain-Verifizierung per Meta-Tag oder DNS – dafür braucht es Sven, oder HTML-Tag-Variante).
3. **Januar:** Kündigung + Anforderung von Code, Domain-Transfer, Mail-Export (Termin steht am 15.1.2027).
4. **Feb/März:** Seite auf Cloudflare Pages umziehen (oder nachbauen), Domain transferieren, E-Mail-Routing einrichten, Analytics an. Vor dem 31.3.2027 fertig, damit es keinen Ausfall gibt.

Nachbau-Aufwand, falls kein Code kommt: ~1–2 Tage mit Claude (Next.js/Astro, Inhalte und Bilder von der Live-Seite übernehmen).
