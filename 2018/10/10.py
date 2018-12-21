import re


def parse_line(line):
    regexp = re.compile(r'position=<(.+),(.+)>\svelocity=<(.+),(.+)>')
    points = list(map(int, regexp.match(line).groups()))
    return points  # dx, dy, vx, vy


def draw_grid(grid):
    for row in grid:
        print(''.join(row))


INPUT = './input'
with open(INPUT) as file:
    dataset = [parse_line(line) for line in file.readlines()]

    seconds = 0
    while True:
        min_dx = min([points[0] for points in dataset])
        min_dy = min([points[1] for points in dataset])
        max_dx = max([points[0] for points in dataset])
        max_dy = max([points[1] for points in dataset])

        if max_dx - min_dx > 100 or max_dy - min_dy > 100:
            # assuming the word is not giant, it should show up
            # when all the points are (arbitrarily) close enough
            grid = []
        else:
            grid = [['.'] * (max_dx - min_dx + 1)
                    for _ in range(min_dy, max_dy + 1)]

            print(f'seconds: {seconds}, dimensions: {len(grid)}x{len(grid[0])}')

        for i, points in enumerate(dataset):
            dx, dy, vx, vy = points

            dataset[i][0] += vx
            dataset[i][1] += vy

            if grid:
                grid[dy - min_dy][dx - min_dx] = '#'

        draw_grid(grid)

        seconds += 1