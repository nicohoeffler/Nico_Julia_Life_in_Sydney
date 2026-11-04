# Setup-Plan Julia (Entwurf v1, 3.11.2026)

Basis: [profil.md](profil.md) (Schätzwerte aus dem Gespräch). ETF- und Broker-Logik: [../../docs/methodik_welt-etf-sparplan.md](../../docs/methodik_welt-etf-sparplan.md).

## 1. Gegenrechnung (Schritt für Schritt)
1. Einkommen 1.000/Woche × 52 / 12 = **4.333/Monat**.
2. Ausgaben 400/Woche × 52 / 12 = **1.733/Monat**.
3. Rechnerischer Überschuss: **~2.600/Monat**.
4. Diskutierte Sparrate: 400/Monat ≈ **15 % des Überschusses**. Wo bleiben die übrigen ~2.200?

Zwei Erklärungen, beide wahrscheinlich teilweise richtig:
- **Ausgaben sind unterschätzt** (Konfidenz 75 %). Es fehlen typischerweise Handy, Kleidung, Geschenke, Reisen, Ausgehen, Gesundheit, Business-Ausgaben (Equipment, Software), Auto/Opal-Karte.
- **Steuer auf das Selbstständigen-Einkommen fehlt** (Konfidenz 70 %). Auf ABN-Einnahmen wird nichts automatisch einbehalten.

→ **Erster Schritt:** Kontoauszüge von 3 Monaten ansehen (die ANZ-App kategorisiert) und die **echten** Ausgaben pro Monat ermitteln. Erst danach die Sparrate festlegen.

