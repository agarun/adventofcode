""" Day 4 tests
Usage: `$ python -m unittest -vb test`
"""
import unittest
main = __import__('4', fromlist='main').main

SAMPLE_FILE = './input.sample'


class TestDay4(unittest.TestCase):
    def setUp(self):
        self.solution = main(SAMPLE_FILE)

    def test_part1(self):
        """ The guard with the most minutes asleep's most frequently slept minute * the ID of said guard """
        self.assertEqual(self.solution.part1, 240)

    def test_part2(self):
        """ The most frequently slept minute by guards * the ID of the guard responsible """
        self.assertEqual(self.solution.part2, 4455)


if __name__ == '__main__':
    unittest.main()