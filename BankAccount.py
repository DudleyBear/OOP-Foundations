class BankAccount:
    def __init__(self, balance=0):
        self._balance = balance  # private attribute

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
        else:
            self._balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self._balance:
            print("Insufficient balance. Cannot withdraw more than available.")
        else:
            self._balance -= amount

    def get_balance(self):
        return self._balance
