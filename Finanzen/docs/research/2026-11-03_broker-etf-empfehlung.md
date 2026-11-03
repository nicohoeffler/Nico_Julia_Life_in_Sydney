# Broker & ETF für Julia: Empfehlung (Entwurf, Stand 3.11.2026)

Nicos Vorgabe (3.11.2026): „ganz normal breiter ETF wie Vanguard FTSE All-World Accumulating. Ein Produkt monatlich bespart, fertig.“ Julia ist bei ANZ.
Fakten und Quellen: [2026-11-03_verifikation.md](2026-11-03_verifikation.md).

## Kurzfassung

Die richtige Antwort hängt an **einer** Frage: **Bleibt Julia dauerhaft in Australien, oder ist eine Rückkehr nach Europa realistisch, und welches Visum hat sie?** (annahmen.md #1, #6)

| Szenario | Empfehlung | Konfidenz |
|---|---|---|
| **A. Bleibt dauerhaft in AU** (Citizen/PR, Rückkehr < 25 %) | **Betashares Direct + ein ETF per Auto-invest**: DHHF (wenn ok mit ~37 % Australien) oder BGBL (wenn „Welt wie MSCI World“, 0,08 %) | 70 % |
| **B. Temporäres Visum und/oder Rückkehr wahrscheinlich** | Der FTSE-All-World-UCITS-ETF als **VWRA** (USD, London) über **CMC Invest** ($0 Brokerage auf LSE) oder IBKR, monatlich manuell gekauft. Vorher Tax Agent | 55 % |

ANZ selbst fällt weg: **ANZ Share Investing wurde 2023 geschlossen** und zu CMC Invest migriert. ANZ bleibt das Konto, von dem der Dauerauftrag läuft.

## Warum VWCE in Australien nicht automatisch „perfekt“ ist

VWCE ist für einen deutschen Anleger fast ideal. Für eine australische Steuerinländerin kippen drei Punkte:

1. **Zugang:** Kein australischer App-Broker bietet Auto-invest in irische UCITS-ETFs. VWCE handelt an Xetra (bei CMC $59 bzw. 0,59 % pro Order). Praktikabel ist nur die USD-Linie **VWRA** an der LSE (CMC: $0 Brokerage, aber FX-Spread bei jedem Kauf). „Monatlich, fertig“ wird dann zu „monatlich selbst kaufen“. (Konfidenz 75 %; Auto-invest bei IBKR nicht verifiziert.)
2. **Steuer unklar:** Keine ATO-Aussage zu thesaurierenden irischen ETFs gefunden; die ATO-Community-Threads haben keine offizielle Antwort. Meine Hypothese: Ein irischer ETF in Gesellschaftsform wird wie Aktien einer ausländischen Gesellschaft behandelt, also keine jährliche Steuer auf thesaurierte Erträge (die FIF-Regeln wurden 2010 abgeschafft) und beim Verkauf CGT mit 50 % Discount. Das wäre sogar **echter Steueraufschub**. Konfidenz nur ~55 %; Anti-Avoidance-Regeln und Spezialregeln (z. B. Foreign Accumulation Fund für anleihenlastige Fonds) habe ich nicht geprüft. **Ohne Tax Agent nicht umsetzen.**
3. **Steuerliche Reibung:** Die 15 % US-Quellensteuer bleibt im irischen Fonds hängen und ist nicht anrechenbar; bei ASX-ETFs wie BGBL/VGS fließt sie als Foreign Income Tax Offset durch. Bei ca. 1,5–2 % Dividendenrendite sind das grob 0,2–0,3 % p. a. Nachteil für VWCE (Annahme, nicht gerechnet). Dazu kommen keine Franking Credits.

**Wann VWCE/VWRA trotzdem gewinnt:** Wenn Julia wahrscheinlich nach Deutschland zurückgeht. ASX-ETFs sind für einen deutschen Steuerinländer später unbequem (Nicht-UCITS: Kauf über EU-Broker meist nicht möglich, Pauschalbesteuerungs-Risiko). Ein UCITS-ETF bleibt einfach weiterführbar. Konfidenz 70 %.

**Zusätzlicher Prüfpunkt für Szenario B:** Wer steuerlich als „temporary resident“ gilt (temporäres Visum, Partner kein AU-Resident), ist auf ausländische Einkünfte und auf Gewinne aus Nicht-australischem-Grundbesitz-Vermögen in AU weitgehend steuerfrei. Falls das auf Julia zutrifft, verschiebt das die gesamte Rechnung. Konfidenz ~60 %, **Tax Agent**.

## Szenario A im Detail: Betashares Direct

- $0 Brokerage, $0 Konto- und Auto-invest-Gebühr; Auto-invest bis zu 5 Betashares-ETFs, Bruchstücke, monatlich.
- Ablauf: ANZ-Dauerauftrag → Betashares Direct Wallet (1–2 Tage vor Ausführung) → Auto-invest kauft.
- Contra: Custodian-Modell (kein CHESS/HIN auf ihren Namen); Übertrag raus kostet bis $9,50 je Wertpapier. Für ein Produkt vertretbar (Konfidenz 75 %).
- Alternative mit CHESS-HIN: Pearler ($6,50 je Kauf → bei z. B. $500/Monat 1,3 % Kaufkosten, also klar schlechter für kleine Raten).

**DHHF vs. BGBL** (beide Betashares, beide auto-invest-fähig):

| | DHHF | BGBL |
|---|---|---|
| Inhalt | AU 37 %, US 41 %, Developed ex-US 15 %, EM 7 % | nur Industrieländer ex-AU, keine EM |
| Kosten | 0,19 % | 0,08 % |
| Nähe zu FTSE All-World | EM ja, aber starkes Australien-Übergewicht | näher an MSCI World, ohne EM und ohne AU |
| Wann sinnvoll | Leben/Rente in AUD, Franking Credits nutzen | „Welt“-Logik wie VWCE gewünscht |

Meine Tendenz für A: **DHHF**, wenn Julia dauerhaft in AU bleibt, weil Ausgaben und Rente in AUD anfallen und Franking Credits steuerlich helfen (60 %). Wenn ihr das Australien-Gewicht zu hoch ist: BGBL (40 %).

## Was müsste stimmen, damit diese Empfehlung falsch ist?
- Betashares ändert Auto-invest/0-$-Modell (Geschäftsmodell lebt von Fondsgebühren; Risiko mittelfristig ~20 %).
- Ein ASX-ETF bildet FTSE All-World ohne Home Bias ab, den ich übersehen habe (~30 %).
- Die ATO bestätigt Steueraufschub für irische Thesaurierer ohne Fallstricke: dann wird B auch für Szenario A interessanter.

## Nächste Schritte
1. Nico klärt mit Julia #1 (Visum), #6 (Rückkehr), #12 (Australien-Anteil ok?).
2. Danach: Setup-Plan (Notgroschen, Staffelung 6–12 Monate, Sparrate) und Szenario-Modell.
