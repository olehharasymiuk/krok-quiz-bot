import random

from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text

from database import questions
from keyboards.custom_keyboards import learning_keyboard


async def next_verb(callback: types.CallbackQuery):
    prew_number = int(callback.data.split('-')[1]) + 1
    if prew_number == len(questions):
        prew_number = 1

    question_obj = questions[str(prew_number)]
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
                                 correct_option_id=poll.correct_option_id, reply_markup=learning_keyboard(prew_number))

    await callback.answer()


async def shuffle_verb(callback: types.CallbackQuery):
    prew_number = int(callback.data.split('-')[1])
    cur_number = random.randint(1, len(questions))
    while cur_number == prew_nimber:
        cur_number = random.randint(1, len(questions))

    question_obj = questions[str(prew_number)]
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
                                 correct_option_id=poll.correct_option_id, reply_markup=learning_keyboard(prew_number))

    await callback.answer()


def register_callback_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(next_verb, Text(startswith='next'))
    dp.register_callback_query_handler(shuffle_verb, Text(startswith='shuffle'))
