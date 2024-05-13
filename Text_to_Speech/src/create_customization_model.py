import spacy
import random
from spacy.training.example import Example
from spacy.training import offsets_to_biluo_tags

# Load a blank English model
nlp = spacy.blank("en")

# Add entity recognizer and intent recognizer to the pipeline
ner = nlp.add_pipe("ner")
ner.add_label("AMOUNT")
ner.add_label("INGREDIENT")
ner.add_label("CUSTOMIZATION")

# Add text classifier to the pipeline for intents
textcat = nlp.add_pipe("textcat")
textcat.add_label("add_ingredient")
textcat.add_label("remove_ingredient")


# Define training data with entities and intents
TRAIN_DATA = [
    (
        "three pumps of vanilla",
        {
            "entities": [(0, 5, "AMOUNT"), (15, 22, "INGREDIENT")],
            "cats": {"add_ingredient": 1.0, "remove_ingredient": 0.0},
        },
    ),
    (
        "one pumps of mocha",
        {
            "entities": [(0, 3, "AMOUNT"), (13, 18, "INGREDIENT")],
            "cats": {"add_ingredient": 1.0, "remove_ingredient": 0.0},
        },
    ),
    (
        "soy milk",
        {
            "entities": [(0, 8, "INGREDIENT")],
            "cats": {"add_ingredient": 1.0, "remove_ingredient": 0.0},
        },
    ),
    (
        "almond milk",
        {
            "entities": [(0, 11, "INGREDIENT")],
            "cats": {"add_ingredient": 1.0, "remove_ingredient": 0.0},
        },
    ),
    (
        "four pumps of white mocha",
        {
            "entities": [(0, 4, "AMOUNT"), (14, 25, "INGREDIENT")],
            "cats": {"add_ingredient": 1.0, "remove_ingredient": 0.0},
        },
    ),
    (
        "sweet cream",
        {
            "entities": [(0, 11, "INGREDIENT")],
            "cats": {"add_ingredient": 1.0, "remove_ingredient": 0.0},
        },
    ),
    (
        "sweet cream foam",
        {
            "entities": [(0, 16, "INGREDIENT")],
            "cats": {"add_ingredient": 1.0, "remove_ingredient": 0.0},
        },
    ),
    (
        "lemonade",
        {
            "entities": [(0, 8, "INGREDIENT")],
            "cats": {"add_ingredient": 1.0, "remove_ingredient": 0.0},
        },
    ),
    (
        "vanilla and caramel syrup",
        {
            "entities": [(0, 7, "INGREDIENT"), (12, 19, "INGREDIENT")],
            "cats": {"add_ingredient": 1.0, "remove_ingredient": 0.0},
        },
    ),
    (
        "four pumps of vanilla and caramel syrup",
        {
            "entities": [
                (0, 4, "AMOUNT"),
                (14, 21, "INGREDIENT"),
                (26, 33, "INGREDIENT"),
            ],
            "cats": {"add_ingredient": 1.0, "remove_ingredient": 0.0},
        },
    ),
]

# Train the NER and text classifier models
optimizer = nlp.initialize()
num_of_iterations = 100
current_itteration = 0
for _ in range(num_of_iterations):  # Adjust the number of iterations as needed
    random.shuffle(TRAIN_DATA)
    for text, annotations in TRAIN_DATA:
        doc = nlp.make_doc(text)
        entities = annotations["entities"]
        biluo_tags = offsets_to_biluo_tags(doc, entities)
        cats = annotations["cats"]

        # Create Example object for NER and text classification
        if len(entities) > 0:
            ner_example = Example.from_dict(
                doc, {"entities": entities, "tags": biluo_tags}
            )
        else:
            ner_example = Example.from_dict(doc, {"entities": [], "tags": biluo_tags})
        textcat_example = Example.from_dict(doc, {"cats": cats})

        # Update NER and text classification models
        nlp.update([ner_example, textcat_example], drop=0.5, sgd=optimizer)
    print(f"Percent complete: {(current_itteration/num_of_iterations)*100:.1f}%")
    current_itteration += 1

# Save the trained model
nlp.to_disk("trained_customization_model")
