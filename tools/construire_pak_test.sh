#!/usr/bin/env bash
# Nuclear Nightmare French fan localization - local TEST-only builder.
# Read-only towards game files; produces a separate patch under ./dist-test.
set -euo pipefail
HERE="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
SOURCE_ARCHIVE="${1:-$HOME/NuclearNightmare_Traduction.tar.gz}"
if [[ ! -f "$SOURCE_ARCHIVE" ]]; then
  printf 'Archive source introuvable : %s\n' "$SOURCE_ARCHIVE" >&2
  printf 'Indiquez son chemin : bash construire_pak_test.sh /chemin/NuclearNightmare_Traduction.tar.gz\n' >&2
  exit 1
fi
if ! command -v python3 >/dev/null; then echo 'python3 manquant' >&2; exit 1; fi
REPAK=""
if command -v repak >/dev/null 2>&1; then REPAK="$(command -v repak)"; fi
if [[ -z "$REPAK" ]]; then
  REPAK="$(find "$HOME/.local/opt/repak" -maxdepth 5 -type f \( -name repak -o -name repak_cli \) -print -quit 2>/dev/null || true)"
fi
if [[ -z "$REPAK" ]]; then
  echo "Outil 'repak' introuvable. Installez l'outil de la première étape." >&2
  exit 1
fi
chmod +x "$REPAK" 2>/dev/null || true
WORK="$(mktemp -d)"
trap 'rm -rf "$WORK"' EXIT
STAGE="$WORK/NN-FR-stage"
ROOT="$HERE"
if [[ -d "$HERE/../translations" ]]; then ROOT="$(cd "$HERE/.." && pwd)"; fi
OUT="$ROOT/dist-test"
if [[ -d "$ROOT/translations" ]]; then
  CSV="$ROOT/translations/NuclearNightmare_traduction_FR.csv"
  RU_OVERRIDES="$ROOT/translations/NuclearNightmare_traduction_RU_overrides.csv"
else
  CSV="$HERE/NuclearNightmare_traduction_FR.csv"
  RU_OVERRIDES="$HERE/NuclearNightmare_traduction_RU_overrides.csv"
fi
TARGET="$STAGE/NuclearNightmare/Content/Localization/Game/ru/Game.locres"
mkdir -p "$(dirname "$TARGET")" "$WORK/paks" "$OUT"
python3 "$HERE/construire_fr_locres.py" "$SOURCE_ARCHIVE" \
  "$CSV" "$TARGET" \
  --ru-overrides "$RU_OVERRIDES"
# The original archive is V11 with path hash seed 0x42459304 = 1111855876.
"$REPAK" pack "$STAGE" "$WORK/paks" \
  --version V11 --path-hash-seed 1111855876 --mount-point '../../../'
PAK="$WORK/paks/NN-FR-stage.pak"
if [[ ! -s "$PAK" ]]; then echo 'Archive PAK non produite' >&2; exit 1; fi
PATCH="$OUT/NuclearNightmare-FR_P.pak"
cp "$PAK" "$PATCH"
"$REPAK" list "$PATCH" | grep -Fx 'NuclearNightmare/Content/Localization/Game/ru/Game.locres' >/dev/null
"$REPAK" get "$PATCH" 'NuclearNightmare/Content/Localization/Game/ru/Game.locres' > "$WORK/check.locres"
cmp "$TARGET" "$WORK/check.locres"
python3 - "$OUT" <<'PY'
from pathlib import Path
import hashlib,sys,zipfile
out=Path(sys.argv[1]);pak=out/'NuclearNightmare-FR_P.pak'
z=out/'NuclearNightmare-FR-TEST.zip'
with zipfile.ZipFile(z,'w',zipfile.ZIP_DEFLATED,9) as f:
    f.write(pak,'NuclearNightmare/Content/Paks/NuclearNightmare-FR_P.pak')
(out/'SHA256SUMS.txt').write_text(f'{hashlib.sha256(z.read_bytes()).hexdigest()}  {z.name}\n')
print(f'ZIP de test créé : {z}')
print('Pas encore validé dans le jeu. À activer en sélectionnant Russe dans le menu de langue.')
PY