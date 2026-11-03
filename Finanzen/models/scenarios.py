"""Szenario-Rechner: Welt-ETF für eine australische Steuerinländerin.

Vergleicht
  A) VWRA (Vanguard FTSE All-World UCITS, thesaurierend, Irland) über CMC Invest
  B) BGBL (Betashares Global Shares, ausschüttend, AU-Trust) über Betashares Direct / CMC
  C) BGBL 88 % + BEMG 12 % (Schwellenländer ergänzt, ≈ FTSE All-World ex AU)

Annahmen (Quellen: docs/research/2026-11-03_*.md). Alles AUD, nominal.
- Gleiche Bruttorendite r für alle Produkte (Indexunterschiede ignoriert).
- AU-ETF: jährliche Ausschüttung d, voll zum Grenzsteuersatz t versteuert, Quellensteuer
  wird als Foreign Income Tax Offset angerechnet (kein Verlust). Netto reinvestiert.
- VWRA: keine Ausschüttung, keine laufende AU-Steuer (Behandlung als Aktie einer ausländischen
  Gesellschaft, siehe Research-Notiz, Konfidenz ~75 %). Dafür Quellensteuer-Leckage im Fonds
  und FX-Spread beim Kauf und beim Verkauf.
- Verkauf am Ende komplett, CGT mit 50 % Discount (Haltedauer > 12 Monate).
- Keine Steuerpflicht-Effekte von Franking (keine AU-Aktien im Vergleich).

Nutzung: python3 models/scenarios.py
"""
from dataclasses import dataclass


@dataclass
class Product:
    name: str
    fee: float            # laufende Kosten p.a.
    dist_yield: float     # jährliche steuerpflichtige Ausschüttung (Anteil am Wert)
    leak: float = 0.0     # nicht anrechenbare Quellensteuer p.a. (Anteil am Wert)
    fx: float = 0.0       # FX-Spread je Kauf und Verkauf


def simulate(p: Product, monthly: float, years: int, r: float, t: float,
             t_exit: float | None = None, lump: float = 0.0, lump_months: int = 1):
    """Gibt (Endwert brutto, Netto nach Exit-CGT, eingezahlt, laufend gezahlte Steuer) zurück.

    lump wird gleichmäßig über lump_months Monate (ab Monat 1) zusätzlich investiert.
    """
    t_exit = t if t_exit is None else t_exit
    g_m = (1 + r - p.fee - p.leak) ** (1 / 12) - 1
    v = base = paid = tax_running = 0.0
    for m in range(1, years * 12 + 1):
        c = monthly + (lump / lump_months if m <= lump_months else 0.0)
        paid += c
        v += c * (1 - p.fx)
        base += c
        v *= 1 + g_m
        if m % 12 == 0 and p.dist_yield:
            d = p.dist_yield * v
            tax = t * d
            v -= tax                  # Ausschüttung minus Steuer wird reinvestiert
            base += d - tax
            tax_running += tax
    sale = v * (1 - p.fx)
    cgt = max(sale - base, 0) * 0.5 * t_exit
    return v, sale - cgt, paid, tax_running


VWRA = Product("VWRA via CMC", fee=0.0014, dist_yield=0.0, leak=0.0015, fx=0.006)
BGBL = Product("BGBL", fee=0.0008, dist_yield=0.012)
# BEMG schüttet nicht aus (thesaurierender irischer Swap-UCITS darunter), daher nur BGBL-Anteil ausschüttend.
# Quellensteuer-Leckage im BEMG-Anteil (keine FITO): 12 % x ~0,25 % = 0,03 % p. a. (Annahme).
BGBL_EM = Product("BGBL 88 % + BEMG 12 %", fee=0.88 * 0.0008 + 0.12 * 0.0035,
                  dist_yield=0.88 * 0.012, leak=0.0003)
VWRA_WORST = Product("VWRA, falls ATO laufend besteuert", fee=0.0014, dist_yield=0.015,
                     leak=0.0015, fx=0.006)


def table(monthly=1000, lump=0.0, lump_months=1, rates=(0.07, 0.05), t=0.32, t_exit=None):
    print(f"\nSparrate A${monthly:,.0f}/Monat, Einmalbetrag A${lump:,.0f} über {lump_months} Mon., "
          f"Grenzsteuer {t:.0%} (inkl. Medicare), Exit-Steuer {(t_exit or t):.0%}")
    for r in rates:
        print(f"  Bruttorendite {r:.1%} p.a.")
        for years in (10, 20, 30):
            row = []
            for p in (BGBL, BGBL_EM, VWRA, VWRA_WORST):
                _, net, paid, _ = simulate(p, monthly, years, r, t, t_exit, lump, lump_months)
                row.append(f"{p.name}: {net:>11,.0f}")
            print(f"    {years} J (eingezahlt {paid:,.0f}): " + " | ".join(row))


if __name__ == "__main__":
    table(t=0.32)                      # 30 % + 2 % Medicare
    table(t=0.39)                      # 37 % + 2 %
    table(t=0.32, t_exit=0.18)         # Verkauf in der Rente bei niedrigerem Satz
    table(monthly=500, lump=50_000, lump_months=12, rates=(0.07,), t=0.32)
