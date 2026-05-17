from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import MY_TELEGRAM_LINK

def get_start_keyboard():
    buttons = [
        [InlineKeyboardButton(text="📝 Рассчитать стоимость проекта", callback_data="start_order")],
        [InlineKeyboardButton(text="👨‍💻 Написать в ЛС напрямую", url=MY_TELEGRAM_LINK)]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)