import unittest
import main


class MyTest(unittest.TestCase):

    def test_normal(self):
        arr = [2, 0, 1]
        self.assertEqual(main.count(arr), 1)
        arr2 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.assertEqual(main.count(arr2), 0)
        arr3 = [0, 0, 0, 2, 0, 2]
        self.assertEqual(main.count(arr3), 2)
        arr4 = [3, 0, 1, 1, 2]
        self.assertEqual(main.count(arr4), 4)

    def test_backwards(self):
        arr = [3, 1, 7]
        self.assertEqual(main.count(arr), 2)
        arr2 = [1, 2, 3, 0, 2, 1, 2, 0, 1, 5, 2, 0]
        self.assertEqual(main.count(arr2), 12)

    def test_complete(self):
        arr = [1, 2, 1, 1, 0, 0, 3, 2, 5, 4, 5, 3]
        self.assertEqual(main.count(arr), 8)
        arr2 = [4, 3, 2, 1, 0, 1, 2]
        self.assertEqual(main.count(arr2), 4)
        arr3 = [1, 3, 1, 0, 6, 2, 0, 1]
        self.assertEqual(main.count(arr3), 6)

    def test_negative(self):
        arr = [1, -2, 1]
        self.assertEqual(main.count(arr), 3)
        arr2 = [2, -4, 0, 0, 1, -3, -3, -3, 1]
        self.assertEqual(main.count(arr2), 19)
        arr3 = [3, 0, 0, -1, 0, 0, 1, 1, 2, 1, 0, 0, -1, 0, 3]
        self.assertEqual(main.count(arr3), 36)


unittest.main()
