from pydantic import BaseSettings, SecretStr, RedisDsn, PostgresDsn, HttpUrl


class Settings(BaseSettings):
    bot_token: SecretStr
    provider_token: SecretStr

    redis_dsn: RedisDsn
    postgres_dsn: PostgresDsn

    webapp_host: str
    webapp_port: int
    webapp_url: HttpUrl

    admin_ids_raw: str

    @property
    def admin_ids(self) -> tuple:
        return tuple(map(int, self.admin_ids_raw.split(",")))

    class Config:
        env_file = ".env"


config = Settings()
