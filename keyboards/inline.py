from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

language_cb = CallbackData("language", "code")

language_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Ўзбек", callback_data=language_cb.new(code="uz_Cyrl")
            ),
            InlineKeyboardButton(
                text="Русский", callback_data=language_cb.new(code="ru")
            ),
            InlineKeyboardButton(
                text="O'zbek", callback_data=language_cb.new(code="uz")
            ),
        ]
    ]
)
