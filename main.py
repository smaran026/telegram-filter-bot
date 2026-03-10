import os
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("TOKEN")
MAKE_WEBHOOK = os.getenv("MAKE_WEBHOOK")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot is running 🚀")


async def router(update: Update, context: ContextTypes.DEFAULT_TYPE):

    command = update.message.text.split()[0].replace("/", "")

    data = {
        "command": command,
        "user_id": update.effective_user.id,
        "username": update.effective_user.username,
        "chat_id": update.effective_chat.id,
        "args": context.args
    }

    try:
        requests.post(MAKE_WEBHOOK, json=data)
        await update.message.reply_text("Processing request...")
    except:
        await update.message.reply_text("Server connection failed")


def main():

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    commands = [
        "add",
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
