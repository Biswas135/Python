# Creating a class named Student
class Student:
    def __init__(self, fullname):         # constructor method
        self.name = fullname              # object attribute
        print("adding new student in Database")

# Creating first object of Student class
s1 = Student("Karan")
print(s1.name)                            # prints the name stored in the object

# Creating second object
s2 = Student("student")
print(s2.name)
