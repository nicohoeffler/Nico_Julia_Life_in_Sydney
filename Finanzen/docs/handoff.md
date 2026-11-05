# Übergabe: Finanzen & ETF-Sparplan für meine Freundin (Australien)

> **Für Claude Code:** Diese Datei ist der Startkontext für ein neues Finanz-Projekt. Lies sie vollständig, bevor du irgendetwas empfiehlst. Sie stammt aus einer Vorbereitung in claude.ai (Stand: 3. Nov 2026). Alles unter „Recherche-Stand“ ist **vor jeder Empfehlung erneut zu verifizieren**, weil sich Broker-Konditionen, Fondskosten und Steuerregeln ändern.
> Empfehlung: Inhalt von Abschnitt 1–3 und 9 als `CLAUDE.md` ins Repo-Root übernehmen, den Rest als `docs/handoff.md` ablegen.

---

## 1. Wer ich bin und wie du mit mir arbeitest

- Nico, BWL-Student (Goethe-Uni Frankfurt), Hintergrund Private Markets / Deal Advisory, selbst aktiver (systematischer) Trader. Ich verstehe Fachbegriffe, **meine Freundin nicht unbedingt**.
- Ich lebe aktuell (seit Okt 2026) ebenfalls in Sydney, in ca. 3-Monats-Blöcken.
- Arbeitsstil: kritisch, direkt, faktenbasiert. **Gib bei Einschätzungen immer eine Wahrscheinlichkeit/Konfidenz in % an.** Prüf Rechnungen Schritt für Schritt, hinterfrag meine Annahmen, keine unkritische Bestätigung.
- Ich bin kein Finanzberater und du auch nicht: Ergebnisse sind Entscheidungsgrundlagen. Bei Steuerfragen mit echter Tragweite → Hinweis auf australischen Tax Agent.

## 2. Ziel des Projekts

Ein **Finanz-Arbeitsbereich** für mich und die Menschen, denen ich helfe. Erster Fall: meine Freundin.

Was sie (laut mir) will:
1. **In den Weltmarkt investieren**, so einfach wie möglich (ein breiter Welt-ETF, z. B. MSCI World / FTSE All-World-Logik).
2. **Langfristiger Vermögensaufbau / Altersvorsorge.**
3. Möglichst **wenig laufende Steuer, lange nicht liquidieren** (meine ursprüngliche Idee: thesaurierende ETFs, siehe aber Abschnitt 4.2, das funktioniert in Australien anders).
4. Sie hat **ein größeres Erspartes**. Das soll **gestaffelt (monatlich) investiert** werden, um den Einstiegszeitpunkt zu streuen.
5. Ich hätte gern Trade Republic / Scalable Capital genutzt. **Das geht sehr wahrscheinlich nicht** (siehe 4.1).

Liefergegenstände am Ende (wie beim Projekt mit meiner Mutter):
- Ein **verständliches PDF** für sie (kein Fachjargon, Lexikon, ehrliche Szenarien inkl. Worst Case).
- Eine **kurze Präsentation** (pptx) für ein gemeinsames Gespräch.
- Ein **Setup-Plan**: Broker, ETF(s), Betrag/Monat, Dauer der Staffelung, Notgroschen, Super-Strategie.
- Optional: ein kleines Python-Szenario-Modell (siehe 7), das ich wiederverwenden kann.

## 3. Was wir über sie wissen und was nicht

**Bekannt:**
- Lebt in **Sydney, Australien**, ist dort (sehr wahrscheinlich) steuerlich ansässig.
- Wir sind seit ca. 6 Jahren zusammen.
- Größeres Erspartes vorhanden (Betrag noch offen).

**Unbekannt. Vor jeder Empfehlung klären (Fragenliste für mich):**

