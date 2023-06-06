from pydantic import BaseSettings, SecretStr, RedisDsn


class Settings(BaseSettings):
    bot_token: SecretStr
    redis_dsn: RedisDsn

    class Config:
        env_file = ".env"


config = Settings()
