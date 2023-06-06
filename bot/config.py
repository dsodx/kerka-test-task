from pydantic import BaseSettings, SecretStr, RedisDsn, PostgresDsn


class Settings(BaseSettings):
    bot_token: SecretStr
    provider_token: SecretStr
    redis_dsn: RedisDsn
    postgres_dsn: PostgresDsn

    class Config:
        env_file = ".env"


config = Settings()
