from points import Point
from triangles import Triangle
import pytest


def test_string():
    assert str(Triangle(0, 0, 5, 10, 10, 0)) == "[(0, 0), (5, 10), (10, 0)]"
    assert repr(Triangle(0, 0, 5, 10, 10, 0)) == "Triangle(0, 0, 5, 10, 10, 0)"


def test_equality():
    assert Triangle(0, 0, 6, 1, 3, 4) == Triangle(3, 4, 6, 1, 0, 0)
    assert Triangle(1, 5, 5, 6, 1, 1) == Triangle(5, 6, 0, 5, 1, 1)
    assert Triangle(3, 4, 7, 7, 8, 9) != Triangle(7, 1, 2, 3, 5, 5)


def test_from_points():
    assert Triangle.from_points((Point(0, 0), Point(6, 1), Point(3, 4))) == Triangle(0, 0, 6, 1, 3, 4)
    assert Triangle.from_points((Point(3, 4), Point(7, 7), Point(8, 9))) == Triangle(3, 4, 7, 7, 8, 9)


def test_properties():
    triangle = Triangle(0, 0, 5, 10, 10, 0)
    assert triangle.top == 10
    assert triangle.bottom == 0
    assert triangle.left == 0
    assert triangle.right == 10
    assert triangle.width == 10
    assert triangle.heigth == 10
    assert triangle.topleft == Point(0, 10)
    assert triangle.topright == Point(10, 10)
    assert triangle.bottomleft == Point(0, 0)
    assert triangle.bottomright == Point(10, 0)


def test_operations():
    assert Triangle(9, 7, 1, 1, 3, 4).center() == (4.333333333333333, 4.0)
    assert Triangle(2, 7, 1, 1, 3, 4).center() == (2.0, 4.0)
    assert Triangle(0, 0, 10, 0, 0, 5).area() == 25.0
    assert Triangle(1, 1, 5, 2, 3, 3).area() == 3.0
    assert Triangle(1, 1, 2, 2, 1, 4).move(1, 1) == Triangle(2, 2, 3, 3, 2, 5)
    assert Triangle(1, 0, 4, 0, 0, 2).move(2, 5) == Triangle(3, 5, 6, 5, 2, 7)


if __name__ == "__main__":
    pytest.main()
