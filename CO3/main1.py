from graphics import circle,rectangle
from graphics.ThreeDGraphics import cuboid,sphere



print("Area and perimeter of circle")

print("area of circle =",circle.area(3))
print("Perimeter of circle =",circle.perimeter(3))
print()

print("Area and perimeter of rectangle")
print("Area of rectangle =",rectangle.area(3,2))
print("Perimeter of rectangle =",rectangle.perimeter(2,3))
print()

print("Area and perimeter of cuboid ")
print("Area of Cuboid =",cuboid.area(2,3,4))
print("Perimeter of Cuboid =",cuboid.perimeter(2,3,4))
print()

print("Area and perimeter of sphere ")
print("Area of sphere =",sphere.area(3))
print("Perimeter of Sphere =",sphere.perimeter(3))