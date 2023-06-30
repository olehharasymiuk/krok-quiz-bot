
from aiogram import Dispatcher, types

from keyboards.custom_keyboards import years_keyboard, shuffle
from middlewares.throttling import rate_limit
from misc.functions import get_new_question


@rate_limit(limit=3)
async def start_command(message: types.Message):

    await message.answer('Вибери рік', reply_markup=years_keyboard())


@rate_limit(limit=3)
async def all_tests(message: types.Message):

    question_index, question, options, answer = get_new_question(shuffle=True)

    await message.bot.send_poll(chat_id=message.chat.id,
                                question=question,
                                options=options,
                                type=types.PollType.QUIZ,
                                correct_option_id=options.index(answer),
                                reply_markup=shuffle(question_index))


def register_user_handlers(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=['start'])
    dp.register_message_handler(all_tests, commands=['all'])
