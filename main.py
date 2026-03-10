import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot is running 🚀")


async def router(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = update.message.text
    command = text.split()[0]

    await update.message.reply_text(f"Command received: {command}")


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
