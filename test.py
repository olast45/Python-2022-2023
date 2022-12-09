import unittest
from SingleList import *


class Test(unittest.TestCase):

    def setUp(self):
        self.single_list = SingleList()

    def test_empty(self):
        self.assertEqual(self.single_list.is_empty(), True)
        self.single_list.insert_head(Node(1))
        self.single_list.insert_head(Node(2))
        self.assertEqual(self.single_list.is_empty(), False)

    def test_count(self):
        self.single_list.insert_head(Node(1))
        self.single_list.insert_head(Node(2))
        self.assertEqual(self.single_list.count(), 2)
        self.single_list.insert_head(Node(3))
        self.assertEqual(self.single_list.count(), 3)

    def test_insert(self):
        self.single_list.insert_head(Node(1))
        self.assertEqual(self.single_list.head.data, 1)
        self.single_list.insert_head(Node(2))
        self.single_list.insert_head(Node(1))
        self.assertEqual(self.single_list.head.next.data, 2)
        self.single_list.insert_tail(Node(4))
        self.assertEqual(self.single_list.tail.data, 4)
        self.single_list.insert_tail(Node(5))
        self.single_list.insert_tail(Node(6))
        self.assertEqual(self.single_list.tail.data, 6)

    def test_remove(self):
        self.single_list.insert_head(Node(1))
        self.single_list.insert_head(Node(2))
        self.single_list.remove_head()
        self.assertEqual(self.single_list.head.data, 1)
        self.single_list.remove_head()
        self.assertEqual(self.single_list.is_empty(), True)

    def test_search(self):
        self.single_list.insert_head(Node(1))
        self.single_list.insert_head(Node(2))
        self.single_list.insert_head(Node(3))
        self.assertIsNotNone(self.single_list.search(2))
        self.assertIsNotNone(self.single_list.search(1))
        self.assertIsNone(self.single_list.search(5))

    def test_find(self):
        self.single_list.insert_head(Node(1))
        self.single_list.insert_head(Node(2))
        self.single_list.insert_head(Node(3))
        self.assertEqual(self.single_list.find_min(), 1)
        self.assertEqual(self.single_list.find_max(), 3)

    def test_reverse(self):
        self.single_list.insert_head(Node(1))
        self.single_list.insert_head(Node(2))
        self.single_list.insert_head(Node(3))
        self.single_list.reverse()
        self.assertEqual(self.single_list.head.data, 1)
        self.single_list.reverse()
        self.assertEqual(self.single_list.head.data, 3)


if __name__ == "__main__":
    unittest.main()

