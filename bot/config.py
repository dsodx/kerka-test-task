from pydantic import BaseSettings, SecretStr, RedisDsn, PostgresDsn, HttpUrl


class Settings(BaseSettings):
    bot_token: SecretStr
    provider_token: SecretStr
    redis_dsn: RedisDsn
    postgres_dsn: PostgresDsn
    webapp_url: HttpUrl

    class Config:
        env_file = ".env"


config = Settings()
