from points import Point
import math
import unittest

class Circle:

    def __init__(self, x, y, radius):
        if radius < 0:
            raise ValueError("Radius can not be less than 0")
        self.pt = Point(x, y)
        self.radius = radius

    def __repr__(self):
        return "Circle({0}, {1}, {2})".format(self.pt.x, self.pt.y, self.radius)

    def __eq__(self, other):
        return self.pt == other.pt and self.radius == other.radius

    def __ne__(self, other):
        return not self == other

    def area(self):
        return math.pi * pow(self.radius, 2)

    def move(self, x, y):
        return Circle(self.pt.x + x, self.pt.y + y, self.radius)

    def cover(self, other):
        if(self.radius > other.radius):
            self, other = other, self

        distance = math.sqrt(math.pow(self.pt.x - other.pt.x, 2) + pow(self.pt.y - other.pt.y, 2))
        if(distance + self.radius <= other.radius):
            return Circle(round(other.pt.x, 2), round(other.pt.y, 2), round(other.radius,2))

        theta = 1/2 + (other.radius - self.radius)/(2*distance)
        center_x = (1-theta) * self.pt.x + theta * other.pt.x
        center_y = (1-theta) * self.pt.y + theta * other.pt.y
        radius = (distance + self.radius + other.radius)/2

        return Circle(round(center_x,2), round(center_y,2), round(radius,2))

class TestCircle(unittest.TestCase):

    def test_print(self):
        self.assertEqual(repr(Circle(2, 8, 5)), "Circle(2, 8, 5)")
        self.assertEqual(repr(Circle(32, -2, 2)), "Circle(32, -2, 2)")

    def test_cmp(self):
        self.assertTrue(Circle(2, 8, 5) == Circle(2, 8, 5))
        self.assertFalse(Circle(2, 8, 5) == Circle(2, 8, 6))
        self.assertFalse(Circle(1, 4, 5) == Circle(2, 8, 5))
        self.assertTrue(Circle(-2, -8, 15) == Circle(-2, -8, 15))

    def test_area(self):
        self.assertAlmostEqual(Circle.area(Circle(2, 8, 5)), 78.54, 2)
        self.assertAlmostEqual(Circle.area(Circle(2, 8, 2)), 12.57, 2)

    def test_move(self):
        self.assertEqual(Circle.move(Circle(2,8,5), 2, 8), Circle(4, 16, 5))
        self.assertEqual(Circle.move(Circle(2,8,5), -2, -8), Circle(0, 0, 5))

    def test_cover(self):
        self.assertEqual(Circle.cover(Circle(0,0,5), Circle(1, 1, 3)), Circle(0, 0, 5))
        self.assertEqual(Circle.cover(Circle(1,1,15), Circle(-5, 12, 3)), Circle(0.87, 1.23, 15.26))
        self.assertEqual(Circle.cover(Circle(25,30,20), Circle(45, 30, 40)), Circle(45, 30, 40))

if __name__ == "__main__":
    unittest.main()