""" 2019 Day 3 tests
Usage: `$ python -m unittest -vb test`
"""
import unittest

day_3 = __import__("3", fromlist="main")


class TestDay3(unittest.TestCase):
    def test_part1(self):
        """ Calculates the manhattan distance from the central port to the closest intersection """
        example_1 = """R8,U5,L5,D3
U7,R6,D4,L4"""
        self.assertEqual(
            day_3.part1(example_1)["closest_intersection_distance"], 6,
        )
        example_2 = """R75,D30,R83,U83,L12,D49,R71,U7,L72
U62,R66,U55,R34,D71,R55,D58,R83"""
        self.assertEqual(
            day_3.part1(example_2)["closest_intersection_distance"], 159,
        )
        example_3 = """R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"""
        self.assertEqual(
            day_3.part1(example_3)["closest_intersection_distance"], 135,
        )
        self.assertEqual(day_3.part1()["closest_intersection_distance"], 806)

    def test_part2(self):
        """ Finds the fewest combined steps the wires take to reach an intersection """
        example_1 = """R8,U5,L5,D3
U7,R6,D4,L4"""
        self.assertEqual(
            day_3.part2(example_1), 30,
        )
        example_2 = """R75,D30,R83,U83,L12,D49,R71,U7,L72
U62,R66,U55,R34,D71,R55,D58,R83"""
        self.assertEqual(
            day_3.part2(example_2), 610,
        )
        example_3 = """R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"""
        self.assertEqual(
            day_3.part2(example_3), 410,
        )
        self.assertEqual(
            day_3.part2(), 66076,
        )


if __name__ == "__main__":
    unittest.main()
