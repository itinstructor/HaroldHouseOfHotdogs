# Harold's Hotdog House
# File: harold_hotdog_house_3_oop.py
# Version: 1
# Description: Functional POS program

# Cost of hotdog for the customer
HOTDOG_COST = 9.99


class HaroldsHotdogs:
    def __init__(self):
        pass

    def get_input(self):
        # TODO: Get int input from user how many hot dogs sold
        self.number_of_hotdogs = int(input("Enter number of hotdogs: "))

    def calculate(self):
        # TODO: Calculate cost of the hotdogs purchased
        self.total_sale = self.number_of_hotdogs * HOTDOG_COST

    def display(self):
        # TODO: Display transaction for customer
        print(f"Your meal was: ${self.total_sale:,.2f}")


harolds_hotdogs = HaroldsHotdogs()
harolds_hotdogs.get_input()
harolds_hotdogs.calculate()
harolds_hotdogs.display()
