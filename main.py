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

profit = 0


# TODO 1: check if there are enough resources
def check_resources(drink):
    ingredients_needed = drink.get('ingredients')
    if resources["water"] < ingredients_needed["water"]:
        print("The machine does not have enough water to make your drink.")
        return False
    if "milk" in ingredients_needed:
        if resources["milk"] < ingredients_needed["milk"]:
            print("The machine does not have enough milk to make your drink.")
            return False
    if resources["coffee"] < ingredients_needed["coffee"]:
        print("The machine does not have enough coffee to make your drink.")
        return False
    return True


# TODO 2: Reduce the resources after an order has been made
def reduce_resources(drink):
    ingredients_needed = drink.get('ingredients')
    resources["water"] -= ingredients_needed["water"]
    if "milk" in ingredients_needed:
        resources["milk"] -= ingredients_needed["milk"]
    else:
        resources["milk"] = resources["milk"]
    resources["coffee"] -= ingredients_needed["coffee"]
    return resources


# TODO 3: Create the looping function that accept the coins and reduce the amount in the resources.
#  If any ingredient goes down to zero, break the loop because the machine is now out of service
def run_machine():
    global profit
    while True:

        user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if user_input == "report":
            print(resources)
            input("Press ENTER to continue...\n")
            continue

        if user_input == "off":
            print("The coffee machine is now turning off.")
            break

        if user_input in MENU:
            selected_drink = MENU[user_input]
            if check_resources(selected_drink):
                quarters = int(input("How many quarters would you like to put in? ($0.25): "))
                dimes = int(input("How many dimes would you like to put in? ($0.15): "))
                nickels = int(input("How many nickels would you like to put in? ($0.05): "))
                pennies = int(input("How many pennies would you like to put in? ($0.01): "))
                amount_paid = (quarters * 0.25) + (dimes * 0.15) + (nickels * 0.05) + (pennies * 0.01)

                if amount_paid < selected_drink["cost"]:
                    print("\nSorry, that's not enough. Money refunded")
                else:
                    cost_of_drink = selected_drink["cost"]
                    change = round((amount_paid - cost_of_drink), 2)
                    print(f"\nHere's your change: ${change}")

                    profit += cost_of_drink
                    reduce_resources(selected_drink)
                    profit_string = "$" + str(profit)
                    resources["profit"] = profit_string

                    print(f"Here's {user_input}. ☕ Enjoy!\n")
                    input("Press a ENTER to continue...")

                    if resources["water"] == 0 or resources["milk"] == 0 or resources["coffee"] == 0:
                        if resources["water"] == 0:
                            out_of_stock = "water"
                            print(f"\nSorry, the machine is out of {out_of_stock}.\n 🛑Please turn off the machine. 🛑")
                        if resources["milk"] == 0:
                            out_of_stock = "milk"
                            print(
                                f"\nSorry, the machine is out of {out_of_stock}.\n🛑Please turn off the machine. 🛑")
                        if resources["coffee"] == 0:
                            out_of_stock = "coffee"
                            print(
                                f"\nSorry, the machine is out of {out_of_stock}.\n🛑Please turn off the machine. 🛑")
                        print(resources)


run_machine()
