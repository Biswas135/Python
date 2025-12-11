# del keyword example

class Student:
    def __init__(self, name):
        self.name1 = name   # object attribute

s1 = Student("Karan")
print(s1.name1)          # prints the name

del s1.name1             # deletes the attribute 'name1'

# print(s1.name1)        # ❌ This will raise AttributeError because name1 no longer exists
