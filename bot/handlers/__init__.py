from aiogram import Dispatcher
from sqlalchemy.ext.asyncio import async_sessionmaker


def setup_routers(dp: Dispatcher, session_pool: async_sessionmaker) -> None:
    from . import start
    dp.include_router(start.router)

    from . import balance
    dp.include_router(balance.router)

    from . import replenish
    dp.include_router(replenish.router)
