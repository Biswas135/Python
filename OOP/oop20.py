# Using @property to calculate percentage

class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math

    # property method to calculate percentage dynamically
    @property
    def percentage(self):
        avg = (self.phy + self.chem + self.math) / 3   # calculate average
        return str(avg) + "%"                          # return as string with %

# Creating object
stu1 = Student(98, 97, 92)

# Accessing property (no parentheses needed)
print(stu1.percentage)   # 95.66666666666667%

# Changing one subject marks
stu1.phy = 86

# Property reflects updated value automatically
print(stu1.percentage)   # 91.66666666666667%
