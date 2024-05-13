import spacy
import random
from spacy.training.example import Example
from spacy.training import offsets_to_biluo_tags

# Load a blank English model
nlp = spacy.blank("en")

# Add entity recognizer and intent recognizer to the pipeline
ner = nlp.add_pipe("ner")
ner.add_label("TEMP")
ner.add_label("SIZE")
ner.add_label("DRINK")
ner.add_label("CUSTOMIZATION")
ner.add_label("INFO")

# Add text classifier to the pipeline for intents
textcat = nlp.add_pipe("textcat")
textcat.add_label("orderDrink")
textcat.add_label("removeDrink")
textcat.add_label("finishedOrder")
textcat.add_label("greeting")
textcat.add_label("editDrink")

# Define training data with entities and intents
TRAIN_DATA = [
    (
        "I'd like a hot grande coffee, please.",
        {
            "entities": [(11, 14, "TEMP"), (15, 21, "SIZE"), (22, 28, "DRINK")],
            "cats": {"orderDrink": 1.0, "removeDrink": 0.0},
        },
    ),
    (
        "Give me a white mocha hot grande.",
        {
            "entities": [(22, 25, "TEMP"), (10, 21, "DRINK"), (26, 32, "SIZE")],
            "cats": {"orderDrink": 1.0, "removeDrink": 0.0},
        },
    ),
    (
        "I will have a white mocha iced venti.",
        {
            "entities": [(26, 30, "TEMP"), (14, 25, "DRINK"), (31, 36, "SIZE")],
            "cats": {"orderDrink": 1.0, "removeDrink": 0.0},
        },
    ),
    (
        "Can I have an iced latte?",
        {
            "entities": [(19, 24, "DRINK"), (14, 18, "TEMP")],
            "cats": {"orderDrink": 1.0, "removeDrink": 0.0},
        },
    ),
    (
        "Can I get a shaken espresso venti with vanilla foam?",
        {
            "entities": [
                (28, 33, "SIZE"),
                (12, 27, "DRINK"),
                (34, 51, "CUSTOMIZATION"),
            ],
            "cats": {"orderDrink": 1.0, "removeDrink": 0.0},
        },
    ),
    (
        "Can I get a iced coffee in a grande add cream and sugar?",
        {
            "entities": [
                (12, 16, "TEMP"),
                (28, 35, "SIZE"),
                (29, 23, "DRINK"),
                (36, 55, "CUSTOMIZATION"),
            ],
            "cats": {"orderDrink": 1.0, "removeDrink": 0.0},
        },
    ),
    (
        "Can I get a grande strawberry acai refresher with lemonade?",
        {
            "entities": [
                (12, 18, "SIZE"),
                (19, 44, "DRINK"),
                (45, 58, "CUSTOMIZATION"),
            ],
            "cats": {"orderDrink": 1.0, "removeDrink": 0.0},
        },
    ),
    (
        "Get me a grande iced caramel macchiato with light ice and add cinnamon powder.",
        {
            "entities": [
                (9, 15, "SIZE"),
                (21, 38, "DRINK"),
                (16, 20, "TEMP"),
                (39, 53, "CUSTOMIZATION"),
                (58, 77, "CUSTOMIZATION"),
            ],
            "cats": {"orderDrink": 1.0, "removeDrink": 0.0},
        },
    ),
    (
        "I will take a cold brew with classic syrup in a venti.",
        {
            "entities": [
                (14, 23, "DRINK"),
                (24, 42, "CUSTOMIZATION"),
                (48, 53, "SIZE"),
            ],
            "cats": {"orderDrink": 1.0, "removeDrink": 0.0},
        },
    ),
    (
        "Remove the venti iced tea.",
        {
            "entities": [(11, 16, "SIZE"), (17, 21, "TEMP"), (22, 25, "DRINK")],
            "cats": {"orderDrink": 0.0, "removeDrink": 1.0},
        },
    ),
    (
        "I want to order a tall iced tea.",
        {
            "entities": [(18, 22, "SIZE"), (23, 27, "TEMP"), (28, 31, "DRINK")],
            "cats": {"orderDrink": 1.0, "removeDrink": 0.0},
        },
    ),
    (
        "I will take a iced venti caramel macchiato.",
        {
            "entities": [(14, 18, "TEMP"), (19, 24, "SIZE"), (25, 42, "DRINK")],
            "cats": {"orderDrink": 1.0, "removeDrink": 0.0},
        },
    ),
    (
        "I want a tall mango dragonfruit refresher with lemonade and light ice.",
        {
            "entities": [(9, 13, "SIZE"), (14, 41, "DRINK"), (42, 70, "CUSTOMIZATION")],
            "cats": {"orderDrink": 1.0, "removeDrink": 0.0},
        },
    ),
    (
        "I want a tall vanilla bean frappuccino with extra caramel.",
        {
            "entities": [(9, 13, "SIZE"), (14, 38, "DRINK"), (39, 57, "CUSTOMIZATION")],
            "cats": {"orderDrink": 1.0, "removeDrink": 0.0},
        },
    ),
    (
        "I want a mocha cookie crumble frappuccino in a venti.",
        {
            "entities": [(47, 52, "SIZE"), (9, 41, "DRINK")],
            "cats": {"orderDrink": 1.0, "removeDrink": 0.0},
        },
    ),
    (
        "Give me a trenta green tea lemonade with four pumps of liquid cane sugar.",
        {
            "entities": [
                (10, 16, "SIZE"),
                (17, 35, "DRINK"),
                (36, 72, "CUSTOMIZATION"),
            ],
            "cats": {"orderDrink": 1.0, "removeDrink": 0.0},
        },
    ),
    (
        "Give me one grande iced latte with almond milk and no ice.",
        {
            "entities": [
                (12, 18, "SIZE"),
                (24, 29, "DRINK"),
                (19, 23, "TEMP"),
                (30, 57, "CUSTOMIZATION"),
            ],
            "cats": {"orderDrink": 1.0, "removeDrink": 0.0},
        },
    ),
    (
        "I will take one grande hot chocolate with extra whip.",
        {
            "entities": [
                (16, 22, "SIZE"),
                (23, 36, "DRINK"),
                (37, 52, "CUSTOMIZATION"),
            ],
            "cats": {"orderDrink": 1.0, "removeDrink": 0.0},
        },
    ),
    (
        "I will take one grande pike place with three sugars.",
        {
            "entities": [
                (16, 22, "SIZE"),
                (23, 33, "DRINK"),
                (34, 51, "CUSTOMIZATION"),
            ],
            "cats": {"orderDrink": 1.0, "removeDrink": 0.0},
        },
    ),
    (
        "I would like a hot cappuccino in a venti",
        {
            "entities": [
                (35, 40, "SIZE"),
                (19, 29, "DRINK"),
                (15, 18, "TEMP"),
            ],
            "cats": {"orderDrink": 1.0, "removeDrink": 0.0},
        },
    ),
    (
        "I want a venti latte hot with extra foam.",
        {
            "entities": [
                (9, 14, "SIZE"),
                (15, 20, "DRINK"),
                (21, 24, "TEMP"),
                (25, 40, "CUSTOMIZATION"),
            ],
            "cats": {"orderDrink": 1.0, "removeDrink": 0.0},
        },
    ),
    (
        "Give me one hot chocolate",
        {
            "entities": [(12, 25, "DRINK")],
            "cats": {"orderDrink": 1.0, "removeDrink": 0.0},
        },
    ),
    (
        "Give me one venti hot mocha with extra whip.",
        {
            "entities": [
                (12, 17, "SIZE"),
                (18, 21, "TEMP"),
                (22, 27, "DRINK"),
                (28, 43, "CUSTOMIZATION"),
            ],
            "cats": {"orderDrink": 1.0, "removeDrink": 0.0},
        },
    ),
    (
        "Let me get one iced coffee with cream and sugar.",
        {
            "entities": [(15, 26, "DRINK"), (27, 47, "CUSTOMIZATION")],
            "cats": {"orderDrink": 1.0, "removeDrink": 0.0},
        },
    ),
    (
        "I would like to  get one iced coffee.",
        {
            "entities": [(25, 36, "DRINK")],
            "cats": {"orderDrink": 1.0, "removeDrink": 0.0},
        },
    ),
    (
        "Give me one white mocha.",
        {
            "entities": [(12, 23, "DRINK")],
            "cats": {"orderDrink": 1.0, "removeDrink": 0.0},
        },
    ),
    (
        "Give me one chai latte.",
        {
            "entities": [(12, 22, "DRINK")],
            "cats": {"orderDrink": 1.0, "removeDrink": 0.0},
        },
    ),
    (
        "I want to order an iced coffee with vanilla and cream.",
        {
            "entities": [(19, 30, "DRINK"), (36, 53, "CUSTOMIZATION")],
            "cats": {"orderDrink": 1.0, "removeDrink": 0.0},
        },
    ),
    (
        "I want to order a nitro cold brew.",
        {
            "entities": [
                (18, 28, "DRINK"),
            ],
            "cats": {"orderDrink": 1.0, "removeDrink": 0.0},
        },
    ),
    (
        "Let me order a nitro cold brew in a grande.",
        {
            "entities": [(15, 30, "DRINK"), (36, 42, "SIZE")],
            "cats": {"orderDrink": 1.0, "removeDrink": 0.0},
        },
    ),
    (
        "I need to order a caramel frappuccino in a grande.",
        {
            "entities": [(18, 37, "DRINK"), (43, 49, "SIZE")],
            "cats": {"orderDrink": 1.0, "removeDrink": 0.0},
        },
    ),
    (
        "Let me get a vanilla bean frappuccino in a venti.",
        {
            "entities": [(13, 37, "DRINK"), (43, 48, "SIZE")],
            "cats": {"orderDrink": 1.0, "removeDrink": 0.0},
        },
    ),
    (
        "let me get a green tea with lemonade and vanilla",
        {
            "entities": [(13, 22, "DRINK"), (23, 48, "CUSTOMIZATION")],
            "cats": {"orderDrink": 1.0, "removeDrink": 0.0},
        },
    ),
]

# Train the NER and text classifier models
optimizer = nlp.initialize()
num_of_iterations = 150
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
print("Training complete.")
# Save the trained model
nlp.to_disk("trained_order_model")
