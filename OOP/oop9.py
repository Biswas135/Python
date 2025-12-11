#CREATE STUDENT CLASS THAT TAKE NAME & MARKS OF 3 SUBJECTS AS ARGUMENT IN CONSTRCTOR 
# . THEN  CREATE A METHOD TO PRINT THE AVERAGE 


# Method 1 — Passing 3 subjects separately
class Student:
    def __init__(self, name, sub1, sub2, sub3):
        self.name = name                 # object attribute
        self.sub1 = sub1
        self.sub2 = sub2
        self.sub3 = sub3

    def avg(self):                       # method to calculate average
        total = self.sub1 + self.sub2 + self.sub3
        print("Hello", self.name, "your average score is:", total / 3)

s1 = Student("karan", 92, 93, 94)
s1.avg()

# Method 2 — Passing subjects in a list (Better for more subjects)

"""class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def avg(self):
        total = 0
        for val in self.marks:
            total += val
        print("Hi", self.name, "Your avg score is", total / len(self.marks))


s1 = Student("karan", [99, 98, 97])
s1.avg()

"""