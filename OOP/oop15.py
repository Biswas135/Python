# Single inheritance example

# Parent class
class Car:
    @staticmethod
    def start():
        print("Car started...")

    @staticmethod
    def stop():
        print("Car stopped")

# Child class inherits from Car
class ToyotaCar(Car):
    def __init__(self, name):
        self.name = name

# Creating objects of child class
car1 = ToyotaCar("Fortuner")
car2 = ToyotaCar("Prius")

# Accessing child class attributes
print(car1.name)
print(car2.name)

# Accessing parent class static method via child object
car1.start()    # ✅ do NOT use print() because start() already prints
