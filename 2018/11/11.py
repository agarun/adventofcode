from functools import partial
from collections import namedtuple


def hundreds_digit(number):
    return number % 1000 // 100


def compute_power(serial_number, x, y):
    rack_id = x + 10
    power = rack_id * y
    power += serial_number
    power *= rack_id
    power = hundreds_digit(power) - 5
    return power


sums = {}


def sum_square(grid, col, row, size):
    """ [col, row] is the top-left X,Y coordinate """
    if size == 0:
        return 0
    elif sums.get((
            col,
            row,
            size,
    )):
        return sums[col, row, size]

    last_row = row + size - 1
    last_col = col + size - 1
    current_power = sum(grid[last_row][col:col + size]) + sum(
        [grid[y][last_col] for y in range(row, row + size - 1)])

    total_power = current_power + sum_square(grid, col, row, size - 1)
    sums[col, row, size] = total_power
    return total_power


def square_power(grid, size):
    print(size)

    largest_power = float('-inf')
    largest_power_coordinates = []

    for row in range(0, 300 - size):
        for col in range(0, 300 - size):
            power = sum_square(grid, col, row, size)
            # power = sum([sum(grid[y][col:col + size]) for y in range(row, row + size)])

            if largest_power < power:
                largest_power = power
                largest_power_coordinates = [col, row]

    return largest_power, largest_power_coordinates


def main(serial_number):
    compute_power_level = partial(compute_power, serial_number)

    grid = [[compute_power_level(x, y) for x in range(0, 300)]
            for y in range(0, 300)]

    part1_power, part1 = square_power(grid, 3)
    print(part1_power, part1)

    square_powers = [square_power(grid, size) for size in range(0, 300)]
    max_square_power, max_square_power_coords = max(
        square_powers, key=lambda p: p[0])
    max_size = square_powers.index((max_square_power, max_square_power_coords))
    part2 = [*max_square_power_coords, max_size]
    print(max_square_power, part2)

    Solution = namedtuple('Solution', 'part1, part2')
    return Solution(part1=part1, part2=part2)


if __name__ == "__main__":
    print(main(6878))