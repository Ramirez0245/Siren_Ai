import spacy
import random
from spacy.training.example import Example
from spacy.training import offsets_to_biluo_tags

# Load a blank English model
nlp = spacy.blank("en")

# # Add entity recognizer and intent recognizer to the pipeline
# ner = nlp.add_pipe("ner")
# ner.add_label("TEMP")
# ner.add_label("SIZE")
# ner.add_label("DRINK")
# ner.add_label("CUSTOMIZATION")
# ner.add_label("INFO")

# Add text classifier to the pipeline for intents
textcat = nlp.add_pipe("textcat")
textcat.add_label("orderDrink")
textcat.add_label("finishedOrder")
textcat.add_label("greeting")
textcat.add_label("reviewOrder")
textcat.add_label("menuInquiry")

# Define training data with entities and intents
TRAIN_DATA = [
    (
        "That will be all.",
        {
            "cats": {
                "finishedOrder": 1.0,
            },
        },
    ),
    (
        "Nothing else for my order.",
        {
            "cats": {"finishedOrder": 1.0},
        },
    ),
    (
        "That is it for my order.",
        {
            "cats": {"finishedOrder": 1.0},
        },
    ),
    (
        "That will be it.",
        {
            "cats": {"finishedOrder": 1.0},
        },
    ),
    (
        "Nothing else for me today.",
        {
            "cats": {"finishedOrder": 1.0},
        },
    ),
    (
        "That is all for now.",
        {
            "cats": {"finishedOrder": 1.0},
        },
    ),
    (
        "Give me one grande iced latte with almond milk and no ice.",
        {
            "cats": {"orderDrink": 1.0},
        },
    ),
    (
        "I will take one grande hot chocolate with extra whip.",
        {
            "cats": {"orderDrink": 1.0},
        },
    ),
    (
        "I will take one grande pike place with three sugars.",
        {
            "cats": {"orderDrink": 1.0},
        },
    ),
    (
        "I would like a hot cappuccino in a venti",
        {
            "cats": {"orderDrink": 1.0},
        },
    ),
    (
        "I want a venti latte hot with extra foam.",
        {
            "cats": {"orderDrink": 1.0},
        },
    ),
    (
        "Give me one hot chocolate",
        {
            "cats": {"orderDrink": 1.0},
        },
    ),
    (
        "Give me one venti hot mocha with extra whip.",
        {
            "cats": {"orderDrink": 1.0},
        },
    ),
    (
        "Good morning.",
        {
            "cats": {"greeting": 1.0},
        },
    ),
    (
        "Good afternoon.",
        {
            "cats": {"greeting": 1.0},
        },
    ),
    ("Hello.", {"cats": {"greeting": 1.0}}),
    (
        "What is my order?",
        {
            "cats": {"reviewOrder": 1.0},
        },
    ),
    (
        "What have i ordered?",
        {
            "cats": {"reviewOrder": 1.0},
        },
    ),
    (
        "What did i order?",
        {
            "cats": {"reviewOrder": 1.0},
        },
    ),
    (
        "What drinks have i ordered?",
        {
            "cats": {"reviewOrder": 1.0},
        },
    ),
    (
        "That will be all.",
        {
            "cats": {"finishedOrder": 1.0},
        },
    ),
    (
        "Nothing else for me.",
        {
            "cats": {"finishedOrder": 1.0},
        },
    ),
    (
        "That will complete my order.",
        {
            "cats": {"finishedOrder": 1.0},
        },
    ),
    (
        "Test.",
        {
            "cats": {"greeting": 1.0},
        },
    ),
    (
        "This is a test.",
        {
            "cats": {"greeting": 1.0},
        },
    ),
    (
        "This is just a test.",
        {
            "cats": {"greeting": 1.0},
        },
    ),
    (
        "Let me get",
        {
            "cats": {"orderDrink": 1.0},
        },
    ),
    (
        "Can i order",
        {
            "cats": {"orderDrink": 1.0},
        },
    ),
    (
        "What kind of {drink} do you have?",
        {
            "cats": {"menuInquiry": 1.0},
        },
    ),
    (
        "What kind of {drink} can i get?",
        {
            "cats": {"menuInquiry": 1.0},
        },
    ),
    (
        "What are the types of {drink} can i get?",
        {
            "cats": {"menuInquiry": 1.0},
        },
    ),
    (
        "let me get a {drink}",
        {
            "cats": {"orderDrink": 1.0},
        },
    ),
    (
        "What comes in a {drink}?",
        {
            "cats": {"menuInquiry": 1.0},
        },
    ),
    (
        "How is a {drink} made?",
        {
            "cats": {"menuInquiry": 1.0},
        },
    ),
    (
        "How do you make a {drink}?",
        {
            "cats": {"menuInquiry": 1.0},
        },
    ),
]

categories = ["espresso", "coffee", "tea", "refresher", "frappuccino"]

for category in categories:
    TRAIN_DATA.append(
        (
            f"{category}",
            {
                "cats": {"menuInquiry": 1.0},
            },
        )
    )

    TRAIN_DATA.append(
        (
            f"What {category} do you have?",
            {
                "cats": {"menuInquiry": 1.0},
            },
        )
    )

    TRAIN_DATA.append(
        (
            f"What {category} do you have avaiable?",
            {
                "cats": {"menuInquiry": 1.0},
            },
        )
    )


# Train the NER and text classifier models
optimizer = nlp.initialize()
num_of_iterations = 150
current_itteration = 0
for _ in range(num_of_iterations):  # Adjust the number of iterations as needed
    random.shuffle(TRAIN_DATA)
    for text, annotations in TRAIN_DATA:
        doc = nlp.make_doc(text)
        cats = annotations["cats"]

        # Create Example object for NER and text classification

        textcat_example = Example.from_dict(doc, {"cats": cats})

        # Update NER and text classification models
        nlp.update([textcat_example], drop=0.5, sgd=optimizer)
    print(f"Percent complete: {(current_itteration/num_of_iterations)*100:.1f}%")
    current_itteration += 1

# Save the trained model
nlp.to_disk("trained_pos_model")
