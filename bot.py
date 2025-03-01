import os
from telegram import Update
from telegram.ext import Application, MessageHandler, filters
from openai import OpenAI

OPENAI_KEY = os.environ['OPENAI_KEY']
TELEGRAM_TOKEN = os.environ['TELEGRAM_TOKEN']

openai = OpenAI(api_key=OPENAI_KEY)

async def reply(update: Update, context):
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": update.message.text}]
    )
    await update.message.reply_text(response.choices[0].message.content)

app = Application.builder().token(TELEGRAM_TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT, reply))
app.run_polling()
