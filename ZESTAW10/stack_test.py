from stack import *
import unittest


class Test(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_empty(self):
        self.assertEqual(self.stack.is_empty(), True)
        self.stack.push(1)
        self.assertEqual(self.stack.is_empty(), False)

    def test_full(self):
        self.assertEqual(self.stack.is_full(), False)
        for i in range(10):
            self.stack.push(i)
        self.assertEqual(self.stack.is_full(), True)

    def test_push_and_pop(self):
        self.assertEqual(self.stack.is_empty(), True)
        self.stack.push(1)
        self.assertEqual(self.stack.is_empty(), False)
        self.stack.pop()
        self.assertEqual(self.stack.is_empty(), True)
        with self.assertRaises(ValueError):
            self.stack.pop()
        for i in range(10):
            self.stack.push(i)
        with self.assertRaises(ValueError):
            self.stack.push(1)
