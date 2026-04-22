#!/usr/bin/env bash
set -euo pipefail

if [[ ! -f .env ]]; then
  echo "Missing .env file. Copy .env.example to .env and set values." >&2
  exit 1
fi

source .env

BACKUP_DIR=${BACKUP_DIR:-./backups}
mkdir -p "$BACKUP_DIR"
STAMP=$(date -u +%Y%m%dT%H%M%SZ)
OUT_FILE="$BACKUP_DIR/flapjack_${POSTGRES_DB}_${STAMP}.dump"

echo "Creating PostgreSQL backup at $OUT_FILE"
docker compose exec -T db pg_dump -U "$POSTGRES_USER" -d "$POSTGRES_DB" -Fc > "$OUT_FILE"

echo "Backup complete: $OUT_FILE"
