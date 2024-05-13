import uuid


def POS_test():
    import sys
    import uuid
    sys.path.append('/Users/david/Documents/school/cpsc_483/siren_ai')
    from src.pos import Order
    from src.drink import Drink

    pos = Order(uuid.uuid4())
    drink = Drink("strawberry acai refresher", "grande", True, [])
    pos.add_drink(drink)
    assert pos.get_drinks() == [drink]