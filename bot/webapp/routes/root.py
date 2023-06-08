from pathlib import Path

from aiohttp.web import Request, FileResponse

path = Path(__file__).parent.parent.parent.parent.resolve() / "static" / "index.html"


async def root_handler(_: Request) -> FileResponse:
    return FileResponse(path)
