import string
import spacy

from data.ingredients import ingredients
from src.util import find_numbers_as_text


def predict_customization_intent(text: string):
    # Load the trained model
    nlp_loaded = spacy.load("trained_customization_model")

    # Process new text
    doc = nlp_loaded(text)

    # Extract entities and intents
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    intents = [(cat, score) for cat, score in doc.cats.items()]

    intent = max(intents, key=lambda x: x[1])

    new_ingredient = {
        "intent": intent,
        "entities": {
            "amount": len([entity[0] for entity in entities if entity[1] == "AMOUNT"])
            > 0
            and [entity[0] for entity in entities if entity[1] == "AMOUNT"][0]
            or None,
            "ingredient": len(
                [entity[0] for entity in entities if entity[1] == "INGREDIENT"]
            )
            > 0
            and [entity[0] for entity in entities if entity[1] == "INGREDIENT"][0]
            or None,
        },
    }
    return build_ingridient(
        new_ingredient["entities"]["amount"], new_ingredient["entities"]["ingredient"]
    )


def build_ingridient(amount, ingredient: str):
    if ingredient.find("milk") != -1:
        ingredient = ingredient.replace("milk", "")

    ingredient = ingredient.replace(" ", "_").lower()
    if ingredient not in ingredients:
        raise ValueError(f"Ingredient {ingredient} not found")

    if amount is not None:
        found_ingredient = ingredients[ingredient]
        amount = find_numbers_as_text(amount)
        return f'{found_ingredient["type"]}.{ingredient}.{amount}'
    else:
        found_ingredient = ingredients[ingredient]
        return f'{found_ingredient["type"]}.{ingredient}'


def proccess_add_ins(add_ins: str):
    add_ins_to_add = []

    add_ins = add_ins.replace("with", "").strip()
    add_ins = add_ins.translate(str.maketrans("", "", string.punctuation))
    add_ins = add_ins.split("and")

    for i in range(len(add_ins)):
        add_ins_to_add.append(predict_customization_intent(add_ins[i]))

    return add_ins_to_add
