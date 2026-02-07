from psycopg import AsyncConnection

from core.config import DB_CONNINFO


async def connect_to_db() -> AsyncConnection:
    """
    Подключается к базе данных и возвращает объект подключения

    :return: Объект подключения
    :rtype: AsyncConnection[TupleRow]
    """
    return await AsyncConnection.connect(DB_CONNINFO)


__all__ = ("connect_to_db",)
