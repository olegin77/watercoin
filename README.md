# Watercoin2 — AI Meme Yield Bot

## 📦 Установка
```bash
git clone https://github.com/yourorg/watercoin2-bot
cd watercoin2-bot
pip install -r requirements.txt
export TG_BOT_TOKEN=your_bot_token
```

## 🚀 Запуск Telegram-бота
```bash
python bot/main.py
```

## 🧠 Запуск AI Backend
```bash
uvicorn backend.app:app --reload --port 8000
```

## 🌐 Открытие админки (mock)
Откройте файл `admin/templates/index.html` в браузере.

## ⚙️ Конфигурация
Все параметры в `config.json`:
- Порог AI (%), комиссия, минимальный стейк
- RPC Solana, список админов

## 🪙 Поддержка токенов
- Токен: $WATER (SPL)
- Интеграция через RPC
- Депозиты, стейкинг, вывод, реф. система

## ✅ Завершение
Этот проект предоставляет полностью готовую архитектуру для запуска Telegram-бота с AI ребалансировкой, мем-элементами и доходной моделью.
