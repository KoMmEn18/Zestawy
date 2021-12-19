import unittest
from queue import Queue

class TestQueue(unittest.TestCase):
    def setUp(self):
        self.empty_queue = Queue()
        self.not_empty_queue = Queue()
        self.not_empty_queue.put(2)
        self.queue1 = Queue()
        self.queue1.put(2)
        self.queue1.put(3)
        self.queue1.put(4)
        self.queue1.put(5)
        self.queue1.put(6)

    
    def test_isempty(self):
        self.assertEqual(self.empty_queue.is_empty(), True)
        self.assertEqual(self.not_empty_queue.is_empty(), False)

    def test_isfull(self):
        self.assertEqual(self.queue1.is_full(), True)
        self.assertEqual(self.empty_queue.is_full(), False)

    def test_push(self):
        self.assertEqual(self.queue1.string_form(), "2->3->4->5->6->")

    def test_pop(self):
        self.assertEqual(self.queue1.get(), 2)
        self.assertEqual(self.queue1.get(), 3)

if __name__ == '__main__':
    unittest.main()