| # | Frage | Warum entscheidend |
|---|---|---|
| 1 | Staatsbürgerschaft / Aufenthaltsstatus (Citizen, PR, temporäres Visum?) | Bei temporärem Visum wird Super beim Wegzug über DASP hoch besteuert; das ändert die Super-vs-ETF-Abwägung komplett |
| 2 | Alter, Job, Bruttoeinkommen (Steuerstufe) | Marginaler Steuersatz bestimmt, wie attraktiv Super-Einzahlungen (15 %) vs. privates Depot sind |
| 3 | Höhe des Ersparten, wo liegt es, zu welchem Zins | Basis für Staffelplan und Notgroschen |
| 4 | Monatliche Sparrate aus dem Gehalt | Laufender Sparplan zusätzlich zur Staffelung |
| 5 | Notgroschen-Bedarf (3–6 Monatsausgaben) | Wird *nicht* investiert |
| 6 | Pläne in den nächsten 5 Jahren: Wohnungskauf? Umzug nach Deutschland/Europa? | Geld mit < 5 J. Horizont gehört nicht in Aktien; Wohnungskauf → First Home Super Saver Scheme prüfen; Umzug → Broker/Steuer-Folgen beim Wegzug |
| 7 | Bestehender Super-Fonds, Kontostand, Anlageoption, Gebühren | Oft der größte, am meisten vernachlässigte Hebel |
| 8 | Schulden (HECS-HELP, Kreditkarte)? | Hochverzinste Schulden zuerst |
| 9 | Risikogefühl: Wie reagiert sie auf −30 % im Depot? | Bestimmt Aktienquote und Staffeldauer |
| 10 | Hat sie noch Konten/Depots in Europa? | Melde- und Wohnsitzpflichten bei EU-Brokern |

## 4. Recherche-Stand (3. Nov 2026), vor Nutzung verifizieren

### 4.1 Trade Republic / Scalable Capital: nicht nutzbar bei Wohnsitz Australien (Konfidenz ~90 %)
- Trade Republic verlangt **ständigen Wohnsitz und unbeschränkte Steuerpflicht in einem unterstützten (europäischen) Land**. Australien gehört nicht dazu. Quelle: Trade-Republic-Support „Why do I have to be a permanent resident…“, kreditkarte24.de, finanzfluss.de.
- Scalable Capital: gleiche Logik (nur ausgewählte EU-Länder). **Noch nicht separat verifiziert, bitte prüfen.**
- Falsche Wohnsitzangabe ist **keine Option** (KYC/Steuermeldung CRS, Kontokündigung möglich).
- **Nebenpunkt für mich selbst:** Wenn ich langfristig in Australien bleibe, kann das meinen eigenen TR-Account und meine Steueransässigkeit betreffen. Separat prüfen.

### 4.2 „Thesaurierend = Steuer aufschieben“ ist ein deutsches Konzept und lässt sich nicht 1:1 übertragen (Konfidenz ~80 %)
- In Deutschland greift selbst bei thesaurierenden ETFs die **Vorabpauschale**. Der Aufschub ist also nur teilweise.
- **Australisch domizilierte ETFs (ASX) schütten Erträge praktisch immer aus** (steuerliche Zurechnung an die Anleger). Wiederanlage läuft über **DRP (Dividend Reinvestment Plan)**, steuerpflichtig ist es trotzdem.
- **Irische thesaurierende UCITS-ETFs** (z. B. VWCE/IWDA) für australische Steuerinländer: steuerliche Behandlung **nicht eindeutig geklärt**, in der ATO-Community kontrovers diskutiert, Aufwand bei der Steuererklärung höher. Eine Branchenstudie (HKEX ETF Tax Report 2019) kommt zu dem Schluss, dass **australische Fonds für australische Anleger in der Regel das steuereffizienteste Vehikel** sind. → Default: **ASX-gelistete, australisch domizilierte ETFs**.
- **Das echte australische Steuer-Aufschub-Vehikel ist Superannuation**: Erträge im Fonds mit max. 15 % besteuert, Concessional Contributions (Salary Sacrifice) mit 15 % statt Grenzsteuersatz, dafür gebunden bis zum Preservation Age. → Aufgabe: Super-Optimierung (Anlageoption, Gebühren, ggf. Salary Sacrifice) als **eigene Säule** neben dem ETF-Depot prüfen, abhängig von Frage 1 und 2.
- Positiv: **CGT-Discount 50 %** auf Gewinne bei Haltedauer > 12 Monate. Langes Halten wird also auch in AU belohnt.

