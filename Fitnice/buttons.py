from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def main_page_button():
    kb = [
        [
            KeyboardButton(text='Filial 📍'),
            KeyboardButton(text='Start ✅')
        ],
        [
            KeyboardButton(text='Admin 👨🏻‍💻'),
            KeyboardButton(text='NewsPost 📄')
        ]
    ]

    rkm = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    return rkm

def male_female_btn():
    kb = [
        [
            KeyboardButton(text='Man 🧑🏻‍💼'),
            KeyboardButton(text='Woman 🤵‍♀️')
        ],
        [
            KeyboardButton(text='Back 🔙'),
        ]
    ]

    rkm = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    return rkm

def months_btn():
    kb = [
        [
            KeyboardButton(text='1-oy'),
            KeyboardButton(text='️2-oy')
        ],
        [
            KeyboardButton(text='3-oy'),
            KeyboardButton(text='️4-oy')
        ],
        [
            KeyboardButton(text='️Back 🔙')
        ]
    ]

    rkm = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    return rkm

def week_days_btn():
    kb = [
        [
            KeyboardButton(text='Dushanba'),
            KeyboardButton(text='️Seshanba'),
            KeyboardButton(text='️Chorshanba')
        ],
        [
            KeyboardButton(text='Payshanba'),
            KeyboardButton(text='️Juma'),
            KeyboardButton(text='️Shanba'),
        ]
    ]

    rkm = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    return rkm