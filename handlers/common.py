from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command

# Создаём роутер для общих команд
common_router = Router()

@common_router.message(Command("start"))
async def cmd_start(message: Message):
    """
    Обработчик команды /start
    """
    await message.answer(
        "👋 Привет! Я бот для проведения онлайн опросов.\n\n"
        "Для регистрации, пожалуйста, поделитесь своим контактом, "
        "нажав на кнопку ниже.",
        reply_markup=None  # Здесь будет клавиатура с кнопкой шаринга контакта
    )

@common_router.message(Command("help"))
async def cmd_help(message: Message):
    """
    Обработчик команды /help
    """
    await message.answer(
        "🤖 Я бот для проведения онлайн опросов.\n\n"
        "Основные команды:\n"
        "/start - Начать работу с ботом\n"
        "/help - Показать это сообщение\n"
        "/register - Зарегистрироваться\n\n"
        "Если вы администратор, используйте:\n"
        "/admin - Панель администратора"
    )

@common_router.message(Command("register"))
async def cmd_register(message: Message):
    """
    Обработчик команды /register
    """
    await message.answer(
        "Для регистрации, пожалуйста, поделитесь своим контактом, "
        "нажав на кнопку ниже.",
        reply_markup=None  # Здесь будет клавиатура с кнопкой шаринга контакта
    ) 