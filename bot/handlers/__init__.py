from aiogram import Dispatcher


def setup_routers(dp: Dispatcher) -> None:
    from . import start
    dp.include_router(start.router)
