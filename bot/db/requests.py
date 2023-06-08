from typing import Type, List

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from .models import User


async def add_new_user(session: AsyncSession, /, user_id: int) -> None:
    user = await session.get(User, ident=user_id)
    if user is None:
        user = User(id=user_id)
        session.add(user)


async def get_all_users(session: AsyncSession) -> List[User]:
    users = await session.scalars(select(User).order_by(User.balance.desc()))
    return [user.as_dict() for user in users]


async def update_user_balance_rel(session: AsyncSession, /, user_id: int, inc: int) -> None:
    user: Type[User] = await session.get(User, ident=user_id)
    user.balance += inc


async def get_user_balance(session: AsyncSession, /, user_id: int) -> float:
    balance: int = (await session.get(User, ident=user_id)).balance
    return balance / 100


async def is_user_banned(session: AsyncSession, /, user_id: int) -> bool:
    user = await session.get(User, ident=user_id)
    return False if user is None else user.banned


async def bun_or_unban_user(session: AsyncSession, /, user_id: int) -> bool:
    user = await session.get(User, ident=user_id)
    ban = False if user.banned else True
    user.banned = ban
    return ban


async def update_user_balance(session: AsyncSession, /, user_id: int, new_balance: str) -> float:
    user = await session.get(User, ident=user_id)
    try:
        float(new_balance)
    except ValueError:
        return user.balance / 100
    if new_balance.startswith("+") or new_balance.startswith("-"):
        user.balance += int(float(new_balance) * 100)
        return user.balance / 100
    else:
        user.balance = int(float(new_balance) * 100)
        return user.balance / 100
