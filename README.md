# Flapjack Fullstack

Flapjack Fullstack is the full-stack repository for the Flapjack web application.

- `flapjack_api`: Django + DRF + Channels backend
- `flapjack_frontend`: React frontend
- `docker-compose.yml`: local development orchestration

## Quick architecture

- **Backend framework**: Django 3.0.5 + Django REST Framework + Channels
- **Frontend framework**: React 16 with `react-app-rewired`
- **Primary data store**: PostgreSQL (durable)
- **Ephemeral dependency**: Redis (channel layer)
- **Auth model**: JWT access/refresh tokens via `djangorestframework-simplejwt`

See `ARCHITECTURE.md` and `ADR-001.md` for production persistence direction.

## Local development

### 1) Prepare environment files

Copy placeholders and adjust locally:

```bash
cp .env.example .env
cp flapjack_api/.env.example flapjack_api/.env.dev
cp flapjack_frontend/.env.example flapjack_frontend/.env.dev
```

### 2) Start services

```bash
docker compose up --build
```

### 3) Run migrations

```bash
docker exec -it flap_api bash
./scripts/migrate.sh
```

### 4) Access services

- Frontend: `http://localhost:3000`
- Backend API root: `http://localhost:8000/api/`
- Auth endpoints: `http://localhost:8000/api/auth/`
- Health endpoint: `http://localhost:8000/healthz/`

## Durability and production guidance

The local Compose stack is for development only.

Production baseline:

- managed PostgreSQL for primary relational persistence
- encrypted automated backups + point-in-time recovery
- TLS in transit
- environment-based secret injection only
- separate dev/staging/prod config
- restore drills and migration workflows

## Backup and restore scripts

From inside the backend container (or any host with `pg_dump`/`pg_restore` and env vars set):

```bash
./scripts/backup_postgres.sh /tmp/flapjack_backup.dump
./scripts/restore_postgres.sh /tmp/flapjack_backup.dump
```

Required env vars:

- `DB_HOST`, `DB_PORT`, `DB_NAME`, `DB_USER`, `DB_PASSWORD`

## Important security notes

- Do **not** commit real secrets.
- Do **not** run production with `DJANGO_DEBUG=1`.
- In production, set explicit `DJANGO_ALLOWED_HOSTS` and CORS origins.
- Redis is not an authoritative store.
