import math


class Point2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2)

    def normalize(self):
        magnitude = self.magnitude()
        if magnitude == 0:
            return Point2(0, 0)
        return Point2(self.x / magnitude, self.y / magnitude)

    def distanceTo(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

    def directionTo(self, other):
        return math.atan2(other.y - self.y, other.x - self.x)

    def avarage(self, other):
        return Point2((self.x + other.x) / 2, (self.y + other.y) / 2)

    def __getitem__(self, item):
        if item == 0:
            return self.x
        elif item == 1:
            return self.y
        else:
            raise IndexError("Index out of range")

    def __setitem__(self, item, value):
        if item == 0:
            self.x = value
        elif item == 1:
            self.y = value
        else:
            raise IndexError("Index out of range")

    def __iter__(self):
        return iter([self.x, self.y])

    def __len__(self):
        return 2

    def __contains__(self, item):
        return item == self.x or item == self.y

    def __add__(self, other):
        if isinstance(other, Point2):
            return Point2(self.x + other.x, self.y + other.y)
        elif isinstance(other, (int, float)):
            return Point2(self.x + other, self.y + other)
        else:
            return Point2(
                self.x + math.cos(other.direction) * (other.force / 10),
                self.y + math.sin(other.direction) * (other.force / 10)
            )

    def __sub__(self, other):
        return Point2(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Point2(self.x * other, self.y * other)

    def __truediv__(self, other):
        return Point2(self.x / other, self.y / other)

    def __floordiv__(self, other):
        return Point2(self.x // other, self.y // other)

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"Vector2({self.x}, {self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return self.x != other.x or self.y != other.y

    def __lt__(self, other):
        return self.x < other.x and self.y < other.y

    def __le__(self, other):
        return self.x <= other.x and self.y <= other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    def __ge__(self, other):
        return self.x >= other.x and self.y >= other.y