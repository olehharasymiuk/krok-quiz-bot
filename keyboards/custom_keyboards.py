from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def learning_keyboard(question_index):

    keyboard = InlineKeyboardMarkup(row_width=2)

    keyboard.insert(InlineKeyboardButton(
        '🔽', callback_data=f'next-{question_index}')
    )

    return keyboard
