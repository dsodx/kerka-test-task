from pydantic import BaseSettings, SecretStr, RedisDsn, PostgresDsn, HttpUrl, BaseModel


class WebApp(BaseModel):
    host: str
    port: int
    url: HttpUrl


class Settings(BaseSettings):
    bot_token: SecretStr
    provider_token: SecretStr

    redis_dsn: RedisDsn
    postgres_dsn: PostgresDsn

    webapp: WebApp
    admin_ids_raw: str

    @property
    def admin_ids(self) -> tuple:
        return tuple(map(int, self.admin_ids_raw.split(",")))

    class Config:
        # env_file = ".env"
        env_nested_delimiter = "_"


config = Settings()
