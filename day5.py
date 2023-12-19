# -------------- First class exercise: --------------

# Input a Python list of student heights
# student_heights = input().split()
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])
# # 🚨 Don't change the code above 👆
  
# # Write your code below this row 👇
# total_height = 0
# total_student_count = 0

# for student in student_heights:
#     total_height = total_height + int(student)
#     total_student_count += 1
    
# avg_height = round(total_height / total_student_count)

# print(f"total height = {total_height}")
# print(f"number of students = {total_student_count}")
# print(f"average height = {avg_height}")




# -------------- Second class exercise: --------------


# # Input a list of student scores
# student_scores = input().split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])

# # Write your code below this row 👇
# highest_score = 0

# for score in student_scores:
#     if int(score) > int(highest_score):
#         highest_score = score

# print(f"The highest score in the class is: {highest_score}")


# -------------- Third class exercise: --------------

# target = int(input()) # Enter a number between 0 and 1000
# # 🚨 Do not change the code above ☝️

# # Write your code here 👇

# total = 0

# for number in range(0, target+1, 2):
#     total += number
    
# print(total)


# -------------- Fourth class exercise: --------------

# Write your code here 👇

# for number in range(1, 101):
#     if number % 3 == 0:
#         if number % 5 == 0:
#             print("FizzBuzz")
#         else:
#             print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)

# -------------- Homework exercise: --------------

# Write your code here 👇

#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

