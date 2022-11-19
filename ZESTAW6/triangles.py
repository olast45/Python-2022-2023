from points import Point
import unittest


class Triangle:
    """Klasa reprezentująca trójkąt na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)
        self.pt3 = Point(x3, y3)

    def __str__(self):  # "[(x1, y1), (x2, y2), (x3, y3)]"
        return f'[{self.pt1}, {self.pt2}, {self.pt3}]'

    def __repr__(self):  # "Triangle(x1, y1, x2, y2, x3, y3)"
        return f'Triangle({self.pt1.x}, {self.pt1.y}, {self.pt2.x}, {self.pt2.y}, {self.pt3.x}, {self.pt3.y})'

    def __eq__(self, other):  # obsługa tr1 == tr2

        # Trójkąty powinny być równe, jeżeli mają ten sam zbiór wierzchołków,
        # niezależnie od kolejności pt1, pt2, pt3

        if isinstance(other, Triangle):
            a = {self.pt1, self.pt2, self.pt3}
            b = {other.pt1, other.pt2, other.pt3}
            return a == b
        else:
            return False

    def __ne__(self, other):  # obsługa tr1 != tr2
        return not self == other

    def center(self):  # zwraca środek (masy) trójkąta
        return (self.pt1.x + self.pt2.x + self.pt3.x) / 3, (self.pt1.y + self.pt2.y + self.pt3.y) / 3

    def area(self):  # pole powierzchni
        return 0.5 * abs(self.pt1.x * (self.pt2.y - self.pt3.y) + self.pt2.x * (self.pt3.y - self.pt1.y) +
                         self.pt3.x * (self.pt1.y - self.pt2.y))

    def move(self, x, y):  # przesunięcie o (x, y)
        return Triangle(self.pt1.x + x, self.pt1.y + y, self.pt2.x + x, self.pt2.y + y, self.pt3.x + x, self.pt3.y + y)


# Kod testujący moduł.


class TestTriangle(unittest.TestCase):

    def setUp(self):
        self.t = Triangle(1, 2, 3, 4, 5, 6)

    def test_string(self):
        self.assertEqual(str(self.t), "[(1, 2), (3, 4), (5, 6)]")
        self.assertEqual(repr(self.t), "Triangle(1, 2, 3, 4, 5, 6)")

    def test_equality(self):
        self.assertEqual(Triangle(3, 4, 5, 7, 0, 0) == Triangle(1, 2, 3, 4, 5, 6), False)
        self.assertEqual(Triangle(0, 5, 5, 6, 1, 1) == Triangle(5, 6, 0, 5, 1, 1), True)
        self.assertEqual(Triangle(3, 4, 7, 7, 8, 9) != Triangle(7, 1, 2, 3, 5, 5), True)

    def test_operations(self):
        self.assertEqual(Triangle(9, 7, 1, 1, 3, 4).center(), (4.333333333333333, 4.0))
        self.assertEqual(Triangle(2, 7, 1, 1, 3, 4).center(), (2.0, 4.0))
        self.assertEqual(Triangle(1, 1, 2, 2, 3, 3).area(), 0.0)
        self.assertEqual(Triangle(1, 1, 5, 2, 3, 3).area(), 3.0)
        self.assertEqual(Triangle(1, 1, 2, 2, 3, 3).move(1, 1), Triangle(2, 2, 3, 3, 4, 4))
        self.assertEqual(Triangle(1, 1, 1, 1, 1, 1).move(2, 5), Triangle(3, 6, 3, 6, 3, 6))


if __name__ == "__main__":
    unittest.main()
