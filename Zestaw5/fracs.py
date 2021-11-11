import math
import unittest

def add_frac(frac1, frac2):
    left_nominator = frac1[0] * frac2[1]
    right_nominator = frac2[0] * frac1[1]
    return cut_frac([left_nominator + right_nominator, frac1[1] * frac2[1]])

def sub_frac(frac1, frac2):
    left_nominator = frac1[0] * frac2[1]
    right_nominator = frac2[0] * frac1[1]
    return cut_frac([left_nominator - right_nominator, frac1[1] * frac2[1]])

def mul_frac(frac1, frac2):
    return cut_frac([frac1[0] * frac2[0], frac1[1] * frac2[1]])

def div_frac(frac1, frac2):
    return cut_frac([frac1[0] * frac2[1], frac1[1] * frac2[0]])

def is_positive(frac):
    if (frac[0] < 0 and frac[1] > 0) or (frac[0] > 0 and frac[1] < 0):
        return False
    return True

def is_zero(frac):
    if (frac[0] == 0):
        return True
    return False

def cmp_frac(frac1, frac2):
    frac1_float = frac2float(frac1)
    frac2_float = frac2float(frac2)
    if(frac1_float < frac2_float):
        return -1
    if(frac1_float > frac2_float):
        return 1
    return 0

def frac2float(frac):
    return frac[0]/frac[1]

def cut_frac(frac):
    nwd = math.gcd(frac[0], frac[1])
    nominator = frac[0] // nwd
    denominator = frac[1] // nwd
    return [nominator, denominator]

class TestFractions(unittest.TestCase):

    def test_add_frac(self):
        self.assertEqual(add_frac([1, 2], [1, 3]), [5, 6])
        self.assertEqual(add_frac([3, 7], [6, 5]), [57, 35])
        self.assertEqual(add_frac([3, 7], [8, 14]), [1, 1])
        self.assertEqual(add_frac([2, 5], [-1, 10]), [3, 10])

    def test_sub_frac(self):
        self.assertEqual(sub_frac([1, 2], [1, 3]), [1, 6])
        self.assertEqual(sub_frac([23, 35], [13, 35]), [2, 7])
        self.assertEqual(sub_frac([11, 7], [-3, 7]), [2, 1])
        self.assertEqual(sub_frac([5, 2], [-2, 3]), [19, 6])

    def test_mul_frac(self):
        self.assertEqual(mul_frac([1, 2], [1, 3]), [1, 6])
        self.assertEqual(mul_frac([2, 3], [1, 8]), [1, 12])
        self.assertEqual(mul_frac([8, 9], [5, 8]), [5, 9])
        self.assertEqual(mul_frac([13, 7], [-6, 26]), [-3, 7])

    def test_div_frac(self):
        self.assertEqual(div_frac([5, 7], [3, 7]), [5, 3])
        self.assertEqual(div_frac([8, 5], [4, 25]), [10, 1])
        self.assertEqual(div_frac([17, 4], [5, 12]), [51, 5])
        self.assertEqual(div_frac([2, 3], [5, -6]), [-4, 5])

    def test_is_positive(self):
        self.assertTrue(is_positive([1, 2]))
        self.assertTrue(is_positive([-1, -2]))
        self.assertFalse(is_positive([-1, 2]))
        self.assertFalse(is_positive([1, -2]))

    def test_is_zero(self):
        self.assertFalse(is_zero([1, 2]))
        self.assertTrue(is_zero([0, 1]))
        self.assertFalse(is_zero([3, 1]))
        self.assertTrue(is_zero([0, 2]))

    def test_cmp_frac(self):
        self.assertEqual(cmp_frac([0, 2], [1,2]), -1)
        self.assertEqual(cmp_frac([1, 2], [2,4]), 0)
        self.assertEqual(cmp_frac([3, 4], [2,4]), 1)
        self.assertEqual(cmp_frac([-1, 2], [1,2]), -1)

    def test_frac2float(self):
        self.assertEqual(frac2float([1, 2]), 1/2)
        self.assertEqual(frac2float([-1, 2]), -1/2)
        self.assertEqual(frac2float([0, 1]), 0)
        self.assertEqual(frac2float([3, 1]), 3)
        self.assertEqual(frac2float([0, 2]), 0)

if __name__ == '__main__':
    unittest.main()