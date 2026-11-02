
class BankAccount:
    def __init__(self, account_holder, balance):
        self.__account_holder = account_holder
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Amount deposited:", amount)
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print("Amount withdrawn:", amount)
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.__balance

    def display(self):
        print("Account Holder:", self.__account_holder)
        print("Balance:", self.__balance)


class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance, interest_rate):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    def withdraw(self, amount):
        print("Savings Account Withdrawal")
        super().withdraw(amount)

    def display(self):
        super().display()
        print("Interest Rate:", self.interest_rate, "%")


class CurrentAccount(BankAccount):
    def __init__(self, account_holder, balance, overdraft_limit):
        super().__init__(account_holder, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        print("Current Account Withdrawal")

        if amount > 0 and amount <= self.get_balance() + self.overdraft_limit:
            super().withdraw(amount)
            if amount > self.get_balance():
                print("Overdraft facility used")
        else:
            print("Overdraft limit exceeded")

    def display(self):
        super().display()
        print("Overdraft Limit:", self.overdraft_limit)


# Polymorphism
accounts = [
    SavingsAccount("Rahul", 10000, 5),
    CurrentAccount("Aman", 15000, 5000)
]

for account in accounts:
    print("\n----------------")
    account.display()
    account.withdraw(2000)
    print("Updated Balance:", account.get_balance())
