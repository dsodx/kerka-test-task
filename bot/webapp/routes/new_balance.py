from aiohttp.web import Request, json_response, Response
from sqlalchemy.ext.asyncio import async_sessionmaker

from ..utils import verify_init_data
from ...db import update_user_balance


async def new_user_balance(request: Request) -> Response:
    """
    Изменить баланс пользователя в бд
    :param request: объект запроса
    :return: объект json-ответа
    """
    new_balance = None
    if await verify_init_data(request):
        session_pool: async_sessionmaker = request.app.get("session_pool")
        json = await request.json()
        user_id = json.get("userId")
        new_balance = json.get("newBalance")
        async with session_pool() as session:
            new_balance = await update_user_balance(session, user_id=user_id, new_balance=new_balance)
            await session.commit()
    return json_response({
        "new_balance": new_balance
    })
