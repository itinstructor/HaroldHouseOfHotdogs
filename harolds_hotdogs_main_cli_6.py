"""
    Harold's House of Hotdogs
    File: harolds_hotdogs_main_cli_6.py
    Version: 6
    Description: Main program
"""
from rich.panel import Panel
from rich.console import Console
import pickle
import rich
import harolds_hotdogs_class_6 as hotdog
FILE_NAME = "harold.pkl"
# Import Console for console printing
from rich.console import Console
# Import Panel for title displays
from rich.panel import Panel
# Initialize rich.console
console = Console()


# ---------------------- MAIN MENU ----------------------------------------#
def main_menu():
    """Main menu"""
    while True:
        console.print(
            Panel.fit(
                " Harold's House of Hotdogs ",
                style="bold blue",
                subtitle="By William Loring")
        )
        print(" (O)rder")
        print(" (S)ave data")
        print(" (L)oad data")
        print(" E(x)it")

        # Convert string input to lower case for easy comparison
        choice = input("Enter your choice: ").lower()

        if choice == 'o':
            start_ordering()
        elif choice == 's':
            save_data()
        elif choice == 'l':
            load_data()
        elif choice == 'x':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")


# ---------------------- ORDER LOOP ---------------------------------------#
def start_ordering():
    """Start the ordering menu"""
    while True:
        # Print the menu for each item order
        print(harold.display_menu())
        # User choose to order another item or quit the order loop
        choice = input(
            "Enter an item to order (q to finish): ").lower()

        if choice == 'q':
            break

        quantity = int(input("Enter the quantity: "))

        # Add ordered item to cart
        # Return cart item string for purchase confirmation
        cart_item = harold.add_to_cart(choice, quantity)
        # print(harold.cart)
        print(cart_item)

    generate_receipt()


# ---------------------- RECEIPT ------------------------------------------#
def generate_receipt():
    """Calculate and display a receipt"""
    harold.calculate_total()
    print("\nReceipt:")
    # Use the __str__ method to print the shopping cart
    print(harold)

    print(f"Total: ${harold.total:.2f}")
    print("Thank you for your order!")


# ---------------------- SAVE DATA ----------------------------------------#
def save_data():
    # Pickle harold
    with open(FILE_NAME, "wb") as file_handle:
        pickle.dump(
            harold,
            file_handle,
            -1
        )
    # Use the __str__ method to print the shopping cart
    print(harold)


# ---------------------- LOAD DATA ----------------------------------------#
def load_data():
    """Unpickle data from file"""
    with open(FILE_NAME, "rb") as file_handle:
        harold = pickle.load(file_handle)
    # Use the __str__ method to print the shopping cart
    print(harold)


# Create HaroldsHotdogs object
harold = hotdog.HaroldsHotdogs()
# Call main menu
main_menu()
