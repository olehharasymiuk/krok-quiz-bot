import os

import requests


def get_new_question(year=None, previous_question_index=0, shuffle=False):
    api_source = os.environ.get('API_SOURCE')
    question_index = previous_question_index + 1

    if shuffle and year:
        json_resp = requests.get(f'{api_source}/{year}').json()

    elif shuffle:
        json_resp = requests.get(f'{api_source}/shuffle').json()

    else:
        json_resp = requests.get(f'{api_source}/{year}?question_index={question_index}').json()

    return Question(json_resp).get_list()


class Question:

    def __init__(self, json_object):

        self.index = json_object['question_index']
        self.question = json_object['question']
        self.options = json_object['options']
        self.answer = json_object['answer']

    def get_list(self):

        return [
            self.index,
            self.question,
            self.options,
            self.answer
        ]
