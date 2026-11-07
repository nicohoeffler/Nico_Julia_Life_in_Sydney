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
# Alle Medien- und Asset-Pfade aus dem HTML ziehen (Bilder, Videos, Logos, CSS, JS, Fonts)
grep -hoE '(src|href|poster|srcSet|srcset)="[^"]+"' "$OUT"/pages/*.html \
  | sed -E 's/^[a-zA-Z]+="//; s/"$//' | tr ',' '\n' | awk '{print $1}' \
  | grep -E '\.(jpe?g|png|webp|svg|gif|mp4|mov|webm|ico|css|js|woff2?)(\?|$)' \
  | sed -E "s#^/#$BASE/#" | grep "^$BASE" | sort -u > "$OUT/asset-urls.txt" || true
# Original-Dateien hinter /_next/image?url=... ebenfalls holen
grep -oE '_next/image\?url=[^&"]+' "$OUT"/pages/*.html | sed -E 's#.*url=##' \
  | python3 -c 'import sys,urllib.parse;[print(urllib.parse.unquote(l.strip())) for l in sys.stdin]' \
  | sed -E "s#^/#$BASE/#" | sort -u >> "$OUT/asset-urls.txt"
sort -u -o "$OUT/asset-urls.txt" "$OUT/asset-urls.txt"
while read -r u; do
  [[ "$u" == *"_next/image"* ]] && continue
  path=$(echo "${u#$BASE/}" | sed 's/?.*//')
  mkdir -p "$OUT/media/$(dirname "$path")"
  echo "Datei: $path"
  curl -sSL "${u// /%20}" -o "$OUT/media/$path" || echo "  FEHLER: $u"
done < "$OUT/asset-urls.txt"
echo; echo "Fertig: $OUT  ($(du -sh "$OUT" | cut -f1))"
