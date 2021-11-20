import unittest

class Time:

    def __init__(self, s=0):
        self.s = int(s)

    def __str__(self):
        h = self.s // 3600
        sec = self.s - h * 3600
        m = sec // 60
        sec = sec - m * 60
        return "{0:02d}:{1:02d}:{2:02d}".format(h, m, sec)

    def __repr__(self):
        return "Time({0})".format(self.s)

    def __add__(self, other):
        return Time(self.s + other.s)

    def __eq__(self, other):
        return self.s == other.s

    def __ne__(self, other):
        return self.s != other.s

    def __lt__(self, other):
        return self.s < other.s

    def __le__(self, other):
        return self.s <= other.s

    def __gt__(self, other):
       return self.s > other.s

    def __ge__(self, other):
       return self.s >= other.s

    def __int__(self):
        return self.s

class TestTime(unittest.TestCase):

    def test_print(self):
        self.assertEqual(str(Time(3600)), "01:00:00")
        self.assertEqual(str(Time(32536)), "09:02:16")
        self.assertEqual(repr(Time(3600)), "Time(3600)")
        self.assertEqual(repr(Time(32536)), "Time(32536)")

    def test_cmp(self):
        self.assertTrue(Time(2) == Time(2))
        self.assertFalse(Time(2) == Time(3))
        self.assertTrue(Time(2) != Time(3))
        self.assertFalse(Time(2) != Time(2))
        self.assertTrue(Time(2) < Time(3))
        self.assertFalse(Time(4) < Time(3))
        self.assertTrue(Time(2) <= Time(3))
        self.assertFalse(Time(4) <= Time(3))
        self.assertTrue(Time(4) > Time(3))
        self.assertFalse(Time(2) > Time(3))
        self.assertTrue(Time(4) >= Time(3))
        self.assertFalse(Time(2) >= Time(3))

    def test_add(self):
        self.assertEqual(Time(1) + Time(2), Time(3))
        self.assertNotEqual(Time(2) + Time(2), Time(3))

    def test_int(self):
        self.assertEqual(int(Time(3000)), 3000)

if __name__ == "__main__":
    unittest.main()