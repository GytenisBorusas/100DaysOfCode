print("Welcome to the tip calculator.")

total_bill = input("What was the total bill? $")

tip = input("What percentage tip would you like to give? 10, 12, or 15? ")

group_count = input("How many people to split the bill? ")

tip = int(tip) / 100 + 1

bill_for_each_member = float(total_bill) * float(tip) / float(group_count)

print(f"Each person should pay: {bill_for_each_member:.2f}")
