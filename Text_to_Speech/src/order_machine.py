from transitions import Machine

from .drink import Drink

from .pos import Order


class OrderBrain:
    states = ["welcome", "order", "confirm", "complete", "error", "idle"]
    current_drink = None
    error_flags = []

    def __init__(self, order: Order) -> None:
        self.order = order
        self.machine = Machine(model=self, states=OrderBrain.states, initial="welcome")

        self.machine.add_transition(
            trigger="start_order", source="welcome", dest="order"
        )
        self.machine.add_transition(
            trigger="confirm_order", source="order", dest="confirm"
        )
        self.machine.add_transition(
            trigger="complete_order", source="confirm", dest="complete"
        )
        self.machine.add_transition(
            trigger="complete_order",
            source="idle",
            dest="complete",
        )
        self.machine.add_transition(
            trigger="order_error", source="*", dest="error", before="show_error"
        )

        self.machine.add_transition(trigger="idle", source="*", dest="idle")
        self.machine.add_transition(trigger="start_order", source="idle", dest="order")
        self.machine.add_transition(
            trigger="confirm_order_trigger",
            source="idle",
            dest="confirm",
            after="complete_order",
        )

    def complete_order(self):
        self.order.status = "complete"
        print(f"Your total is {self.order.total}")
        self.machine.set_state("complete")

    def show_error(self):
        print("There was an error with your order. Please try again.")
