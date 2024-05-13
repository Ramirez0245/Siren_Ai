from enum import verify
from transitions import Machine

from data.menu import get_drink_category, verify_drink, categories

from .drink import Drink


class Drink_Brain:
    states = ["unfinished", "built", "error", "confirmed"]
    current_drink: Drink = None
    error_flags = []

    def __init__(self, drink) -> None:
        self.drink = drink

        self.machine = Machine(
            model=self, states=Drink_Brain.states, initial="unfinished"
        )

        self.machine.add_transition(
            trigger="finish_drink",
            source="unfinished",
            dest="built",
            before="build_drink",
        )
        self.machine.add_transition(
            trigger="drink_error",
            source="*",
            dest="error",
        )

        self.machine.add_transition(
            trigger="finish_drink",
            source="*",
            dest="built",
            before="build_drink",
        )

        self.machine.add_transition(
            trigger="confirm_drink",
            source="built",
            dest="confirmed",
            before="confirm_drink",
        )

        if drink["drink"] == None:
            self.error_flags.append("no_drink")
            self.drink_error()
        else:
            if verify_drink(drink["drink"]) == False:
                self.error_flags.append("wrong_drink")
                self.drink_error()
            else:
                temp_needed_drinks = ["espresso"]
                if get_drink_category(drink["drink"]) in temp_needed_drinks:
                    if drink["temp"] == None:
                        self.error_flags.append("no_temp")
                        self.drink_error()
                else:
                    drink["temp"] = "iced"

            if drink["size"] == None:
                self.error_flags.append("no_size")
                self.drink_error()

    def confirm_drink(self):
        print("Added: ")
        print(self.current_drink)
        print("To order")

    def build_drink(self):
        if self.error_flags == []:
            try:
                self.current_drink = Drink(
                    self.drink["drink"],
                    self.drink["size"],
                    self.drink["temp"] == "iced",
                    self.drink["customization"],
                )
            except Exception as e:
                print(e)
                self.drink_error()

        else:
            self.drink_error()
