# CommentSenseBot

Этот проект — Telegram-бот, который анализирует комментарии под YouTube-видео на основе настроения. Используются модели OpenAI для анализа текста и API YouTube для получения комментариев.

## Структура проекта

- `main.py` — главный файл, где настраиваются все маршруты FastAPI и запуск бота.
- `bot.py` — настройка Telegram-бота с использованием aiogram.
- `sentiment.py` — анализ настроений с помощью OpenAI.
- `utils.py` — вспомогательные функции, такие как создание графиков.

## Установка

### 1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/yourusername/yourrepository.git
   ```
### 2. Установка зависимостей

Убедитесь, что у вас установлен Python 3.10 или выше. Затем установите зависимости:

```bash
pip install -r requirements.txt
```
### 3. Настройка переменных окружения
Создайте файл .env в корне проекта и добавьте туда следующие переменные:
```env
TELEGRAM_BOT_TOKEN=ваш_токен_бота
OPENAI_API_KEY=ваш_ключ_openai
YOUTUBE_API_KEY=ваш_ключ_youtube_api
```
## Пример работы 
### 1. Отправьте боту ссылку на видео:
```
https://www.youtube.com/watch?v=example_video_id
```
### 2. Бот обработает комментарии и отправит диаграмму:
![image](https://github.com/user-attachments/assets/c1ba6f96-a01a-4342-85a1-e7e5caf188bc)

