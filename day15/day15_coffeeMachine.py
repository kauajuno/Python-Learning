MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def report():
    """
    Prints how many resources are left
    :return:
    """
    for resource in resources:
        print(f"{resource}: {resources[resource]}")


def check_resources(coffee_type):
    """
    Checks if the machine has enough resources to do the selected type of coffee
    If it does have enough resources, it returns True
    Otherwise, it prints the missing ingredient and returns False
    :param coffee_type:
    :return:
    """
    for ingredient in MENU[coffee_type]['ingredients']:
        if MENU[coffee_type]['ingredients'][ingredient] > resources[ingredient]:
            print(f"Sorry, there's not enough {ingredient}")
            return False
    # TODO-1 Realocate this part of the code so the ingredients of the machine don't get changed before the coffee is
    #  actually made
    for ingredient in MENU[coffee_type]['ingredients']:
        resources[ingredient] -= MENU[coffee_type]['ingredients'][ingredient]
    return True


def process_coins(pennies, nickels, dimes, quarters):
    """
    Processes the quantity of coins given from the user into their real value and returns it
    :param pennies:
    :param nickels:
    :param dimes:
    :param quarters:
    :return:
    """
    pennies *= 0.01
    nickels *= 0.05
    dimes *= 0.1
    quarters *= 0.25
    return pennies + nickels + dimes + quarters


def check_transation(money_given, coffee_type):
    """
    Checks if the money given by the user is enough to buy the coffee
    If it isn't, it tells the user how much money is missing to complete the coffee value
    Otherwise, it gives the exchange to the user
    :param money_given:
    :param coffee_type:
    :return:
    """
    coffee_price = MENU[coffee_type]['cost']
    if money_given < coffee_price:
        print(f"Sorry, that's not enough money, there's ${round(coffee_price - money_given, 2)} missing!")
        return False
    print(f"Here's ${round(money_given - coffee_price, 2)} in exchange!")
    return True


while True:
    action = input('Welcome to the coffee machine! Type 1 to make coffee or 2 to have a report\n')
    if action == '1':
        coffee = input('1.Espresso\n2.Latte\n3.Cappuccino\n').lower()
        while coffee != 'espresso' and coffee != 'latte' and coffee != 'cappuccino':
            coffee = input('Not a valid type of coffee...\n1. Espresso\n2.Latte\n3.Cappuccino\n')
        if check_resources(coffee) is True:
            penny = int(input('How many pennies?\n'))
            nickel = int(input('How many nickels?\n'))
            dime = int(input('How many dimes?\n'))
            quarter = int(input('How many quarters?\n'))
            money = process_coins(penny, nickel, dime, quarter)
            if check_transation(money, coffee) is True:
                print(f"Enjoy your {coffee}!")
    elif action == '2':
        report()
