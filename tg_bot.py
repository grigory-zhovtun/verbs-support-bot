import os
import dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters
from dialogflow_api import get_dialogflow_response


LANGUAGE_CODE = 'ru-RU'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Здравствуйте!")


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.message.chat_id
    text = update.message.text
    project_id = context.bot_data['project_id']
    response_text, is_fallback = get_dialogflow_response(
        project_id,
        str(chat_id),
        text,
        LANGUAGE_CODE
    )
    if not is_fallback:
        await update.message.reply_text(response_text)


def main():
    dotenv.load_dotenv()
    token = os.getenv("TG_TOKEN")
    project_id = os.getenv("PROJECT_ID")

    app = ApplicationBuilder().token(token).build()
    app.bot_data['project_id'] = project_id
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    app.run_polling()


if __name__ == '__main__':
    main()