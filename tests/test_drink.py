# Drink Creation Test

def test_simple_drink_creation1():
    import sys
    sys.path.append('/Users/david/Documents/school/cpsc_483/siren_ai')
    from src.drink import Drink
    drink = Drink("strawberry acai refresher", "grande", True, ['inclusion.strawberry.7'])
    assert drink.name == "strawberry acai refresher"
    assert drink.price == 3.45
    assert drink.category == "refresher"
    assert drink.type == "iced"
    assert drink.size == "grande"
    assert str(drink) == "strawberry acai refresher - $3.45 - refresher - iced - {'inclusion.strawberry': 7, 'ice.ice': 2}"

def test_simple_drink_creation2():   
    import sys
    sys.path.append('/Users/david/Documents/school/cpsc_483/siren_ai') 
    from src.drink import Drink

    drink = Drink("strawberry acai refresher", "trenta", True, [])
    assert str(drink) == "strawberry acai refresher - $4.45 - refresher - iced - {'inclusion.strawberry': 2, 'ice.ice': 2}"
    

