# from database.models import User, Progress
import random

from database import get_all, get_year


def get_question_from_all_years(previous_question_index=0):

    all_years = get_all()
    random_year = get_year(random.choice(all_years))
    random_key = random.choice(list(random_year.keys()))
    while random_key == previous_question_index:
        random_key = random.choice(list(random_year.keys()))

    question_obj = random_year[str(random_key)]

    question = question_obj['question']
    options = question_obj['options']
    answer = question_obj['answer']

    if options:
        random.shuffle(options)

    if len(question) >= 300:
        question = question[:297] + '...'

    return random_key, question, options, answer


def get_question_from_special_year(year, previous_question_index=0, shuffle=False):

    tests = get_year(year)
    index = previous_question_index + 1
    if previous_question_index == len(tests):
        index = 1

    if shuffle:
        index = random.randint(1, len(tests))
        while index == previous_question_index:
            index = random.randint(1, len(tests))

    question_obj = tests[str(index)]
    question = question_obj['question']
    options = question_obj['options']
    answer = question_obj['answer']

    if options:
        random.shuffle(options)

    if len(question) >= 300:
        question = question[:295] + '...'

    # prew_number = int(callback.data.split('-')[1])
    # year = callback.data.split('-')[2]
    #
    # cur_number = random.randint(1, len(get_year(year)))
    # while cur_number == prew_number:
    #     cur_number = random.randint(1, len(get_year(year)))
    #
    # question_obj = get_year(year)[str(cur_number)]
    # question = question_obj['question']  # Питання опитування
    #
    # options = question_obj['options']
    #
    # if options:
    #     random.shuffle(options)  # Список варіантів для опитування
    #
    # answer = question_obj['answer']
    #
    # if len(question) >= 300:
    #     question = question[:295] + '...'
    #

    return index, question, options, answer
