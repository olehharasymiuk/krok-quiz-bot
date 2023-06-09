import json
from pathlib import Path

with open(f'{Path(__file__).parent}/main.json') as file:
    questions = json.load(file)