### 4.3 Broker-Kandidaten in Australien (Konditionen verifizieren)
| Broker | Pro | Contra |
|---|---|---|
| **Betashares Direct** (Finder „Best ETF Investing Platform“ 2025 und 2026) | $0 Brokerage auf alle ASX-ETFs; Auto-invest für DCA; Bruchstücke | Auto-invest nur in **bis zu 5 Betashares-ETFs**, Mindestrate ca. A$100; Verwahrung über Custodian (kein CHESS-HIN auf ihren Namen) |
| Pearler | Auto-invest, CHESS-gesponsert | geringe Gebühren pro Trade (prüfen) |
| Vanguard Personal Investor | Auto-invest in Vanguard-ETFs | Produktpalette auf Vanguard fokussiert |
| CMC Invest | $0 auf ASX-ETF-Trades < A$1.000 | kein echtes Auto-invest (prüfen) |
| Interactive Brokers | global, günstig | komplexer, für sie eher nicht „so easy wie möglich“ |

Tendenz (Konfidenz ~65 %): **Betashares Direct**, wenn ein Betashares-Welt-ETF passt; sonst **Pearler**, wenn CHESS-Sponsorship oder ein Nicht-Betashares-ETF gewünscht ist.

### 4.4 ETF-Kandidaten (Kosten und Indexe verifizieren, Werte aus dem Gedächtnis)
- **One-Ticket inkl. Australien + Schwellenländer:** Betashares **DHHF** (Diversified All Growth), Vanguard **VDHG** (enthält ~10 % Anleihen).
- **Welt ex Australien (ähnlich MSCI World):** Betashares **BGBL**, Vanguard **VGS**, iShares **IWLD**.
- Fragen dazu: Wie viel **Home Bias Australien** (Dividenden mit Franking Credits sind für AU-Steuerinländer steuerlich attraktiv)? Schwellenländer ja/nein? Währungsabsicherung (hedged/unhedged)? Default-Vorschlag: unhedged, globale Aktien inkl. eines Australien-Anteils. Am einfachsten ist ein einziges One-Ticket-ETF.

### 4.5 Gestaffelter Einstieg (DCA) vs. Einmalanlage
- Historisch schlägt die Einmalanlage das gestaffelte Investieren in ca. **2 von 3 Fällen** (Vanguard-Studien; Konfidenz ~80 %). DCA ist vor allem eine **Verhaltens-Absicherung** gegen Reue nach einem schlechten Einstieg.
- Vorschlag zum Diskutieren: **Staffelung über 6–12 Monate**, nicht länger. Notgroschen vorher abziehen, Geld bis zur Investition im Hochzins-Sparkonto parken.

## 5. Lessons Learned aus dem Projekt mit meiner Mutter (Okt 2026)

Was gut funktioniert hat:
- **PDF zum ruhigen Lesen + kurze Präsentation** fürs Gespräch, persönlicher Ton („Liebe …“), Lexikon für Fachbegriffe.
- **Alle Annahmen explizit** und mit „?“ markieren; zu jeder Annahme eine Rückfrage.
- **Zwei Rechnungen** (realistisch + vorsichtig) und ein **Crash-Test** (−30 % im 1. Jahr). Den ehrlichen Worst Case zeigen, auch wenn er das eigene Argument schwächt. Das schafft Vertrauen.
- Modell „Töpfe nach Zeithorizont“ (Sicherheit / planbar / Wachstum) war sehr verständlich.

Was du vermeiden sollst:
- Keine ungeprüften Marktzahlen in Dokumente für sie (ich habe z. B. Renditen und Verluste falsch im Kopf gehabt). **Zahlen nur mit Quelle oder als Annahme gekennzeichnet.**
- Keine Rendite-Erwartungen aus den letzten Boom-Jahren ableiten. Langfristig ca. 6,5–7 % nominal für globale Aktien als Annahme, mit Minusjahren.
- Ängste oder Bedenken nicht wegargumentieren. Vorsicht als legitimen Teil des Plans einbauen.
- Für meine Freundin passt aber ein **anderes Profil** als bei Mama: jung, langer Horizont, Aufbauphase statt Entnahmephase. Also Fokus auf Sparquote, Kosten, Super, Disziplin; keine Entnahmeplanung.

## 6. Arbeitsweise in diesem Repo

- Sprache der Dokumente für sie: **[Deutsch oder Englisch: klären, Default Englisch, weil sie in Australien lebt?]**
- Währungen: AUD für ihren Fall.
- Jede Empfehlung mit: Begründung, Alternativen, Konfidenz in %, „was müsste stimmen, damit das falsch ist“.
- Aktuelle Fakten (Gebühren, MER, Steuerregeln, Super-Caps) **immer per Websuche verifizieren** und mit Quelle + Datum notieren.

