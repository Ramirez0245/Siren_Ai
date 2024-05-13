menu = {
    "hot chocolate": {
        "id": "HCC",
        "price": 4.25,
        "category": "espresso",
        "type": "hot",
        "ingredients": {"syrup.mocha": 2, "milk.2%": 2},
    },
    "cappuccino": {
        "id": "CC",
        "price": 4.95,
        "category": "espresso",
        "type": "hot",
        "ingredients": {"coffee.espresso": 2, "milk.2%": 2},
    },
    "caramel macchiato": {
        "id": "CM",
        "price": 5.45,
        "category": "espresso",
        "type": "hot",
        "ingredients": {"coffee.espresso": 2, "milk.2%": 2, "syrup.vanilla": 4},
    },
    "latte": {
        "id": "CL",
        "price": 4.95,
        "category": "espresso",
        "type": "hot",
        "ingredients": {"coffee.espresso": 2, "milk.2%": 2},
    },
    "mocha": {
        "id": "CM",
        "price": 5.45,
        "category": "espresso",
        "type": "hot",
        "ingredients": {"coffee.espresso": 2, "milk.2%": 2, "syrup.mocha": 4},
    },
    "white mocha": {
        "id": "CWM",
        "price": 5.95,
        "category": "espresso",
        "type": "hot",
        "ingredients": {
            "coffee.espresso": 2,
            "milk.2%": 2,
            "syrup.white_mocha": 4,
        },
    },
    "pike place": {
        "id": "PP",
        "price": 2.95,
        "category": "coffee",
        "type": "hot",
        "ingredients": {},
    },
    "iced coffee": {
        "id": "IC",
        "price": 3.95,
        "category": "coffee",
        "type": "iced",
        "ingredients": {"syrup.classic": 4},
    },
    "nitro cold brew": {
        "id": "NCB",
        "price": 5.25,
        "category": "coffee",
        "type": "iced",
        "ingredients": {},
    },
    "cold brew": {
        "id": "CB",
        "price": 4.45,
        "category": "coffee",
        "type": "iced",
        "ingredients": {},
    },
    "vanilla sweet cream cold brew": {
        "id": "VSCCB",
        "price": 4.75,
        "category": "coffee",
        "type": "iced",
        "ingredients": {"syrup.vanilla": 4, "milk.sweet_cream%": 2},
    },
    "green tea": {
        "id": "GT",
        "price": 3.65,
        "category": "tea",
        "type": "iced",
        "ingredients": {},
    },
    "passion tea": {
        "id": "PT",
        "price": 3.65,
        "category": "tea",
        "type": "iced",
        "ingredients": {},
    },
    "black tea": {
        "id": "BT",
        "price": 3.65,
        "category": "tea",
        "type": "iced",
        "ingredients": {},
    },
    "strawberry acai refresher": {
        "id": "SAR",
        "price": 3.45,
        "category": "refresher",
        "type": "iced",
        "ingredients": {"inclusion.strawberry": 1, "juice.strawberry_base": 2},
    },
    "mango dragonfruit refresher": {
        "id": "MDR",
        "price": 4.75,
        "category": "refresher",
        "type": "iced",
        "ingredients": {"inclusion.dragonfruit": 1, "juice.mango_dragon_base": 2},
    },
    "dragon drink": {
        "id": "DD",
        "price": 5.25,
        "category": "refresher",
        "type": "iced",
        "ingredients": {
            "inclusion.dragonfruit": 1,
            "milk.coconut": 1,
            "juice.pineapple_base": 2,
        },
    },
    "pineapple passion refresher": {
        "id": "PPR",
        "price": 4.75,
        "category": "refresher",
        "type": "iced",
        "ingredients": {
            "inclusion.pineapple": 1,
            "juice.pineapple_base": 2,
            "juice.water": 2,
        },
    },
    "caramel frappuccino": {
        "id": "CF",
        "price": 5.65,
        "category": "frappuccino",
        "type": "iced",
        "ingredients": {"syrup.caramel": 2, "milk.milk": "2%"},
    },
    "vanilla bean frappuccino": {
        "id": "VBF",
        "price": 5.25,
        "category": "frappuccino",
        "type": "iced",
        "ingredients": {"syrup.vanilla": 2, "milk.milk": "2%"},
    },
    "brown sugar oatmilk shaken espresso": {
        "id": "BSOMSE",
        "price": 5.95,
        "category": "espresso",
        "type": "iced",
        "ingredients": {
            "coffee.espresso": 3,
            "milk.oat": 1,
            "syrup.brown_sugar": 2,
            "topping.cinnamon": 2,
        },
    },
    "honey citrus mint tea": {
        "id": "HCMT",
        "price": 3.95,
        "category": "tea",
        "type": "hot",
        "ingredients": {"syrup.honey": 2, "juice.lemonade": 2},
    },
    "shaken espresso": {
        "id": "SE",
        "price": 4.45,
        "category": "espresso",
        "type": "iced",
        "ingredients": {"coffee.espresso": 3},
    },
    "pink drink": {
        "id": "PD",
        "price": 5.25,
        "category": "refresher",
        "type": "iced",
        "ingredients": {
            "inclusion.strawberry": 1,
            "milk.coconut": 1,
            "juice.strawberry_base": 2,
        },
    },
    "matcha green tea latte": {
        "id": "MGT",
        "price": 5.45,
        "category": "tea",
        "type": "hot",
        "ingredients": {"syrup.classic": 2, "milk.2%": 2, "syrup.matcha": 2},
    },
    "chai latte": {
        "id": "cl",
        "price": 5.45,
        "category": "espresso",
        "type": "hot",
        "ingredients": {"milk.2%": 2, "syrup.chai": 2},
    },
}

categories = ["espresso", "coffee", "tea", "refresher", "frappuccino"]

drinks_by_category = {}
for category in categories:
    drinks_by_category[category] = [
        drink for drink in menu if menu[drink]["category"] == category
    ]


def verify_drink(drink_name):
    return drink_name in menu


def get_drink_category(drink_name):
    return menu[drink_name]["category"]
