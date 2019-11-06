class myClass:
    name = "Anas"

    def __int__(self, name, age):
        self.name = name
        self.age = age

    def Sum(self, a, b):
        print(a + b)

    def multiply(self, a, b):
        print(a * b)


x = myClass()
print(x.name)
x.Sum(20, 34)
# del x.name  #to delete the object
print(x.multiply(2, 5))


# --------------------------------------------------------------
class Rectangle:
    def __init__(self, length, breadth, unit_cost=0):
        self.length = length
        self.breadth = breadth
        self.unit_cost = unit_cost

    def get_perimeter(self):
        return 2 * (self.length + self.breadth)

    def get_area(self):
        return self.length * self.breadth

    def calculate_cost(self):
        area = self.get_area()
        return area * self.unit_cost


# breadth = 120 cm, length = 160 cm, 1 cm^2 = Rs 2000
r = Rectangle(160, 120, 2000)
print("Area of Rectangle: %s cm^2" % (r.get_area()))
print("Cost of rectangular field: Rs. %s " % (r.calculate_cost()))

# r = Rectangle(160, 120, 2000)
#
# Note: "r" is the representation of the object outside of the class and "self"  is the representation of the object inside  the class.

# ------------------------------------------------------------------------
class Car(object):
    """
    blueprint for car
  """

    def __init__(self, model, color, company, speed_limit):
        self.color = color
        self.company = company
        self.speed_limit = speed_limit
        self.model = model

    def start(self):
        print("started")

    def stop(self):
        print("stopped")

    def accelarate(self):
        print("accelarating...")
        "accelarator functionality here"

    def change_gear(self, gear_type):
        print("gear changed")
        " gear related functionality here"


# Lets try to create different types of cars

maruthi_suzuki = Car("ertiga", "black", "suzuki", 60)
audi = Car("A6", "red", "audi", 80)


