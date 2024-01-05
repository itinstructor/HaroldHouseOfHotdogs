# Harold's House of Hotdogs
# File: harolds_hotdogs_class_5.py
# Version: 5
# Description: Harold's House of Hotdogs class

# Cost of hotdog for the customer
HOTDOG_COST = 9.99


class HaroldsHotdogs:
    def __init__(self):
        self._qty_hotdogs = 0
        # Initialize parallel lists for menu items and prices
        self.menu_items = ["Hot Dog", "Crisps", "Soda", "Gourmet Ketchup"]
        self.menu_prices = [7.50, 1.00, 1.50, 10.00]
        # Initialize a parallel cart to store the current quantity
        self.cart = [0, 0, 0, 0]

# --------------------- CLASS PROPERTIES ----------------------------------#
    @property
    def name(self):
        return self._qty_hotdogs

    @name.setter
    def name(self, qty_hotdogs):
        self._qty_hotdogs = qty_hotdogs

    def get_menu_items(self) -> list:
        return self.menu_items

    def get_menu_prices(self) -> list:
        return self.menu_prices

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
        """Return menu items and prices as a string"""
        display = ""
        for n in range(len(self.menu_items)):
            # Increment for numbering of menu
            i = n + 1
            # Concatenate menu items for line by line display
            display += f"({i}) {self.menu_items[n]} {self.menu_prices[n]:.2f}\n"
        return display

# --------------------- DISPLAY ORDER -------------------------------------#
    def display_order(self) -> str:
        """Display menu items and prices"""
        # for n in range(3):
        #     print(f"{self.menu_items[n]} {self.menu_prices[n]}")
        display = ""
        for n in range(len(self.menu_items)):
            i = n + 1
            display += f"({i}) {self.menu_items[n]} {self.menu_prices[n]:.2f}\n"
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
        

    # def calculate
    #     for item, price, quantity in harold.cart:
    #     print(f"{item}: ${price:.2f} x {quantity} = ${price * quantity:.2f}")
