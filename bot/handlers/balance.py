from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

from ..ui import get_prices
from ..config import Settings

router = Router()


class RepBalance(StatesGroup):
    input_amount = State()


@router.callback_query(F.data == "replenish_balance")
async def start_cmd(callback: CallbackQuery, state: FSMContext) -> None:
    await callback.message.answer("Введите сумму, на которую вы хотите пополнить баланс (min 100 RUB)")
    await callback.answer()
    await state.set_state(RepBalance.input_amount)


@router.message(RepBalance.input_amount, F.text.cast(int)[F >= 100].as_("amount"))
async def input_amount(message: Message, state: FSMContext, amount: int, config: Settings) -> None:
    await state.clear()
    await message.answer(f"Сумма пополнения: {amount}\u20BD")
    await message.answer_invoice(
        title="Пополнение баланса",
        description="Пополнение баланса",
        payload="_",
        provider_token=config.provider_token.get_secret_value(),
        currency="RUB",
        prices=get_prices(amount*100),
        start_parameter="_",
        need_name=True,
    )


@router.message(RepBalance.input_amount)
async def incorrect_input_amount(message: Message) -> None:
    await message.answer("Некорректная сумма пополнения")
