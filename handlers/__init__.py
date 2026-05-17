from aiogram import Router
from . import start, register

# Создаем общий роутер папки handlers
router = Router()

# Включаем в него подроутеры
router.include_routers(
    start.router,
    register.router
)