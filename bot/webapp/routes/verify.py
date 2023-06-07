from aiogram.utils.web_app import check_webapp_signature
from aiohttp.web import Request, json_response, Response


async def verify_init_data(request: Request) -> Response:
    token = request.app.get("bot_token")
    init_data: str = (await request.json()).get("initData", "")
    res = check_webapp_signature(token=token, init_data=init_data)
    return json_response({
        "ok": res
    })
