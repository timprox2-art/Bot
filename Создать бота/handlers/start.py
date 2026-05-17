from aiogram import Router, html
from aiogram.filters import CommandStart
from aiogram.types import Message
from keyboards.reply import get_start_keyboard

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    welcome_text = (
        f"Привет, {html.bold(message.from_user.full_name)}! 👋\n\n"
        f"Нужен качественный Telegram-бот для бизнеса, канала или магазина?\n"
        f"Я помогаю создавать надежных ботов под любые задачи.\n\n"
        f"💰 {html.bold('Цена:')} от 1000 рублей\n"
        f"⏱ {html.bold('Сроки:')} от 1 дня\n\n"
        f"Нажми кнопку ниже, чтобы оставить заявку и рассчитать точную стоимость 👇"
    )
    await message.answer(welcome_text, reply_markup=get_start_keyboard(), parse_mode="HTML")