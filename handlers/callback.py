from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from keyboards.custom_keyboards import learning_keyboard, shuffle
from middlewares.throttling import rate_limit
from misc.functions import get_new_question


@rate_limit(limit=3)
async def next_verb(callback: types.CallbackQuery):

    previous_question_index = int(callback.data.split('-')[1])
    year = callback.data.split('-')[2]

    question_index, question, options, answer = get_new_question(year, previous_question_index)

    await callback.answer()
    await callback.bot.send_poll(chat_id=callback.message.chat.id,
                                 question=question,
                                 options=options,
                                 type=types.PollType.QUIZ,
                                 correct_option_id=options.index(answer),
                                 reply_markup=learning_keyboard(question_index, year))


@rate_limit(limit=3)
async def shuffle_verb(callback: types.CallbackQuery):

    year = callback.data.split('-')[2]

    question_index, question, options, answer = get_new_question(year, shuffle=True)

    await callback.answer()
    await callback.bot.send_poll(chat_id=callback.message.chat.id,
                                 question=question,
                                 options=options,
                                 type=types.PollType.QUIZ,
                                 correct_option_id=options.index(answer),
                                 reply_markup=learning_keyboard(question_index, year))


@rate_limit(limit=3)
async def all_years(callback: types.CallbackQuery):

    question_index, question, options, answer = get_new_question(shuffle=True)

    await callback.answer()
    await callback.bot.send_poll(chat_id=callback.message.chat.id,
                                 question=question,
                                 options=options,
                                 type=types.PollType.QUIZ,
                                 correct_option_id=options.index(answer),
                                 reply_markup=shuffle(question_index))


@rate_limit(limit=3)
async def choice_year(callback: types.CallbackQuery):
    year = callback.data.split('-')[1]

    question_index, question, options, answer = get_new_question(year, shuffle=True)

    await callback.answer()
    await callback.bot.send_poll(chat_id=callback.message.chat.id,
                                 question=question,
                                 options=options,
                                 type=types.PollType.QUIZ,
                                 correct_option_id=options.index(answer),
                                 reply_markup=learning_keyboard(question_index, year))


def register_callback_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(next_verb, Text(startswith='next'))
    dp.register_callback_query_handler(shuffle_verb, Text(startswith='shuffle'))
    dp.register_callback_query_handler(all_years, Text(startswith='all'))
    dp.register_callback_query_handler(choice_year, Text(startswith='year'))
