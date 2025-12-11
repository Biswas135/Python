# Multi-level inheritance example

# Parent class
class Car:
    @staticmethod
    def start():
        print("Car started...")

    @staticmethod
    def stop():
        print("Car stopped...")

# Child class
class ToyotaCar(Car):
    def __init__(self, brand):
        self.brand = brand      # attribute of child

# Grandchild class
class Fortuner(ToyotaCar):
    def __init__(self, brand, type):
        super().__init__(brand)  # call parent constructor to set brand
        self.type = type         # attribute of grandchild

# Creating object
car1 = Fortuner("Toyota", "Diesel")

# Accessing inherited method from parent
car1.start()                     # Car started...
print(car1.brand, car1.type)     # Toyota Diesel
