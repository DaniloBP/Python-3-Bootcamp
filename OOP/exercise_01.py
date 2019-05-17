# Bank Account OOP exercise.

class BankAccount:
    
    def __init__(self, name):
        self.owner = name
        self.balance = 0.0

    def deposit(self, amount):
    	self.balance += amount
    	return self.balance

    def withdraw(self, amount):
    	self.balance -= amount
    	return self.balance

account = BankAccount("Sam")
print(account.owner)

balance = account.deposit(10300)
print(f"R$ {balance}")

balance = account.withdraw(350)
print(f"R$ {balance}")