import math
import unittest

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

    def __repr__(self):
        return "Point({0}, {1})".format(self.x, self.y)

    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y)

    def __ne__(self, other):
        return not self == other

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y

    def cross(self, other):
        return self.x * other.y - self.y * other.x

    def length(self):
        return math.sqrt(pow(self.x, 2) + pow(self.y, 2))

    def __hash__(self):
        return hash((self.x, self.y))

class TestPoint(unittest.TestCase):

    def test_print(self):
        self.assertEqual(str(Point(2, 8)), "(2, 8)")
        self.assertEqual(str(Point(32, -2)), "(32, -2)")
        self.assertEqual(repr(Point(2, 8)), "Point(2, 8)")
        self.assertEqual(repr(Point(32, -2)), "Point(32, -2)")

    def test_cmp(self):
        self.assertTrue(Point(2, 8) == Point(2, 8))
        self.assertFalse(Point(-32, -2) == Point(32, -2))
        self.assertTrue(Point(2, 8) != Point(-2, -8))
        self.assertFalse(Point(2, 8) != Point(2, 8))

    def test_add(self):
        self.assertEqual(Point(2, 2) + Point(3, 4), Point(5, 6))
        self.assertEqual(Point(-2, 2) + Point(2, -4), Point(0, -2))
        self.assertEqual(Point(6, 10) + Point(-3, -4), Point(3, 6))

    def test_sub(self):
        self.assertEqual(Point(2, 2) - Point(3, 4), Point(-1, -2))
        self.assertEqual(Point(-2, 2) - Point(2, -4), Point(-4, 6))
        self.assertEqual(Point(6, 10) - Point(-3, -4), Point(9, 14))

    def test_mul(self):
        self.assertEqual(Point(2, 2) * Point(3, 4), 14)
        self.assertEqual(Point(-2, 2) * Point(2, -4), -12)
        self.assertEqual(Point(6, 10) * Point(-3, -4), -58)

    def test_cross(self):
        self.assertEqual(Point.cross(Point(2, 2), Point(3, 4)), 2)
        self.assertEqual(Point.cross(Point(-2, 2), Point(2, -4)), 4)
        self.assertEqual(Point.cross(Point(6, 10), Point(-3, -4)), 6)

    def test_length(self):
        self.assertAlmostEqual(Point.length(Point(3, 4)), 5, 2)
        self.assertAlmostEqual(Point.length(Point(6, 10)), 11.66, 2)
        self.assertAlmostEqual(Point.length(Point(-2, 2)), 2.83, 2)

if __name__ == "__main__":
    unittest.main()