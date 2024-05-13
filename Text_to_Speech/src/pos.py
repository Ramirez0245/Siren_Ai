import enum
import stat
import uuid
from .drink import Drink


class OrderStatus(enum.Enum):
    COMPLETE = "complete"
    ORDERING = "ordering"
    WELCOMING = "welcoming"
    DRINK_ERROR = "drink_error"
    ADD_INS_ERROR = "add_ins_error"
    DEFAUL_ERROR = "default_error"
    CONFIRM = "confirm"


class Order:
    status: OrderStatus = OrderStatus.WELCOMING
    def __init__(self, customer_id):
        order: list[Drink] = []
        self.id = str(uuid.uuid4())
        self.drinks = []
        self.total = 0.0
        self.customer_id = customer_id

    def add_drink(self, drink):
        self.drinks.append(drink)
        self.total += drink.price

    def remove_drink(self, drink):
        self.drinks.remove(drink)
        self.total -= drink.price

    def update_drink(self, drink, new_drink):
        self.drinks.remove(drink)
        self.drinks.append(new_drink)
        self.total += new_drink.price - drink.price

    def get_drinks(self) -> list[Drink]:
        return self.drinks

    def __str__(self):
        return (
            "Order: "
            + self.id
            + " - "
            + str(self.order)
            + " - "
            + str(self.total)
            + " - "
            + self.customer_id
        )
