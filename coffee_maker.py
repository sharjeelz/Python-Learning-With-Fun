print("KARAK CHAI MAKER")
is_machine_on = True
profit = 0
CURRENCY = "DHS"
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


def check_resources(order_ingredients, qty):
    for item in order_ingredients:
        if order_ingredients[item] * qty > resources[item]:
            print(f"Not Enough {item}, Please Ask on the counter to refill")
            return False
    return True


def process_coins():
    print("Insert coins")
    return float(input(f"Enter Dirhams: {CURRENCY}  "))


def is_payment_done(money, cost, qty):
    global profit
    if money >= cost:
        change = money - cost * qty
        print(f"here is your change {change} {CURRENCY} ")
        profit += cost
        return True
    else:
        print(f"Sorry that's not enough money.{money} {CURRENCY} refunded.")
        return False


def make_tea(drink_name, order_ingredients, qty):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item] * qty
    print(f"Here is your {drink_name} ☕️. Enjoy!")


def refill(missing_item):
    if missing_item == "water":
        resources[missing_item] = 1000
    elif missing_item == "tea":
        resources[missing_item] = 2000
    elif missing_item == "milk":
        resources[missing_item] = 4000
    print("Thank you sir, please proceed to machine, its refilled now")
    return True


while is_machine_on:
    choice = input("Enter  Your Choice  karak , sulemani: ").lower()
    if choice == "off":
        is_machine_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Tea: {resources['tea']}g")
        print(f"Money: ${profit}")
    elif choice == "karak" or choice == "sulemani":
        quantity = int(input(f"How many cups of {choice} would you like to have ? "))
        drink = MENU[choice]
        if check_resources(drink["ingredients"], quantity):
            payment = process_coins()
            if is_payment_done(payment, drink["cost"], quantity):
                make_tea(choice, drink["ingredients"], quantity)
        else:
            missing_ingredient = input("Welcome to counter, what is it that is missing from the machine? "
                                       "water, milk, tea ?").lower()
            if refill(missing_ingredient):
                continue

    else:
        print("Hey!!!!!!!!!!!! What are you doing")
