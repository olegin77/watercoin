
# 🌊 Watercoin2 Project (Full Release)

## Состав проекта:
- `/bot/` — Telegram бот (aiogram, Redis)
- `/backend/` — FastAPI API, admin tools
- `/webapp/` — Telegram Mini App (React)
- `.env.example` — пример конфигурации
- `requirements.txt` — зависимости Python

## Запуск:
1. Установите зависимости:
   ```
   pip install -r requirements.txt
   ```
2. Запустите backend:
   ```
   cd backend
   uvicorn app:app --reload
   ```
3. Запустите бота:
   ```
   cd bot
   python3 main.py
   ```
4. Разверните WebApp (папка webapp/) на Vercel или Netlify

## Переменные окружения:
- TG_BOT_TOKEN
- SENDER_SECRET
- WATER_MINT
- USDT_MINT
- WEBAPP_URL
