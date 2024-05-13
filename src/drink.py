from enum import Enum
from math import e
from operator import is_
import sys
from telnetlib import NEW_ENVIRON
from data.menu import menu
from data.ingredients import ingredients_by_type


quantities = {
    "tall": {
        "hot": {
            "syrup": 3,
            "coffee": 1,
            "milk": "2%",
            "topping": 2,
            "juice": 2,
        },
        "iced": {
            "syrup": 3,
            "coffee": 1,
            "inclusion": 1,
            "milk": 1,
            "ice": 2,
            "topping": 2,
            "juice": 2,
            "foam": 2,
        },
        "frappuccino": {
            "syrup": 2,
            "coffee": 1,
            "milk": 1,
            "ice": 2,
            "topping": 2,
        },
    },
    "grande": {
        "hot": {
            "syrup": 4,
            "coffee": 2,
            "milk": 1,
            "topping": 2,
            "juice": 2,
        },
        "iced": {
            "syrup": 4,
            "coffee": 2,
            "inclusion": 1,
            "milk": 1,
            "ice": 2,
            "topping": 2,
            "juice": 2,
            "foam": 2,
        },
        "frappuccino": {"syrup": 3, "coffee": 1, "milk": 1, "ice": 2, "topping": 2},
    },
    "venti": {
        "hot": {
            "syrup": 5,
            "coffee": 3,
            "milk": 1,
            "topping": 2,
            "juice": 2,
        },
        "iced": {
            "syrup": 6,
            "coffee": 3,
            "inclusion": 1,
            "milk": 1,
            "ice": 2,
            "topping": 2,
            "juice": 2,
            "foam": 2,
        },
        "frappuccino": {"syrup": 4, "coffee": 1, "milk": 1, "ice": 2, "topping": 2},
    },
    "trenta": {
        "iced": {
            "syrup": 5,
            "coffee": 3,
            "inclusion": 2,
            "milk": 1,
            "ice": 2,
            "topping": 2,
            "juice": 2,
            "foam": 2,
        }
    },
}


class DrinkStatus(Enum):
    COMPLETE = "complete"
    ORDERING = "ordering"
    NEW = "new"


class Drink:
    ingredients = {}
    status: DrinkStatus = DrinkStatus.NEW
    std_price = 0.0
    error_flags = []
    def __init__(self, name, size="grande", is_iced=False, add_ins=[]):
        self.customizations = add_ins
        self.ingredients = {}
        if is_iced:
            self.ingredients["ice.ice"] = 2
        self.name = name
        self.category = menu[name]["category"]
        if self.category == "frappuccino":
            self.type = "frappuccino"
        else:
            self.type = is_iced and "iced" or "hot"
        self.std_price = menu[name]["price"]
        self.id = menu[name]["id"]
        self.set_size(size)
        self.add_ingridents(menu[name]["ingredients"])
        self.add_ingridents(add_ins)

    def add_ingridents(self, ingredients: list[str]):
        for i in ingredients:
            ingredient_array = i.split(".")
            ingredient_type = ingredient_array[0]
            if len(ingredient_array) > 2:
                quantity = int(ingredient_array[2])
            else:
                quantity = quantities[self.size][self.type][ingredient_type]

            self.ingredients[ingredient_array[0] + "." + ingredient_array[1]] = quantity
            if (
                ingredient_array[0] + "." + ingredient_array[1]
                not in menu[self.name]["ingredients"]
            ):
                if ingredient_type == "coffee":
                    self.price += ingredients_by_type[ingredient_type][0][1] * quantity
                    print(
                        "Espresso"
                        + ingredients_by_type[ingredient_type][0][1] * quantity
                    )
                else:
                    self.price += ingredients_by_type[ingredient_type][0][1]

    def get_customizations(self) -> list[str]:
        formated_customizations = []
        for i in self.customizations:
            formated_customizations.append(
                i.replace(".", ": ").replace("_", " ").title()
            )
        return formated_customizations

    def get_ingredients(self) -> list[str]:
        formated_ingredients = []
        for i in self.ingredients:
            formated_ingredients.append(i.replace(".", ": ").replace("_", " ").title())
        return formated_ingredients

    def set_price(self, price):
        if (self.size == "tall"):
            price = price - 0.5
        elif (self.size == "venti"):
            price = price + 0.5
        elif (self.size == "trenta"):
            price = price + 1.0

        if self.type == "iced" and (
            self.category not in ["refresher", "tea", "frappuccino"]
        ):
            price = price + 0.5
        self.price = price

    def set_size(self, size):
        if (self.type not in quantities[size]):
            raise ValueError("Invalid size")

        self.size = size
        self.set_price(self.std_price)

    def __str__(self):
        return (
            self.name
            + " - $"
            + str(self.price)
            + " - "
            + self.category
            + " - "
            + self.type
            + " - "
            + str(self.get_customizations())
        )
