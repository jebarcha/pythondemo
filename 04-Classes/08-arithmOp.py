class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)


point = Point(10, 20)
other = Point(1, 2)
print(point + other)  # <__main__.Point object at 0x00000224DC569E20>
combined = point + other
print(combined.x)  # 11
