class Point:
    default_color = "red"

    def __init__(self, x, y):
        self.x = x  # x and y are instance attributes
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


point = Point(0, 0)
# <bound method Point.__str__ of <__main__.Point object at 0x000001B77404A060>>
print(point.__str__)

print(point)  # (0, 0)
print(str(point))  # (0, 0), got same result using the str function
