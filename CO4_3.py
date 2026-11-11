class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def __lt__(self, other):
        return self.area() < other.area()


r1 = Rectangle(6, 5)
r2 = Rectangle(6, 8)

if r1 < r2:
    print("Rect1 has a smaller area.")
else:
    print("Rect1 does not have a smaller area.")

print("Area of Rect1:", r1.area())
print("Area of Rect2:", r2.area())