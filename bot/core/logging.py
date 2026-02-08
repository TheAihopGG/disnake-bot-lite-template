from logging import basicConfig

from core.config import LOGGING_LEVEL


def configure_logging():
    """
    Настраивает логгирование
    """
    basicConfig(level=LOGGING_LEVEL)


__all__ = ("configure_logging",)
