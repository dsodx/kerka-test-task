from aiohttp.web import Request, json_response, Response
from sqlalchemy.ext.asyncio import async_sessionmaker

from ...db import get_all_users


async def get_users(request: Request) -> Response:
    session_pool: async_sessionmaker = request.app.get("session_pool")
    async with session_pool() as session:
        users = await get_all_users(session)
    return json_response({
        "users": users
    })
