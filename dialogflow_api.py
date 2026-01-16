import os
import json
from google.cloud import dialogflow
from google.oauth2 import service_account


def get_dialogflow_credentials():
    credentials_json = os.getenv("GOOGLE_APPLICATION_CREDENTIALS_JSON")

    if credentials_json:
        credentials_info = json.loads(credentials_json)
        return service_account.Credentials.from_service_account_info(credentials_info)

    return None


def detect_intent(project_id, session_id, query_input):
    credentials = get_dialogflow_credentials()
    session_client = dialogflow.SessionsClient(credentials=credentials)
    session = session_client.session_path(project_id, session_id)

    return session_client.detect_intent(
        request={"session": session, "query_input": query_input}
    )


def get_dialogflow_response(project_id, session_id, text, language_code):
    text_input = dialogflow.TextInput(text=text, language_code=language_code)
    query_input = dialogflow.QueryInput(text=text_input)
    response = detect_intent(project_id, session_id, query_input)

    return (
        response.query_result.fulfillment_text,
        response.query_result.intent.is_fallback
    )
