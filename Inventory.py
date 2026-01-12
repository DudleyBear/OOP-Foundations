class Product:
    def __init__(self, name, price, quantity):
        self._name = name
        self._price = price if price >= 0 else 0
        self._quantity = quantity

    def sell(self, amount):
        if amount <= 0:
            print("Sale amount must be positive.")
        elif amount > self._quantity:
            print("Cannot sell more than available quantity.")
        else:
            self._quantity -= amount

    def restock(self, amount):
        if amount <= 0:
            print("Restock amount must be positive.")
        else:
            self._quantity += amount

    def get_product_info(self):
        return f"Product: {self._name}, Price: ${self._price}, Quantity: {self._quantity}"
