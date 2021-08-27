print("KARAK CHAI MAKER")
is_machine_on = True
profit = 0

MENU = {
    "karak": {
        "ingredients": {
            "water": 50,
            "tea": 10,
            "milk": 15
        },
        "cost": 2.0,
    },
    "sulemani": {
        "ingredients": {
            "water": 100,
            "tea": 50,

        },
        "cost": 1.5,
    }
}
resources = {
    "water": 300,
    "milk": 200,
    "tea": 100,
}


def check_resources(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Not Enough {item}")
            return False
    return True


def process_coins():
    print("Insert coins")
    return float(input("Enter Dirhams: "))


def is_payment_done(money, cost):
    global profit
    if money >= cost:
        change = money - cost
        print(f"here is your change {change}")
        profit += cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_tea(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


while is_machine_on:
    choice = input("Enter  Your Choice  karak , sulemani: ")
    if choice == "off":
        is_machine_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Tea: {resources['tea']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if check_resources(drink["ingredients"]):
            payment = process_coins()
            if is_payment_done(payment, drink["cost"]):
                make_tea(choice, drink["ingredients"])



