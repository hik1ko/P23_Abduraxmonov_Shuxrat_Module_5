from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def email_btn():
    ikb = InlineKeyboardBuilder()
    btn = InlineKeyboardButton(text="emailga habar yuborish", callback_data='email')
    ikb.add(btn)
    ikb.adjust(2, repeat=True)
    return ikb.as_markup()