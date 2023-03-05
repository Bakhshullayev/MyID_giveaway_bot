from aiogram.dispatcher.filters.state import StatesGroup, State


class Form(StatesGroup):
    phoneNumber = State()
    instagramUsername = State()
    age = State()
    idea = State()
    ideaDescription = State()
    ideaAboutBot = State()
