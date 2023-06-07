from typing import Callable, Dict, Any, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, Update
from sqlalchemy.ext.asyncio import async_sessionmaker

from ..db import is_user_banned


class BanMiddleware(BaseMiddleware):
    def __init__(self, session_pool: async_sessionmaker):
        self.session_pool = session_pool

    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: Update,
            data: Dict[str, Any]
    ) -> Any:
        if hasattr(event.event, "from_user"):
            async with self.session_pool() as session:
                is_banned = await is_user_banned(session, user_id=event.event.from_user.id)
            if is_banned:
                return
        return await handler(event, data)
