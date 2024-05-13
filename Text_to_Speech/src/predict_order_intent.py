import string
import spacy


def predict_order_intent(text: string):
    # Load the trained model
    nlp_loaded = spacy.load("trained_order_model")

    # Process new text

    doc = nlp_loaded(text)

    # Extract entities and intents
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    intents = [(cat, score) for cat, score in doc.cats.items()]
    intent = max(intents, key=lambda x: x[1])

    return {
        "intent": intent,
        "entities": {
            "drink": len([entity[0] for entity in entities if entity[1] == "DRINK"]) > 0
            and [entity[0] for entity in entities if entity[1] == "DRINK"][0]
            or None,
            "size": len([entity[0] for entity in entities if entity[1] == "SIZE"]) > 0
            and [entity[0] for entity in entities if entity[1] == "SIZE"][0]
            or None,
            "temp": len([entity[0] for entity in entities if entity[1] == "TEMP"]) > 0
            and [entity[0] for entity in entities if entity[1] == "TEMP"][0]
            or None,
            "customization": [
                entity[0] for entity in entities if entity[1] == "CUSTOMIZATION"
            ],
        },
    }
