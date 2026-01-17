import json
import os
import dotenv
from google.cloud import dialogflow


def load_intents_data(filename):
    with open(filename, "r") as my_file:
        phrases_json = my_file.read()

    return json.loads(phrases_json)


def create_intent(project_id, display_name, training_phrases_parts, message_texts):
    intents_client = dialogflow.IntentsClient()

    parent = dialogflow.AgentsClient.agent_path(project_id)
    training_phrases = []
    for training_phrases_part in training_phrases_parts:
        part = dialogflow.Intent.TrainingPhrase.Part(text=training_phrases_part)
        training_phrase = dialogflow.Intent.TrainingPhrase(parts=[part])
        training_phrases.append(training_phrase)

    text = dialogflow.Intent.Message.Text(text=message_texts)
    message = dialogflow.Intent.Message(text=text)

    intent = dialogflow.Intent(
        display_name=display_name, training_phrases=training_phrases, messages=[message]
    )

    return intents_client.create_intent(
        request={"parent": parent, "intent": intent}
    )


if __name__ == '__main__':
    dotenv.load_dotenv()
    project_id = os.environ['PROJECT_ID']

    intents_data = load_intents_data("questions.json")
    for intent_name, intent_data in intents_data.items():
        response = create_intent(
            project_id,
            intent_name,
            intent_data["questions"],
            [intent_data["answer"]]
        )
        print(f"Intent created: {response}")
