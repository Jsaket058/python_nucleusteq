# 1. Create a class representing a Bank Account with deposit and withdraw methods.

class BankAccount:
    """
    A class to represent a simple bank account.
    """

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        """
        Deposit money into the account.
        """
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.balance += amount
        print(f"Deposited Rs{amount}. New balance: Rs{self.balance}")

    def withdraw(self, amount):
        """
        Withdraw money from the account.
        """
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        if amount > self.balance:
            print("Insufficient balance.")
            return
        self.balance -= amount
        print(f"Withdrew Rs{amount}. New balance: Rs{self.balance}")

    def get_balance(self):
        """
        Return current balance.
        """
        return self.balance

account = BankAccount("Saket", 1000)

account.deposit(500)
account.withdraw(300)
account.withdraw(1500)

print(f"Final balance: Rs{account.get_balance()}")
