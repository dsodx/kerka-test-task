from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

router = Router()


class RepBalance(StatesGroup):
    input_amount = State()


@router.callback_query(F.data == "rep_balance")
async def start_cmd(callback: CallbackQuery, state: FSMContext) -> None:
    await callback.message.answer("Введите сумму, на которую вы хотите пополнить баланс")
    await callback.answer()
    await state.set_state(RepBalance.input_amount)


@router.message(RepBalance.input_amount, F.text.cast(int)[F >= 1].as_("amount"))
async def input_amount(message: Message, state: FSMContext, amount: int) -> None:
    await state.clear()
    await message.answer(f"Сумма пополнения: {amount}\u20BD")


@router.message(RepBalance.input_amount)
async def incorrect_input_amount(message: Message) -> None:
    await message.answer("Некорректная сумма пополнения")
