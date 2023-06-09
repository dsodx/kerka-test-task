# Kerka Test Task

## Setup
1. Fill `.env.dist` with your data and rename it to `.env`
2. To build from the source, run:  
```shell
docker compose build
```
3. To apply migrations, run:
```shell
docker compose up -d postgres
docker compose run --rm --no-deps bot alembic upgrade head
```
4. Run bot:
```shell
docker compose up -d
```

## Stack:
* Python 3.11
* PostgreSQL 15
* Redis 7
* SQLAlchemy 2
* Aiogram 3
* Alembic
* Asyncpg (as driver)

### I hope you like it =)
