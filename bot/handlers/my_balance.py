from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from sqlalchemy.ext.asyncio import AsyncSession

from ..db import get_user_balance

router = Router()


@router.message(Command("my_balance"))
async def confirm(message: Message, session: AsyncSession) -> None:
    """
    Отправить пользователю его текущий баланс
    :param message: объект сообщения
    :param session: объект сессии
    :return:
    """
    balance = await get_user_balance(session, user_id=message.from_user.id)
    await message.answer(f"Ваш баланс: <b>{balance}\u20BD</b>")
