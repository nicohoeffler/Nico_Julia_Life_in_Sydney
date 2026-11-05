# Broker & ETF für Julia: Empfehlung (Stand 3.11.2026, v2)

Vorgabe Nico (3.11.2026): ein breiter Welt-ETF (Logik MSCI World / Vanguard FTSE All-World), **ohne** Australien-Übergewicht, ein Produkt, monatlich. Julia ist **Australian Citizen, keine Rückkehr geplant**, Bank ANZ. Nico tendiert zu CMC.
Fakten und Quellen: [2026-11-03_verifikation.md](2026-11-03_verifikation.md). Rechnung: [`models/scenarios.py`](../../models/scenarios.py).

## 1. Prämisse korrigiert: Australien zwingt nicht zu Australien-Aktien

Australien-lastig sind nur die **Multi-Asset-„All-in-one“-Fonds** (DHHF 37 %, VDAL 40 %), weil sie bewusst einen Home Bias einbauen. Reine Welt-ETFs **ohne Australien** gibt es an der ASX mehrere:

| ETF | Index | Kosten | Australien | Schwellenländer |
|---|---|---|---|---|
| **BGBL** (Betashares) | Solactive GBS Developed Markets ex Australia, ~1.300 Titel | **0,08 %** | 0 % | nein |
| VGS (Vanguard) | MSCI World ex Australia, ~1.500 Titel | 0,18 % | 0 % | nein |
| BEMG (Betashares) | MSCI Emerging Markets | 0,35 % | 0 % | ja |
| **VWRA** (Vanguard, Irland, LSE) | FTSE All-World, 3.821 Titel, US 62 % | **0,14 %** (seit 28.7.2026) | ~2 % (Annahme, nicht im Factsheet) | ja |

BGBL ist faktisch „MSCI World minus ~2 % Australien“. Was an der ASX fehlt, ist **ein einziges** Produkt, das zusätzlich Schwellenländer enthält (Konfidenz 70 %). Schwellenländer sind ca. 10 % des Weltmarkts (Annahme).

## 2. Steuer: irischer Thesaurierer (VWRA) bei einer australischen Steuerinländerin

| Prüfpunkt | Ergebnis | Konfidenz |
|---|---|---|
| Rechtsform | Vanguard Funds plc = irische Gesellschaft (UCITS). Für AU: Aktien einer ausländischen Gesellschaft | 85 % |
| FIF-Regeln (laufende Besteuerung ausländischer Fonds) | 2010 abgeschafft | 90 % |
| Foreign Accumulation Fund (FAF) | Nur Entwurf (2011), nie in Kraft; hätte ohnehin nur Fonds mit ≥ 80 % Anleihen erfasst | 90 % |
| CFC-Regeln | Brauchen Kontrolle (Beteiligungsschwellen), bei Retail-Anteil nicht erfüllt | 95 % |
| Transferor-Trust-Regeln | Gelten für Trusts, VWRA ist eine Gesellschaft | 85 % |
| Laufend | Keine Ausschüttung → nichts jährlich zu versteuern | 75 % |
| Verkauf | CGT in AUD (inkl. Währungseffekt); **ab 1.7.2027 neue Regel** (CPI-Indexierung, mind. 30 %), siehe Methodik 4a | 85 % |
| Nachteil | 15 % US-Quellensteuer bleibt im Fonds, nicht anrechenbar (Leckage ca. 0,15 % p. a., Annahme) | 80 % |

Fazit: Der Steueraufschub per Thesaurierung **funktioniert in AU wahrscheinlich sogar besser als in DE** (keine Vorabpauschale; Dividenden werden in rabattierten Kursgewinn umgewandelt). Gesamtkonfidenz 75 %. Es gibt aber **keine veröffentlichte ATO-Aussage**. Ein Restrisiko bleibt, dass die ATO das anders sieht. Das ist im Modell als Worst Case gerechnet.

BGBL dagegen: ein australischer Trust, schüttet aus (12-Monats-Rendite 1,2 %), wird jährlich zum Grenzsteuersatz versteuert. Die Quellensteuer wird angerechnet (FITO), es gibt einen sauberen jährlichen Steuerbericht (AMIT), und beim Verkauf greift ebenfalls der 50-%-Discount.

## 3. Rechnung (models/scenarios.py)

