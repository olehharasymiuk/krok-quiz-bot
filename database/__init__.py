import json
from pathlib import Path


def get_year(year):

    with open(f'{Path(__file__).parent}/{year}.json') as file:
        questions = json.load(file)

    return questions


def get_all():

    years = ['2019', '2018', '2023']

    final = []

    for year in years:
        final.append(get_year(year))

    return final
