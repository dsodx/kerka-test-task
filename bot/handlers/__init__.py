from aiogram import Dispatcher


def setup_routers(dp: Dispatcher) -> None:
    from . import start
    dp.include_router(start.router)

    from . import balance
    dp.include_router(balance.router)

    from . import replenish
    dp.include_router(replenish.router)
