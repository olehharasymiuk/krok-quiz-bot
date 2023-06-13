import random

from aiogram import Dispatcher, types

from database import get_all
# from bot import config
# from bot.database.models.goods import Order
# from bot.misc.functions import work_with_product
from keyboards.custom_keyboards import learning_keyboard, years_keyboard, shuffle


# from bot.middlewares.throttling import rate_limit
# from bot.misc.pars import Shop, Product
#
# from bot.data.texts import HELP_COMMAND


# @rate_limit(limit=3)
async def start_command(message: types.Message):

    await message.answer('Вибери рік', reply_markup=years_keyboard())


async def all_tests(message: types.Message):

    all_years = get_all()
    random_year = random.choice(all_years)
    random_key = random.choice(list(random_year.keys()))

    question_obj = random_year[str(random_key)]

    question = question_obj['question']
    options = question_obj['options']
    answer = question_obj['answer']

    if options:
        random.shuffle(options)

    if len(question) >= 300:
        question = question[:295] + '...'

    poll = types.Poll(question=question,
                      type=types.PollType.QUIZ,
                      correct_option_id=options.index(answer))
    await message.bot.send_poll(chat_id=message.chat.id,
                                question=poll.question,
                                options=options,
                                type=poll.type,
                                correct_option_id=poll.correct_option_id,
                                reply_markup=shuffle(random_key))


def register_user_handlers(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=['start'])
    dp.register_message_handler(all_tests, commands=['all'])
