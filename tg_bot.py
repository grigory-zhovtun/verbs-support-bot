import os
import dotenv
import logging
import traceback

from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters
from dialogflow_api import get_dialogflow_response
from error_handler import send_error_to_telegram


LANGUAGE_CODE = 'ru-RU'
logger = logging.getLogger(__name__)

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


async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.error(f"Exception: {context.error}")
    send_error_to_telegram(
        "TG Bot",
        traceback.format_exc(),
        context.bot_data['tg_token'],
        context.bot_data['admin_chat_id']
    )



def main():
    dotenv.load_dotenv()
    token = os.environ['TG_TOKEN']
    project_id = os.environ['PROJECT_ID']

    logging.basicConfig(level=logging.ERROR)

    app = ApplicationBuilder().token(token).build()
    app.bot_data['tg_token'] = token
    app.bot_data['admin_chat_id'] = os.getenv("TG_ADMIN_CHAT_ID")
    app.bot_data['project_id'] = project_id
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.add_error_handler(error_handler)

    app.run_polling()


if __name__ == '__main__':
    main()