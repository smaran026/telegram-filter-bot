import os
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("TOKEN")
MAKE_WEBHOOK = os.getenv("MAKE_WEBHOOK")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot is running 🚀")


async def router(update: Update, context: ContextTypes.DEFAULT_TYPE):

    message = update.message
    text = message.text

    command = text.split()[0].replace("/", "")

    payload = {
        "command": command,
        "text": text,
        "user_id": message.from_user.id,
        "username": message.from_user.username or "",
        "first_name": message.from_user.first_name or "",
        "chat_id": message.chat.id,
        "args": context.args
    }

    try:
        requests.post(MAKE_WEBHOOK, json=payload)
        await update.message.reply_text("Processing request...")
    except Exception as e:
        print(e)
        await update.message.reply_text("Server connection failed")


def main():

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    commands = [
        "addme",
        "tokens",
        "level",
        "base",
        "cry",
        "me",
        "clan",
        "reg",
        "reset",
        "missing"
    ]

    for c in commands:
        app.add_handler(CommandHandler(c, router))

    app.run_polling()


if __name__ == "__main__":
    main()
