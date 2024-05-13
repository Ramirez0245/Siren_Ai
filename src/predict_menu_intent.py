import string
import spacy


def predict_menu_intent(text: string):
    # Load the trained model
    nlp_loaded = spacy.load("trained_menu_model")

    # Process new text

    doc = nlp_loaded(text)

    # Extract entities and intents
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    intents = [(cat, score) for cat, score in doc.cats.items()]

    intent = max(intents, key=lambda x: x[1])

    return {"intent": intent, "entities": entities}


# print(predict_menu_intent("what is a strawberry acai refresher made of?"))
