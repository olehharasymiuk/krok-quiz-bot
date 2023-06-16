# from database.models import User, Progress
import random

from database import get_all, get_year


def get_question(year=None, previous_question_index=0, shuffle=False):

    if not year:
        all_years = get_all()
        year = random.choice(all_years)

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

    return index, question, options, answer
