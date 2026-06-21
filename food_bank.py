"""
food_bank.py — Non-profit Food Bank Stock Management System
"""


class FoodBankStock:
    """Manages stock inventory for a non-profit food bank."""

    def __init__(self):
        self._stock = {}
        self._active = True

    def is_active(self):
        return self._active

    def add_stock(self, item: str, quantity: int) -> bool:
        if quantity <= 0:
            raise ValueError("Quantity must be a positive integer")
        item = item.lower().strip()
        self._stock[item] = self._stock.get(item, 0) + quantity
        return True

    def get_stock(self, item: str) -> int:
        return self._stock.get(item.lower().strip(), 0)

    def allocate_to_beneficiary(self, item: str, quantity: int) -> bool:
        item = item.lower().strip()
        available = self.get_stock(item)
        if quantity > available:
            raise ValueError("Insufficient stock available")
        self._stock[item] -= quantity
        return True
