from google.cloud import dialogflow


def detect_intent(
        project_id,
        session_id,
        query_input,
        credentials=None):
    session_client = dialogflow.SessionsClient(credentials=credentials)
    session = session_client.session_path(project_id, session_id)

    return session_client.detect_intent(
        request={"session": session, "query_input": query_input}
    )


def get_dialogflow_response(
        project_id,
        session_id,
        text,
        language_code,
        credentials=None):
    text_input = dialogflow.TextInput(text=text, language_code=language_code)
    query_input = dialogflow.QueryInput(text=text_input)
    response = detect_intent(project_id, session_id, query_input, credentials)

    return (
        response.query_result.fulfillment_text,
        response.query_result.intent.is_fallback
    )
