import math

class Circle:

    def __init__(self, radius):
        
         self.radius = radius
        
    def calculate_area(self):
       
        return math.pi * (self.radius ** 2)
        
    def calculate_perimeter(self):
        
        return 2 * math.pi * self.radius
my_circle = Circle(radius=10)
print(f"Radius of the circle: {my_circle.radius}")
print(f"Area of the circle:   {my_circle.calculate_area():.2f}")
print(f"Perimeter of the circle: {my_circle.calculate_perimeter():.2f}")