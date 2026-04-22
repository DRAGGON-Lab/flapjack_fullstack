#!/usr/bin/env bash
set -euo pipefail

if [[ $# -ne 1 ]]; then
  echo "Usage: $0 <path-to-backup.dump>" >&2
  exit 1
fi

if [[ ! -f .env ]]; then
  echo "Missing .env file. Copy .env.example to .env and set values." >&2
  exit 1
fi

source .env

BACKUP_FILE=$1
if [[ ! -f "$BACKUP_FILE" ]]; then
  echo "Backup file does not exist: $BACKUP_FILE" >&2
  exit 1
fi

echo "Restoring $BACKUP_FILE into database '$POSTGRES_DB'"
cat "$BACKUP_FILE" | docker compose exec -T db pg_restore -U "$POSTGRES_USER" -d "$POSTGRES_DB" --clean --if-exists --no-owner

echo "Restore complete."
