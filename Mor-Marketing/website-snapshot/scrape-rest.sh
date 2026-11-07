#!/usr/bin/env bash
# Lädt die Dateien nach, die scrape.sh wegen Leerzeichen/& im Namen verpasst hat.
cd ~/Desktop/mor-marketing.com-2026-11-07/media || exit 1
rm -f "PIRLOS&amp;MIXDELI.mov"
BASE="https://www.mor-marketing.com"
while IFS='|' read -r file url; do
  echo "Datei: $file"
  curl -sSL "$BASE/$url" -o "$file" || echo "  FEHLER: $file"
done <<'LIST'
MIX DELI.jpg|MIX%20DELI.jpg
MIX DELI.mp4|MIX%20DELI.mp4
PIRLOS&MIXDELI.mov|PIRLOS%26MIXDELI.mov
RIADA CONCEPT.mp4|RIADA%20CONCEPT.mp4
RIADA CONCEPT(1).mp4|RIADA%20CONCEPT(1).mp4
RIADA CONCEPT(2).mp4|RIADA%20CONCEPT(2).mp4
Updated image for Mix Deli slide.jpg|Updated%20image%20for%20Mix%20Deli%20slide.jpg
site.webm|site.webm
LIST
echo; echo "Fertig. Prüfung (Dateityp):"
file "MIX DELI.jpg" "MIX DELI.mp4" "PIRLOS&MIXDELI.mov" RIADA* "Updated image for Mix Deli slide.jpg" site.webm
