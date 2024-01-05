"""
    Harold's House of Hotdogs
    File: harolds_hotdogs_main_cli_5.py
    Version: 5
    Description: Main program
"""
import harolds_hotdogs_class_5 as hotdog


# Main ordering loop
def start_ordering():
    while True:
        # Print the menu for each item order
        print(harold.display_menu())
        choice = input(
            "Enter an item to order (q to quit): ").lower()

        if choice == 'q':
            break

        quantity = int(input("Enter the quantity: "))

        # Add ordered item to cart
        # Return cart item string for purchase confirmation
        cart_item = harold.add_to_cart(choice, quantity)
        # print(harold.cart)
        print(cart_item)


# Generate a receipt
def generate_receipt():
    harold.calculate_total()
    print("\nReceipt:")
    
    # loop through each item in the cart
    # for item, price, quantity in harold.cart:
    #     print(f"{item}: ${price:.2f} x {quantity} = ${price * quantity:.2f}")
    print(f"Total: ${harold.total:.2f}")
    print("Thank you for your order!")


# Create HaroldsHotdogs object
harold = hotdog.HaroldsHotdogs()
start_ordering()
generate_receipt()
