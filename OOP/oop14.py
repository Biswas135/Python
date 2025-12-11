# Private-like attribute example

class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no          # public attribute
        self.__accpass = acc_pass     # private-like attribute (name mangling)

    def reset_pass(self):             # method to access private attribute
        print("Password is:", self.__accpass)

# create object
acc1 = Account(1234, "abcde")

print(acc1.acc_no)        # public attribute can be accessed

# print(acc1.__accpass)   # ❌ This will raise AttributeError

acc1.reset_pass()         # ✅ Access private attribute via method
