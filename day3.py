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

name1 = name1.lower()
name2 = name2.lower()

score1 = 0
score2 = 0

true_list = ["t", "r", "u", "e"]
love_list = [ "l", "o", "v", "e"]


for letter in name1:
    if letter in true_list:
        score1 += 1

for letter in name2:
    if letter in true_list:
        score1 += 1
        
    
for letter in name1:
    if letter in love_list:
        score2 += 1

for letter in name2:
    if letter in love_list:
        score2 += 1
        
        
sum = str(score1) + str(score2)

if (int(sum) < 10) or (int(sum) > 90):
    print(f"Your score is {sum}, you go together like coke and mentos.")
elif (int(sum) > 40) and (int(sum) < 50):
    print(f"Your score is {sum}, you are alright together.")
else:
    print(f"Your score is {sum}.")