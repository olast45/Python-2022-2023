from randomqueue import *
import unittest


class Test(unittest.TestCase):

    def setUp(self):
        self.randomqueue = RandomQueue()

    def test_insert(self):
        self.assertEqual(self.randomqueue.is_empty(), True)
        self.randomqueue.insert(5)
        self.assertEqual(self.randomqueue.is_empty(), False)

    def test_empty(self):
        self.assertEqual(self.randomqueue.is_empty(), True)
        self.randomqueue.insert(1)
        self.assertEqual(self.randomqueue.is_empty(), False)

    def test_full(self):
        self.assertEqual(self.randomqueue.is_full(), False)
        for i in range(15):
            self.randomqueue.insert(i)
        self.assertEqual(self.randomqueue.is_full(), True)

    def test_remove(self):
        self.assertEqual(self.randomqueue.is_empty(), True)
        self.randomqueue.insert(1)
        self.assertEqual(self.randomqueue.remove(), 1)
        for i in range(10):
            self.randomqueue.insert(i)
        self.assertTrue(self.randomqueue.remove() in range(10))

    def test_clear(self):
        for i in range(5):
            self.randomqueue.insert(i)
        self.randomqueue.clear()
        self.assertEqual(self.randomqueue.is_empty(), True)



