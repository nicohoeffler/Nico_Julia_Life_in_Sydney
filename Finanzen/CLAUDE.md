# CLAUDE.md – Finanzen (Arbeitsbereich für Nico und die Menschen, denen er hilft)

Gilt für alles unter `Finanzen/`. Vollständiger Startkontext: [docs/handoff.md](docs/handoff.md).
Erster Fall: Julia (Nicos Freundin), Sydney. Ordner: [people/julia/](people/julia/).

## 1. Wer Nico ist und wie wir arbeiten
- Nico: BWL-Student (Goethe-Uni Frankfurt), Hintergrund Private Markets / Deal Advisory, aktiver systematischer Trader. Versteht Fachbegriffe; **Julia nicht unbedingt**.
- Nico lebt seit Okt 2026 in Sydney, in ca. 3-Monats-Blöcken.
- Stil: kritisch, direkt, faktenbasiert. **Jede Einschätzung mit Konfidenz in %.** Rechnungen Schritt für Schritt prüfen, Annahmen hinterfragen, keine unkritische Bestätigung.
- Weder Nico noch Claude sind Finanzberater: Ergebnisse sind Entscheidungsgrundlagen. Steuerfragen mit echter Tragweite → registrierter australischer Tax Agent.

## 2. Ziel (Fall Julia)
1. In den Weltmarkt investieren, so einfach wie möglich: **ein** breiter Welt-ETF, monatlich bespart.
2. Langfristiger Vermögensaufbau / Altersvorsorge.
3. Wenig laufende Steuer, lange nicht liquidieren.
4. Größeres Erspartes gestaffelt (monatlich) investieren.
5. Trade Republic / Scalable gehen bei Wohnsitz Australien nicht (verifiziert, siehe `docs/research/`).

Liefergegenstände: verständliches PDF (kein Jargon, Lexikon, ehrliche Szenarien inkl. Worst Case), kurze pptx fürs Gespräch, 1-seitiger Setup-Plan (Broker, ETF, Betrag/Monat, Staffeldauer, Notgroschen, Super), optional `models/scenarios.py`.

## 3. Was wir über Julia wissen
Siehe [people/julia/annahmen.md](people/julia/annahmen.md). Dort steht jede Annahme mit Status `offen` / `bestätigt`. **Nichts als Fakt behandeln, was dort `offen` ist.**

## 4. Arbeitsregeln
- Währung AUD. Dokumentsprache für Julia: **offen** (siehe annahmen.md).
- Jede Empfehlung mit: Begründung, Alternativen, Konfidenz %, „was müsste stimmen, damit das falsch ist“.
- Gebühren, MER, Steuerregeln, Super-Caps **immer per Websuche verifizieren** und mit Quelle + Datum in `docs/research/` notieren. Keine ungeprüften Marktzahlen in Dokumente für Julia; Zahlen nur mit Quelle oder als Annahme markiert.
- Renditeannahme langfristig 6,5–7 % nominal für globale Aktien, mit Minusjahren; nie aus Boom-Jahren ableiten.
- Ängste nicht wegargumentieren; Vorsicht ist Teil des Plans.

## 5. Guardrails
- **Niemals Orders ausführen oder Konten eröffnen**, auch wenn Broker-MCPs (z. B. Interactive Brokers) verbunden sind: nur lesen und analysieren.
- **Keine sensiblen Daten im Repo:** keine Tax File Number, keine Konto-/Kartennummern, keine Passwörter, keine Kontoauszüge. `data/` ist in `.gitignore` und bleibt lokal.
- Keine Empfehlung, Wohnsitzangaben bei Brokern zu „umgehen“.
- Steuer-/Super-Fragen mit großer Tragweite (Visum, Wegzug, Salary Sacrifice nahe den Caps, ausländische ETFs) → ausdrücklich auf registrierten Tax Agent / Financial Adviser verweisen.
