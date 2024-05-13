from uuid import UUID
from src.drink import Drink
from src.predict_menu_intent import predict_menu_intent
from src.drink_machine import Drink_Brain
from src.predict_order_intent import predict_order_intent
from src.predict_pos_intent import predict_pos_intent
from src.pos import Order
from src.generate_response import ResponseGenerator
from data.menu import drinks_by_category, menu
from data.ingredients import ingredients
from src.order_machine import OrderBrain
from src.predict_customization_intent import proccess_add_ins


order = Order(str(UUID(int=1)))
rg = ResponseGenerator()
order_machine = OrderBrain(order)


while order_machine.state != "complete":
    customer_response = input(rg.generate_response(order_machine.state))
    customer_intent = predict_pos_intent(customer_response)
    if customer_intent["intent"][1] < 0.5:
        print(rg.generate_disagree_response())
        continue
    if customer_intent["intent"][0] == "goodbye":
        print(rg.generate_response("goodbye"))
        break
    if customer_intent["intent"][0] == "greeting":
        print(rg.generate_greeting_response())
    if customer_intent["intent"][0] == "orderDrink":
        order_intent = predict_order_intent(customer_response)

        if order_machine.state != "order":
            order_machine.start_order()

        drink_brain = Drink_Brain(order_intent["entities"])
        while drink_brain.state != "built":

            if "no_drink" in drink_brain.error_flags:
                drink_response = rg.generate_drink_error_response(["no_drink"])
                drink_intent = predict_order_intent(input(drink_response))
                if drink_intent["entities"]["drink"] in menu:
                    drink_brain.drink["drink"] = drink_intent["entities"]["drink"]
                    drink_brain.error_flags.remove("no_drink")
                continue

            if "wrong_drink" in drink_brain.error_flags:
                drink_response = rg.generate_drink_error_response(["wrong_drink"])
                drink_intent = predict_order_intent(input(drink_response))
                if drink_intent["entities"]["drink"] in menu:
                    drink_brain.drink["drink"] = drink_intent["entities"]["drink"]
                    drink_brain.error_flags.remove("wrong_drink")
                continue

            if "no_temp" in drink_brain.error_flags:
                temp_response = input(rg.generate_drink_error_response(["no_temp"]))
                if temp_response.find("iced") != -1 or temp_response.find("hot") != -1:
                    # get iced or hot from the response
                    iced_or_hot = temp_response.find("iced") != -1 and "iced" or "hot"
                    drink_brain.drink["temp"] = iced_or_hot
                    drink_brain.error_flags.remove("no_temp")
                continue

            if "no_size" in drink_brain.error_flags:
                sizes = ["short", "tall", "grande", "venti", "trenta"]
                size_response = input(rg.generate_drink_error_response(["no_size"]))
                if any(size in size_response for size in sizes):
                    size_intent = predict_order_intent(size_response)
                    size = size_intent["entities"]["size"]
                    drink_brain.drink["size"] = size
                    drink_brain.error_flags.remove("no_size")
                continue

            if (
                "customization" in drink_brain.drink
                and len(drink_brain.drink["customization"]) > 0
            ):
                add_ins = proccess_add_ins(drink_brain.drink["customization"][0])
                drink_brain.drink["customization"] = add_ins

            drink_brain.finish_drink()
            if drink_brain.current_drink != None:
                order_machine.order.add_drink(drink_brain.current_drink)
                drink_brain.confirm_drink()
                order_machine.idle()
    elif customer_intent["intent"][0] == "reviewOrder":
        print(rg.generate_order_confirmation_response(order_machine.order))
    elif customer_intent["intent"][0] == "finishedOrder":
        order_machine.complete_order()
        rg.generate_order_confirmation_response(order_machine.order)
    elif customer_intent["intent"][0] == "menuInquiry":
        menu_inquiry = predict_menu_intent(customer_response)
        if menu_inquiry["intent"][0] == "menuQuestion":
            print(rg.generate_menu_inquiry_response(menu_inquiry["entities"].pop()[0]))
        if menu_inquiry["intent"][0] == "recipeQuestion":
            drink_name = menu_inquiry["entities"].pop()[0]
            drink = menu[drink_name]
            if drink != None:
                temp_drink = Drink(name=drink_name, size="grande", is_iced=True)
                print(rg.generate_drink_recipes_response(temp_drink))
