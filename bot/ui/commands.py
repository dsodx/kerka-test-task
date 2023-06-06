from typing import List

from aiogram import Bot
from aiogram.types import BotCommand


def get_default_commands() -> List[BotCommand]:
    return [
        BotCommand(command="start", description="Перезапустить бота"),
        BotCommand(command="my_balance", description="Посмотреть свой баланс")
    ]


async def setup_default_commands(bot: Bot) -> None:
    await bot.set_my_commands(get_default_commands())
