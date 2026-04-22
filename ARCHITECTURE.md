# Architecture

## Overview

Flapjack is a research data platform for genetic circuit and assay workflows. The codebase contains:

- `flapjack_api`: Django/Channels backend (system of record and business logic)
- `flapjack_frontend`: React frontend
- `docker-compose.yml`: local orchestration for backend, frontend, PostgreSQL, and Redis

## Runtime boundaries

- **Primary durable store**: PostgreSQL (registry/auth/domain data)
- **Ephemeral coordination**: Redis (Channels transport)
- **Client**: React (REST + websocket consumer)
- **Backend**: Django REST Framework + Channels (API + websocket orchestration)

## Security and persistence baseline

- No hardcoded secrets in committed runtime config.
- Environment variables drive Django secrets, DB config, hosts, and CORS.
- Production should run with managed PostgreSQL + automated encrypted backups + PITR.
- Redis is non-authoritative (losing Redis must not lose operational data).
- Local Docker Compose is development-only and not production hardening by itself.

## Data placement model

- **PostgreSQL**: users, auth relations, studies, assays, samples, vectors, strains, media, signals, measurements.
- **Redis**: websocket channel-layer state and short-lived coordination.
- **Object storage (target for scale)**: large uploaded/raw assay files and binary artifacts; DB stores references/metadata.

## Operational expectations

- `healthz` endpoint checks DB and Redis reachability.
- Migrations are the schema evolution path.
- Backup and restore must be tested and documented.
- Separate dev/staging/prod env configuration is required.
