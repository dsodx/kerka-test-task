# Kerka Test Task

## Setup
1. Fill `.env.dist` with your data and rename it to `.env`
2. To apply migrations, run:
```shell
docker compose up -d postgres
docker compose run --rm --no-deps bot alembic upgrade head
```
3. Run bot:
```shell
docker compose up -d
```
4. Optional. Start tunnel:
```shell
ssh -R 80:localhost:8080  # set ports to custom
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
