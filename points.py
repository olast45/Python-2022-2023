import math as m
import unittest


class Point:
    """Klasa reprezentująca punkty na płaszczyźnie."""

    def __init__(self, x, y):  # konstuktor
        self.x = x
        self.y = y

    def __str__(self):  # zwraca string "(x, y)"
        return f'({self.x}, {self.y})'

    def __repr__(self):  # zwraca string "Point(x, y)"
        return f'Point({self.x}, {self.y})'

    def __eq__(self, other):  # obsługa point1 == point2
        if isinstance(other, Point):
            return (self.x == other.x) and (self.y == other.y)
        else:
            return False

    def __ne__(self, other):  # obsługa point1 != point2
        return not self == other

    # Punkty jako wektory 2D.
    def __add__(self, other):  # v1 + v2
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):  # v1 - v2
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):   # v1 * v2, iloczyn skalarny, zwraca liczbę
        return (self.x * other.x) + (self.y * other.y)

    def cross(self, other):         # v1 x v2, iloczyn wektorowy 2D, zwraca liczbę
        return self.x * other.y - self.y * other.x

    def length(self):  # długość wektora
        return m.sqrt((self.x ** 2 + self.y ** 2))

    def __hash__(self):
        return hash((self.x, self.y))  # bazujemy na tuple, immutable points


# Kod testujący moduł.

class TestPoint(unittest.TestCase):
    def setUp(self):
        self.v = Point(3, 5)

    def test_string(self):
        self.assertEqual(str(self.v), "(3, 5)")
        self.assertEqual(repr(self.v), "Point(3, 5)")

    def test_equality(self):
        self.assertEqual(Point(5, 6) == Point(5, 6), True)
        self.assertEqual(Point(3, 1) == Point(4, 5), False)
        self.assertEqual(Point(2, 1) != Point(4, 6), True)

    def test_operations(self):
        self.assertEqual(Point(5, 6) + Point(3, 1), Point(8, 7))
        self.assertEqual(Point(0, 0) + Point(8, 1), Point(8, 1))
        self.assertEqual(Point(5, 5) - Point(1, 1), Point(4, 4))
        self.assertEqual(Point(3, 1) - Point(0, 1), Point(3, 0))
        self.assertEqual(Point(4, 9) * Point(0, 0), 0)
        self.assertEqual(Point(1, 2) * Point(1, 2), 5)

    def test_cross(self):
        self.assertEqual(Point(1, 1). cross(Point(3, 3)), 0)
        self.assertEqual(Point(5, 1).cross(Point(2, 3)), 13)

    def test_length(self):
        self.assertEqual(Point(1, 1).length(), m.sqrt(2))
        self.assertEqual(Point(4, 6).length(), m.sqrt(52))

    def test_hash(self):
        self.assertEqual(hash(Point(1, 1)), 8389048192121911274)
        self.assertEqual(hash(Point(6, 0)), -5491666964808633865)


if __name__ == "__main__":
    unittest.main()