
from day15_menu import MENU, resources


def report():
    print(f" Water: {water_total}ml")
    print(f" Milk: {milk_total}ml")
    print(f" Coffee: {coffee_total}g")
    print(f" Money: ${money_total}")


def money_count(quarters_in, dimes_in, nickles_in, pennies_in):
    quarters = quarters_in * 0.25
    dimes = dimes_in * 0.10
    nickles = nickles_in * 0.05
    pennies = pennies_in * 0.01
    sum = quarters + dimes + nickles + pennies
    return sum


def check_resources(
    water_needed, milk_needed, coffee_needed, 
    water_resource, milk_resource, coffee_resource):
    water = False
    milk = False
    coffee = False
    text = None
    
    if water_resource >= water_needed:
        water = True
    if milk_resource >= milk_needed:
        milk = True
    if coffee_resource >= coffee_needed:
        coffee = True
        
    if water == True and milk == True and coffee == True:
        text = None
    elif water == False and milk == True and coffee == True:
        text = "Sorry there is not enough water"
    elif water == True and milk == False and coffee == True:
        text = "Sorry there is not enough milk"
    elif water == True and milk == True and coffee == False:
        text = "Sorry there is not enough coffee"
    elif water == False and milk == False and coffee == True:
        text = "Sorry there is not enough water and milk"
    elif water == True and milk == False and coffee == False:
        text = "Sorry there is not enough milk and coffee"
    elif water == False and milk == True and coffee == False:
        text = "Sorry there is not enough water and coffee"
    elif water == False and milk == False and coffee == False:
        text = "Sorry there is not enough water, milk, and coffee"
    return text
    
    
def retrieve_recipe(name):
    water = MENU[name]['ingredients']['water']
    milk = MENU[name]['ingredients'].get('milk', 0)
    coffee = MENU[name]['ingredients']['coffee']
    cost = MENU[name]['cost']
    return water, milk, coffee, cost
    
    
def coffee_machine(coffee_choice):
    global water_total
    global milk_total
    global coffee_total
    global money_total
    
    water, milk, coffee, cost = retrieve_recipe(coffee_choice)
    text = check_resources(
        water_resource=water_total, water_needed=water, 
        milk_resource=milk_total, milk_needed=milk,
        coffee_resource=coffee_total, coffee_needed=coffee)
    if text == None:
        quarters_input = int(input("How many quarters: "))
        dimes_input = int(input("How many dimes: "))
        nickles_input = int(input("How many nickles: "))
        pennies_input = int(input("How many pennies]: "))
        total_input_money = money_count(quarters_in=quarters_input, 
                    dimes_in=dimes_input, 
                    nickles_in=nickles_input, 
                    pennies_in=pennies_input)
        if total_input_money >= cost:
            water_total -= water
            milk_total -= milk
            coffee_total -= coffee
            money_total += cost
            refund = total_input_money - cost
            print(f"Here is ${refund:.2f} dollars in change.")
            print(f"Here is your {coffee_choice}. Enjoy!")
        else:
            quarters_input = 0
            dimes_input = 0
            nickles_input = 0
            pennies_input = 0
            print("Sorry that's not enough money. Money Refunded")
    else:
        print(text)
    

water_total = resources['water'] #300
milk_total = resources['milk'] #200
coffee_total = resources['coffee'] #100
money_total = 0.0

off_fuctionality = False


while off_fuctionality == False:
    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_input == "espresso":
        coffee_machine(user_input)
    elif user_input == "latte":
        coffee_machine(user_input)
    elif user_input == "cappuccino":
        coffee_machine(user_input)
    elif user_input == "report":
        report()
    elif user_input == "off":
        off_fuctionality = True
    
    
    



