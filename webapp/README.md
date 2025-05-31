
# Watercoin2 WebApp (Telegram Mini App)

## 🔧 Установка
1. Убедитесь, что установлен Node.js (v18+)
2. Клонируйте репозиторий и перейдите в директорию:
   ```
   npm install
   npm run dev
   ```
3. Установите переменные окружения (если нужно):
   - `NEXT_PUBLIC_WEBHOOK_URL=https://yourapi.com`

## 📦 Интеграция
- `/api/me`        → информация пользователя
- `/api/history`   → история AI-доходности
- `/api/claim`     → POST: выдача токенов
- `/api/withdraw`  → POST: вывод средств

## 📱 Telegram WebApp
- Размещайте на Vercel/Netlify
- Используйте `WebAppInfo(url=...)` в боте
