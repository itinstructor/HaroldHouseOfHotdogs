# Harold's House of Hotdogs
# File: harolds_hotdogs_class_6.py
# Version: 6
# Description: Harold's House of Hotdogs class


class HaroldsHotdogs:
    def __init__(self):
        self._qty_hotdogs = 0
        # Initialize parallel lists for menu items and prices
        self.menu_items = ["Hot Dog", "Crisps", "Soda", "Gourmet Ketchup"]
        self.menu_prices = [7.50, 1.00, 1.50, 10.00]

        # Parallel cart list to store the current purchase quantity
        self.cart = [0, 0, 0, 0]

# --------------------- CLASS PROPERTIES ----------------------------------#
    @property
    def name(self):
        return self._qty_hotdogs

    @name.setter
    def name(self, qty_hotdogs):
        self._qty_hotdogs = qty_hotdogs

    def get_menu_items(self) -> list:
        """Return menu items as a list"""
        return self.menu_items

    def get_menu_prices(self) -> list:
        """Return menu prices as a list"""
        return self.menu_prices

    def __str__(self) -> str:
        """A string representation of the class. This normally
           prints the reference memory address
        """
        # return f"Shopping cart: {self.cart}"
        str_cart = ""
        for i in range(len(self.cart)):
            item = self.menu_items[i]
            quantity = self.cart[i]
            price = self.menu_prices[i]
            str_cart += f"{item}: ${price:.2f} x {quantity} "
            str_cart += f"${price * quantity:.2f}\n"
        return str_cart

# --------------------- ADD ITEMS TO CART ---------------------------------#
    def add_to_cart(self, choice: int, quantity: int) -> str:
        """Add items choice (list) and quantity to cart. 

           Parameters:
              choice (int):    Index number of list item  
              quantity (int):  How many items purchased

           Returns:
              cart_item (str): String representation of cart
        """
        try:
            index = int(choice) - 1
            if 0 <= index < len(self.menu_items):
                item = self.menu_items[index]
                price = self.menu_prices[index]
                # self.cart.append((item, price, quantity))
                self.cart[index] = quantity + self.cart[index]
                cart_item = f"{quantity} {item}(s) added to the cart."
                return cart_item
            else:
                print("Invalid choice. Please select a valid item number.")
        except ValueError:
            print("Invalid input. Please enter a valid item number.")

# --------------------- DISPLAY MENU --------------------------------------#
    def display_menu(self) -> str:
        """
        Return a string representation of the menu items and their prices.

        Returns:
            str: A string containing the menu items and their prices.

        Example Usage:
            hotdogs = HaroldsHotdogs()
            menu = hotdogs.display_menu()
            print(menu)

        Expected Output:
            (1) Hot Dog 7.50
            (2) Crisps 1.00
            (3) Soda 1.50
            (4) Gourmet Ketchup 10.00
        """
        display = ""
        for n in range(len(self.menu_items)):
            # Increment for numbering of menu
            i = n + 1
            # Concatenate menu items for line by line display
            display += f"({i}) {self.menu_items[n]} "
            display += f"{self.menu_prices[n]:.2f}\n"
        return display

# --------------------- CALCULATE TOTAL -----------------------------------#
    def calculate_total(self):
        """Calculate cost of items purchased

            Returns:
                total cost of items
        """
        # total = sum(price * quantity for _, price, quantity in self.cart)
        self.total = 0
        for i in range(3):
            self.total += self.cart[i] * self.menu_prices[i]
