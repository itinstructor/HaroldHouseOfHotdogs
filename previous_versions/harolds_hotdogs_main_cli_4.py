# Harold's House of Hotdogs
# File: harolds_hotdogs_main_cli.py
# Version: 4
# Description: Main program
import harolds_hotdogs_class_4 as hotdog


def get_input():
    # TODO: Get int input from user how many hot dogs sold
    number_of_hotdogs = int(input("Enter number of hotdogs: "))
    return number_of_hotdogs


def display():
    # TODO: Display transaction for customer
    number_of_hotdogs = harolds_hotdogs.get_number_hotdogs()
    total_sale = harolds_hotdogs.get_total_sale()

    print(f"Number of hotdogs: {number_of_hotdogs}")
    print(f"Your total: ${total_sale:,.2f}")


# Get number of hotdogs from user
number_of_hotdogs = get_input()

# Create HaroldsHotdogs object
harolds_hotdogs = hotdog.HaroldsHotdogs()

# Calculat the number of hotdogs
harolds_hotdogs.calculate(number_of_hotdogs)

# Display the results of the transaction
display()
