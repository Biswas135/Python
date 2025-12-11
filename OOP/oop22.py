# Define a Circle class to create a circle with radius r using the constructor.
# Define the area() method to calculate the area of the circle.
# Define a perimeter() method to calculate the perimeter of the circle.


class Circle:
    def __init__(self, radius):
        self.radius = radius   # object attribute

    # Method to calculate area of circle
    def area(self):
        return (22/7) * (self.radius ** 2)

    # Method to calculate perimeter of circle
    def perimeter(self):
        return 2 * (22/7) * self.radius

# Taking input from user
x = int(input("Enter the radius: "))

# Creating circle object
c1 = Circle(x)

# Displaying area and perimeter
print("Area:", c1.area())
print("Perimeter:", c1.perimeter())

