from aiogram import Router, F, html
from aiogram.types import Message, PreCheckoutQuery

router = Router()


@router.pre_checkout_query()
async def confirm(update: PreCheckoutQuery) -> None:
    await update.answer(True)


@router.message(F.successful_payment)
async def success(message: Message):
    payment = message.successful_payment
    await message.answer(f"Успешно зачислено <b>{payment.total_amount / 100}\u20BD</b> "
                         f"на имя <i>{html.quote(payment.order_info.name)}</i>")
