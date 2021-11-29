import unittest

class Frac:

    def __init__(self, x=0, y=None):
        if y is None:
            if type(x) is float:
                integer_ratio = x.as_integer_ratio()
                self.x = integer_ratio[0]
                self.y = integer_ratio[1]
        else:
            if(y == 0):
                raise ValueError('Denominator can not be 0')
            self.x = x
            self.y = y

    def __str__(self):
        return "{0}/{1}".format(self.x, self.y) if self.y != 1 else "{0}".format(self.x)

    def __repr__(self):
        return "Frac({0}, {1})".format(self.x, self.y)

    def __eq__(self, other):
        return float(self) == float(other)

    def __ne__(self, other):
        return float(self) != float(other)

    def __lt__(self, other):
        return float(self) < float(other)

    def __le__(self, other):
        return float(self) <= float(other)

    def __gt__(self, other):
        return float(self) > float(other)

    def __ge__(self, other):
        return float(self) >= float(other)

    def __add__(self, other):
        if type(other) is int:
            return Frac(self.x + self.y * other, self.y)

        return Frac((self.x * other.y + other.x * self.y), (self.y * other.y))

    __radd__ = __add__

    def __sub__(self, other):
        if type(other) is int:
            return Frac(self.x - self.y * other, self.y)

        return Frac((self.x * other.y - other.x * self.y), (self.y * other.y))

    def __rsub__(self, other):
        return Frac(self.y * other - self.x, self.y)

    def __mul__(self, other):
        if type(other) is int:
            return Frac(self.x * other, self.y)

        return Frac(self.x * other.x, self.y * other.y)

    __rmul__ = __mul__ 

    def __truediv__(self, other):
        if type(other) is int:
            if(other == 0):
                raise ValueError('Denominator can not be 0')
            return Frac(self.x, self.y * other)

        return Frac(self.x * other.y, self.y * other.x)

    def __rtruediv__(self, other):
        if(other == 0):
            raise ValueError('Denominator can not be 0')
        return Frac(other * self.y, self.x)

    def __pos__(self):
        return self

    def __neg__(self):
        return Frac(-self.x, self.y)

    def __invert__(self):
        if self.x == 0:
            raise ValueError('Numerator can not be 0')
        return Frac(self.y, self.x)

    def __float__(self):
        return self.x/self.y

    def __hash__(self):
        return hash(float(self))

class TestFrac(unittest.TestCase):

    def test_print(self):
        self.assertEqual(str(Frac(2, 8)), "2/8")
        self.assertEqual(str(Frac(32, -2)), "32/-2")
        self.assertEqual(str(Frac(32, 1.0)), "32")
        self.assertEqual(str(Frac(32/2)), "16")
        self.assertEqual(str(Frac(-32, 1)), "-32")
        self.assertEqual(repr(Frac(2, 8)), "Frac(2, 8)")
        self.assertEqual(repr(Frac(32, -2)), "Frac(32, -2)")
        self.assertEqual(repr(Frac(32/2)), "Frac(16, 1)")

    def test_cmp(self):
        self.assertTrue(Frac(2, 8) == Frac(1,4))
        self.assertTrue(Frac(8, 8) == 1)
        self.assertTrue(Frac(11, 8) == Frac(11,8))
        self.assertTrue(Frac(21, 8) != Frac(1,4))
        self.assertTrue(Frac(21, 8) != Frac(4,4))

    def test_add(self):
        self.assertEqual(Frac(2, 8) + Frac(1,4), Frac(2,4))
        self.assertEqual(Frac(2, 8) + 2, Frac(18,8))
        self.assertEqual(2 + Frac(2, 8), Frac(18,8))

    def test_sub(self):
        self.assertEqual(Frac(4, 8) - Frac(1,4), Frac(1,4))
        self.assertEqual(Frac(4, 8) - 2, Frac(-12,8))
        self.assertEqual(2 - Frac(1,4), Frac(7,4))

    def test_mul(self):
        self.assertEqual(Frac(4, 8) * Frac(1,4), Frac(4,32))
        self.assertEqual(Frac(4, 8) * 2, Frac(8,8))
        self.assertEqual(4 * Frac(3,2), Frac(12,2))

    def test_truediv(self):
        self.assertEqual(Frac(4, 8) / Frac(1,4), Frac(2,1))
        self.assertEqual(Frac(4, 8) / 2, Frac(1,4))
        self.assertEqual(2 / Frac(4,8), Frac(4,1))

    def test_pos(self):
        self.assertEqual(Frac(2, 8), +Frac(2, 8))
        self.assertEqual(Frac(11, 8), +Frac(11, 8))

    def test_neg(self):
        self.assertEqual(Frac(-2, 8), -Frac(2, 8))
        self.assertEqual(Frac(-11, 8), -Frac(11, 8))

    def test_invert(self):
        self.assertEqual(~Frac(-6, 2), Frac(2, -6))
        self.assertEqual(~Frac(2, 8), Frac(8, 2))

    def test_float(self):
        self.assertEqual(float(Frac(5,10)), 0.5)
        self.assertEqual(float(Frac(0,5)), 0.0)

    def test_hash(self):
        self.assertEqual(Frac(-10, 2), Frac(-10.0, 2.0))
        self.assertEqual(Frac(0, 1), Frac(0.0, 1.0))

if __name__ == "__main__":
    unittest.main()
