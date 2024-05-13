from ast import List
from email.policy import default
import enum
import random

from .drink import Drink
from .pos import Order
from data.menu import categories, drinks_by_category
from data.ingredients import ingredients_by_type


default_error_responses = [
    "Sorry, I didn't understand that.",
    "I'm not sure what you mean.",
    "I didn't get that. Can you rephrase?",
    "I'm sorry, I don't understand.",
]

greeting_responses = [
    "Hello! How can I help you today?",
    "Hi! What can I do for you today?",
    "Hey! What can I do for you today?",
    "Hello! What can I do for you today?",
]

order_responses = [
    "What can I get for you today?",
    "What would you like to order?",
    "Please place your order.",
    "What can I get you?",
]

no_size_responses = [
    "I'm sorry, I didn't catch the size of the drink you want.",
    "I didn't get the size of the drink you want.",
    "I didn't catch the size of the drink you want.",
    "I didn't get the size of the drink you want.",
    "I didn't catch the size of the drink you want.",
]

incorrect_size_responses = [
    "I'm sorry, that drink size is not available for that drink.",
]


no_type = [
    "I'm sorry, was that going tp be iced or hot?",
    "I didn't catch if you wanted that iced or hot?",
    "I didn't get if you wanted that iced or hot?",
]

no_add_ins = [
    "I'm sorry, I didn't catch the add-ins you wanted.",
    "I didn't catch the add-ins you wanted.",
    "Can you please repeat the add-ins you wanted?",
]

no_drink = [
    "I'm sorry, I didn't catch the drink you wanted.",
    "I didn't catch the drink you wanted.",
    "Can you please repeat the drink you wanted?",
]

wrong_drink = [
    "I'm sorry, that drink is not available.",
    "I didn't catch the drink you wanted.",
    "The drink you wanted is not available."
    "Can you please repeat the drink you wanted?",
]

farewell_responses = [
    "Goodbye! Have a great day!",
    "Bye! Have a great day!",
    "See you later!",
]

hold_responses = [
    "What else can I help you with?",
    "What else can I do for you?",
    "What else would you like to do?",
    "What else can I get you?",
]

agree_responses = [
    "Got it!",
    "Understood!",
    "Alright!",
    "Okay!",
]

disagree_responses = [
    "I'm sorry, I didn't catch that.",
    "I didn't get that.",
    "I'm not sure what you mean.",
    "I didn't understand that.",
]

no_temp = [
    "I'm sorry, I didn't catch if you wanted that hot or iced.",
    "I didn't catch if you wanted that hot or iced.",
]


class DrinkErrorType(enum.Enum):
    NO_SIZE = "no_size"
    INNCORECT_SIZE = "incorrect_size"
    TYPE = "type"
    NO_DRINK = "no_drink"
    WRONG_DRINK = "wrong_drink"
    NO_TEMP = "no_temp"


class ResponseGenerator:
    def __init__(self):
        pass

    def generate_response(self, orderState):
        if orderState == "welcome":
            return self.generate_greeting_response()
        if orderState == "order":
            return self.generate_order_response()
        if orderState == "confirm":
            return self.generate_agree_response()
        if orderState == "complete":
            return self.generate_farwell_response()
        if orderState == "error":
            return self.generate_default_error_response()
        if orderState == "idle":
            return self.generate_hold_response()

    def generate_drink_error_response(self, drink_error_type: List):
        error_response = ""
        for error in drink_error_type:
            error = DrinkErrorType(error)
            if error == DrinkErrorType.NO_SIZE:
                error_response += random.choice(no_size_responses)
            elif error == DrinkErrorType.INNCORECT_SIZE:
                error_response += random.choice(incorrect_size_responses)
            elif error == DrinkErrorType.TYPE:
                error_response += random.choice(no_type)
            elif error == DrinkErrorType.NO_DRINK:
                error_response += random.choice(no_drink)
            elif error == DrinkErrorType.WRONG_DRINK:
                error_response += random.choice(wrong_drink)
            elif error == DrinkErrorType.NO_TEMP:
                error_response += random.choice(no_temp)

            error_response += "\n"

        return error_response

    def generate_order_response(self):
        return random.choice(order_responses)

    def generate_menu_inquiry_response(self, drink_type: str):
        if drink_type.endswith("s"):
            drink_type = drink_type[:-1]

        if drink_type not in drinks_by_category:
            return f"Sorry, we don't have any {drink_type} drinks available."
        drinks = drinks_by_category[drink_type]
        return f"Here are our {drink_type} options: {', '.join(drinks)}"

    def generate_greeting_response(self):
        return random.choice(greeting_responses)

    def generate_drink_confirmation_response(self, drink: Drink):
        return f"Got it! One {drink.size.title()} {drink.name.title()} added to your order!"

    def generate_add_ins_confirmation_response(self, drink: Drink):
        add_ins = drink.get_customizations()
        return f"Got it! Added {', '.join(add_ins)} to your {drink.size.title()} {drink.name.title()}."

    def generate_drink_removal_confirmation_response(self, drink: Drink):
        return f"Got it! Removed {drink.size.title()} {drink.name.title()} from your order!"

    def generate_order_confirmation_response(self, order: Order):
        drinks = [
            f"{drink.size.title()} {drink.name.title()}" for drink in order.get_drinks()
        ]
        total = order.total
        return f"Got it! Your order of {', '.join(drinks)} has been placed. Your total is ${total:.2f}."

    def generate_menu_query_response(self, drink_type=None):
        if drink_type:
            if drink_type not in drinks_by_category:
                return f"Sorry, we don't have any {drink_type} drinks available."
            drinks = drinks_by_category[drink_type]
            return f"Here are our {drink_type} options: {', '.join(drinks)}"
        else:
            return f"Here are the categories of drinks we have: {', '.join(categories)}"

    def generate_drink_recipes_response(self, drink: Drink):
        ingredients = drink.get_ingredients()
        return f"The ingredients for a {drink.size.title()} {drink.name.title()} are: {', '.join(ingredients)}"

    def generate_drink_price_response(self, drink: Drink):
        return f"The price for a {drink.size.title()} {drink.name.title()} is ${drink.price:.2f}."

    def generate_available_add_ins_response(self, addin_type=None):
        if not addin_type:
            return f"Here are the available add-ins: {', '.join(ingredients_by_type.keys())}"

        if addin_type not in ingredients_by_type:
            return f"Sorry, we don't have any {addin_type} add-ins available."

        add_ins = ingredients_by_type[addin_type]
        return f"Here are the available {addin_type} add-ins: {', '.join([add_in[0] for add_in in add_ins])}"

    def generate_farwell_response(self):
        return random.choice(farewell_responses)

    def generate_default_error_response(self):
        return random.choice(default_error_responses)

    def generate_hold_response(self):
        return random.choice(hold_responses)

    def generate_agree_response(self):
        return random.choice(agree_responses)

    def generate_disagree_response(self):
        return random.choice(disagree_responses)
