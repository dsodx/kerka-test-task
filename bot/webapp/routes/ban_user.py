from aiohttp.web import Request, json_response, Response
from sqlalchemy.ext.asyncio import async_sessionmaker

from ...db import bun_or_unban_user


async def edit_banned_field(request: Request) -> Response:
    session_pool: async_sessionmaker = request.app.get("session_pool")
    user_id = (await request.json()).get("userId")
    async with session_pool() as session:
        ban = await bun_or_unban_user(session, user_id=user_id)
        await session.commit()
    return json_response({
        "is_banned": ban
    })
