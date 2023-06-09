from aiogram import Router, html
from aiogram.filters import CommandStart
from aiogram.types import Message
from sqlalchemy.ext.asyncio import AsyncSession

from ..db import add_new_user
from ..ui import get_balance_kb

router = Router()


@router.message(CommandStart())
async def start_cmd(message: Message, session: AsyncSession) -> None:
    """
    Приветственное сообщение;
    добавить пользователя в бд, если его там нет
    :param message: объект сообщения
    :param session: объект сессии
    :return:
    """
    await add_new_user(session, user_id=message.from_user.id)
    await session.commit()
    await message.answer(f"Привет, {html.quote(message.from_user.full_name)}!")
    await message.answer("Я - бот для пополнения баланса.\n"
                         "Нажмите на кнопку, чтобы пополнить баланс.", reply_markup=get_balance_kb())
