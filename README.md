# Flapjack Fullstack

Flapjack Fullstack is the deployment and development repository for the Flapjack web application: a full-stack system for storing, querying, analyzing, and visualizing genetic circuit and assay data.

This repository brings together:

- `flapjack_api`: Django/Channels backend, REST API, authentication, websocket endpoints
- `flapjack_frontend`: React frontend
- `docker-compose.yml`: local orchestration for frontend, backend, PostgreSQL, and Redis

## Current stack

### Backend
- Python / Django 3.0.x
- Django REST Framework
- Channels + Redis channel layer
- JWT authentication via `djangorestframework-simplejwt`
- Gunicorn + Uvicorn worker for ASGI serving

### Frontend
- React 16
- `react-app-rewired`
- Ant Design
- Redux
- Plotly

### Infrastructure
- Docker Compose
- PostgreSQL 12
- Redis

## Quick start (local development)

### 1) Create environment files

```bash
cp .env.example .env
cp flapjack_frontend/.env.dev.example flapjack_frontend/.env.dev
```

Populate `.env` with local-only secrets and credentials.

### 2) Build and start stack

```bash
docker compose up --build -d
```

### 3) Run migrations

```bash
./scripts/migrate.sh
```

### 4) Verify health

```bash
curl http://localhost:8000/api/healthz/
```

### 5) Access app

- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- Auth endpoints: http://localhost:8000/api/auth/
- Registry endpoints: http://localhost:8000/api/
- Websocket base paths: `/ws/plot`, `/ws/analysis`, `/ws/registry`

## Backup and restore (local runbook)

Create a backup dump:

```bash
./scripts/backup_db.sh
```

Restore from a dump:

```bash
./scripts/restore_db.sh ./backups/<backup-file>.dump
```

## Production posture (required)

This repository is now structured so local development and production expectations are clearly separated.

For production deployments:

- use managed PostgreSQL as the durable system of record
- enable encrypted backups and point-in-time recovery
- provide TLS in transit to app and database endpoints
- inject secrets via environment/secret manager only
- keep Redis as ephemeral infrastructure only
- use object storage for large uploaded artifacts where needed

See `ARCHITECTURE.md` and `ADR-001.md` for the target persistence model.

## Maintainer notes

- Keep changes small and reversible.
- Keep Docker Compose runnable.
- Never commit secrets.
- Use migrations for schema changes.
- Update docs when runtime behavior changes.

## Related projects

- API docs: https://flapjacksynbio.github.io/flapjack_api
- Python client: https://github.com/flapjacksynbio/pyFlapjack
