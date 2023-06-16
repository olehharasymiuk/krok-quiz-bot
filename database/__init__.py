import json
from pathlib import Path


def get_year(year):

    with open(f'{Path(__file__).parent}/{year}.json') as file:
        questions = json.load(file)

    return questions


def get_all():

    years = ['2018', '2019', '2020', '2021', '2022', '2023']

    final = []

    for year in years:
        final.append(get_year(year))

    return final
