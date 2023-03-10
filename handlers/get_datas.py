from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.reply import age_btn
from loader import dp, bot
from middlewares import i18n
from utils.database import db
from utils.states import Form
import re

_ = i18n.lazy_gettext
instagram_pattern = re.compile(r"^@(?!.*\.\.)(?!.*\.$)[^\W][\w.]{0,29}$")


@dp.message_handler(content_types=["contact"], state=Form.phoneNumber)
async def get_phone_number(msg: types.Message, state: FSMContext):
    await state.update_data(phoneNumber=msg.contact.phone_number)
    text = _(
        "Tanlovning barcha shartlari bajarilganligini tekshirish uchun Instagramdagi nikneymingizni yozib qoldiring (masalan: @username)"
    )
    await msg.answer(text, reply_markup=types.ReplyKeyboardMarkup())
    await Form.instagramUsername.set()


@dp.message_handler(state=Form.instagramUsername)
async def get_instagram_username(msg: types.Message, state: FSMContext):
    await state.update_data(instagramUsername=msg.text)
    ins_username = instagram_pattern.match(msg.text)
    if ins_username is None:
        text = _(
            "Tanlovning barcha shartlari bajarilganligini tekshirish uchun Instagramdagi nikneymingizni yozib qoldiring (masalan: @username)"
        )
        await msg.answer(text)
        return
    text = _("Yoshingizni kiriting")
    await msg.answer(text, reply_markup=age_btn)
    return await Form.age.set()


@dp.message_handler(state=Form.age)
async def get_age(msg: types.Message, state: FSMContext):
    await state.update_data(age=msg.text)
    text = _("Sizning fikr-mulohazangiz")

    await msg.answer(text, reply_markup=types.ReplyKeyboardMarkup())
    await Form.idea.set()


@dp.message_handler(state=Form.idea)
async def get_age(msg: types.Message, state: FSMContext):
    await state.update_data(idea=msg.text)
    text = _("Fikr-mulohazangizni batafsil ifodalab bering")
    await msg.answer(text)
    await Form.ideaAboutBot.set()


@dp.message_handler(state=Form.ideaAboutBot)
async def get_age(msg: types.Message, state: FSMContext):
    await state.update_data(ideaAboutBot=msg.text)
    data = await state.get_data()
    text = _("Javobingiz qabul qilindi! Ishtirok etganingiz uchun rahmat.")
    await msg.answer(text)
    await db.update_info(user_id=msg.from_user.id, data=data)
    text = (
        f"<b>📲 Telefon raqam:</b> {data.get('phoneNumber')}\n"
        f"<b>🪧 Instagram Username:</b> {data.get('instagramUsername')}\n"
        f"<b>⌛️ Yosh:</b> {data.get('age')}\n"
        f"<b>💭 Fikr-mulohaza:</b> {data.get('idea')}\n"
        f"<b>🤖 Batafsil xulosa:</b> {data.get('ideaAboutBot')}\n"
    )
    await bot.send_message(chat_id="-1001705998442", text=text)
    await state.finish()
