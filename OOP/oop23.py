# Define an Employee class with attributes role, department, salary.
# This class also has a show_details() method.
# Create an Engineer class that inherits from Employee and has
# additional attributes name and age.

class Employee:
    def __init__(self, role, department, salary):
        self.role = role
        self.department = department
        self.salary = salary

    # Method to show employee details
    def details(self):
        print("Role       :", self.role)
        print("Department :", self.department)
        print("Salary     :", self.salary)

# Engineer class inherits from Employee
class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name        # engineer-specific attribute
        self.age = age          # engineer-specific attribute
        # Initialize parent class with fixed values for Engineer
        super().__init__("Engineer", "IT", 75000)

    # Override details() to include engineer info
    def details(self):
        print("Name       :", self.name)
        print("Age        :", self.age)
        super().details()      # call parent method to show Employee details

# Creating Employee object
E1 = Employee("Housekeeping", "A1", 2300)
E1.details()

print("\nEngineer Details:")
# Creating Engineer object
En1 = Engineer("Elon", 40)
En1.details()
