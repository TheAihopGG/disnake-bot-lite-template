from typing import Any
from os import getenv

from core.errors import EnvironmentVariableIsRequired


def get_env(
    name: str,
    default: Any = None,
    raise_on_none: bool = False,
) -> Any:
    """
    Возвращает значение переменной окружения

    :param default: Значение по умолчанию
    :param raise_on_none: Если истина - вызывает исключение
    :return: Description
    :rtype: Any
    """
    if value := getenv(name, default):
        return value
    else:
        if raise_on_none:
            raise EnvironmentVariableIsRequired(name=name)
        return None


__all__ = ("get_env",)