## 2. Steuer bei Selbstständigkeit (Australien)
- Steuerfreibetrag **A$18.200** gilt für das **Gesamteinkommen** (Anstellung + Selbstständigkeit zusammen), nicht pro Einkommensart ([ATO, 2026–27](https://www.ato.gov.au/tax-rates-and-codes/tax-rates-australian-residents)). Konfidenz 95 %.
- Beispiel 52.000/Jahr: 4.288 + 30 % × 7.000 = 6.388 + 2 % Medicare 1.040 = **7.428 (≈ 14 % im Schnitt, Grenzsatz 32 %)**.
- Auf ABN-Gewinn wird nichts einbehalten → **jeden Monat 25 % des Business-Gewinns auf ein separates Steuerkonto** (Faustregel, Annahme; der Grenzsatz liegt bei 32 %, ist also eher zu wenig als zu viel). Ab einer bestimmten Höhe schickt die ATO PAYG-Vorauszahlungen (Instalments); Details nicht verifiziert.
- **Versicherung:** Australien hat keine deutsche Sozialversicherung (12–15 %). Gesetzlich gibt es nur die **Medicare Levy von 2 %** über die Steuer. Private Krankenversicherung ist freiwillig, die Medicare Levy Surcharge greift erst bei höherem Einkommen (Grenze nicht verifiziert). Konfidenz 85 %.
- **Super:** Bei Anstellung zahlt der Arbeitgeber Super Guarantee (12 %, Konfidenz 85 %, nicht in dieser Runde verifiziert). **Als Selbstständige zahlt niemand Super für sie.** Später prüfen: freiwillige, steuerlich absetzbare Einzahlungen (15 % statt 32 %) und Government Co-contribution für niedrige/mittlere Einkommen (nicht verifiziert).

## 3. Topf-Modell (25.000 Cash)

| Topf | Betrag | Wo | Warum |
|---|---|---|---|
| **Notgroschen** | ~10.000 (≈ 6 Monate echte Ausgaben, vorläufig) | ANZ Hochzins-Sparkonto | Selbstständige mit schwankendem Einkommen brauchen eher 6 als 3 Monate |
| **Steuer-Reserve** | ~3.000–5.000 bis die Steuer klar ist | separates Sparkonto | ABN-Steuer nachzahlen, ohne Panikverkauf |
| **Investieren** | **10.000** | Betashares Direct, 1.000/Monat × 10 | Nicos Vorschlag, passt |
| Rest / Puffer | ~0–2.000 | Sparkonto | Business-Equipment, Unvorhergesehenes |

Nicos 10.000 passen zu dieser Aufteilung (Konfidenz 70 %). Mehr würde ich erst investieren, wenn die echten Ausgaben und die Steuerlast bekannt sind.

## 4. Sparplan: sofort starten, nicht nach 10 Monaten
- Empfehlung: **laufende Rate ab Monat 1** zusätzlich zur Staffelung, also z. B. 1.000 + 300 = **1.300/Monat** für 10 Monate, danach 300–400/Monat (Konfidenz 70 %).
- Gründe: Die Gewohnheit entsteht sofort, und es gibt einen einzigen Auto-invest-Betrag statt einer späteren Umstellung. Ist der Überschuss real ~2.600, ist das leicht tragbar.
- Gegenargument: Wenn die echten Ausgaben deutlich höher sind, fängt sie erst mit der Staffelung an und startet die Rate nach dem Ausgaben-Check.
- Die Staffelung über 10 Monate ist eine Reue-Versicherung und keine Renditeoptimierung. Eine Einmalanlage gewinnt historisch in ca. 2/3 der Fälle (Konfidenz 80 %). Bei 10k und einer Anfängerin ist die Staffelung trotzdem vertretbar.

**Update 4.11.2026 (Entscheidung Nico):** Die Staffelung bleibt: morgen $1.300 von Hand (1.144 BGBL / 156 BEMG), ab 19.12.2026 Auto-invest $1.300 für 9 Monate, ab 19.9.2027 $300 (264 / 36). ANZ-Dauerauftrag am 17.

## 5. Umsetzung
1. ANZ: Hochzins-Sparkonto für Notgroschen + Steuer-Reserve (Konditionen prüfen).
2. Betashares Direct Konto eröffnen (macht Julia selbst).
3. Auto-invest: monatlich, **88 % BGBL / 12 % BEMG** (oder 100 % BGBL), Betrag 1.300.
4. ANZ-Dauerauftrag ins Betashares-Wallet, 1–2 Tage vor dem Auto-invest-Termin.
5. Nach 10 Monaten: Betrag auf die laufende Rate umstellen.
6. Schritt-für-Schritt-Anleitung für Julia (Englisch): [auto-invest-setup.md](auto-invest-setup.md).

## 6. Offene Fragen an Julia
1. Echte Ausgaben laut 3 Monaten Kontoauszug?
2. Wie viel des Einkommens ist Anstellung und wie viel ABN? Hat sie eine ABN, und hat sie schon PAYG-Instalments bekommen?
3. Super-Fonds, Kontostand, Anlageoption?
4. Größere Ausgaben in den nächsten 2–3 Jahren (Equipment, Reisen, Auto, Wohnung)?
5. Investiert sie schon etwas (z. B. kleine Monatsrate irgendwo)?

## 7. Steuer-Checkliste (Stand 4.11.2026, ohne neue Verifikation)
- Steuerjahr 1.7.–30.6.; Erklärung selbst bis 31.10., über Tax Agent später (95 %).
- BGBL: Ausschüttungen jedes Jahr steuerpflichtig, auch wenn reinvestiert; Werte aus dem AMMA-Statement, Quellensteuer als FITO (90 %).
- BEMG: keine Ausschüttung, also keine laufende Steuer (75 %).
- Verkauf: CGT zum Grenzsteuersatz. **Bis 30.6.2027:** nach > 12 Monaten nur 50 % des Gewinns. **Ab 1.7.2027 (Gesetz):** nur der inflationsbereinigte Gewinn, aber **mind. 30 %** Steuer darauf. Jede Monatsrate ist eine eigene Tranche, Kaufbelege aufheben (90 %).
- Kapitalverluste nur mit Kapitalgewinnen verrechenbar (90 %).
- ABN: kein Steuerabzug → 25 % des Gewinns zurücklegen; Business-Ausgaben (Software, Equipment-Abschreibung) absetzbar; GST-Pflicht erst ab A$75.000 Umsatz (95 %).
- Mehrere Arbeitgeber: Steuerfreibetrag nur bei einem beanspruchen (90 %).
- Super als Selbstständige: freiwillige Beiträge absetzbar, vorher „Notice of intent“ an den Fonds (90 %).
- Belege 5 Jahre aufbewahren (95 %). Tax-Agent-Gebühren sind absetzbar (90 %).
