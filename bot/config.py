from pydantic import BaseSettings, SecretStr, RedisDsn, PostgresDsn, HttpUrl


class Settings(BaseSettings):
    bot_token: SecretStr
    admin_ids_raw: str
    provider_token: SecretStr
    redis_dsn: RedisDsn
    postgres_dsn: PostgresDsn
    webapp_url: HttpUrl

    @property
    def admin_ids(self) -> tuple:
        return tuple(map(int, self.admin_ids_raw.split(",")))

    class Config:
        env_file = ".env"


config = Settings()
