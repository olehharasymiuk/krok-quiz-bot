from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def learning_keyboard(question_index):

    keyboard = InlineKeyboardMarkup(row_width=2)
    button1 = InlineKeyboardButton('🔽', callback_data=f'next-{question_index}')
    button2 = InlineKeyboardButton('🔀', callback_data=f'shuffle-{question_index}')
    keyboard.insert(button2).insert(button1)

    return keyboard
