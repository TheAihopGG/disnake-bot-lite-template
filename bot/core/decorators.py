from logging import getLogger
from psycopg import DatabaseError
from typing import Callable, Awaitable
from functools import wraps

from core.database import connect_to_db

logger = getLogger(__name__)


def create_db_conn[**P, R](rollback_on_error: bool = True) -> Callable[
    [Callable[P, Awaitable[R]]],
    Callable[P, Awaitable[R]],
]:
    """
    Создаёт объект-подключение к базе данных и передаёт его в асинхронную функцию первым аргументом

    > @create_db_conn()
    > async def my_func(db_conn: AsyncConnection, ...) -> ...: # Аргумент для параметра db_conn будет подставлен автоматически
    >   ...

    :param rollback_on_error: Если истина, то при вызове исключения `DatabaseError` транзакция будет отменена
    :type rollback_on_error: bool
    :return: Возвращает декоратор
    :rtype: Callable[[Callable[P, Awaitable[R]]], Callable[P, Awaitable[R]]]
    """

    def inner(
        func: Callable[P, Awaitable[R]],
    ) -> Callable[P, Awaitable[R]]:
        @wraps(func)
        async def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            db_conn = await connect_to_db()
            try:
                result = await func(*args, **kwargs, db_conn=db_conn)
            except DatabaseError:
                if rollback_on_error:
                    await db_conn.rollback()
                logger.exception("Ошибка при выполнении запроса в базу данных")
            else:
                await db_conn.commit()
                return result
            finally:
                await db_conn.close()

        return wrapper

    return inner


__all__ = ("create_db_conn",)
