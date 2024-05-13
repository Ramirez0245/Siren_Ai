from gettext import find

# from util import find_numbers_as_text


ingredients = {
    "espresso_shot": {"type": "coffee", "price": 1.50, "available": True},
    "oat": {"type": "milk", "price": 0.50, "available": True},
    "2%": {"type": "milk", "price": 0.50, "available": True},
    "soy": {"type": "milk", "price": 0.50, "available": True},
    "whole": {"type": "milk", "price": 0.50, "available": True},
    "cream": {"type": "milk", "price": 0.50, "available": True},
    "half_and_half": {"type": "milk", "price": 0.50, "available": True},
    "mocha": {"type": "syrup", "price": 0.50, "available": True},
    "chai": {"type": "syrup", "price": 0.50, "available": True},
    "half_half": {"type": "milk", "price": 0.50, "available": True},
    "white_mocha": {"type": "syrup", "price": 0.50, "available": True},
    "classic": {"type": "syrup", "price": 0.50, "available": True},
    "caramel": {"type": "syrup", "price": 0.50, "available": True},
    "vanilla": {"type": "syrup", "price": 0.50, "available": True},
    "lemonade": {"type": "juice", "price": 0.50, "available": True},
    "water": {"type": "juice", "price": 0.50, "available": True},
    "strawberry": {"type": "inclusion", "price": 0.50, "available": True},
    "dragonfruit": {"type": "inclusion", "price": 0.50, "available": True},
    "pineapple": {"type": "inclusion", "price": 0.50, "available": True},
    "peach": {"type": "juice", "price": 0.50, "available": True},
    "strawberry_puree": {"type": "juice", "price": 0.50, "available": True},
    "strawberry_base": {"type": "juice", "price": 0.50, "available": True},
    "mango_base": {"type": "juice", "price": 0.50, "available": True},
    "pineapple_base": {"type": "juice", "price": 0.50, "available": True},
    "ice": {"type": "ice", "price": 0.00, "available": True},
    "caramel_drizzle": {"type": "topping", "price": 0.50, "available": True},
    "whip_cream": {"type": "topping", "price": 0.00, "available": True},
    "cinnamon": {"type": "topping", "price": 0.00, "available": True},
    "sugar_free_vanilla": {"type": "syrup", "price": 0.50, "available": True},
    "vanilla_sweet_cream_foam": {"type": "foam", "price": 1.0, "available": True},
}


def get_ingredients_by_type(ingredients):
    ingredients_by_type = {}

    for ingredient, details in ingredients.items():
        ingredient_type = details["type"]
        ingredient_price = details["price"]
        if ingredient_type not in ingredients_by_type:
            ingredients_by_type[ingredient_type] = []
        ingredients_by_type[ingredient_type].append((ingredient, ingredient_price))

    return ingredients_by_type


ingredients_by_type = get_ingredients_by_type(ingredients)
