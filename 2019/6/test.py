""" 2019 Day 6 tests
Usage: `$ python -m unittest -vb test`
"""
import unittest

day_6 = __import__("6", fromlist="main")


class TestDay6(unittest.TestCase):
    def test_part1(self):
        """ Finds the total number of direct and indirect orbits in the orbit map """
        example_1 = """COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L"""
        self.assertEqual(
            day_6.part1(example_1), 42,
        )
        self.assertEqual(
            day_6.part1(), 270768,
        )

    def test_part2(self):
        """ Finds the minimum number of orbital transfers needed to move from you to santa """
        example_1 = """COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
K)YOU
I)SAN"""
        self.assertEqual(
            day_6.part2(example_1), 4,
        )
        self.assertEqual(
            day_6.part2(), 451,
        )


if __name__ == "__main__":
    unittest.main()
