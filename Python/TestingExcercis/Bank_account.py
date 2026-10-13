class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal must be positive")

        if amount > self.balance:
            raise ValueError("Insufficient funds")

        self.balance -= amount

    def get_balance(self):
        return self.balance

    