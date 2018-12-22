""" Day 11 tests
Usage: `$ python -m unittest -vb test`
"""
import unittest
main = __import__('11', fromlist='main').main


class TestDay11(unittest.TestCase):
    def setUp(self):
        self.solution = main(42)

    def test_part1(self):
        """ Finds the X,Y coordinate of the top-left fuel cell of the 3x3 square with the largest total power """
        self.assertEqual(self.solution.part1, [21, 61])

    def test_part2(self):
        """ Finds the X,Y,size identifier when checking squares of all sizes for the largest power """
        self.assertEqual(self.solution.part2, [232, 251, 12])


if __name__ == '__main__':
    unittest.main()