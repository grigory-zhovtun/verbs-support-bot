import os
import argparse

from google.cloud import dialogflow
import dotenv


def fetch_intent_texts(project_id, session_id, query_input):
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, session_id)

    return session_client.detect_intent(
            request={"session": session, "query_input": query_input}
    )

def get_dialogflow_response(project_id, session_id, text, language_code):
    text_input = dialogflow.TextInput(text=text, language_code=language_code)
    query_input = dialogflow.QueryInput(text=text_input)
    response = fetch_intent_texts(project_id, session_id, query_input)

    return response.query_result.fulfillment_text


if __name__ == '__main__':
    dotenv.load_dotenv()
    project_id = os.getenv("PROJECT_ID")

    parser = argparse.ArgumentParser(description='Dialogflow intent detection')
    parser.add_argument('text', nargs='+', help='Texts to detect intent for')
    parser.add_argument('--session_id', default='123456789', help='Session ID (default: 123456789)')
    parser.add_argument('--language', default='ru-RU', help='Language code (default: ru-RU)')

    args = parser.parse_args()

    get_dialogflow_response(
        project_id,
        args.session_id,
        args.text,
        args.language
    )