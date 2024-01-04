# print("Thank you for choosing Python Pizza Deliveries!")
# size = input() # What size pizza do you want? S, M, or L
# add_pepperoni = input() # Do you want pepperoni? Y or N
# extra_cheese = input() # Do you want extra cheese? Y or N
# # 🚨 Don't change the code above 👆
# # Write your code below this line 👇

# total_bill = 0

# if size == "L":
#     total_bill += 25
# elif size == "M":
#     total_bill += 20
# else:
#     total_bill += 15

# if add_pepperoni == "Y" and size == "S":
#     total_bill += 2
# elif (add_pepperoni == "Y" and size == "M") or (add_pepperoni == "Y" and size == "L"):
#     total_bill += 3

# if extra_cheese == "Y":
#     total_bill += 1


# Other small exercise


# print("The Love Calculator is calculating your score...")
# name1 = input() # What is your name?
# name2 = input() # What is their name?
# # 🚨 Don't change the code above 👆
# # Write your code below this line 👇

# name1 = name1.lower()
# name2 = name2.lower()

# score1 = 0
# score2 = 0

# true_list = ["t", "r", "u", "e"]
# love_list = [ "l", "o", "v", "e"]


# for letter in name1:
#     if letter in true_list:
#         score1 += 1

# for letter in name2:
#     if letter in true_list:
#         score1 += 1


# for letter in name1:
#     if letter in love_list:
#         score2 += 1

# for letter in name2:
#     if letter in love_list:
#         score2 += 1


# sum = str(score1) + str(score2)

# if (int(sum) < 10) or (int(sum) > 90):
#     print(f"Your score is {sum}, you go together like coke and mentos.")
# elif (int(sum) > 40) and (int(sum) < 50):
#     print(f"Your score is {sum}, you are alright together.")
# else:
#     print(f"Your score is {sum}.")


# main day exercise
print(
    '''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
'''
)
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

# Write your code below this line 👇


choice1 = input("Choose left or right?").lower()

if choice1 == "left":
    choice2 = input("Choose wait or swim?").lower()
    if choice2 == "wait":
        choice3 = input("Choose red, yellow, blue?").lower()
        if choice3 == "red":
            print("You died from fire!")
        elif choice3 == "blue":
            print("You were eaten by a beast!")
        elif choice3 == "yellow":
            print("You WOOOOOON!")
        else:
            print("You died!")

    else:
        print("You died!")
else:
    print("You died!")
