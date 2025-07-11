class BankAccount:
    def __init__(self, account_balance, initial_balance= 0.0):
        self.account_balance = account_balance
        self.initial_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount
            return True
        else:
            return False

    def withdraw(self, amount):
        if 0 < amount <= self.account_balance:
            self.account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.2f}")