import subprocess

def clear_term():
    subprocess.run(["powershell", "Clear-Host"])

class Account:
    def __init__(self, name, number, balance):
        self.name = name
        self.number = number
        self.balance = balance

    def account_info(self):
        print("Name:", self.name)
        print("Number:", self.number)
        print("Balance:", self.balance)

    def withdraw(self, amount):
        if (self.balance - amount < 0):
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(amount, " withdrawn, new balance:", self.balance)

    def deposit(self, amount):
        self.balance += amount
        print(amount, " deposited, new balance:", self.balance)

acc = Account("Berkay Kocak", 170777, 1000)

while True:
    choice = int(input("What operation would you like to perform? (To view account information, enter 1, to deposit money, enter 2, to withdraw money, enter 3, to exit, enter 0):"))

    if choice == 1:
        clear_term()
        acc.account_info()
    elif choice == 2:
        clear_term()
        deposit_amount = int(input("How much money would you like to deposit:"))
        acc.deposit(deposit_amount)
    elif choice == 3:
        clear_term()
        withdraw_amount = int(input("How much money would you like to withdraw:"))
        acc.withdraw(withdraw_amount)
    elif choice == 0:
        print("Exiting.")
        break
    else:
        print("Incorrect operation choice. Please try again.")
