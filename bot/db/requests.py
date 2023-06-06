from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from .models import User


async def add_new_user(session: AsyncSession, /, user_id: int) -> None:
    user = await session.scalar(select(User).where(User.id == user_id))
    if user is None:
        user = User(id=user_id)
        session.add(user)


async def update_user_balance(session: AsyncSession, /, user_id: int, inc: int) -> None:
    user = await session.scalar(select(User).where(User.id == user_id))
    user.balance += inc


async def get_user_balance(session: AsyncSession, /, user_id: int) -> float:
    balance = await session.scalar(select(User.balance).where(User.id == user_id))
    return balance / 100
