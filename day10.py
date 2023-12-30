# -------------- Class work --------------

# def format_name(f_name, l_name):
#     formatted_f_name = f_name.title()
#     formatted_l_name = l_name.title()
#     print(formatted_f_name, formatted_l_name)
    
    
# format_name("asdas", "dgfhdfgh")

# -------------- First class work exercise --------------


# def is_leap(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 return True
#                 print("Leap year")
#             else:
#                 return False
#                 print("Not leap year")
#         else:
#             return True
#             print("Leap year")
#     else:
#         return False
#         print("Not leap year")
  
# # TODO: Add more code here 👇
# def days_in_month(year, month):
#     month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
#     if is_leap == False:
#         return month_days[month-1]
#     else:
#         if month == int(2):
#             return int(29)
#         else:
#             return month_days[month-1]
  
# #🚨 Do NOT change any of the code below 
# year = int(input()) # Enter a year
# month = int(input()) # Enter a month
# days = days_in_month(year=year, month=month)
# print(days)



# -------------- Home class work exercise --------------

from replit import clear
from art import logo

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator():
  print(logo)

  num1 = float(input("What's the first number?: "))
  for symbol in operations:
    print(symbol)
  should_continue = True
 
  while should_continue:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")

    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
      num1 = answer
    else:
      should_continue = False
      clear()
      calculator()

calculator()
