# Multiple inheritance example
# Class C inherits from both A and B

class A:
    varA = "Welcome to class A"   # attribute of class A

class B:
    varB = "Welcome to class B"   # attribute of class B

class C(A, B):                     # C inherits from A and B
    varC = "Welcome to class C"   # attribute of class C

# Creating object of class C
c1 = C()

# Accessing attributes from all parent classes
print(c1.varC)   # from class C
print(c1.varB)   # from class B
print(c1.varA)   # from class A
