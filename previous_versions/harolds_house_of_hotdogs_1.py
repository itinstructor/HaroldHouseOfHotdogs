# Harold's Hotdog House
# File: harold_hotdog_house_1.py
# Version: 1
# Description: POS program

# Cost of hotdog for the customer
HOTDOG_COST = 8.99

# TODO: Get int input from user how many hot dogs sold
number_of_hotdogs = int(input("Enter number of hotdogs: "))

# TODO: Calculate cost of the hotdogs purchased
total_receipt = number_of_hotdogs * HOTDOG_COST

# TODO: Display transaction for customer
print(f"Your meal was: ${total_receipt:,.2f}")
