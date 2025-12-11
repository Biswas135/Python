# Create Account class with:
# 1. balance
# 2. account number
# Methods:
# - debit()
# - credit()
# - get_balance()

class Account:
    def __init__(self, bal, acc):
        self.balance = bal          # object attribute
        self.account_no = acc       # object attribute

    # debit method
    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount, "was debited")
        print("Total balance =", self.get_balance())

    # credit method
    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, "was credited")
        print("Total balance =", self.get_balance())

    # check balance
    def get_balance(self):
        return self.balance


# creating object
acc1 = Account(1000, 12345)

print("Account balance is", acc1.balance)
print("Account number is", acc1.account_no)

# Testing methods
acc1.debit(500)
acc1.credit(200)
