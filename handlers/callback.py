import random

from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text

from database import get_year, get_all
from keyboards.custom_keyboards import learning_keyboard, shuffle


async def next_verb(callback: types.CallbackQuery):
    prew_number = int(callback.data.split('-')[1]) + 1
    year = callback.data.split('-')[2]

    if prew_number == len(get_year(year)):
        prew_number = 1

    question_obj = get_year(year)[str(prew_number)]
    question = question_obj['question']  # Питання опитування

    options = question_obj['options']
    print(options)

    if options:
        random.shuffle(options)  # Список варіантів для опитування

    answer = question_obj['answer']

    print(prew_number - 1)

    if len(question) >= 300:
        question = question[:295] + '...'

    poll = types.Poll(question=question, type=types.PollType.QUIZ, correct_option_id=options.index(answer))
    await callback.bot.send_poll(chat_id=callback.message.chat.id, question=poll.question, options=options, type=poll.type,
                                 correct_option_id=poll.correct_option_id, reply_markup=learning_keyboard(prew_number, year))

    await callback.answer()


async def shuffle_verb(callback: types.CallbackQuery):

    prew_number = int(callback.data.split('-')[1])
    year = callback.data.split('-')[2]

    cur_number = random.randint(1, len(get_year(year)))
    while cur_number == prew_number:
        cur_number = random.randint(1, len(get_year(year)))

    question_obj = get_year(year)[str(cur_number)]
    question = question_obj['question']  # Питання опитування

    options = question_obj['options']

    if options:
        random.shuffle(options)  # Список варіантів для опитування

    answer = question_obj['answer']


    if len(question) >= 300:
        question = question[:295] + '...'

    poll = types.Poll(question=question, type=types.PollType.QUIZ, correct_option_id=options.index(answer))
    await callback.bot.send_poll(chat_id=callback.message.chat.id, question=poll.question, options=options, type=poll.type,
                                 correct_option_id=poll.correct_option_id, reply_markup=learning_keyboard(cur_number, year))

    await callback.answer()


async def all_years(callback: types.CallbackQuery):

    prewious_key = callback.data.split('-')[1]

    all_years = get_all()
    random_year = random.choice(all_years)
    random_key = random.choice(list(random_year.keys()))

    while random_key == prewious_key:
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
    await callback.message.bot.send_poll(chat_id=callback.message.chat.id,
                                question=poll.question,
                                options=options,
                                type=poll.type,
                                correct_option_id=poll.correct_option_id,
                                reply_markup=shuffle(random_key))

    await callback.answer()


def register_callback_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(next_verb, Text(startswith='next'))
    dp.register_callback_query_handler(shuffle_verb, Text(startswith='shuffle'))
    dp.register_callback_query_handler(all_years, Text(startswith='all'))
