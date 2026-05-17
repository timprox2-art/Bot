from aiogram import Router, F, html
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from config import ADMIN_ID, MY_TELEGRAM_LINK

router = Router()


# Описываем шаги опроса
class OrderForm(StatesGroup):
    waiting_for_task = State()
    waiting_for_budget = State()
    waiting_for_contact = State()


@router.callback_query(F.data == "start_order")
async def start_order_process(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    await callback.message.answer("1️⃣ Опишите кратко: какого бота вы хотите создать? Что он должен делать?")
    await state.set_state(OrderForm.waiting_for_task)


@router.message(OrderForm.waiting_for_task)
async def process_task(message: Message, state: FSMContext):
    await state.update_data(task=message.text)
    await message.answer(
        "2️⃣ Какой у вас планируемый бюджет на разработку? (Например: от 1000₽, 5000₽, открытый бюджет)")
    await state.set_state(OrderForm.waiting_for_budget)


@router.message(OrderForm.waiting_for_budget)
async def process_budget(message: Message, state: FSMContext):
    await state.update_data(budget=message.text)
    await message.answer("3️⃣ Напишите ваш юзернейм в Telegram или номер телефона для связи (например: @my_username):")
    await state.set_state(OrderForm.waiting_for_contact)


@router.message(OrderForm.waiting_for_contact)
async def process_contact(message: Message, state: FSMContext):
    await state.update_data(contact=message.text)
    user_data = await state.get_data()

    thanks_text = (
        "✅ Спасибо! Ваша заявка успешно принята.\n\n"
        "Наш специалист уже изучает ваше ТЗ и свяжется с вами в ближайшее время.\n"
        f"Если не хотите ждать, можете написать ему сами: {MY_TELEGRAM_LINK}"
    )
    await message.answer(thanks_text)

    admin_notification = (
        f"🚨 {html.bold('НОВАЯ ЗАЯВКА ИЗ ПОИСКА')} 🚨\n\n"
        f"👤 {html.bold('Имя пользователя:')} {message.from_user.full_name} (@{message.from_user.username})\n"
        f"📝 {html.bold('Что нужно сделать:')} {user_data['task']}\n"
        f"💰 {html.bold('Бюджет:')} {user_data['budget']}\n"
        f"📞 {html.bold('Контакты для связи:')} {user_data['contact']}"
    )

    try:
        # Важно: используем контекст бота через message.bot
        await message.bot.send_message(chat_id=ADMIN_ID, text=admin_notification, parse_mode="HTML")
    except Exception as e:
        print(f"Ошибка отправки уведомления админу: {e}")

    await state.clear()