class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


point = Point(1, 2)
point.draw()

# print("y=", point.y)
# print(type(point))  # <class '__main__.Point'>
# print(isinstance(point, Point))  # True
# print(isinstance(point, int))  # False
