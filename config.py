import os

from pydantic import BaseSettings


class Settings(BaseSettings):
    bot_token: str
    admins: list[int]
    debug: bool = False

    db_host: str = "localhost"
    db_port: int = 27017
    db_username: str = ""
    db_password: str = ""
    db_database: str = "myidbot"

    i18n_domain: str = "myidbot"
    i18n_localedir = os.path.join(os.path.dirname(__file__), "locales")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
