# Harold's Hotdog House
# File: harold_hotdog_house_2.py
# Version: 1
# Description: Functional POS program

# Cost of hotdog for the customer
HOTDOG_COST = 8.99


def main():
    num_of_hotdogs = get_input()
    total_sale = calculate(num_of_hotdogs)
    display(total_sale)


def get_input():
    # TODO: Get int input from user how many hot dogs sold
    number_of_hotdogs = int(input("Enter number of hotdogs: "))
    return number_of_hotdogs


def calculate(number_of_hotdogs):
    # TODO: Calculate cost of the hotdogs purchased
    total_sale = number_of_hotdogs * HOTDOG_COST
    return total_sale


def display(total_sale):
    # TODO: Display transaction for customer
    print(f"Your meal was: ${total_sale:,.2f}")


if __name__ == '__main__':
    main()