Annahmen: A$1.000/Monat, 7 % bzw. 5 % brutto, Grenzsteuer 32 % (30 % + 2 % Medicare; ATO-Tarif 2026–27), VWRA mit 0,60 % FX-Spread beim Kauf **und** Verkauf (CMC: „bis zu 0,60 %“), alles nach Exit-CGT.

| Netto nach Verkauf, 7 % | 10 J | 20 J | 30 J |
|---|---|---|---|
| BGBL (Betashares Direct, $0) | 160.900 | 448.500 | 974.100 |
| BGBL 90 % + BEMG 10 % | 160.500 | 446.000 | 965.100 |
| **VWRA via CMC** | 159.800 | 448.200 | **982.800** |
| VWRA, Worst Case (ATO besteuert laufend) | 157.200 | 430.700 | 916.700 |

Lesart:
- Der Unterschied zwischen BGBL und VWRA liegt bei **≤ 1 % nach 30 Jahren** (bei 39 % Grenzsteuer ca. +2 % für VWRA). Das liegt innerhalb der Modellunschärfe. Wer mit „VWRA ist klar besser“ argumentiert, kann das mit diesen Zahlen nicht belegen.
- Bis ca. 15–20 Jahre liegt BGBL vorn (FX-Spread wiegt schwerer als der Steueraufschub).
- Fair verglichen (beide mit Schwellenländern): VWRA schlägt BGBL+BEMG um ca. 0,5 % (20 J) bis 1,8 % (30 J).
- Das Risiko ist asymmetrisch: Im Worst Case verliert VWRA rund 6 % nach 30 Jahren.

## 4. Empfehlung

**Option 1 (meine Empfehlung, 60 %): BGBL über Betashares Direct mit Auto-invest.**
- Erfüllt „ein Produkt, monatlich, fertig“ wirklich: ANZ-Dauerauftrag → Auto-invest, $0 Gebühren, kein Mindestbetrag pro Order, keine FX-Kosten, klare Steuerberichte.
- Preis: ca. 10 % Schwellenländer fehlen. Wer sie will, nimmt BEMG mit 10 % in denselben Auto-invest-Plan (bleibt automatisch).
- Contra: Custodian statt CHESS-HIN.

**Option 2 (deine Präferenz, 40 %): VWRA über CMC Invest.**
- Der echte FTSE All-World in einem Produkt, CHESS ist hier egal (international = Custodian BNP Paribas), $0 Brokerage an der LSE, langfristig minimal steuergünstiger.
- Contra, und das ist für Julia entscheidend: **CMC hat kein Auto-invest**, sie muss jeden Monat selbst kaufen. Mindestorder **A$1.000** international, also nur ab A$1.000/Monat oder alle 2–3 Monate. Bis zu 0,60 % FX je Kauf. Steuerbehandlung nicht ATO-bestätigt. CGT pro Kauf-Tranche in AUD (Tool wie Sharesight sinnvoll).
- Hebt die Disziplin-Frage auf: Ein Sparplan, der manuell läuft, wird erfahrungsgemäß häufiger ausgesetzt (Annahme, keine Quelle).

**Hybrid, falls CMC wegen CHESS gewünscht:** BGBL über CMC. Der erste Kauf unter A$1.000 pro Tag und Wertpapier ist $0, CHESS-HIN auf ihren Namen, aber ebenfalls kein Auto-invest.

**Was müsste stimmen, damit Option 1 falsch ist?** Julia kauft zuverlässig jeden Monat selbst, spart ≥ A$1.000/Monat, hat einen Horizont von 25+ Jahren und einen hohen Grenzsteuersatz, und die ATO bestätigt die Behandlung als Gesellschaftsanteil. Dann ist VWRA leicht besser.

## 5. Nicht vergessen (größerer Hebel als die ETF-Wahl)
Als Citizen mit Langfrist-Horizont ist **Super** der größte Steuerhebel: 15 % statt 32 % auf Salary-Sacrifice-Beiträge bis zum Concessional Cap (A$32.500 in 2026–27 inkl. Arbeitgeberbeitrag). Dazu kommt die Super-Anlageoption: Default-Optionen sind oft „Balanced“ mit nennenswertem Anleiheanteil (Annahme, prüfen). Nächster Schritt: Super-Check (annahmen.md #7).
