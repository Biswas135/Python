# Using super() to call parent constructor and methods

class Car:
    def __init__(self, type):
        self.type = type              # parent class attribute
    
    @staticmethod
    def start():
        print("Car started...")      # parent class method
        
    @staticmethod
    def stop():
        print("Car stopped...")      # parent class method

class ToyotaCar(Car):
    def __init__(self, name, type):
        self.name = name             # child class attribute
        super().__init__(type)       # call parent constructor to set 'type'
        super().start()              # call parent method 'start()'

# Creating object of child class
car1 = ToyotaCar("Prius", "Electric")

# Accessing attributes
print(car1.type)   # inherited from parent
print(car1.name)   # child attribute
