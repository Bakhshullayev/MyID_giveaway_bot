from aiogram import types

from keyboards.inline import language_btn
from keyboards.reply import contact_btn
from loader import dp
from middlewares import i18n
from utils.database import db
from utils.states import Form

_ = i18n.lazy_gettext


@dp.message_handler(commands=["start"], state="*")
async def start_cmd(msg: types.Message):
    info = await db.user_info(msg.from_user.id)

    if not info.get("lang"):
        text = "🇷🇺 Выберите язык\n" "🇺🇿 Tilni tanlang\n" "🇺🇿 Тилни танланг\n"
        await msg.answer(text, reply_markup=language_btn)
        return

    if not info.get("phoneNumber"):
        text = _("Siz bilan bog’lanish mumkin bo’ladigan raqamni kiriting")
        await msg.answer(text, reply_markup=contact_btn)
        await Form.phoneNumber.set()
        return

    text = _("Siz ro'yxatdan o'tgansiz")
    await msg.answer(text)
