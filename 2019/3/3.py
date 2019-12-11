""" 2019 Day 3 """
RIGHT = "R"
UP = "U"
DOWN = "D"
LEFT = "L"


def manhattan_distance(point_1, point_2):
    return abs(point_1[0] - point_2[0]) + abs(point_1[1] - point_2[1])


def wire_paths_input():
    with open("./input") as file_input:
        return file_input.read()


class Wire:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.history = {}
        self.step_number = 0

    def move(self, direction, distance):
        dx = 0
        dy = 0

        # `range` -> start at next new coordinate, end at last new coordinate
        if direction == RIGHT:
            dx = +distance
            new_x = self.x + dx

            for move_x in range(self.x + 1, new_x + 1):
                self.record(move_x, self.y)
        if direction == LEFT:
            dx = -distance
            new_x = self.x + dx

            for move_x in reversed(range(new_x, self.x)):
                self.record(move_x, self.y)
        if direction == UP:
            dy = +distance
            new_y = self.y + dy

            for move_y in range(self.y + 1, new_y + 1):
                self.record(self.x, move_y)
        if direction == DOWN:
            dy = -distance
            new_y = self.y + dy

            for move_y in reversed(range(new_y, self.y)):
                self.record(self.x, move_y)

        self.x += dx
        self.y += dy

    def record(self, x, y):
        self.step_number += 1
        position = f"[{x}, {y}]"
        if not self.history.get(position):
            self.history[position] = self.step_number


def part1(wire_paths_input=wire_paths_input()):
    wire_1 = Wire()
    wire_2 = Wire()

    wire_paths = [line.split(",") for line in wire_paths_input.splitlines()]
    wire_1_path, wire_2_path = wire_paths

    for instruction in wire_1_path:
        direction = instruction[0]
        distance = int(instruction[1:])
        wire_1.move(direction, distance)

    for instruction in wire_2_path:
        direction = instruction[0]
        distance = int(instruction[1:])
        wire_2.move(direction, distance)

    intersection_points = []
    for point in wire_1.history.keys():
        if (point != "[0, 0]") and (point in wire_2.history):
            intersection_points.append([int(coord) for coord in point[1:-1].split(",")])

    closest_intersection = min(
        intersection_points, key=lambda point: manhattan_distance(point, [0, 0]),
    )
    return {
        "wire_1": wire_1,
        "wire_2": wire_2,
        "intersection_points": intersection_points,
        "closest_intersection_distance": manhattan_distance(
            closest_intersection, [0, 0]
        ),
    }


def part2(wire_paths_input=wire_paths_input()):
    part1_solution = part1(wire_paths_input)

    wire_1 = part1_solution["wire_1"]
    wire_2 = part1_solution["wire_2"]
    intersection_points = part1_solution["intersection_points"]
    best_intersection_point = min(
        intersection_points,
        key=lambda point: wire_1.history[str(point)] + wire_2.history[str(point)],
    )
    return (
        wire_1.history[str(best_intersection_point)]
        + wire_2.history[str(best_intersection_point)]
    )


# retrospectively:
# storing the directions as integers for DX and DY (+1, 0, -1, etc.) as others did would've been much more elegant lol
