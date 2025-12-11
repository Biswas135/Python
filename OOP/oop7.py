class Student:
    collage_name = "ABC Collage"   # class attribute
    name = "anonymous"             # class attribute

    def __init__(self, fullname, marks):
        self.name = fullname       # object attribute (overrides class attribute)
        self.marks = marks         # object attribute
        print("adding new student in Database")

# Creating an object of Student class
s1 = Student("Karan", 97)

# This prints object attributes, NOT class attributes
print(s1.name, s1.marks)

# NOTE : object attribute has higher priority than class attribute
