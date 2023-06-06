from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def get_rep_balance_kb() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button("Пополнить баланс", callback_data="rep_balance")
    return builder.as_markup()
