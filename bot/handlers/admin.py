from aiogram import Router, F
from aiogram.enums import ChatType
from aiogram.filters import Command
from aiogram.types import Message

from ..config import Settings
from ..filters import IsAdminFilter
from ..ui import get_admin_kb

router = Router()
router.message.filter(F.chat.type == ChatType.PRIVATE)


@router.message(Command("admin"), IsAdminFilter(is_admin=True))
async def start_cmd(message: Message, config: Settings) -> None:
    await message.answer("Here", reply_markup=get_admin_kb(config.webapp_url))
