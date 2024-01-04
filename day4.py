# import random

# random_ingeger = random.randint(1,10)
# print(random_ingeger)


# random_float = random.random()
# print(random_float)


################# First class exercise:
# Write your code below this line 👇
# Hint: Remember to import the random module first. 🎲


# import random
# random_integer = random.randint(0,1)
# # print(random_integer)

# if random_integer == 1:
#     print("Heads")
# else:
#     print("Tails")

# ################# Second class exercise:
# names = names_string.split(", ")
# # The code above converts the input into an array seperating
# #each name in the input by a comma and space.
# # 🚨 Don't change the code above 👆

# number_of_people = len(names)
# random_person =  random.randint(0,number_of_people-1)

# print(f"{names[random_person]} is going to buy the meal today!")


################# Homework exercise:
import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

players_choice = int(
    input("What do yo u choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. ")
)
pc_choice = random.randint(0, 2)

if players_choice == 0:
    print(rock)
elif players_choice == 1:
    print(paper)
else:
    print(scissors)

print("Computer choose:")

if pc_choice == 0:
    print(rock)
elif pc_choice == 1:
    print(paper)
else:
    print(scissors)


if players_choice == 0 and pc_choice == 0:
    print("Draw")
elif players_choice == 0 and pc_choice == 1:
    print("You lose")
elif players_choice == 0 and pc_choice == 2:
    print("You win!")
elif players_choice == 1 and pc_choice == 0:
    print("You win!")
elif players_choice == 1 and pc_choice == 1:
    print("Draw")
elif players_choice == 1 and pc_choice == 2:
    print("You lose")
elif players_choice == 2 and pc_choice == 0:
    print("You lose!")
elif players_choice == 2 and pc_choice == 1:
    print("You win!")
elif players_choice == 2 and pc_choice == 2:
    print("Draw!")


# Write your code below this line 👇
