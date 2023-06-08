from aiohttp.web import Application, AppRunner, TCPSite
from sqlalchemy.ext.asyncio import async_sessionmaker

from .routes import setup_routers
from ..config import Settings


async def setup_webapp(session_pool: async_sessionmaker, bot_token: str, config: Settings) -> None:
    app = Application()
    app["session_pool"] = session_pool
    app["bot_token"] = bot_token
    app["config"] = config
    setup_routers(app=app)

    runner = AppRunner(app)
    await runner.setup()
    site = TCPSite(runner, host=config.webapp_host, port=config.webapp_port)
    await site.start()
