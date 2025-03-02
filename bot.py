import os
from telegram import Update
from telegram.ext import Application, MessageHandler, filters
from openai import OpenAI

# Загрузка ключей из переменных окружения
OPENAI_KEY = os.environ['OPENAI_KEY']
TELEGRAM_TOKEN = os.environ['TELEGRAM_TOKEN']

# Инициализация OpenAI
openai = OpenAI(api_key=OPENAI_KEY)

# Функция обработки сообщений
async def reply(update: Update, context):
    # Запрос к OpenAI
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": update.message.text}]  # Исправлено: [] вместо {}
    )
    # Отправка ответа пользователю
    await update.message.reply_text(response.choices[0].message.content)

# Создание и настройка приложения
app = Application.builder().token(TELEGRAM_TOKEN).build()

# Добавление обработчика текстовых сообщений
app.add_handler(MessageHandler(filters.TEXT, reply))  # Исправлено: add_handler

# Запуск бота
app.run_polling()  # Добавлено: запуск бота
