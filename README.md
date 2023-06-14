# Kerka Test Task

## Setup
1. Fill `.env.dist` with your data and rename it to `.env`
2. Optional. Apply migrations:
```shell
docker compose up -d postgres
docker compose run --rm bot alembic upgrade head
```
3. Run bot:
```shell
docker compose up -d
```

## Stack:
* Docker Compose 2.18
* Python 3.11
* PostgreSQL 15.3
* Redis 7.0
* SQLAlchemy 2
* Aiogram 3
* Alembic
* Asyncpg (as driver)

### I hope you like it =)
