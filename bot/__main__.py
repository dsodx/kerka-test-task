import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode

logger = logging.getLogger(__name__)


async def main() -> None:
    logging.basicConfig(level=logging.INFO)

    bot = Bot(token=..., parse_mode=ParseMode.HTML)
    dp = Dispatcher()

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
