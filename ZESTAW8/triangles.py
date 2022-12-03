from points import Point


class Triangle:
    """Klasa reprezentująca trójkąty na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2, x3, y3):
        # Należy zabezpieczyć przed sytuacją, gdy punkty są współliniowe.
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)
        self.pt3 = Point(x3, y3)
        if self.area() == 0:
            raise ValueError("Those points do not form a triangle")

    def __str__(self):  # "[(x1, y1), (x2, y2), (x3, y3)]"
        return f'[{self.pt1}, {self.pt2}, {self.pt3}]'

    def __repr__(self):  # "Triangle(x1, y1, x2, y2, x3, y3)"
        return f'Triangle({self.pt1.x}, {self.pt1.y}, {self.pt2.x}, {self.pt2.y}, {self.pt3.x}, {self.pt3.y})'

    def __eq__(self, other):  # obsługa tr1 == tr2
        if isinstance(other, Triangle):
            a = {self.pt1, self.pt2, self.pt3}
            b = {other.pt1, other.pt2, other.pt3}
            return a == b
        else:
            return False

    def __ne__(self, other):  # obsługa tr1 != tr2
        return not self == other

    @classmethod
    def from_points(cls, points):
        if len(points) != 3:
            raise ValueError("You need three points to form a triangle!")
        for point in points:
            assert True == (isinstance(point, Point))
        if isinstance(points, (tuple, list)):
            return cls(points[0].x, points[0].y, points[1].x, points[1].y, points[2].x, points[2].y)

    @property
    def top(self):
        return max(self.pt1.y, self.pt2.y, self.pt3.y)

    @property
    def left(self):
        return min(self.pt1.x, self.pt2.x, self.pt3.x)

    @property
    def bottom(self):
        return min(self.pt1.y, self.pt2.y, self.pt3.y)

    @property
    def right(self):
        return max(self.pt1.x, self.pt2.x, self.pt3.x)

    @property
    def width(self):
        return abs(self.right - self.left)

    @property
    def heigth(self):
        return abs(self.top - self.bottom)

    @property
    def topleft(self):
        return Point(self.left, self.top)

    @property
    def bottomleft(self):
        return Point(self.left, self.bottom)

    @property
    def topright(self):
        return Point(self.right, self.top)

    @property
    def bottomright(self):
        return Point(self.right, self.bottom)

    def center(self):  # zwraca środek trójkąta
        return (self.pt1.x + self.pt2.x + self.pt3.x) / 3, (self.pt1.y + self.pt2.y + self.pt3.y) / 3

    def area(self):  # pole powierzchni
        return 0.5 * abs(self.pt1.x * (self.pt2.y - self.pt3.y) + self.pt2.x * (self.pt3.y - self.pt1.y) +
                         self.pt3.x * (self.pt1.y - self.pt2.y))

    def move(self, x, y):  # przesunięcie o (x, y)
        return Triangle(self.pt1.x + x, self.pt1.y + y, self.pt2.x + x, self.pt2.y + y, self.pt3.x + x, self.pt3.y + y)

    def make4(self):  # zwraca krotkę czterech mniejszych
        return Triangle(self.pt1.x, self.pt1.y, 0.5 * (self.pt1.x + self.pt2.x), 0.5 * (self.pt1.y + self.pt2.y),
                        0.5 * (self.pt1.x + self.pt3.x), 0.5 * (self.pt1.y + self.pt3.y)), \
               Triangle(0.5 * (self.pt1.x + self.pt2.x), 0.5 * (self.pt1.y + self.pt2.y), self.pt2.x, self.pt2.y,
                        0.5 * (self.pt2.x + self.pt3.x), 0.5 * (self.pt2.y + self.pt3.y)), \
               Triangle(0.5 * (self.pt1.x + self.pt3.x), 0.5 * (self.pt1.y + self.pt3.y),
                        0.5 * (self.pt2.x + self.pt3.x), 0.5 * (self.pt2.y + self.pt3.y), self.pt3.x, self.pt3.y), \
               Triangle(0.5 * (self.pt1.x + self.pt3.x), 0.5 * (self.pt1.y + self.pt3.y),
                        0.5 * (self.pt1.x + self.pt2.x), 0.5 * (self.pt1.y + self.pt2.y),
                        0.5 * (self.pt2.x + self.pt3.x), 0.5 * (self.pt2.y + self.pt3.y))


#     A       po podziale    A
#    / \                    / \
#   /   \                  +---+
#  /     \                / \ / \
# C-------B              C---+---B



