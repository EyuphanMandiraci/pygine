import math

from pygine.math import Point2


class Vector2:
    def __init__(self, position, direction, force):
        self.position = position
        self.direction = math.radians(direction)
        self.force = force

        self.x = self.position.x
        self.y = self.position.y

    def getEndPosition(self):
        return Point2(self.position.x + math.cos(self.direction) * self.force, self.position.y + math.sin(self.direction) * self.force)

    def __getitem__(self, item):
        if item == 0:
            return self.position
        elif item == 1:
            return self.direction
        elif item == 2:
            return self.force
        else:
            raise IndexError("Index out of range")

    def __setitem__(self, item, value):
        if item == 0:
            self.position = value
        elif item == 1:
            self.direction = value
        elif item == 2:
            self.force = value
        else:
            raise IndexError("Index out of range")

    def __iter__(self):
        return iter([self.position, self.direction, self.force])

    def __len__(self):
        return 3

    def __contains__(self, item):
        return item == self.position or item == self.direction or item == self.force

    def __str__(self):
        return "Vector2(position={}, direction={}, force={})".format(self.position, self.direction, self.force)

    def __repr__(self):
        return "Vector2({}, {}, {})".format(self.position, self.direction, self.force)

    def __eq__(self, other):
        return self.position == other.position and self.direction == other.direction and self.force == other.force

    def __ne__(self, other):
        return self.position != other.position or self.direction != other.direction or self.force != other.force

    def __lt__(self, other):
        return self.position < other.position and self.direction < other.direction and self.force < other.force

    def __le__(self, other):
        return self.position <= other.position and self.direction <= other.direction and self.force <= other.force

    def __gt__(self, other):
        return self.position > other.position and self.direction > other.direction and self.force > other.force

    def __ge__(self, other):
        return self.position >= other.position and self.direction >= other.direction and self.force >= other.force

    def __add__(self, other):
        temp = Vector2(
            self.getEndPosition(),
            math.degrees(other.direction),
            other.force
        )
        vec = Vector2(
            self.position,
            math.degrees(self.position.directionTo(temp.getEndPosition())),
            self.position.distanceTo(temp.getEndPosition())
        )
        return vec

    def __sub__(self, other):
        return Vector2(self.position - other.position, self.direction - other.direction, self.force - other.force)

    def __mul__(self, other):
        return Vector2(self.position * other, self.direction * other, self.force * other)

    def __truediv__(self, other):
        return Vector2(self.position / other, self.direction / other, self.force / other)

    def __floordiv__(self, other):
        return Vector2(self.position // other, self.direction // other, self.force // other)
