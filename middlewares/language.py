from typing import Any, Tuple, Optional

from aiogram import types
from aiogram.contrib.middlewares.i18n import I18nMiddleware

from config import settings

from utils.database import db


class Localization(I18nMiddleware):
    def __init__(
        self,
        domain: str = settings.i18n_domain,
        path: str = settings.i18n_localedir,
    ):
        super().__init__(domain, path, default="uz")

    async def get_user_locale(self, action: str, args: Tuple[Any]) -> Optional[str]:
        """
        User locale getter
        You can override the method if you want to use different way of
        getting user language.

        :param action: event name
        :param args: event arguments
        :return: locale name or None
        """
        user: Optional[types.User] = types.User.get_current()

        *_, data = args
        language = data["locale"] = await db.language(user_id=user.id)
        return language


i18n = Localization()
