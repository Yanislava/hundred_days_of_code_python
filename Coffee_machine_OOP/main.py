from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


barista = CoffeeMaker()
kassa = MoneyMachine()
local_menu = Menu()

is_on = True

while is_on:
    command = input('What would you like? (espresso/latte/cappuccino): ')

    if command == 'off':
        is_on = False
    elif command == 'report':
        barista.report()
        kassa.report()
    elif command in local_menu.get_items():
        command = local_menu.find_drink(command)
        if barista.is_resource_sufficient(command):
            if kassa.make_payment(command.cost):
                barista.make_coffee(command)

