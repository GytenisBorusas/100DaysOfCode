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


# -------------- Third class exercise: --------------


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




country = input() # Add country name
visits = int(input()) # Number of visits
list_of_cities = eval(input()) # create list from formatted string

travel_log = [
  {
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
  },
  {
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
  },
]
# Do NOT change the code above 👆

# TODO: Write the function that "will allow new countries
# to be added to the travel_log. 
def add_new_country(func_country, func_visits, func_list_of_cities):
    travel_log.append({"country": func_country, "visits": func_visits, "cities": func_list_of_cities})
    # print(travel_log)

# Do not change the code below 👇
add_new_country(country, visits, list_of_cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")






