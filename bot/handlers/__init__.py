from aiogram import Dispatcher
from sqlalchemy.ext.asyncio import async_sessionmaker

from ..middlewares import SessionMiddleware


def setup_routers(dp: Dispatcher, session_pool: async_sessionmaker) -> None:
    session_m = SessionMiddleware(session_pool=session_pool)

    from . import start
    start.router.message.middleware(session_m)
    dp.include_router(start.router)

    from . import balance
    dp.include_router(balance.router)

    from . import replenish
    replenish.router.message.middleware(session_m)
    dp.include_router(replenish.router)

    from . import my_balance
    my_balance.router.message.middleware(session_m)
    dp.include_router(my_balance.router)

    from . import admin
    dp.include_router(admin.router)
