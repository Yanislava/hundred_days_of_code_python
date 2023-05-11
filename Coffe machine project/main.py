from data import MENU, resources

MONEY = 0

coins = {'quarter': 0.25,
         'dime': 0.1,
         'nickle': 0.05,
         'pennie': 0.01,
         }


def turn_off():
    global IS_ON
    IS_ON = False
    return


def print_report():
    print(f"Water: {resources['water']}ml\n"
          f"Milk: {resources['milk']}ml\n"
          f"Coffee: {resources['coffee']}g\n"
          f"Money: ${MONEY}")


def get_command():
    valid_commands = list(('off', 'report'))
    valid_commands.extend(list(MENU.keys()))
    user_pick = input("What would you like?\n"
                      "cappuccino/espresso/latte\n").lower()
    if user_pick in valid_commands:
        return user_pick
    else:
        print('Invalid input')


def check_if_resource_sufficient(coffee_type):
    enough_ingredients = 0
    for ing, amount in MENU[coffee_type]['ingredients'].items():
        if resources[ing] >= MENU[coffee_type]['ingredients'][ing]:
            enough_ingredients += 1
        else:
            print(f'Sorry, not enough {ing}')
            break
    if enough_ingredients == len(MENU[coffee_type]['ingredients']):
        return True
    else:
        return False


def enter_coins():
    money_entered = 0
    for coin, nominal in coins.items():
        coins_entered = int(input(f'How many {coin}s do you have?'))
        money_entered += coins_entered * nominal
    return money_entered


def check_if_money_if_enough(coffee_type, money_entered):
    global MONEY
    cost = MENU[coffee_type]['cost']
    if money_entered >= cost:
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def add_money(cost):
    global MONEY
    MONEY += cost


def get_change(money_entered, cost):
    global MONEY
    change = 0
    change += round(money_entered - cost, 2)
    return change


def make_coffee(coffee_type):
    for ing, amount in MENU[coffee_type]['ingredients'].items():
        resources[ing] = resources[ing] - amount
    print(f'Here is your {coffee_type}. Enjoy!')


def operate_coffee_machine(command):
    if command == 'off':
        turn_off()
    elif command == 'report':
        print_report()
    elif command in MENU.keys():
        cost = MENU[command]['cost']
        if check_if_resource_sufficient(command):
            coins_entered = enter_coins()
            if check_if_money_if_enough(command, coins_entered):
                add_money(cost)
                change = get_change(coins_entered, cost)
                make_coffee(command)
                if change > 0:
                    print(f'Here is ${change} dollars in change.')
                

IS_ON = True

while IS_ON:
    operate_coffee_machine(get_command())
