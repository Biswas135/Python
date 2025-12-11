class Student:
    # ❌ This default constructor gets overridden
    def __init__(self):
        pass

    # ✅ This constructor overwrites the above one
    def __init__(self, fullname, marks):
        self.name = fullname       # object attribute
        self.marks = marks         # object attribute
        print("adding new student in Database")

# Creating first student object
s1 = Student("Karan", 97)
print(s1.name, s1.marks)

# Creating second student object
s2 = Student("student", 63)
print(s2.name, s2.marks)
