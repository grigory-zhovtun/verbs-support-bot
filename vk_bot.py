import os
import random

import dotenv
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from app import get_dialogflow_response


def reply(event, vk, project_id):
    response_text, is_fallback = get_dialogflow_response(
        project_id,
        str(event.user_id),
        event.text,
        'ru-RU'
    )

    print(f"Text: {event.text}")
    print(f"Response: {response_text}")
    print(f"Is fallback: {is_fallback}")

    if not is_fallback:
        vk.messages.send(
            user_id=event.user_id,
            message=response_text,
            random_id=random.randint(1, 1000)
        )


if __name__ == "__main__":
    dotenv.load_dotenv()
    vk_token = os.getenv("VK_TOKEN")
    project_id = os.getenv("PROJECT_ID")

    vk_session = vk_api.VkApi(token=vk_token)
    vk = vk_session.get_api()

    longpoll = VkLongPoll(vk_session)

    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            reply(event, vk, project_id)
