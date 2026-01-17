import requests


def send_error_to_telegram(
        bot_name,
        error_message,
        tg_token,
        admin_chat_id):
    if not tg_token or not admin_chat_id:
        return

    text = f"🚨🚨🚨 Ошибка в {bot_name}:\n\n{error_message} 🚨🚨🚨"

    url = f"https://api.telegram.org/bot{tg_token}/sendMessage"
    requests.post(url, data={"chat_id": admin_chat_id, "text": text})

