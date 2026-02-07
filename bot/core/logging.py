from logging import basicConfig, StreamHandler, FileHandler

from core.config import LOGGING_FILENAME, LOGGING_LEVEL


def configure_logging():
    """
    Настраивает логгирование
    """
    basicConfig(
        level=LOGGING_LEVEL,
        handlers=(
            StreamHandler(),
            FileHandler(LOGGING_FILENAME, mode="w"),
        ),
    )


__all__ = ("configure_logging",)
