'''
Aryan Singhal
CIS 41A   Winter 2024
Unit I, Exercise I
'''
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def getArea(self):
        return math.pi * (self.radius ** 2)

class Cylinder(Circle):
    def __init__(self, radius, height):
        super().__init__(radius)
        self.height = height

    def getVolume(self):
        return self.getArea() * self.height


# Test the Circle class
circle = Circle(4)
print(f"Circle area is: {circle.getArea():.2f}")

# Test the Cylinder class
cylinder = Cylinder(2, 5)
print(f"Cylinder volume is: {cylinder.getVolume():.2f}")

'''
Execution results:
Circle area is: 50.27
Cylinder volume is: 62.83
'''