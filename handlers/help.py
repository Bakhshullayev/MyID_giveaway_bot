from aiogram import types

from middlewares import i18n

_ = i18n.lazy_gettext

from loader import dp


@dp.message_handler(commands=["help"], state="*")
async def start_cmd(msg: types.Message):
    text = _("Bu bot nima bera oladi? \"MyID texnologiyasini biznesda qo‘llash\" mavzusidagi tanlov haqida fikringizni yozib qoldiring")
    await msg.answer(text)
