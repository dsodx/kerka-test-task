from aiogram.utils.web_app import safe_parse_webapp_init_data

from ...config import Settings


def verify_init_data(token: str, init_data: str, config: Settings) -> bool:
    try:
        init_data_unsafe = safe_parse_webapp_init_data(token=token, init_data=init_data)
        return init_data_unsafe.user.id in config.admin_ids
    except ValueError:
        return False
