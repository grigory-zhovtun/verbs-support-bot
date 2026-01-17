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
    response = requests.post(url, data={"chat_id": admin_chat_id, "text": text})
    response.raise_for_status()

    # телега иногда возвращает 200, но с ошибкой в JSON
    decoded_response = response.json()
    if 'error' in decoded_response:
        raise requests.exceptions.HTTPError(decoded_response['error'])
