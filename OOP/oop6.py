class Student:
    collage_name = "ABC Collage"     # class attribute (same for all students)

    def __init__(self, fullname, marks):   # constructor
        self.name = fullname               # object attribute
        self.marks = marks                 # object attribute
        print("adding new student in Database")

# Creating first student object
s1 = Student("Karan", 97)
print(s1.name, s1.marks)

# Creating second student object
s2 = Student("student", 63)
print(s2.name, s2.marks)

# Accessing class attribute using object
print(s2.collage_name)
