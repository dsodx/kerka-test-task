from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import CallbackQuery, Message

from ..config import Settings
from ..ui import get_prices

router = Router()


class RepBalance(StatesGroup):
    input_amount = State()


@router.message(Command("replenish"))
@router.callback_query(F.data == "replenish_balance")
async def start_cmd(callback: CallbackQuery, state: FSMContext) -> None:
    # сумма должна быть от $1 до $10**4; я чуть округлил =)
    # https://core.telegram.org/bots/payments#supported-currencies
    await callback.message.answer("Введите сумму, на которую вы хотите пополнить баланс\n\n"
                                  "Сумма должна быть от 100 до 75000\u20BD\n"
                                  "в формате: <code>x[.yy]</code>, "
                                  "где <code>x</code> - рубли, а <code>yy</code> - копейки")
    await callback.answer()
    await state.set_state(RepBalance.input_amount)


@router.message(RepBalance.input_amount, F.text.cast(float)[100 <= F <= 75_000].as_("amount"))
async def input_amount(message: Message, state: FSMContext, amount: float, config: Settings) -> None:
    await state.clear()
    await message.answer_invoice(
        title="Пополнить баланс",
        description=f"Сумма пополнения: {amount}\u20BD",
        payload="_",  # не используется
        provider_token=config.provider_token.get_secret_value(),
        currency="RUB",
        prices=get_prices(int(amount * 100)),
        start_parameter="_",  # для того чтобы нельзя было оплатить из других чатов
        need_name=True,
    )


@router.message(RepBalance.input_amount)
async def incorrect_input_amount(message: Message) -> None:
    await message.answer("Некорректная сумма пополнения")
