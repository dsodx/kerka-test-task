# Kerka Test Task

### [Don't build from source](https://github.com/dsodx/kerka-test-task/tree/master)

## Setup
1. Fill `.env.dist` with your data and rename it to `.env`
2. Build image:
```shell
docker compose build
```
3. Optional. Apply migrations:
```shell
docker compose up -d postgres
docker compose run --rm bot alembic upgrade head
```
4. Run bot:
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
