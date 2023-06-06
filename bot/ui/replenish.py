from typing import List

from aiogram.types import InlineKeyboardMarkup, LabeledPrice
from aiogram.utils.keyboard import InlineKeyboardBuilder


def get_balance_kb() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(text="Пополнить баланс", callback_data="replenish_balance")
    return builder.as_markup()


def get_prices(amount: int) -> List[LabeledPrice]:
    return [
        LabeledPrice(label="Сумма", amount=amount)
    ]
