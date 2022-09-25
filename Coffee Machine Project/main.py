from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


is_on = True

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

while is_on:
    order = input(f"What would you like ot have {menu.get_items()}: ")

    if order == "off":
        is_on = False
    elif order == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        resource = menu.find_drink(order)
        if coffee_maker.is_resource_sufficient(resource):
            if money_machine.make_payment(resource.cost):
                print(coffee_maker.make_coffee(resource))