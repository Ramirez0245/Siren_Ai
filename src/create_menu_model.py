import spacy
import random
from spacy.training.example import Example
from spacy.training import offsets_to_biluo_tags

# Load a blank English model
nlp = spacy.blank("en")

# Add entity recognizer and intent recognizer to the pipeline
ner = nlp.add_pipe("ner")
ner.add_label("DRINK")

# Add text classifier to the pipeline for intents
textcat = nlp.add_pipe("textcat")
textcat.add_label("menuQuestion")
textcat.add_label("recipeQuestion")


# Define training data with entities and intents
TRAIN_DATA = [
    (
        "What teas do you have available?",
        {"entities": [(5, 9, "DRINK")], "cats": {"menuQuestion": 1.0}},
    ),
    (
        "What kind of refreshers do you have right now?",
        {"entities": [(13, 23, "DRINK")], "cats": {"menuQuestion": 1.0}},
    ),
    (
        "Do you have any frappuccinos?",
        {"entities": [(16, 28, "DRINK")], "cats": {"menuQuestion": 1.0}},
    ),
    (
        "What espresso drinks do you have available?",
        {"entities": [(5, 13, "DRINK")], "cats": {"menuQuestion": 1.0}},
    ),
    (
        "Do you have any coffees available?",
        {"entities": [(16, 23, "DRINK")], "cats": {"menuQuestion": 1.0}},
    ),
    (
        "What comes in a caramel macchiato?",
        {"entities": [(16, 33, "DRINK")], "cats": {"recipeQuestion": 1.0}},
    ),
    (
        "What is a caramel frappuccino made of?",
        {"entities": [(10, 29, "DRINK")], "cats": {"recipeQuestion": 1.0}},
    ),
    (
        "what is a strawberry acai refresher made of?",
        {
            "entities": [(10, 35, "DRINK")],
            "cats": {"recipeQuestion": 1.0},
        },
    ),
    (
        "What is in a latte?",
        {"entities": [(13, 18, "DRINK")], "cats": {"recipeQuestion": 1.0}},
    ),
    (
        "How is a mocha made?",
        {"entities": [(9, 14, "DRINK")], "cats": {"recipeQuestion": 1.0}},
    ),
    (
        "What comes in a pink drink?",
        {"entities": [(16, 26, "DRINK")], "cats": {"recipeQuestion": 1.0}},
    ),
    (
        "How is a strawberry acai refresher made?",
        {"entities": [(9, 34, "DRINK")], "cats": {"recipeQuestion": 1.0}},
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
nlp.to_disk("trained_menu_model")
