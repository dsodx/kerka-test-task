from typing import Callable, Dict, Any, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, Update
from sqlalchemy.ext.asyncio import async_sessionmaker

from ..db import is_user_banned


class BanMiddleware(BaseMiddleware):
    def __init__(self, session_pool: async_sessionmaker):
        """
        Инициализация
        :param session_pool: объект пула сессий
        """
        self.session_pool = session_pool

    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: Update,
            data: Dict[str, Any]
    ) -> Any:
        """
        Проверить, заблокирован ли пользователь
        :param handler: объект обработчика событий
        :param event: объект события
        :param data: объект данных события
        :return: результат работы обработчика событий ИЛИ None, если он не был вызван
        """
        if hasattr(event.event, "from_user"):
            async with self.session_pool() as session:
                is_banned = await is_user_banned(session, user_id=event.event.from_user.id)
            if is_banned:
                return
        return await handler(event, data)
