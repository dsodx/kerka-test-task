from aiohttp.web import Application


def setup_routers(app: Application) -> None:
    from .root import root_handler
    app.router.add_get("/", root_handler)

    from .verify import verify_data
    app.router.add_post("/verifyInitData", verify_data)

    from .get_users import get_users
    app.router.add_post("/getUsers", get_users)

    from .ban_user import edit_banned_field
    app.router.add_post("/editBanField", edit_banned_field)

    from .new_balance import new_user_balance
    app.router.add_post("/editBalanceField", new_user_balance)

    from .get_logs import get_logs
    app.router.add_post("/getLogs", get_logs)
