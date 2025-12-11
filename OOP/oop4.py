# Creating a class named Student
class Student:
    def __init__(self, fullname, marks):    # constructor with 2 parameters
        self.name = fullname               # object attribute: name
        self.marks = marks                 # object attribute: marks
        print("adding new student in Database")

# Creating first object of Student class
s1 = Student("Karan", 97)
print(s1.name, s1.marks)                   # prints "Karan 97"

# Creating second object
s2 = Student("student", 63)
print(s2.name, s2.marks)                   # prints "student 63"
