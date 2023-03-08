from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.inline import language_cb, language_btn
from keyboards.reply import contact_btn
from loader import dp
from middlewares import i18n
from utils.database import db
from utils.states import Form

_ = i18n.lazy_gettext


@dp.message_handler(commands=["language"], state="*")
async def language_cmd(msg: types.Message, state: FSMContext):
    await msg.answer(_("Tilni o'zgartirish uchun bosing."), reply_markup=language_btn)
    await state.finish()


@dp.callback_query_handler(language_cb.filter())
@dp.callback_query_handler(language_cb.filter())
@dp.callback_query_handler(language_cb.filter())
async def language(call: types.CallbackQuery, callback_data: dict):
    lang = callback_data.get("code")
    await db.update_info(call.from_user.id, data={"lang": lang})
    await db.language(user_id=call.from_user.id, language=lang)

    await call.message.delete()

    info = await db.user_info(call.from_user.id)

    if not info.get("phoneNumber"):
        text = _("Siz bilan bog’lanish mumkin bo’ladigan raqamni kiriting", locale=lang)
        await call.message.answer(text, reply_markup=contact_btn)
        await Form.phoneNumber.set()
        return
