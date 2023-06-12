from aiohttp.web import Request, json_response, Response

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
            f.seek(0, 2)
            f.seek(max(-10240, -f.tell()), 2)
            logs = f.read().decode("utf-8")
    return json_response({
        "logs": logs
    })
