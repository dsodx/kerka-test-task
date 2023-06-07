from typing import Type

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from .models import User


async def add_new_user(session: AsyncSession, /, user_id: int) -> None:
    user = await session.get(User, ident=user_id)
    if user is None:
        user = User(id=user_id)
        session.add(user)


async def update_user_balance(session: AsyncSession, /, user_id: int, inc: int) -> None:
    user: Type[User] = await session.get(User, ident=user_id)
    user.balance += inc


async def get_user_balance(session: AsyncSession, /, user_id: int) -> float:
    balance: int = (await session.get(User, ident=user_id)).balance
    return balance / 100
