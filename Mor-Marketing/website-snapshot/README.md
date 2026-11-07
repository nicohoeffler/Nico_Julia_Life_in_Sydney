# Website-Snapshot mor-marketing.com

- [site-inventory.md](site-inventory.md): Struktur aller 16 Seiten, Überschriften, Buttons, Medien-URLs und Verbesserungsliste für den Nachbau.
- [scrape.sh](scrape.sh): lädt die komplette Seite herunter, also das HTML aller Seiten und alle Bilder, Videos, CSS- und JS-Dateien. Es braucht nur `curl` und `python3`, beides ist auf macOS vorinstalliert.

## So machst du die Kopie (Mac, Terminal)

```bash
cd ~/Desktop
curl -sSLO https://raw.githubusercontent.com/nicohoeffler/Nico_Julia_Life_in_Sydney/claude/project-thread-xagvgl/Mor-Marketing/website-snapshot/scrape.sh
bash scrape.sh
```

Das Skript legt auf dem Desktop einen Ordner `mor-marketing.com-<Datum>` an, mit `pages/` (HTML) und `media/` (Bilder und Videos). Weil das Repo privat ist, klappt der `curl`-Download des Skripts nur mit Login. Am einfachsten öffnest du `scrape.sh` auf GitHub, kopierst den Inhalt und speicherst ihn auf dem Desktop als `scrape.sh`.

Die Videos sind wahrscheinlich ein paar hundert MB groß. Lade den Ordner nicht ins Repo hoch, er gehört in die Cloud (iCloud oder Google Drive). Ins Repo kommen später nur die optimierten Dateien des Nachbaus.
