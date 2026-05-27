import math
class Circle:

    def __init__(self , radius ):
        self.radius = radius
        self.area = math.pi**2
        self.perimeter = 2*math.pi*radius

my_circle=Circle(radius=10)
print("Area of the circle:" , my_circle.area)
print("Perimeter of the circle:" ,my_circle.perimeter)
print("Radius of the circle:" , my_circle.radius)



   




