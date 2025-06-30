class BankAccount:
    def __init__(self, account_balance, initial_balance=0):
        self.account_balance = account_balance
        self.initial_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount
            return self.account_balance
        else:
            raise ValueError("Deposit amount must be positive")

    def withdraw(self, amount):
        if 0 < amount <= self.account_balance:
            self.account_balance -= amount
            return self.account_balance
        else:
            return False
        
    def display_balance(self):
        print("Current balance:", "$" + str(self.account_balance))