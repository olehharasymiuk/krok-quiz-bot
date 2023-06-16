from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from keyboards.custom_keyboards import learning_keyboard, shuffle
from misc.functions import get_question_from_special_year, get_question_from_all_years


async def next_verb(callback: types.CallbackQuery):

    previous_question_index = int(callback.data.split('-')[1])
    year = callback.data.split('-')[2]

    question_index, question, options, answer = get_question_from_special_year(year, previous_question_index)

    await callback.answer()
    await callback.bot.send_poll(chat_id=callback.message.chat.id,
                                 question=question,
                                 options=options,
                                 type=types.PollType.QUIZ,
                                 correct_option_id=options.index(answer),
                                 reply_markup=learning_keyboard(question_index, year))


async def shuffle_verb(callback: types.CallbackQuery):

    previous_question_index = int(callback.data.split('-')[1])
    year = callback.data.split('-')[2]

    question_index, question, options, answer = get_question_from_special_year(year, previous_question_index,
                                                                               shuffle=True)

    await callback.answer()
    await callback.bot.send_poll(chat_id=callback.message.chat.id,
                                 question=question,
                                 options=options,
                                 type=types.PollType.QUIZ,
                                 correct_option_id=options.index(answer),
                                 reply_markup=learning_keyboard(question_index, year))


async def all_years(callback: types.CallbackQuery):
    previous_question_index = callback.data.split('-')[1]

    question_index, question, options, answer = get_question_from_all_years(previous_question_index)

    await callback.answer()
    await callback.bot.send_poll(chat_id=callback.message.chat.id,
                                 question=question,
                                 options=options,
                                 type=types.PollType.QUIZ,
                                 correct_option_id=options.index(answer),
                                 reply_markup=shuffle(question_index))


async def choice_year(callback: types.CallbackQuery):
    year = callback.data.split('-')[1]

    question_index, question, options, answer = get_question_from_special_year(year)

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
