from typing import List

from aiogram.types import InlineKeyboardMarkup, LabeledPrice
from aiogram.utils.keyboard import InlineKeyboardBuilder


def get_balance_kb() -> InlineKeyboardMarkup:
    """
    Получить встроенную клавиатуру для пополнения баланса
    :return: объект клавиатуры
    """
    builder = InlineKeyboardBuilder()
    builder.button(text="Пополнить баланс", callback_data="replenish_balance")
    return builder.as_markup()


def get_prices(amount: int) -> List[LabeledPrice]:
    """
    Получить массив цен пополнения баланса
    :param amount: сумма пополнения баланса
    :return: массив цен
    """
    return [
        LabeledPrice(label="Сумма", amount=amount)
    ]
