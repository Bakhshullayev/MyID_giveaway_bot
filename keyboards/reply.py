from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from middlewares import i18n

_ = i18n.lazy_gettext

contact_btn = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="Contact", request_contact=True)]],
    resize_keyboard=True,
    one_time_keyboard=True,
)

age_btn = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(_("18 yoshgacha")),
        ],
        [
            KeyboardButton(_("18 yoshdan 25 yoshgacha")),
        ],
        [
            KeyboardButton(_("26 yoshdan 35 yoshgacha")),
        ],
        [KeyboardButton(_("35 yoshdan katta"))],
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)
