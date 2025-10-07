# config.py
from dataclasses import dataclass
from environs import Env

@dataclass
class DatabaseConfig:
    database_url: str

@dataclass
class Config:
    db: DatabaseConfig
    secret_key: str
    debug: bool

def load_config(path = r'F:\Phyton\api_edu\api_project\file.env') -> Config:
    env = Env()
    env.read_env(path)  # Загружаем переменные окружения из файла .env

    return Config(
        db=DatabaseConfig(database_url=env("DATABASE_URL")),
        secret_key=env("SECRET_KEY"),
        debug=env.bool("DEBUG", default=False)
    )