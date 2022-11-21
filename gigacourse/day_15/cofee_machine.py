from menu import *
from eslib import *


def get_coins(price):
    print("Please insert your coins")
    quarters = int(digit_input("How many quarters? \t : "))
    dimes = int(digit_input("How many dimes? \t :"))
    nickles = int(digit_input("How many nickles? \t : "))
    pennies = int(digit_input("How many pennies? \t : "))
    total = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
    stock["Money"] += round(total)
    if stock["Money"] >= price:
        print(f"Here is {stock['Money']:.2f}")
    else:
        print("That's not enough money. Money refunded")
    return stock["Money"] >= price


# Data espresso
espresso_cost = MENU["espresso"]["cost"]
espresso_water = MENU["espresso"]["ingredients"]["water"]
espresso_coffee = MENU["espresso"]["ingredients"]["coffee"]

# Data latte
latte_cost = MENU["latte"]["cost"]
latte_water = MENU["latte"]["ingredients"]["water"]
latte_coffee = MENU["latte"]["ingredients"]["coffee"]
latte_milk = MENU["latte"]["ingredients"]["milk"]

# Data cappuccino
cappuccino_cost = MENU["cappuccino"]["cost"]
cappuccino_water = MENU["cappuccino"]["ingredients"]["water"]
cappuccino_coffee = MENU["cappuccino"]["ingredients"]["coffee"]
cappuccino_milk = MENU["cappuccino"]["ingredients"]["milk"]

# Data stock
stock_water = stock["Water"]
stock_coffee = stock["Coffee"]
stock_milk = stock["Milk"]
stock_money = stock["Money"]

ask_coffee = True
while ask_coffee:

    coffee = exact_str_input(possibilities=["espresso", "latte", "cappuccino", "report", "off"],
                             text="What do you like? (espresso/latte/cappuccino) \n")

    if coffee == "report":
        print_dictionary(stock)
    elif coffee == "espresso":
        if stock["Water"] > espresso_water:
            if stock["Coffee"] > espresso_coffee:
                if get_coins(espresso_cost):
                    print(f"Here is your {coffee}. Enjoy! ")
                    stock["Water"] -= espresso_water
                    stock["Coffee"] -= espresso_coffee
                    stock["Money"] -= espresso_cost
            else:
                print("Sorry! There is not enough coffee")
        else:
            print("Sorry! There is not enough water")

    elif coffee == "latte":
        if stock["Water"] > latte_water:
            if stock["Coffee"] > latte_coffee:
                if stock["Milk"] > latte_milk:
                    if get_coins(latte_cost):
                        print(f"Here is your {coffee}. Enjoy! ")
                        stock["Water"] -= latte_water
                        stock["Coffee"] -= latte_coffee
                        stock["Milk"] -= latte_milk
                        stock["Money"] -= latte_cost
                else:
                    print("Sorry! There is not enough milk")
            else:
                print("Sorry! There is not enough coffee")
        else:
            print("Sorry! There is not enough water")

    elif coffee == "cappuccino":
        if stock["Water"] > cappuccino_water:
            if stock["Coffee"] > cappuccino_coffee:
                if stock["Milk"] > cappuccino_milk:
                    if get_coins(cappuccino_cost):
                        print(f"Here is your {coffee}. Enjoy! ")
                        stock["Water"] -= cappuccino_water
                        stock["Coffee"] -= cappuccino_coffee
                        stock["Milk"] -= cappuccino_milk
                        stock["Money"] -= cappuccino_cost
                else:
                    print("Sorry! There is not enough milk")
            else:
                print("Sorry! There is not enough coffee")
        else:
            print("Sorry! There is not enough water")
    else:
        ask_coffee = False
        print("GoodBye 🖐")
