"""App settings, read from the .env file or environment variables."""

from pydantic import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """BeeWell settings.

    Values come from ``.env`` locally and from environment variables on Railway.
    """

    model_config = SettingsConfigDict(env_file=".env")
    log_level: str = "INFO"
    debug: bool = False

settings = Settings()
