import os

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils import executor
from dotenv import load_dotenv
from middlewares import setup_middleware

from utils.set_commands import set_bot_commands
from aiogram.utils.executor import start_webhook
from pathlib import Path

DEPLOY = os.environ.get('DEPLOY', False)
if not DEPLOY:
    load_dotenv(dotenv_path=f'{Path(__file__).parent}/.env')

BOT_TOKEN = str(os.environ.get('BOT_TOKEN'))
ADMIN_ID = os.getenv('ADMIN_ID')

bot = Bot(BOT_TOKEN, parse_mode='HTML')
dp = Dispatcher(bot, storage=MemoryStorage())

WEBHOOK_PORT = 8080

WEBHOOK_HOST = str(os.getenv('WEBHOOK_HOST'))
WEBHOOK_PATH = ''
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"

WEBAPP_HOST = '0.0.0.0'  # or ip
WEBAPP_PORT = int(os.getenv('PORT', 5000))


async def on_startup(_):
    from handlers import register_all_handlers

    if DEPLOY:
        await bot.set_webhook(url=WEBHOOK_URL, drop_pending_updates=True)

    # init_db()
    # scheduler()
    setup_middleware(dp)
    register_all_handlers(dp)

    await set_bot_commands(dp)


async def on_shutdown(_):

    await bot.delete_webhook()
    await dp.storage.close()
    await dp.storage.wait_closed()


def main():

    if DEPLOY:
        start_webhook(
            dispatcher=dp,
            webhook_path=WEBHOOK_PATH,
            on_startup=on_startup,
            on_shutdown=on_shutdown,
            skip_updates=True,
            host=WEBAPP_HOST,
            port=WEBAPP_PORT
        )

    else:
        executor.start_polling(dp, skip_updates=True, on_startup=on_startup)


if __name__ == '__main__':

    main()
