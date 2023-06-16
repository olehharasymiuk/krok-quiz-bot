import json
from pathlib import Path
import os

folder_path = Path(__file__).parent


def get_year(year):

    with open(f'{folder_path}/{year}.json') as file:
        questions = json.load(file)

    return questions


def get_all():
    years = []

    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)

        if os.path.isfile(file_path) and 'json' in file_name:
            years.append(file_name.strip('.json'))

    return years
