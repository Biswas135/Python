# Abstraction in OOP:
# Abstraction means hiding complex details and showing only essential features.

class Car:
    def __init__(self):
        self.acc = False      # accelerator state
        self.brk = False      # brake state
        self.clutch = False   # clutch state

    def start(self):          # abstraction: user only calls start()
        # internal complex steps (hidden from user)
        self.clutch = True
        self.acc = True
        print("Car Started")


car1 = Car()
car1.start()   # user doesn't need to know the internal working
