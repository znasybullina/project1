from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def get_main_keyboard():
    buttons = [
        [KeyboardButton(text="7А"), KeyboardButton(text="7Б")],
        [KeyboardButton(text="8А"), KeyboardButton(text="8Б")],
        [KeyboardButton(text="9А"), KeyboardButton(text="9Б")],
        [KeyboardButton(text="10А"), KeyboardButton(text="10Б")],
        [KeyboardButton(text="11А"), KeyboardButton(text="11Б")],
    ]

    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)


def get_second_keyboard():
    buttons = [
        [KeyboardButton(text="Понедельник"), KeyboardButton(text="Четверг")],
        [KeyboardButton(text="Вторник"), KeyboardButton(text="Пятница")],
        [KeyboardButton(text="Среда"), KeyboardButton(text="Суббота")],
        [KeyboardButton(text="Назад ↩️")]
    ]
    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True,one_time_keyboard=False)




