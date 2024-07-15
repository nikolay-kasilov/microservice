from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    CORE_HOST: str
    CORE_PORT: int

    class Config:
        env_file = "../.env"
        case_sensitive = True
        env_file_encoding = "utf-8"


settings = Settings()
