# It is possible to:
# Type (espresso/latte/cappuccino),
# report(prints quantity of: water, milk, coffee),
# off (stops machine activity).
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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def report_finance():
    for key in resources:
        index = "ml"
        if key == "coffee":
            index = "g"
        print(f"{key.capitalize()}: {resources[key]}{index}")
    # print(f"Money: ${money}")
    choice_of_coffee()


def possible_to_make(choice):
    amount_of_resources = []
    for key in resources:
        amount_of_resources.append(resources[key])
    water = MENU[choice]["ingredients"]["water"]
    if choice != "espresso":
        milk = MENU[choice]["ingredients"]["milk"]
    else:
        milk = 0
    coffee = MENU[choice]["ingredients"]["coffee"]
    all_resources = [water, milk, coffee]
    for i in range(0, 3):
        if amount_of_resources[i] - all_resources[i] < 0:
            if i == 0:
                print("Sorry, there is not enough water")
                return choice_of_coffee()
            if i == 1:
                print("Sorry, there is not enough milk")
                return choice_of_coffee()
            else:
                print("Sorry, there is not enough coffe")
                return choice_of_coffee()

    if coins(choice) == 1:
        resources["water"] -= water
        resources["milk"] -= milk
        resources["coffee"] -= coffee
        choice_of_coffee()


def coins(choice):
    # latte 2.5
    # quarter = 0.25
    # dime = 0.10
    # nickel = 0.05
    # penny = 0.01
    print("Please insert coins.")
    quarter = int(input("how many quarters?")) * 0.25
    dime = int(input("how many dimes?")) * 0.10
    nickel = int(input("how many nickel?")) * 0.05
    penny = int(input("how many penny?")) * 0.01
    cost_of_coffee = MENU[choice]["cost"]
    money_from_customer = quarter + dime + nickel + penny
    if money_from_customer < cost_of_coffee:
        print("Sorry that's not enough money. Money refunded.")
        choice_of_coffee()
    if money_from_customer >= cost_of_coffee:
        print(f"Here is ${money_from_customer - cost_of_coffee} in change.")
        print(f"Here is your {choice}☕️. Enjoy!")
        return 1


def choice_of_coffee():
    choice = (input(f"What would you like? (espresso/latte/cappuccino)")).lower()
    if choice == "report":
        report_finance()
    if choice == "off":
        return
    possible_to_make(choice)


choice_of_coffee()
