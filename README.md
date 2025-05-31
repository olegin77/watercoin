# Watercoin2 Full AI Bot (Solana + Telegram)

## Установка
```bash
sudo apt install redis
pip install -r requirements.txt
export TG_BOT_TOKEN=your_token
python3 bot/main.py
```

## Backend (AI Engine)
```bash
uvicorn backend.app:app --reload --port 8000
```

## AI Тест
```bash
curl http://localhost:8000/ai
```

## В боте:
- /start
- 🔗 Привязка кошелька
- 💧 Стейкинг (1000 $WATER)
- 📈 AI Стратегия
- 💰 Вывод в USDT
- 📊 История + мем-награды

## База: Redis
- stake:{uid}
- income:{uid}
- wallet:{uid}
- strategy:{uid}
