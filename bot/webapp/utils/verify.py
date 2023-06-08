from aiogram.utils.web_app import safe_parse_webapp_init_data
from aiohttp.web import Request

from ...config import Settings


async def verify_init_data(request: Request) -> bool:
    token: str = request.app.get("bot_token")
    init_data: str = (await request.json()).get("initData", "")
    config: Settings = request.app.get("config")
    try:
        init_data_unsafe = safe_parse_webapp_init_data(token=token, init_data=init_data)
        return init_data_unsafe.user.id in config.admin_ids
    except ValueError:
        return False
