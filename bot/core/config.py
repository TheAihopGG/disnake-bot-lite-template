from typing import Literal
from logging import INFO
from pathlib import Path

from core.utils import get_env


BASE_DIR = Path(__file__).resolve().parent.parent

BOT_TOKEN: str = get_env("BOT_TOKEN", raise_on_none=True)

POSTGRES_PASSWORD: str = get_env("POSTGRES_PASSWORD", raise_on_none=True)
POSTGRES_USERNAME: str = get_env("POSTGRES_USERNAME", raise_on_none=True)
POSTGRES_DB: str = get_env("POSTGRES_DB", raise_on_none=True)

DB_CONNINFO: str = (
    f"postgressql://{POSTGRES_USERNAME}:{POSTGRES_PASSWORD}@postgres:5432/{POSTGRES_DB}"
)

LOGGING_FILENAME = BASE_DIR / "logs.log"
LOGGING_LEVEL: Literal[10, 20, 30, 40, 50] = INFO

__all__ = (
    "BOT_TOKEN",
    "POSTGRES_PASSWORD",
    "POSTGRES_USERNAME",
    "POSTGRES_DB",
    "DB_CONNINFO",
    "LOGGING_FILENAME",
    "LOGGING_LEVEL",
)
