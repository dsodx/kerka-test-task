from aiohttp.web import Application


def setup_handlers(app: Application) -> None:
    from .root import root_handler
    app.router.add_get("/", root_handler)

    from .verify import verify_init_data
    app.router.add_post("/verifyInitData", verify_init_data)
