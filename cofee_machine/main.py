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
    "milk": 100,
    "coffee": 100
}


def check_ingredients(oreder_ingredience):
    for item in oreder_ingredience:
        if oreder_ingredience[item]>=resources[item]:
            print(f"​Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    print("How many coins do you have")
    #total = 0
    total = int(input("How many quarters you have? ")) * 0.25
    total += int(input("How many dimes you have? ")) * 0.10
    total += int(input("How many nickles you have? ")) * 0.05
    total += int(input("How many pennies you have? ")) * 0.01
    return total


def is_transaction_succesfull(payment, cost):
    if payment>= cost:
        change = round(payment - cost,2)
        global profit
        profit += cost
        print(f"Here is ${change} in change")
        return True ## if there was enough money inserted, add to profit
    else: 
        print("Sorry that's not enough money. Money refunded.")
        return False ## if not enough money was inserted give back the coins


def deduct_resources(oreder_ingredience,answer):
    for item in oreder_ingredience:
        resources[item] -= oreder_ingredience[item]
    print(f"Here is yout {answer}")


is_on =True


while is_on:
    answer = input("What would you like? (espresso/latte/cappuccino): ")
    if answer == "off":
        is_on = False
    elif answer =="report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    elif answer in ["espresso", "latte", "cappuccino"]:
        drink = MENU[answer]  ##MENU[latte]
        if  check_ingredients(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_succesfull(payment,MENU[answer]["cost"]):
                deduct_resources(drink["ingredients"],answer)
                