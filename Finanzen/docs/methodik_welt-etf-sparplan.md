# Methodik & Plan: Welt-ETF-Sparplan für eine australische Staatsbürgerin

**Zweck dieses Dokuments:** Es soll für sich allein verständlich sein, damit eine externe KI oder ein Mensch prüfen kann, ob der Plan der klügste ist. Jede Faktenaussage hat Quelle und Datum. Jede Einschätzung hat eine Konfidenz in %. Annahmen sind als **(Annahme)** markiert.
**Stand:** 3.11.2026 · **Autor:** Claude (für Nico) · **Status:** Entwurf zur Prüfung, noch nicht umgesetzt.
**Kein Finanz- oder Steuerrat.** Endgültige Steuerfragen gehören zu einem registrierten australischen Tax Agent.

---

## 1. Ausgangslage und Ziel

| Punkt | Wert | Status |
|---|---|---|
| Person | Julia, **Australian Citizen**, lebt in Sydney, steuerlich in AU ansässig | bestätigt (Nico, 3.11.2026) |
| Rückkehr nach Europa | nicht geplant | bestätigt |
| Ziel | langfristiger Vermögensaufbau, so einfach wie möglich | bestätigt |
| Produktwunsch | Abbild von **Vanguard FTSE All-World UCITS Acc** (VWRA/VWCE) oder **MSCI World**, ohne Australien-Übergewicht | bestätigt |
| Ausführung | **automatisch, mindestens 1× pro Monat** | bestätigt |
| Broker | **Betashares Direct** (Entscheidung Nico, 3.11.2026) | bestätigt |
| Bank | ANZ (Quelle des Dauerauftrags) | bestätigt |
| Alter, Einkommen, Grenzsteuersatz | unbekannt; gerechnet mit 32 % und 39 % inkl. Medicare | offen |
| Höhe Erspartes, Sparrate, Notgroschen | unbekannt | offen |
| Super-Fonds, Option, Gebühren | unbekannt | offen |
| Wohnungskauf in < 5 J. | unbekannt | offen |

**Zielfunktion:** maximales Endvermögen **nach Steuern und Kosten**, unter der Nebenbedingung „läuft automatisch und Julia muss nichts entscheiden“. Einfachheit ist Teil der Zielfunktion und kein Nice-to-have. Ein manueller Sparplan, der ausgesetzt wird, kostet mehr als jede Kostendifferenz unten (Annahme).

## 2. Ausgeschlossene Wege (mit Grund)

