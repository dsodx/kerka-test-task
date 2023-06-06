from aiogram import Router, html
from aiogram.filters import CommandStart
from aiogram.types import Message

router = Router()


@router.message(CommandStart())
async def start_cmd(message: Message) -> None:
    await message.answer(f"Привет, {html.quote(message.from_user.full_name)}!")
    await message.answer("Я - бот для пополнения баланса.\n"
                         "Нажмите на кнопку, чтобы пополнить баланс.")
