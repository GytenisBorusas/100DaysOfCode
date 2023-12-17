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
    




# Other exercise


print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

score1 = 0
score2 = 0

letter_list = ("t", "r", "u", "e", "l", "o"", "v"", "e")


for letters in name1:
    if name1 == letter_list:
        score1 =+ 1
    
for letters in name2:
    if name2 == letter_list:
        score2 =+ 1
        
print(f"{score1} {score2}")