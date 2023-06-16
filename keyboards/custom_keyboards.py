from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def learning_keyboard(question_index, year):

    keyboard = InlineKeyboardMarkup(row_width=2)
    button1 = InlineKeyboardButton('🔽', callback_data=f'next-{question_index}-{year}')
    button2 = InlineKeyboardButton('🔀', callback_data=f'shuffle-{question_index}-{year}')
    keyboard.insert(button2).insert(button1)

    return keyboard


def years_keyboard():

    keyboard = InlineKeyboardMarkup()

    button1 = InlineKeyboardButton('2018', callback_data=f'years-2018')
    button2 = InlineKeyboardButton('2019', callback_data=f'years-2019')
    button3 = InlineKeyboardButton('2020', callback_data=f'years-2020')
    button4 = InlineKeyboardButton('2021', callback_data=f'years-2021')
    button5 = InlineKeyboardButton('2022', callback_data=f'years-2022')
    button6 = InlineKeyboardButton('2023', callback_data=f'years-2023')

    keyboard.insert(button1).insert(button2).insert(button3).insert(button4).insert(button5).insert(button6)

    return keyboard


def shuffle(previous_key):

    keyboard = InlineKeyboardMarkup()

    button1 = InlineKeyboardButton('🔽', callback_data=f'all-{previous_key}')

    keyboard.insert(button1)

    return keyboard
