from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine=MoneyMachine()
coffee_maker=CoffeeMaker()
menu=Menu()

is_on=True

while is_on:
    options=menu.get_items()
    choice= input(f"What would you like? ({options}) ")
    if choice=="off":
        is_on=False
    elif choice == "report":
        print(coffee_maker.report())
        print(money_machine.report())
    elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
        drink=menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
    else:
        print("Sorry, wrong entry, plz try again.")

    