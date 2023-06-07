import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.fsm.storage.redis import RedisStorage
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from .config import config
from .handlers import setup_routers
from .ui import setup_default_commands
from .middlewares import BanMiddleware
from .webapp import setup_webapp

logger = logging.getLogger(__name__)


async def setup(*, bot: Bot, dp: Dispatcher, session_pool: async_sessionmaker) -> None:
    await bot.delete_webhook(drop_pending_updates=True)
    await setup_default_commands(bot)
    dp.update.middleware(BanMiddleware(session_pool=session_pool))
    setup_routers(dp=dp, session_pool=session_pool)
    await setup_webapp(session_pool=session_pool, bot_token=bot.token)


async def main() -> None:
    logging.basicConfig(level=logging.INFO)

    engine = create_async_engine(config.postgres_dsn)
    session_pool = async_sessionmaker(engine, expire_on_commit=False)

    bot = Bot(token=config.bot_token.get_secret_value(), parse_mode=ParseMode.HTML)
    storage = RedisStorage.from_url(config.redis_dsn)
    dp = Dispatcher(storage=storage)
    dp["config"] = config

    await setup(bot=bot, dp=dp, session_pool=session_pool)

    logger.warning("Running bot..")
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types()+["pollanswer"])


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (SystemExit, KeyboardInterrupt):
        logger.warning("Bot stopped")
