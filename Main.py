import art

MENU = {
    'espresso': {
        'ingredients':{
            'water':50,
            'milk': 0,
            'coffee': 18,    
        },
        'cost' : 1.5,
    },
    'latte': {
        'ingredients':{
            'water':200,
            'milk': 150,
            'coffee': 24,
        },
        'cost': 2.5 

    },
    'cappuccino': {
        'ingredients':{
            'water':250,
            'milk': 100,
            'coffee': 24,
        },
        'cost':3.0
    },
}
profit = 0 
resources = {
    'water': 300,        
    'milk': 200,
    'coffee': 100,
}

def is_resource_suffi(order):
    """Return True when order can be made, False if ingredients is insufficient"""
    for item in order["ingredients"]:
        if order["ingredients"][item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True


def process_coins():
    """Returns the total calculates from coins inserted"""
    print("Please insert coins: ")
    total = 0
    total += int(input("How many $0.25? ")) * 0.25
    total += int(input("How many $0.10? ")) * 0.10
    total += int(input("How many $0.05? ")) * 0.05
    total += int(input("How many $0.01? ")) * 0.01
    return total

def show_info():

    for item in MENU:
        print(f"{item}:")
        print(f"Water: {MENU[item]["ingredients"]["water"]}ml")
        print(f"Milk: {MENU[item]["ingredients"]["milk"]}ml")
        print(f"Coffee: {MENU[item]["ingredients"]["coffee"]}ml")
        print(f"Cost: ${MENU[item]["cost"]}")
        print("\n")

def is_transaction_successful(money_received, drinks_cost):
    """Return true if the payment is accepted, or False if money is insufficient"""
    if money_received >=drinks_cost:
        change = round(money_received - drinks_cost, 2)
        print(f"Here is ${change} in change.")

        global profit
        profit += drinks_cost
        return True
    else:
        print("Sorry, that not enough money. Money refunded") 
        return False

def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}.")


choice =''
print(art.logo)
while choice.lower() != 'off':
    choice = input("What would you like? (espresso / latte / cappuccino): ")
    if choice == 'report':
        for resource in resources:
            print(f"{resource}: {resources[resource]}")
        print(f"Money: ${profit}")
    elif choice == 'info':
        show_info()
    else:
        drink = MENU[choice]
        print(f"{choice} selected. Cost: {MENU[choice]["cost"]}")
        if is_resource_suffi(drink):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])

        