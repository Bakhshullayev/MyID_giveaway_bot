from aiogram import types

from keyboards.inline import language_btn
from loader import dp


@dp.message_handler(commands=['start'], state='*')
async def start_cmd(msg: types.Message):
    text = (
        "Выберите язык"
        "Tilni tanlang"
        "Тилни танланг"
    )
    await msg.answer(text, reply_markup=language_btn)
