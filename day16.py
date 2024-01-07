


# # from turtle import Turtle, Screen




# # timmy = Turtle()
# # print(timmy)
# # timmy.shape("turtle")
# # timmy.color("coral", "green")

# # print(timmy.position())
# # timmy.forward(100)
# # print(timmy.position())



# # my_screen = Screen()
# # print(my_screen.canvheight)
# # my_screen.exitonclick()



# from prettytable import PrettyTable

# table = PrettyTable()

# table.field_names = ["Pokemon Name", "Type"]
# table.add_row(["Pikachu", "Electric"])
# table.add_row(["Squirtle", "Water"])
# table.add_row(["Charmander", "Fire"])
# table.align = "l"



# print(table)


# ----------------- Homework ------------------------

from day16_menu import Menu, MenuItem
from day16_coffee_maker import CoffeeMaker
from day16_money_machine import MoneyMachine


coffe_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()

is_on = True


while is_on == True:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffe_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffe_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffe_maker.make_coffee(drink)
    







