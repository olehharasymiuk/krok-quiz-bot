import random

from aiogram import Dispatcher, types

from database import questions
# from bot import config
# from bot.database.models.goods import Order
# from bot.misc.functions import work_with_product
from keyboards.custom_keyboards import learning_keyboard


# from bot.middlewares.throttling import rate_limit
# from bot.misc.pars import Shop, Product
#
# from bot.data.texts import HELP_COMMAND


# @rate_limit(limit=3)
async def start_command(message: types.Message):

    question_index = str(random.randint(1, len(questions)))
    question_onj = questions[question_index]

    options = question_onj['options']
    if options:
        random.shuffle(options)  # Список варіантів для опитування


    question = question_onj['question']  # Питання опитування
    answer = question_onj['answer']
    if len(question) >= 300:
        question = question[:295] + '...'


    poll = types.Poll(question=question, type=types.PollType.QUIZ, correct_option_id=options.index(answer))
    await message.bot.send_poll(chat_id=message.chat.id, question=poll.question, options=options, type=poll.type,
                        correct_option_id=poll.correct_option_id, reply_markup=learning_keyboard(question_index))


def register_user_handlers(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=['start'])
