from aiogram import Router, F, html
from aiogram.types import Message, PreCheckoutQuery
from sqlalchemy.ext.asyncio import AsyncSession

from ..db import update_user_balance_rel

router = Router()


@router.pre_checkout_query()
async def confirm(update: PreCheckoutQuery) -> None:
    """
    Ответить на запрос перед оформлением заказа (всегда положительно)
    :param update: объект запроса перед оформлением заказа
    :return:
    """
    await update.answer(True)


@router.message(F.successful_payment)
async def success(message: Message, session: AsyncSession) -> None:
    """
    Ответить на успешное пополнение баланса пользователя
    :param message: объект сообщения
    :param session: объект сессии
    :return:
    """
    payment = message.successful_payment
    await update_user_balance_rel(session, user_id=message.from_user.id, inc=payment.total_amount)
    await session.commit()
    await message.answer(f"Успешно зачислено <b>{payment.total_amount / 100}\u20BD</b> "
                         f"на имя <i>{html.quote(payment.order_info.name)}</i>")
