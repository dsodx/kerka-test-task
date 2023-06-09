from aiohttp.web import Request, json_response, Response
import os

from ..utils import verify_init_data


async def get_logs(request: Request) -> Response:
    """
    Получить логи ошибок из файла логов
    :param request: объект запроса
    :return: объект json-ответа
    """
    logs = None
    if await verify_init_data(request):
        with open("logs/warn.log", "rb") as f:
            logs = os.system("tail -n 100 logs/warn.log")
    return json_response({
        "logs": logs
    })

