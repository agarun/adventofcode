""" Day 7 tests
Usage: `$ python -m unittest -vb test`
"""
import unittest
main = __import__('7', fromlist='main').main

SAMPLE_FILE = './input.sample'


class TestDay7(unittest.TestCase):
    def setUp(self):
        self.solution = main(SAMPLE_FILE)

    def test_part1(self):
        """ Finds the correct order of steps """
        self.assertEqual(self.solution.part1, 'CABDFE')

    def test_part2(self):
        """ Finds how long 2 workers would take to execute the steps """
        self.assertEqual(self.solution.part2, 15)


if __name__ == '__main__':
    unittest.main()