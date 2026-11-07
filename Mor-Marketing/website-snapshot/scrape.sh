#!/usr/bin/env bash
# Komplette Kopie von mor-marketing.com (HTML + Bilder + Videos) – nur mit curl, läuft auf macOS ohne Installation.
# Aufruf:  bash scrape.sh   → legt den Ordner ./mor-marketing.com-<Datum> an
set -euo pipefail
BASE="https://www.mor-marketing.com"
OUT="mor-marketing.com-$(date +%Y-%m-%d)"
mkdir -p "$OUT/pages" "$OUT/media"
PAGES="/ /contact /legal-notice /privacy-policy
/services/content-creation /services/social-media-campaigns /services/event-launch-coverage
/services/hospitality-venue-content /services/fashion-campaign-shoots /services/editing-post-production
/work/badlambs /work/mix-deli /work/poke-mix /work/554 /work/pirlos-pizza /work/riada-concept"
for p in $PAGES; do
  name=$(echo "$p" | sed 's#^/##; s#/#_#g'); [ -z "$name" ] && name="index"
  echo "Seite: $p"
  curl -sSL "$BASE$p" -o "$OUT/pages/$name.html"
done
# Alle Medien-Pfade aus dem HTML ziehen (auch mit Leerzeichen/& im Namen)
grep -ohE '/[^"\\<>]*\.(jpe?g|png|webp|gif|svg|ico|mp4|mov|webm)' "$OUT"/pages/*.html \
  | sed 's/&amp;/\&/g' | grep -v '_next' | sed -E "s#^/#$BASE/#" | sort -u > "$OUT/asset-urls.txt"
while read -r u; do
  path=$(echo "${u#$BASE/}" | sed 's/?.*//')
  mkdir -p "$OUT/media/$(dirname "$path")"
  echo "Datei: $path"
  enc="${u// /%20}"; enc="${enc//&/%26}"
  curl -sSL "$enc" -o "$OUT/media/$path" || echo "  FEHLER: $u"
done < "$OUT/asset-urls.txt"
echo; echo "Fertig: $OUT  ($(du -sh "$OUT" | cut -f1))"
