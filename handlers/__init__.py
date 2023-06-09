from aiogram import Dispatcher
from handlers import callback
from handlers import command


def register_all_handlers(dp: Dispatcher):

    handlers = [
        command.register_user_handlers,
        callback.register_callback_handlers,
    ]

    for handler in handlers:
        handler(dp)
