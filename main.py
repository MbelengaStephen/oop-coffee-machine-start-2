from menu import Menu, MenuItem
menu = Menu()
from coffee_maker import CoffeeMaker
coffee_maker = CoffeeMaker()
from money_machine import MoneyMachine
money_machine = MoneyMachine()
is_on = True
while is_on:
    print("Welcome To Coffee Machine Cafe.")
    options = menu.get_items()
    customer_choice = input(f"What would you like? ({options}): ")
    if customer_choice == "off":
        is_on = False
    elif customer_choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(customer_choice)
        resouces_enough = coffee_maker.is_resource_sufficient(drink)
        payment = money_machine.make_payment(drink.cost)
        if resouces_enough and payment:
                coffee_maker.make_coffee(drink)   