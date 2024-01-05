# Harold's House of Hotdogs
# File: harolds_hotdogs_class_4.py
# Version: 4
# Description: Harold's House of Hotdogs class

# Cost of hotdog for the customer
HOTDOG_COST = 9.99


class HaroldsHotdogs:
    def __init__(self):
        pass

    def get_number_hotdogs(self):
        """Input validation-the customer must order
        # at least one hotdog"""
        if self._number_of_hotdogs > 0:
            return self._number_of_hotdogs
        else:
            return "You must order at least one hotdog."

    def get_total_sale(self):
        """Return total sale"""
        return self._total_sale

    def calculate(self, number_of_hotdogs):
        """Calculate cost of the hotdogs purchased"""
        self._number_of_hotdogs = number_of_hotdogs
        self._total_sale = self._number_of_hotdogs * HOTDOG_COST
