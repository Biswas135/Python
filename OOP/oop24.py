#Create a class order which store item and price . Use Dunder function __gt__() to convey 
# that order1>order2 if price of orer1>price of the order 2 


class Order:
    def __init__(self, item, price):
        self.item = item      # item name
        self.price = price    # item price

    # Overload '>' operator
    def __gt__(self, odr2):
        return self.price > odr2.price  # True if self.price > other price

# Creating orders
odr1 = Order("chips", 20)
odr2 = Order("tea", 15)

# Compare using > operator
print(odr1 > odr2)  # True, because 20 > 15
