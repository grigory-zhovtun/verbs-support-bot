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

def detect_intent(project_id, session_id, texts, language_code):
    for text in texts:
        text_input = dialogflow.TextInput(text=text, language_code=language_code)

        query_input = dialogflow.QueryInput(text=text_input)

        response = fetch_intent_texts(project_id, session_id, query_input)

        print("=" * 20)
        print(f"Query text: {response.query_result.query_text}")
        print(
            f"Detected intent: "
            f"{response.query_result.intent.display_name} "
            f"(confidence: {response.query_result.intent_detection_confidence})\n"
            )

        print(f"Fulfillment text: {response.query_result.fulfillment_text}\n")


if __name__ == '__main__':
    dotenv.load_dotenv()
    project_id = os.getenv("PROJECT_ID")

    parser = argparse.ArgumentParser(description='Dialogflow intent detection')
    parser.add_argument('texts', nargs='+', help='Texts to detect intent for')
    parser.add_argument('--session_id', default='123456789', help='Session ID (default: 123456789)')
    parser.add_argument('--language', default='ru-RU', help='Language code (default: ru-RU)')

    args = parser.parse_args()

    detect_intent(
        project_id,
        args.session_id,
        args.texts,
        args.language
    )