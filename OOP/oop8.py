class Student:
    college_name = "ABC College"     # class attribute

    def __init__(self, name, marks): # constructor
        self.name = name             # object attribute
        self.marks = marks           # object attribute

    def welcome(self):               # method 1
        print("Welcome student", self.name)

    def get_marks(self):             # method 2
        return self.marks

# Creating object
s1 = Student("karan", 97)

s1.welcome()                         # calling method
print(s1.get_marks())                # printing marks
