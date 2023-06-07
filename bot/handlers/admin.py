from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from ..config import Settings
from ..ui import get_admin_kb

router = Router()


@router.message(Command("admin"))
async def start_cmd(message: Message, config: Settings) -> None:
    await message.answer("Here", reply_markup=get_admin_kb(config.webapp_url))
