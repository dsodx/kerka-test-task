import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode

from .config import config
from .handlers import setup_routers

logger = logging.getLogger(__name__)


async def setup(dp: Dispatcher) -> None:
    setup_routers(dp)


async def main() -> None:
    logging.basicConfig(level=logging.INFO)

    bot = Bot(token=config.bot_token.get_secret_value(), parse_mode=ParseMode.HTML)
    dp = Dispatcher()

    await setup(dp=dp)

    logger.warning("Running bot..")
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (SystemExit, KeyboardInterrupt):
        logger.warning("Bot stopped")
