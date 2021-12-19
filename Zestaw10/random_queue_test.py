import unittest
from random_queue import RandomQueue

class TestRadomQueue(unittest.TestCase):
    def setUp(self):
        self.empty_queue = RandomQueue()
        self.not_empty_queue = RandomQueue()
        self.not_empty_queue.insert(2)
        self.queue1 = RandomQueue()
        self.queue1.insert(2)
        self.queue1.insert(3)
        self.queue1.insert(4)

    def test_isempty(self):
        self.assertEqual(self.empty_queue.is_empty(), True)
        self.assertEqual(self.not_empty_queue.is_empty(), False)

    def test_isfull(self):
        self.assertEqual(self.empty_queue.is_full(), False)

    def test_insert(self):
        self.assertEqual(self.queue1.string_form(), "[2, 3, 4]")

if __name__ == '__main__':
    unittest.main()
