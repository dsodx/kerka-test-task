from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo


def get_admin_kb(url: str) -> InlineKeyboardMarkup:
    """
    Получить клавиатуру с веб-приложением панели управления
    :param url: url-адрес веб-приложения
    :return: объект клавиатуры
    """
    webapp = WebAppInfo(url=url)
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Control Panel", web_app=webapp)]
    ])
    return kb
