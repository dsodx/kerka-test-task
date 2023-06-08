from aiogram.filters import Filter
from aiogram.types import Message

from ..config import Settings


class IsAdminFilter(Filter):
    def __init__(self, is_admin: bool) -> None:
        self.is_admin = is_admin

    async def __call__(self, message: Message, config: Settings) -> bool:
        return (message.from_user.id in config.admin_ids) == self.is_admin
