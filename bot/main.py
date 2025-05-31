from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils import executor
import os

API_TOKEN = os.getenv("TG_BOT_TOKEN", "PLACEHOLDER_TOKEN")

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

main_menu = ReplyKeyboardMarkup(resize_keyboard=True)
main_menu.row("💧 Залить Воду", "💼 Мой Стейкинг")
main_menu.row("📈 Стратегия AI", "💰 Получить $USDT")
main_menu.row("🎁 Мем-Награды", "🛠 Кликер")
main_menu.row("🔗 Кошелёк", "👥 Рефералы")

@dp.message_handler(commands=["start"])
async def send_welcome(message: types.Message):
    await message.reply("Добро пожаловать в Watercoin2! 🐘💦", reply_markup=main_menu)

@dp.message_handler(lambda message: message.text == "💧 Залить Воду")
async def stake_water(message: types.Message):
    await message.reply("Введите количество $WATER для стейкинга:")

@dp.message_handler(lambda message: message.text == "🛠 Кликер")
async def clicker(message: types.Message):
    from random import randint
    amount = randint(1, 10)
    await message.reply(f"💦 Вы получили {amount} $WATER капель!")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
