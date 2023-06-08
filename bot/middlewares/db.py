from typing import Callable, Dict, Any, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject
from sqlalchemy.ext.asyncio import async_sessionmaker


class SessionMiddleware(BaseMiddleware):
    def __init__(self, session_pool: async_sessionmaker):
        """
        Инициализация
        :param session_pool: объект пула сессий
        """
        self.session_pool = session_pool

    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any]
    ) -> Any:
        """
        Добавить объект сессии в параметры обработчика событий
        :param handler: объект обработчика событий
        :param event: объект события
        :param data: объект данных события
        :return: результат работы обработчика событий
        """
        async with self.session_pool() as session:
            data["session"] = session
            return await handler(event, data)