| Option | Grund | Konfidenz | Quelle |
|---|---|---|---|
| Trade Republic, Scalable Capital | Erfordern Wohnsitz in EU-Ländern; AU nicht unterstützt | 95 % | [TR Support](https://support.traderepublic.com/en-de/701-Why-do-I-have-to-be-a-permanent-resident-to-open-an-account), [Scalable FAQ](https://de.scalable.capital/en/trading-faq) |
| ANZ Share Investing | **Geschlossen** seit 15.3.2023, Kunden zu CMC Invest migriert | 95 % | [CMC](https://www.cmcmarkets.com/transitionanzshareinvestingcomau/) |
| VWRA direkt (LSE) via CMC Invest | Inhaltlich ideal, aber **kein Auto-invest**, Mindestorder A$1.000 international, FX-Spread bis 0,60 % je Kauf und Verkauf | 80 % | [Quantroutine 7/2026](https://quantroutine.com/brokers/cmc-invest/), [CMC Brokerage 5/2026](https://www.cmcmarkets.com/en-au/stockbroking/brokerage-rates) |
| DHHF, VDAL, VDHG (All-in-one) | 37–40 % Australien, widerspricht Vorgabe; VDHG zusätzlich 10 % Anleihen | 95 % | [Betashares DHHF](https://www.betashares.com.au/fund/diversified-all-growth-etf/), [Vanguard VDAL](https://fund-docs.vanguard.com/ETF-Vanguard_Diversified_All_Growth_Index_ETF_F100_FS_VDAL.pdf) |
| VGS (MSCI World ex AU) | Inhaltlich wie BGBL, aber 0,18 % statt 0,08 % und nicht im Betashares-Auto-invest | 80 % | [Trackinsight](https://www.trackinsight.com/en/fund/VGS) |
| IWLD | ESG-Leaders-Index, kein neutraler Weltmarkt | 85 % | [Trackinsight](https://www.trackinsight.com/en/fund/IWLD) |
| US-ETFs (z. B. VT) | W-8BEN, US-Erbschaftsteuerthema, Aufwand; nicht „einfach“ | 80 % | – |
| Pearler | $6,50 je Kauf; bei A$500/Monat 1,3 % Kaufkosten | 85 % | [Pearler](https://pearler.com/help/4644340-how-much-does-pearler-cost) |

## 3. Methodik der Nachbildung

### 3.1 Zielindex wählen
- **Variante „MSCI World“:** 100 % **BGBL**. MSCI World enthält ca. 2 % Australien (Annahme). BGBL ist ex Australien, für eine Australierin aber gewollt, weil ihr übriges Vermögen (Super, Job, Immobilie) ohnehin australisch ist.
- **Variante „FTSE All-World“ (inkl. Schwellenländer):** **BGBL + BEMG**.

### 3.2 Gewicht der Schwellenländer bestimmen
Vorgehen: Länderweights von VWRA durch die Länderweights von BEMG (MSCI EM) teilen. Das gibt an, welcher BEMG-Anteil die Länder von VWRA trifft.

| Land | VWRA (30.9.2026) | BEMG-Index (30.9.2026) | implizierter BEMG-Anteil |
|---|---|---|---|
| Taiwan | 3,5 % | 28,9 % | 12,1 % |
| Korea | 2,6 % | 21,4 % | 12,1 % |
| China | 2,7 % | 19,5 % | 13,8 % |

→ **12 % BEMG, 88 % BGBL.** Konfidenz 75 %. Der Wert ist robust für die Länder Taiwan und Korea. China liegt höher, weil FTSE China-A-Aktien anders gewichtet als MSCI (Annahme). Hinweis: Korea ist bei FTSE „Developed“, bei MSCI „Emerging“. Die Rechnung nutzt Länder und keine Labels, deshalb stört das nicht.

### 3.3 Ergebnis: Vergleich der Länder (berechnet)

| | VWRA | BGBL 88 / BEMG 12 | BGBL 100 |
|---|---|---|---|
| USA | 62,2 | 65,0 | 73,9 |
| Japan | 6,1 | 6,1 | 6,9 |
| Taiwan | 3,5 | 3,5 | 0 |
| Kanada | 2,9 | 2,9 | 3,3 |
| Korea | 2,6 | 2,6 | 0 |
| UK | 3,1 | 2,5 | 2,8 |
| China | 2,7 | 2,3 | 0 |
| Indien | < 1,8 | 1,3 | 0 |
| Australien | < 1,8 | 0 | 0 |

Die Abweichung liegt bei USA +2,8 Pp., der Rest bei ±0,6 Pp. Die Ursache: VWRA enthält Small/Mid-Anteile und Australien, BGBL ist Large & Mid Cap. Quellen: [VWRA Factsheet](https://fund-docs.vanguard.com/FTSE_All-World_UCITS_ETF_USD_Accumulating_9679_NETH_INT_EN.pdf), [BGBL](https://www.betashares.com.au/fund/global-shares-etf), [BEMG](https://www.betashares.com.au/fund/emerging-markets-complex-etf/). Volle Tabellen mit Sektoren: [research/2026-11-03_welt-etf-kandidaten.md](research/2026-11-03_welt-etf-kandidaten.md).

### 3.4 Produkte im Detail

| | BGBL | BEMG |
|---|---|---|
| Index | Solactive GBS Developed Markets ex Australia Large & Mid Cap, 1.310 Titel | MSCI Emerging Markets Net TR (AUD) |
| Kosten | 0,08 % p. a. | 0,35 % p. a. |
| Struktur | AU-Trust, hält Aktien physisch | AU-Trust, investiert in **Amundi MSCI EM II UCITS ETF** (Irland, **swap-basiert**, thesaurierende Anteilsklasse) |
| Ausschüttung | mind. jährlich, 12-M-Rendite 1,2 % | **keine** („no intention to distribute“) |
| Fondsgröße | ~A$5,6 Mrd. | ~A$0,2 Mrd. |
| Quelle | [Betashares](https://www.betashares.com.au/fund/global-shares-etf), 2.11.2026 | [Betashares](https://www.betashares.com.au/fund/emerging-markets-complex-etf/), [BEMG FAQ](https://www.betashares.com.au/files/BEMG/BEMG-Frequently-Asked-Questions.pdf) |

## 4. Steuerliche Analyse (AU-Steuerinländerin)

| Produkt | Laufend | Verkauf | Quellensteuer | Konfidenz |
|---|---|---|---|---|
| BGBL | Ausschüttung (~1,2 %) jedes Jahr zum Grenzsteuersatz (laut AMMA-Statement), auch bei Wiederanlage | CGT: bis 30.6.2027 50 % Discount; ab 1.7.2027 nur der **reale** (CPI-indexierte) Gewinn, zum Grenzsteuersatz, **mind. 30 %** | als FITO anrechenbar | 90 % |
| BEMG | Laut Betashares keine Ausschüttung, also keine laufende Steuer. Ob die AMIT-Zurechnung trotzdem etwas erfasst, ist nicht explizit bestätigt | CGT: bis 30.6.2027 50 % Discount; ab 1.7.2027 nur der **reale** (CPI-indexierte) Gewinn, zum Grenzsteuersatz, **mind. 30 %** | **keine** FITO (laut BEMG-FAQ) | 75 % |
| VWRA (Vergleich) | keine (irische plc; FIF 2010 abgeschafft; FAF nie in Kraft und nur für ≥ 80 % Anleihen; CFC braucht Kontrolle) | CGT: bis 30.6.2027 50 % Discount; ab 1.7.2027 nur der **reale** (CPI-indexierte) Gewinn, zum Grenzsteuersatz, **mind. 30 %** | nicht anrechenbar | 75–80 % |

Bemerkenswert: Betashares selbst baut BEMG auf genau der Logik „AU-Anleger hält irischen thesaurierenden UCITS-Fonds, steuerpflichtig erst bei Verkauf“. Das stützt die Hypothese zu VWRA (Konfidenz dadurch 75 → 80 %).

Der Grenzsteuersatz (ATO 2026–27, Residents): 16 % bis A$45.000, 30 % bis A$135.000, 37 % bis A$190.000, 45 % darüber, zuzüglich 2 % Medicare ([ATO, 13.8.2026](https://www.ato.gov.au/tax-rates-and-codes/tax-rates-australian-residents)).

## 4a. CGT-Reform ab 1.7.2027 (Gesetz)
- *Treasury Laws Amendment (Tax Reform No. 1) Act 2026*; ATO: „now law“ ([ATO, aktualisiert 29.6.2026](https://www.ato.gov.au/about-ato/new-legislation/in-detail/individuals/tax-reform-boosting-home-ownership-reforming-negative-gearing-and-capital-gains-tax), [Budget 2026–27](https://budget.gov.au/content/04-tax-reform.htm)).
- Für Individuals, Trusts, Partnerships: 50 %-Discount wird durch **CPI-Indexierung der Kostenbasis** und eine **Mindeststeuer von 30 % auf Gewinne** ersetzt.
- Gilt nur für Gewinne, die **nach dem 1.7.2027** entstehen. Laut [Moore Australia (5/2026)](https://www.moore-australia.com.au/news/federal-budget-series-cgt-discount-reform/) wird die Kostenbasis zum 1.7.2027 auf den Marktwert gesetzt (sekundär, Konfidenz 70 %).
- Superfonds: auf der ATO-Seite nicht behandelt (offen).
- Folgen für den Plan: (1) Der Steuervorteil thesaurierender Fonds (VWRA, BEMG) schrumpft, weil umgewandelte Dividenden nicht mehr zum halben Satz besteuert werden; BGBL liegt im Modell jetzt **vor** VWRA. (2) Auch bei niedrigem Einkommen im Ruhestand gelten mind. 30 % auf reale Gewinne. (3) Super wird relativ attraktiver (abhängig von der noch offenen Super-Behandlung).

## 5. Kosten- und Steuermodell

Code: [`models/scenarios.py`](../models/scenarios.py). Annahmen:
- Gleiche Bruttorendite für alle Produkte, **7 %** (realistisch) bzw. **5 %** (vorsichtig) nominal p. a. **(Annahme)**
- Grenzsteuersatz 32 % oder 39 %, Exit-Steuer gleich (Variante: 18 % in Rente)
- BGBL: Ausschüttung 1,2 % jährlich versteuert, Rest reinvestiert; VWRA: 0,15 % Quellensteuer-Leckage p. a. **(Annahme)**, 0,6 % FX je Kauf/Verkauf
- Verkauf aller Anteile am Ende. **CGT nach Regel ab 1.7.2027** (CPI 2,5 % **(Annahme)**, Mindeststeuer 30 %), vereinfacht für die ganze Haltedauer

Ergebnis (A$1.000/Monat, 7 %, 32 %, netto nach Exit-CGT):

| | 10 J | 20 J | 30 J |
|---|---|---|---|
| BGBL | 159.800 | 439.400 | 938.500 |
| **BGBL 88 / BEMG 12** | 159.400 | 437.500 | 932.200 |
| VWRA via CMC | 157.400 | 431.200 | 919.900 |
| VWRA, Worst Case (ATO besteuert laufend) | 157.100 | 426.700 | 897.100 |

Interpretation (neue CGT-Regel): BGBL liegt nach 30 Jahren ~2 % vor VWRA. Mit der alten 50 %-Regel lag VWRA ~1 % vorn. Beides innerhalb der Modellunsicherheit. **Die Wahl zwischen VWRA und der Betashares-Lösung ist kostenseitig neutral.** Entscheidend sind Automatik und steuerliche Klarheit, und dort liegt Betashares vorn.
Modellstand: BEMG ist als nicht ausschüttend gerechnet, mit 0,03 % p. a. Quellensteuer-Leckage **(Annahme)**. Indexunterschiede (z. B. Small Caps in VWRA) sind nicht modelliert.

## 6. Vorgeschlagener Plan

1. **Notgroschen:** 3–6 Monatsausgaben bleiben auf einem Hochzins-Sparkonto (nicht investiert). Betrag offen.
2. **Kurzfristige Ziele (< 5 J., z. B. Wohnungskauf):** nicht in Aktien. FHSS prüfen (max. A$15.000/Jahr, A$50.000 gesamt; [ATO](https://www.ato.gov.au/individuals-and-families/super-for-individuals-and-families/super/withdrawing-and-using-your-super/early-access-to-super/first-home-super-saver-scheme/about-fhss-release-amounts)).
3. **Depot:** Betashares Direct, ein Auto-invest-Plan, **monatlich**:
   - Standard: **88 % BGBL / 12 % BEMG** (≈ FTSE All-World ex Australien)
   - Einfachste Alternative: 100 % BGBL (≈ MSCI World ex Australien, ~74 % USA)
4. **Geldfluss:** ANZ-Dauerauftrag ins Betashares Direct Wallet, 1–2 Tage vor dem Auto-invest-Termin ([Betashares Auto-invest](https://www.betashares.com.au/direct/auto-invest)).
5. **Einmalbetrag (Erspartes minus Notgroschen):** gestaffelt über **6–12 Monate** als erhöhte Auto-invest-Rate; bis dahin auf dem Hochzins-Sparkonto. Begründung: Einmalanlage schlägt Staffelung historisch in ca. 2/3 der Fälle (Vanguard-Studien, Konfidenz 80 %). Die Staffelung ist eine bewusste Absicherung gegen Reue, keine Renditeoptimierung.
6. **Rebalancing:** keins. Die feste 88/12-Aufteilung jeder Rate hält die Gewichte nahe am Ziel; einmal pro Jahr prüfen.
7. **Ausschüttungen BGBL:** wiederanlegen (ob Betashares Direct automatische Wiederanlage anbietet, ist **nicht verifiziert**; sonst landen sie im Wallet und gehen in die nächste Auto-invest-Rate).
8. **Steuer:** jährliches AMMA-Statement in die Steuererklärung. Ab 1.7.2027 gilt die neue CGT-Regel (s. Abschnitt 4a); die 12-Monats-Grenze verliert für Verkäufe danach ihre Bedeutung (Konfidenz 70 %, Detailregeln prüfen).
9. **Super (separater, größerer Hebel):** Anlageoption und Gebühren prüfen; Salary Sacrifice bis zum Concessional Cap (A$32.500 in 2026–27 inkl. Arbeitgeberbeitrag, [ATO](https://www.ato.gov.au/tax-rates-and-codes/key-superannuation-rates-and-thresholds/contributions-caps)) prüfen, wenn der Grenzsteuersatz ≥ 30 % ist und das Geld bis zum Preservation Age gebunden sein darf.

## 7. Risiken und offene Punkte

| Risiko | Einschätzung |
|---|---|
| **Custodian-Modell** Betashares Direct (kein CHESS-HIN auf ihren Namen) | Vermögen ist getrennt verwahrt (laut Betashares); Übertrag raus bis A$9,50 je Wertpapier. Akzeptabel (Konfidenz 75 %) |
| **BEMG ist swap-basiert** (Kontrahentenrisiko) und klein (A$0,2 Mrd.) | Swap täglich resettet, Exposure ≈ Tagesdifferenz (laut BEMG-FAQ). Bei 12 % Gewicht vertretbar (70 %). Alternative wäre 100 % BGBL |
| Betashares ändert das $0-Modell oder die Auto-invest-Regeln | ~20 % in 5 Jahren (Annahme); Wechsel möglich |
| Steuerbehandlung BEMG nicht von ATO bestätigt | 75 %; mit Tax Agent einmalig verifizieren |
| US-Konzentration (65–74 %) und Tech-Anteil (~40 % inkl. Kommunikation) | marktbedingt, gilt auch für VWRA; bewusst akzeptiert |
| Persönliche Daten fehlen (Einkommen, Betrag, Horizont, Super) | Plan ist bis dahin nur ein Rahmen |

## 8. Fragen an den Reviewer

1. Ist 88/12 (BGBL/BEMG) die beste Nachbildung von FTSE All-World **mit nur Betashares-ETFs**, oder ist 100 % BGBL wegen Einfachheit, Kontrahentenrisiko und Fondsgröße von BEMG die klügere Wahl?
2. Ist die Steuerlogik in Abschnitt 4 korrekt, vor allem für BEMG (Nicht-Ausschüttung) und die Einschätzung zu irischen Thesaurierern (FIF, FAF, CFC)?
3. Übersehen wir einen ASX-ETF, der FTSE All-World/ACWI ex AU in **einem** Produkt abbildet und für Auto-invest verfügbar ist?
4. Ist es richtig, null Australien zu halten, wenn Super, Job und Immobilie ohnehin australisch sind? Oder sollte gerade wegen Franking Credits ein kleiner Australien-Anteil rein?
5. Ist eine Staffelung über 6–12 Monate sinnvoll, oder spricht bei ihrem Profil mehr für eine Einmalanlage?
6. Gibt es eine bessere Plattform mit Auto-invest **und** CHESS-HIN bei $0 bzw. nahe $0?
7. Sollte Super-Optimierung zeitlich **vor** dem Depot stehen?

## Quellenverzeichnis
Alle Einzelquellen mit Datum: [research/2026-11-03_verifikation.md](research/2026-11-03_verifikation.md) · Kandidatenvergleich: [research/2026-11-03_welt-etf-kandidaten.md](research/2026-11-03_welt-etf-kandidaten.md) · Broker-Empfehlung: [research/2026-11-03_broker-etf-empfehlung.md](research/2026-11-03_broker-etf-empfehlung.md)
