# Class method example
# Class methods can modify class attributes

class Person:
    name="annoymous" # class attribute
     
    #def changeName(self,name):
        #self.__class__.name = "Rahul Kumar "
        #Person.name=name #(When self.name)
        
    @classmethod
    def changeName(cls, name):  # cls refers to the class itself
        cls.name = name          # modifies the class attribute
        
# Creating object
p1 = Person()

# Calling class method using object
p1.changeName("Rahul Kumar")

# Accessing class attribute via object
print(p1.name)        # Rahul Kumar

# Accessing class attribute via class
print(Person.name)    # Rahul Kumar (class attribute is modified for all instances)
    
        
        