import unittest
from stack import Stack

class TestStack(unittest.TestCase):
    def setUp(self):
        self.empty_stack = Stack()
        self.not_empty_stack = Stack()
        self.not_empty_stack.push(2)
        self.stack1 = Stack()
        self.stack1.push(2)
        self.stack1.push(3)
        self.stack1.push(4)
        self.stack1.push(5)
        self.stack1.push(6)

    def test_isempty(self):
        self.assertEqual(self.empty_stack.is_empty(), True)
        self.assertEqual(self.not_empty_stack.is_empty(), False)

    def test_isfull(self):
        self.assertEqual(self.stack1.is_full(), True)
        self.assertEqual(self.empty_stack.is_full(), False)

    def test_push(self):
        self.assertEqual(self.stack1.string_form(), "2<-3<-4<-5<-6<-")

    def test_pop(self):
        self.assertEqual(self.stack1.pop(), 6)
        self.assertEqual(self.stack1.pop(), 5)

if __name__ == '__main__':
    unittest.main()