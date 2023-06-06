from aiogram.types import InlineKeyboardMarkup, LabeledPrice
from aiogram.utils.keyboard import InlineKeyboardBuilder
from typing import List


def get_rep_balance_kb() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(text="Пополнить баланс", callback_data="rep_balance")
    return builder.as_markup()


def get_prices(amount: int) -> List[LabeledPrice]:
    return [
        LabeledPrice(label="Сумма пополнения", amount=amount)
    ]
