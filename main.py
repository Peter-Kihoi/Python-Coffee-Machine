from store import resources
from store import MENU


# check the resource sufficient
def check_resources(ingredients):
    for item in ingredients:
        if ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
        else:
            return True


# process coins
def process_coins(order):
    print("Please insert coins")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    total = (0.25 * quarters) + (0.1 * dimes) + (0.05 * nickles) + (0.01 * pennies)
    cost = MENU[order]["cost"]

    if total < cost:
        print("sorry that's not enough money. Money refunded....")
        return 0
    elif total > cost:
        change = total - cost
        print(f"Here is ${change:.2f} dollars in change")
        print(f"Here is your {order} ☕ enjoy")
        return cost
    else:
        return cost


def machine():
    money = 0
    should_continue = True

    while should_continue:
        # user by asking What would you like? (espresso/latte/cappuccino):
        order = input("What would you like? (espresso/latte/cappuccino):").lower()

        if order == "off":
            # Turn off the Coffee Machine by entering “off” to the prompt
            return
        elif order == "report":
            # print report
            print(f"water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"coffee: {resources['coffee']}g")
            print(f"money: ${money}")

        elif order == "latte" or order == "cappuccino" or order == "espresso":
            drink = MENU[order]
            check = check_resources(drink["ingredients"])
            if check:

                profit = process_coins(order)
                if profit != 0:
                    money += profit
                    if order == "cappuccino" or order == "latte":
                        resources["milk"] -= MENU[order]["ingredients"]["milk"]
                    resources["water"] -= MENU[order]["ingredients"]["water"]
                    resources["coffee"] -= MENU[order]["ingredients"]["coffee"]

        else:
            print("wrong input")


machine()
