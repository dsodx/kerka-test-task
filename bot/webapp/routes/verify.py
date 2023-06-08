from aiohttp.web import Request, json_response, Response

from ..utils import verify_init_data
from ...config import Settings


async def verify_data(request: Request) -> Response:
    res = await verify_init_data(request)
    return json_response({
        "ok": res
    })
