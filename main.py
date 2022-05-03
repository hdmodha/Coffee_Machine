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
    "money": 0
}


def check_resources_for(a_coffee):
    if a_coffee == 'espresso':
        if resources['water'] >= MENU[a_coffee]['ingredients']['water']:
            if resources['coffee'] >= MENU[a_coffee]['ingredients']['coffee']:
                return True
            else:
                return False
        else:
            return False
    else:
        if resources['water'] >= MENU[a_coffee]['ingredients']['water']:
            if resources['milk'] >= MENU[a_coffee]['ingredients']['milk']:
                if resources['coffee'] >= MENU[a_coffee]['ingredients']['coffee']:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False


def check_money(quarters, dimes, nickles, pennies, usr_choice):
    user_money = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    if user_money < MENU[usr_choice]['cost']:
        print("Enter sufficient amount")
    else:
        resources['money'] += MENU[usr_choice]['cost']
        change = (user_money - MENU[usr_choice]['cost'])
        change = round(change, 2)
        print(f"Here is your ${change} change")
        return True


should_continue = True
while should_continue:
    choice = input("What would you like? (espresso/latte/cappuccino)").lower()
    if choice == 'off':
        should_continue = False

    elif choice == 'report':
        print(f"Water: {resources['water']}")
        print(f"Milk: {resources['milk']}")
        print(f"Coffee: {resources['coffee']}")
        print(f"Money: {resources['money']}")

    elif choice == 'espresso':
        if check_resources_for(a_coffee=choice):
            money_quarters = float(input("Enter number of quarters: "))
            money_dimes = float(input("Enter number of dimes: "))
            money_nickles = float(input("Enter number of nickles: "))
            money_pennies = float(input("Enter number of pennies: "))
            if check_money(money_quarters, money_dimes, money_nickles, money_pennies, choice):
                resources['water'] -= MENU[choice]['ingredients']['water']
                resources['coffee'] -= MENU[choice]['ingredients']['coffee']
                print(f"Here is your {choice} coffee, enjoy!!!")
        else:
            if resources['water'] < MENU[choice]['ingredients']['water'] or resources['water'] == 0:
                print("There is not enough water")
            elif resources['coffee'] < MENU[choice]['ingredients']['coffee'] or resources['coffee'] == 0:
                print("There is not enough coffee")

    elif choice == 'latte':
        if check_resources_for(a_coffee=choice):
            money_quarters = float(input("Enter number of quarters: "))
            money_dimes = float(input("Enter number of dimes: "))
            money_nickles = float(input("Enter number of nickles: "))
            money_pennies = float(input("Enter number of pennies: "))
            if check_money(money_quarters, money_dimes, money_nickles, money_pennies, choice):
                resources['water'] -= MENU[choice]['ingredients']['water']
                resources['milk'] -= MENU[choice]['ingredients']['milk']
                resources['coffee'] -= MENU[choice]['ingredients']['coffee']
                print(f"Here is your {choice} coffee, enjoy!!!")
        else:
            if resources['water'] < MENU[choice]['ingredients']['water'] or resources['water'] == 0:
                print("There is not enough water")
            elif resources['coffee'] < MENU[choice]['ingredients']['coffee'] or resources['coffee'] == 0:
                print("There is not enough coffee")
            elif resources['milk'] < MENU[choice]['ingredients']['milk'] or resources['milk'] == 0:
                print("There is not enough milk")

    elif choice == 'cappuccino':
        if check_resources_for(a_coffee=choice):
            money_quarters = float(input("Enter number of quarters: "))
            money_dimes = float(input("Enter number of dimes: "))
            money_nickles = float(input("Enter number of nickles: "))
            money_pennies = float(input("Enter number of pennies: "))
            if check_money(money_quarters, money_dimes, money_nickles, money_pennies, choice):
                resources['water'] -= MENU[choice]['ingredients']['water']
                resources['milk'] -= MENU[choice]['ingredients']['milk']
                resources['coffee'] -= MENU[choice]['ingredients']['coffee']
                print(f"Here is your {choice} coffee, enjoy!!!")
        else:
            if resources['water'] < MENU[choice]['ingredients']['water'] or resources['water'] == 0:
                print("There is not enough water")
            elif resources['coffee'] < MENU[choice]['ingredients']['coffee'] or resources['coffee'] == 0:
                print("There is not enough coffee")
            elif resources['milk'] < MENU[choice]['ingredients']['milk'] or resources['milk'] == 0:
                print("There is not enough milk")
    else:
        print("Enter a valid input! ")
