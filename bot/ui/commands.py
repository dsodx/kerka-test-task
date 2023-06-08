from typing import List

from aiogram import Bot
from aiogram.types import BotCommand


def get_default_commands() -> List[BotCommand]:
    """
    Получить массив стандартных команд бота
    :return: массив команд бота
    """
    return [
        BotCommand(command="start", description="Перезапустить бота"),
        BotCommand(command="replenish", description="Пополнить баланс"),
        BotCommand(command="my_balance", description="Посмотреть свой баланс")
    ]


async def setup_default_commands(bot: Bot) -> None:
    """
    Применить стандартные команды бота
    :param bot: объект бота
    :return:
    """
    await bot.set_my_commands(get_default_commands())
