from loader import dp
from .language import i18n

from .throttling import ThrottlingMiddleware

if __name__ == "middlewares":
    dp.middleware.setup(ThrottlingMiddleware())
    dp.middleware.setup(i18n)
