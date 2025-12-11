class Student:
    def __init__(self, name, marks):
        self.name = name            # object attribute
        self.marks = marks          # list of marks

    @staticmethod
    def hello():                    # static method (does not use self or class)
        print("hello")

    def avg(self):                  # instance method
        total = 0
        for val in self.marks:
            total += val
        print("Hi", self.name, "Your avg score is", total / len(self.marks))


# creating object
s1 = Student("karan", [99, 98, 97])

s1.avg()       # calling instance method
s1.hello()     # calling static method
