from aiohttp.web import Request, json_response, Response

from ..utils import verify_init_data
from ...config import Settings


async def verify_data(request: Request) -> Response:
    token: str = request.app.get("bot_token")
    init_data: str = (await request.json()).get("initData", "")
    config: Settings = request.app.get("config")
    res = verify_init_data(token=token, init_data=init_data, config=config)
    return json_response({
        "ok": res
    })
