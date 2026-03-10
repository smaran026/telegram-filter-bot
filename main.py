import os
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("TOKEN")
MAKE_WEBHOOK = os.getenv("MAKE_WEBHOOK")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot is running 🚀")


async def router(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = update.message.text
    command = text.split()[0].replace("/", "")

    MAKE_COMMANDS = [
        "add",
        "tokens",
        "level",
        "base",
        "cry",
        "reset"
    ]

    if command in MAKE_COMMANDS:

        data = {
            "command": command,
            "user_id": update.effective_user.id,
            "username": update.effective_user.username,
            "args": context.args
        }

        try:
            requests.post(MAKE_WEBHOOK, json=data)
            await update.message.reply_text("Processing request...")
        except:
            await update.message.reply_text("Server connection failed")

    else:
        await update.message.reply_text("Command handled locally (coming soon)")


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
