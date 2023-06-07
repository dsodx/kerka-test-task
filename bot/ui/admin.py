from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo


def get_admin_kb(url: str) -> InlineKeyboardMarkup:
    webapp = WebAppInfo(url=url)
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Control Panel", web_app=webapp)]
    ])
    return kb
