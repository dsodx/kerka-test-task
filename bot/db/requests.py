from typing import Type, List

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from .models import User


async def add_new_user(session: AsyncSession, /, user_id: int) -> None:
    """
    Добавить пользователя в бд, если его там нет
    :param session: объект сессии
    :param user_id: id пользователя
    :return:
    """
    user = await session.get(User, ident=user_id)
    if user is None:
        user = User(id=user_id)
        session.add(user)


async def get_all_users(session: AsyncSession) -> List[User]:
    """
    Получить всех пользователей из бд
    :param session: объект сессии
    :return: массив пользователей в формате словарей
    """
    users = await session.scalars(select(User).order_by(User.balance.desc()))
    return [user.as_dict() for user in users]


async def update_user_balance_rel(session: AsyncSession, /, user_id: int, inc: int) -> None:
    """
    Обновить баланс пользователя в бд
    :param session: объект сессии
    :param user_id: id пользователя
    :param inc: надбавка баланса
    :return:
    """
    user: Type[User] = await session.get(User, ident=user_id)
    user.balance += inc


async def get_user_balance(session: AsyncSession, /, user_id: int) -> float:
    """
    Получить баланс пользователя из бд
    :param session: объект сессии
    :param user_id: id пользователя
    :return: баланс пользователя
    """
    balance: int = (await session.get(User, ident=user_id)).balance
    return balance / 100


async def is_user_banned(session: AsyncSession, /, user_id: int) -> bool:
    """
    Проверить, заблокирован ли пользователь
    :param session: объект сессии
    :param user_id: id пользователя
    :return: заблокирован ли пользователь
    """
    user = await session.get(User, ident=user_id)
    return False if user is None else user.banned


async def bun_or_unban_user(session: AsyncSession, /, user_id: int) -> bool:
    """
    Изменить статус блокировки пользователя в бд
    :param session: объект сессии
    :param user_id: id пользователя
    :return: статус блокировки пользователя после изменения
    """
    user = await session.get(User, ident=user_id)
    ban = False if user.banned else True
    user.banned = ban
    return ban


async def update_user_balance(session: AsyncSession, /, user_id: int, new_balance: str) -> float:
    """
    Изменить баланс пользователя в бд;
    если строка начинается с "+" или "-", значение изменяется относительно текущего
    :param session: объект сессии
    :param user_id: id пользователя
    :param new_balance: изменения баланса
    :return: новый баланс пользователя
    """
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
