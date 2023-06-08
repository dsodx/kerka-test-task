from aiohttp.web import Request, json_response, Response
from sqlalchemy.ext.asyncio import async_sessionmaker

from ..utils import verify_init_data
from ...db import get_all_users


async def get_users(request: Request) -> Response:
    """
    Получить список пользователей из бд
    :param request: объект запроса
    :return: объект json-ответа
    """
    users = None
    if await verify_init_data(request):
        session_pool: async_sessionmaker = request.app.get("session_pool")
        async with session_pool() as session:
            users = await get_all_users(session)
    return json_response({
        "users": users
    })
