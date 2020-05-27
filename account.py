import math


class Account:

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Amount deposited successfully! Available balance is {self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Amount withdrawn successfully! Available balance is {self.balance}")
        else:
            print(f"Insufficient balance! Available balance is {self.balance}")

    def __str__(self):
        return f"Account Details:\n\n" \
               f"  Owner   : {self.owner}\n " \
               f"  Balance : {self.balance}"


acc1 = Account("Allan", 0)

print(acc1)

acc1.deposit(100)
acc1.deposit(50.43)
acc1.deposit(57)
acc1.deposit(1111)
acc1.withdraw(1300)
