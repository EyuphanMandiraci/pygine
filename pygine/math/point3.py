import math


class Point3:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def normalize(self):
        magnitude = self.magnitude()
        if magnitude == 0:
            return Point3(0, 0, 0)
        return Point3(self.x / magnitude, self.y / magnitude, self.z / magnitude)

    def distanceTo(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2 + (self.z - other.z)**2)

    def directionTo(self, other):
        return math.atan2(other.y - self.y, other.x - self.x)

    def avarage(self, other):
        return Point3((self.x + other.x) / 2, (self.y + other.y) / 2, (self.z + other.z) / 2)

    def __getitem__(self, item):
        if item == 0:
            return self.x
        elif item == 1:
            return self.y
        elif item == 2:
            return self.z
        else:
            raise IndexError("Index out of range")

    def __setitem__(self, item, value):
        if item == 0:
            self.x = value
        elif item == 1:
            self.y = value
        elif item == 2:
            self.z = value
        else:
            raise IndexError("Index out of range")

    def __iter__(self):
        return iter([self.x, self.y, self.z])

    def __len__(self):
        return 3

    def __contains__(self, item):
        return item == self.x or item == self.y or item == self.z

    def __add__(self, other):
        return Point3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Point3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        return Point3(self.x * other, self.y * other, self.z * other)

    def __truediv__(self, other):
        return Point3(self.x / other, self.y / other, self.z / other)

    def __floordiv__(self, other):
        return Point3(self.x // other, self.y // other, self.z // other)

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

    def __repr__(self):
        return f"Vector3({self.x}, {self.y}, {self.z})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __ne__(self, other):
        return self.x != other.x or self.y != other.y or self.z != other.z

    def __lt__(self, other):
        return self.x < other.x and self.y < other.y and self.z < other.z

    def __le__(self, other):
        return self.x <= other.x and self.y <= other.y and self.z <= other.z

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y and self.z > other.z

    def __ge__(self, other):
        return self.x >= other.x and self.y >= other.y and self.z >= other.z
