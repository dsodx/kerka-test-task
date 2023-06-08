from aiohttp.web import Application, AppRunner, TCPSite
from sqlalchemy.ext.asyncio import async_sessionmaker

from .routes import setup_routers
from ..config import Settings


async def setup_webapp(session_pool: async_sessionmaker, bot_token: str, config: Settings) -> None:
    """
    Настройка веб-приложения
    :param session_pool: объект пула сессий
    :param bot_token: токен бота
    :param config: объект настроек бота
    :return:
    """
    app = Application()
    app["session_pool"] = session_pool
    app["bot_token"] = bot_token
    app["config"] = config
    setup_routers(app=app)

    runner = AppRunner(app)
    await runner.setup()
    site = TCPSite(runner, host=config.webapp.host, port=config.webapp.port)
    await site.start()
