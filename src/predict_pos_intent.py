import string
import spacy


def predict_pos_intent(text: string):
    # Load the trained model
    nlp_loaded = spacy.load("trained_pos_model")

    # Process new text

    doc = nlp_loaded(text)

    # Extract entities and intents
    intents = [(cat, score) for cat, score in doc.cats.items()]
    intent = max(intents, key=lambda x: x[1])

    return {"intent": intent}
