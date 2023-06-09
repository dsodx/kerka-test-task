from aiohttp.web import Request, json_response, Response

from ..utils import verify_init_data


async def verify_data(request: Request) -> Response:
    """
    Верифицировать данные из веб-приложения при старте
    :param request: объект запроса
    :return: объект json-ответа
    """
    res = await verify_init_data(request)
    return json_response({
        "ok": res
    })
