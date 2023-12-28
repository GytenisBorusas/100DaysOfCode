# -------------- First class exercise: --------------

# programming_dictionary = {
#     "Bug": "An error in a program that prevents the program from running as expected.", 
#     "Function": "A piece of code that you can easily call over and over again.",
#     }

# #Retrieving item from dictionary
# # print(programming_dictionary["Function"])

# #adding new items to dictionary
# programming_dictionary["Loop"] = "The action of doing something over and over again"
# print(programming_dictionary)

# #crete an empty dictionary.
# empty_dictionary = {}
# print(empty_dictionary)


# # #Wipe an existing dictionary
# # programming_dictionary = {}
# # print(programming_dictionary)

# #edit an item a dictionary
# programming_dictionary["Bug"] = "A month in your computer"
# print(programming_dictionary)

# #loop through a dictionary
# for key in programming_dictionary:
#     print(key)
#     print(programming_dictionary[key])
    
    
    
    
# -------------- Second class exercise: --------------
    
# student_scores = {
#   "Harry": 81,
#   "Ron": 78,
#   "Hermione": 99, 
#   "Draco": 74,
#   "Neville": 62,
# }
# # 🚨 Don't change the code above 👆
# # TODO-1: Create an empty dictionary called student_grades.
# student_grades = {}

# # TODO-2: Write your code below to add the grades to student_grades.👇
# for key in student_scores:
#     grade = "Fail"
#     if student_scores[key] > 90:
#         student_grades[key] = "Outstanding"
#     elif student_scores[key] > 80:
#         student_grades[key] = "Exceeds Expectations"
#     elif student_scores[key] > 70:
#         student_grades[key] = "Acceptable"
#     else:
#         student_grades[key] = "Fail"

# # 🚨 Don't change the code below 👇
# print(student_grades)


# -------------- Class work: --------------


# #Nesting Dictionary in a Dictionary

# travel_log = {
#   "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
#   "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
# }

# #Nesting Dictionaries in Lists

# travel_log = [
# {
#   "country": "France", 
#   "cities_visited": ["Paris", "Lille", "Dijon"], 
#   "total_visits": 12,
# },
# {
#   "country": "Germany",
#   "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
#   "total_visits": 5,
# },
# ]

# -------------- Third class exercise: --------------


# country = input() # Add country name
# visits = int(input()) # Number of visits
# list_of_cities = eval(input()) # create list from formatted string

# travel_log = [
#   {
#     "country": "France",
#     "visits": 12,
#     "cities": ["Paris", "Lille", "Dijon"]
#   },
#   {
#     "country": "Germany",
#     "visits": 5,
#     "cities": ["Berlin", "Hamburg", "Stuttgart"]
#   },
# ]
# # Do NOT change the code above 👆

# # TODO: Write the function that "will allow new countries
# # to be added to the travel_log. 
# def add_new_country(func_country, func_visits, func_list_of_cities):
#     travel_log.append({"country": func_country, "visits": func_visits, "cities": func_list_of_cities})
#     # print(travel_log)

# # Do not change the code below 👇
# add_new_country(country, visits, list_of_cities)
# print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
# print(f"My favourite city was {travel_log[2]['cities'][0]}.")



# -------------- Homework exercise: --------------

from day9_art import logo
#to create a local clear_screen function()
import os
import platform

print(logo)
print("Welcome to the secret auction program.")

#clear screen function
def clear_screen():
    if platform.system() == "Windows":
        os.system('cls')  # For Windows
    else:
        os.system('clear')  # For Unix/Linux/MacOS


def highest_bidder():
    highest_bidder_name = "none"
    highest_bidder_bid = 0
    
    for key in bidders_dict:
        if bidders_dict[key] > highest_bidder_bid:
            highest_bidder_bid = bidders_dict[key]
            highest_bidder_name = key
            
    print(f"The winner is {highest_bidder_name} with a bid of ${highest_bidder_bid}")



#initialization
bidders_dict = {}
more_bidders = "yes"


while more_bidders == "yes":
    #get user information
    name = input("What's your name?: ")
    bid = int(input("What's your bid?: "))

    #store user data in a dict
    bidders_dict[name] = bid

    more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.")
    clear_screen()
    
    

print(bidders_dict)

highest_bidder()
    
















