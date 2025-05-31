import os
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils import executor
import redis
import json
from datetime import datetime

logging.basicConfig(level=logging.INFO)

API_TOKEN = os.getenv("TG_BOT_TOKEN", "PLACEHOLDER_TOKEN")
r = redis.Redis(host="localhost", port=6379, db=0, decode_responses=True)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

main_menu = ReplyKeyboardMarkup(resize_keyboard=True)
main_menu.row("💧 Залить Воду", "💼 Мой Стейкинг")
main_menu.row("📈 Стратегия AI", "💰 Вывод")
main_menu.row("🛠 Кликер", "🔗 Кошелёк")
main_menu.row("📊 История", "🎁 Мем-награды")

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    uid = str(message.from_user.id)
    if not r.exists(f"wallet:{uid}"):
        r.set(f"wallet:{uid}", "")
    await message.answer("🐘 Добро пожаловать в Watercoin2!", reply_markup=main_menu)

@dp.message_handler(lambda m: m.text == "🔗 Кошелёк")
async def wallet(message: types.Message):
    uid = str(message.from_user.id)
    wallet = r.get(f"wallet:{uid}")
    await message.answer(f"Ваш Solana-адрес: {wallet or 'не привязан'}\n\nОтправьте адрес одним сообщением")

@dp.message_handler(lambda m: m.text.startswith("4") and len(m.text) >= 32)
async def save_wallet(message: types.Message):
    uid = str(message.from_user.id)
    r.set(f"wallet:{uid}", message.text.strip())
    await message.reply("✅ Адрес сохранён")

@dp.message_handler(lambda m: m.text == "📈 Стратегия AI")
async def strategy_select(message: types.Message):
    uid = str(message.from_user.id)
    r.set(f"strategy:{uid}", "AI")
    await message.answer("Стратегия установлена: AI Stream Mode ✅")

@dp.message_handler(lambda m: m.text == "💧 Залить Воду")
async def deposit(message: types.Message):
    uid = str(message.from_user.id)
    r.incrby(f"stake:{uid}", 1000)
    await message.reply("💧 Стейк увеличен на 1000 $WATER")

@dp.message_handler(lambda m: m.text == "💼 Мой Стейкинг")
async def my_stake(message: types.Message):
    uid = str(message.from_user.id)
    stake = r.get(f"stake:{uid}") or 0
    income = r.get(f"income:{uid}") or 0
    await message.answer(f"💧 Стейк: {stake} $WATER\n💰 Доход: {income} USDT")

@dp.message_handler(lambda m: m.text == "🛠 Кликер")
async def clicker(message: types.Message):
    from random import randint
    uid = str(message.from_user.id)
    r.incrby(f"stake:{uid}", randint(1, 10))
    await message.reply("💦 +капля воды! (авто в стейк)")

@dp.message_handler(lambda m: m.text == "💰 Вывод")
async def withdraw(message: types.Message):
    uid = str(message.from_user.id)
    income = float(r.get(f"income:{uid}") or 0)
    if income >= 1:
        r.set(f"income:{uid}", 0)
        await message.reply(f"💸 Отправлено {income:.2f} USDT на ваш кошелёк!")
    else:
        await message.reply("❌ Недостаточный баланс для вывода")

@dp.message_handler(lambda m: m.text == "📊 История")
async def history(message: types.Message):
    uid = str(message.from_user.id)
    await message.answer(f"📅 История (фиктивная):\n22.05 +3.4% AI\n23.05 -1.2% AI\n24.05 +5.1% AI")

@dp.message_handler(lambda m: m.text == "🎁 Мем-награды")
async def rewards(message: types.Message):
    await message.answer("🏅 Мем-награды:\n👑 Хозяин Потока\n🧻 Бумажный Ходлер\n🚿 Кран Разума")

if __name__ == "__main__":
    logging.info("✅ Watercoin2 Бот запущен")
    executor.start_polling(dp, skip_updates=True)
