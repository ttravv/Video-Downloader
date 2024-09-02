from aiogram import types


def start_keyboard():
    kb = [
        [
            types.KeyboardButton(text="Скачать видео из YouTube"),
            types.KeyboardButton(text="Скачать видео из Instagram"),
            types.KeyboardButton(text="Скачать видео из ТикТок"),
        ]
    ]
    return types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
