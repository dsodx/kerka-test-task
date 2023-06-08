from aiohttp.web import Application, AppRunner,TCPSite
from sqlalchemy.ext.asyncio import async_sessionmaker
from .routes import setup_routers


async def setup_webapp(session_pool: async_sessionmaker, bot_token: str) -> None:
    app = Application()
    app["session_pool"] = session_pool
    app["bot_token"] = bot_token
    setup_routers(app=app)

    runner = AppRunner(app)
    await runner.setup()
    site = TCPSite(runner, host="localhost", port=80)
    await site.start()
