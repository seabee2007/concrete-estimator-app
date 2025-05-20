from pydantic import BaseSettings


class Settings(BaseSettings):
    openweather_api_key: str
    class Config:
        env_file = ".env"


def get_settings():
    return Settings()
