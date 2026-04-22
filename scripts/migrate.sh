#!/usr/bin/env bash
set -euo pipefail

if [[ ! -f .env ]]; then
  echo "Missing .env file. Copy .env.example to .env and set values." >&2
  exit 1
fi

source .env

docker compose run --rm flapjack_api python manage.py migrate
