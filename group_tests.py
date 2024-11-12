import unittest
import group
from group import groups_of_3


class UnitTests(unittest.TestCase):
    pass

# Part 1
    def test_groups_of_3_a(self):
        array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        result = groups_of_3(array)
        expected = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(result, expected)

    def test_groups_of_3_b(self):
        array = [1,2,3,4,5,6,7,8]
        result = groups_of_3(array)
        expected = [[1, 2, 3], [4, 5, 6], [7, 8]]
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()