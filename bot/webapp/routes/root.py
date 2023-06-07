from aiohttp.web import Request, FileResponse
from pathlib import Path

path = Path(__file__).parent.parent.parent.parent.resolve() / "static" / "index.html"


async def root_handler(request: Request) -> FileResponse:
    return FileResponse(path)
