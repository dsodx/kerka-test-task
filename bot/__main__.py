import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.fsm.storage.redis import RedisStorage

from .config import config
from .handlers import setup_routers

logger = logging.getLogger(__name__)


async def setup(dp: Dispatcher) -> None:
    setup_routers(dp)


async def main() -> None:
    logging.basicConfig(level=logging.INFO)

    bot = Bot(token=config.bot_token.get_secret_value(), parse_mode=ParseMode.HTML)
    storage = RedisStorage.from_url(config.redis_dsn)
    dp = Dispatcher(storage=storage)
    dp["config"] = config

    await setup(dp=dp)

    logger.warning("Running bot..")
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (SystemExit, KeyboardInterrupt):
        logger.warning("Bot stopped")
