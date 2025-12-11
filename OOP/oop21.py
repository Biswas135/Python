# Class to represent complex numbers
class Complex:
    def __init__(self, real, img):
        self.real = real   # real part
        self.img = img     # imaginary part

    # Method to display the complex number
    def showNumber(self):
        print(self.real, "i+", self.img, "j")

    # Overloading the + operator
    def __add__(self, num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal, newImg)  # return a new Complex object

# Creating first complex number
num1 = Complex(1, 3)
num1.showNumber()    # 1 i+ 3 j

# Creating second complex number
num2 = Complex(1, 3)
num2.showNumber()    # 1 i+ 3 j

# Adding two complex numbers using + operator
num3 = num1 + num2   # internally calls num1.__add__(num2)
num3.showNumber()    # 2 i+ 6 j