## 7. Vorgeschlagene Repo-Struktur

```
finanzen/
├── CLAUDE.md                 # Abschnitte 1–3 + 9 dieser Datei
├── docs/
│   ├── handoff.md            # diese Datei
│   └── research/             # Recherche-Notizen mit Quelle + Datum
├── people/
│   ├── freundin/
│   │   ├── profil.md         # Ziele, Horizont, Risikoprofil (KEINE TFN/Kontonummern)
│   │   ├── annahmen.md       # alle Annahmen mit Status: offen / bestätigt
│   │   └── outputs/          # PDF, pptx
│   └── mama/                 # später: Projekt Mutter hierher migrieren
├── models/
│   └── scenarios.py          # Sparplan-/Szenario-Rechner (DCA, Sparrate, Crash-Test, Super vs. Depot)
└── data/                     # Kontoauszüge, Exporte → in .gitignore!
```

## 8. Erste Aufgaben (in dieser Reihenfolge)

1. Repo-Struktur anlegen, `.gitignore` für `data/`, `CLAUDE.md` aus dieser Datei erzeugen.
2. **Fragenliste aus Abschnitt 3** als `people/freundin/annahmen.md` anlegen. Ich fülle sie mit ihr aus.
3. Recherche verifizieren (Websuche, mit Quellen): Scalable-Wohnsitzregeln; Betashares Direct / Pearler Konditionen; MER und Index von DHHF, BGBL, VGS, IWLD, VDHG; aktuelle Super-Contribution-Caps; DASP-Steuersätze; FHSS-Regeln.
4. `models/scenarios.py`: Einmalanlage vs. 6 vs. 12 Monate Staffelung; Sparrate × 10/20/30 Jahre; realistische und vorsichtige Renditeannahme; Crash-Test; optional Super (15 %) vs. privates Depot (Grenzsteuersatz, 50 % CGT-Discount).
5. Entwurf Setup-Plan (1 Seite): Notgroschen, Broker, ETF, Staffelplan, laufender Sparplan, Super-Check.
6. Danach PDF + pptx für sie (Stil wie bei Mama: einfach, ehrlich, mit Worst Case).

## 9. Guardrails

- **Niemals Orders ausführen** oder Konten eröffnen. Auch wenn Broker-Tools/MCPs (z. B. Interactive Brokers) verbunden sind: nur lesen und analysieren.
- **Keine sensiblen Daten im Repo:** keine Tax File Number, keine Konto-/Kartennummern, keine Passwörter. `data/` bleibt lokal und in `.gitignore`.
- Keine Empfehlung, Wohnsitzangaben bei Brokern zu „umgehen“.
- Bei Steuer- oder Super-Fragen mit großer Tragweite (Visum, Wegzug, Salary Sacrifice nahe den Caps) → ausdrücklich auf einen registrierten australischen Tax Agent / Financial Adviser verweisen.

## 10. Quellen (Stand 3. Nov 2026)

- Trade Republic Support: Wohnsitzanforderung: https://support.traderepublic.com/en-de/701-Why-do-I-have-to-be-a-permanent-resident-to-open-an-account
- Trade Republic Voraussetzungen (Wohnsitz + unbeschränkte Steuerpflicht): https://www.kreditkarte24.de/trade-republic/anleitung-kontoeroeffnung/
- Betashares Direct Brokerage & Auto-invest: https://bd.betashares.com.au/brokerage-free
- Betashares Direct Finder Award 2026: https://www.betashares.com.au/direct/news/finder-awards-best-etf-investing-platform-2026
- Finder: Best ETF platforms Australia 2026: https://www.finder.com.au/share-trading/exchange-traded-funds/best-etf-trading-platforms
- ATO Community: Accumulating overseas ETFs: https://community.ato.gov.au/s/question/a0J9s0000001CXN/p00024500 und https://community.ato.gov.au/s/question/a0JRF000000jLgD2AU/p00273314
- HKEX ETF Tax Report 2019 (Australien): https://www.hkex.com.hk/-/media/HKEX-Market/Products/Securities/Exchange-Traded-Products/Launch/ETF-Tax-Report-2019_Australia.pdf
