from aiogram.utils.web_app import safe_parse_webapp_init_data
from aiohttp.web import Request, json_response, Response

from ...config import Settings


async def verify_init_data(request: Request) -> Response:
    token: str = request.app.get("bot_token")
    config: Settings = request.app.get("config")
    init_data: str = (await request.json()).get("initData", "")
    try:
        init_data_unsafe = safe_parse_webapp_init_data(token=token, init_data=init_data)
        res = init_data_unsafe.user.id in config.admin_ids
    except ValueError:
        res = False
    return json_response({
        "ok": res
    })
