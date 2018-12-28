import copy
from collections import Counter

CART_UP = '^'
CART_DOWN = 'v'
CART_LEFT = '<'
CART_RIGHT = '>'
CARTS = (CART_UP, CART_DOWN, CART_LEFT, CART_RIGHT)
CART_TURNS_LEFT = (CART_UP, CART_LEFT, CART_DOWN, CART_RIGHT)
CART_TURNS_RIGHT = tuple(reversed(CART_TURNS_LEFT))

LEFT_CORNER = '\\'
RIGHT_CORNER = '/'

VERTICAL = '|'
HORIZONTAL = '-'

INTERSECTION = '+'


class Cart:
    def __init__(self, position, direction):
        self.position = position
        self.direction = direction
        self.turn = 0
        self.turn_order = ['LEFT', 'STRAIGHT', 'RIGHT']

    def turn_at_intersection(self):
        """ Change direction based on turn history (`self.turn`) """
        current_turn = self.turn_order[self.turn]
        self.turn = (self.turn + 1) % len(self.turn_order)

        if current_turn == 'LEFT':
            next_direction_idx = (
                CART_TURNS_LEFT.index(self.direction) + 1) % 4
            if next_direction_idx == -1:
                raise SystemExit
            self.direction = CART_TURNS_LEFT[next_direction_idx]
        elif current_turn == 'STRAIGHT':
            pass
        elif current_turn == 'RIGHT':
            next_direction_idx = (
                CART_TURNS_RIGHT.index(self.direction) + 1) % 4
            if next_direction_idx == -1:
                raise SystemExit
            self.direction = CART_TURNS_RIGHT[next_direction_idx]


def print_grid(carts, grid):
    display = copy.deepcopy(grid)
    for cart in carts:
        x, y = cart.position
        display[y][x] = cart.direction
    for row in display:
        print(''.join(row))


def find_crashes(grid, carts):
    coords = Counter(str(getattr(cart, 'position')) for cart in carts)
    return [
        list(map(int, coord[1:-1].split(', ')))
        for coord, occurrence in coords.items() if occurrence > 1
    ]


def main(file_input):
    with open(file_input) as f:
        grid = [list(line) for line in f.read().splitlines()]

    carts = []

    # Fill out the grid, including spots initially occupied by carts
    for y, tracks in enumerate(grid):
        for x, spot in enumerate(tracks):
            if spot in (CART_UP, CART_DOWN):
                cart = Cart([x, y], spot)
                carts.append(cart)
                grid[y][x] = VERTICAL
            elif spot in (CART_LEFT, CART_RIGHT):
                cart = Cart([x, y], spot)
                carts.append(cart)
                grid[y][x] = HORIZONTAL

    ticks = 0
    crashes = []
    while len(carts) >= 2:
        carts = sorted(carts, key=lambda cart: list(reversed(cart.position)))

        for cart in carts:

            x, y = cart.position

            if cart.direction == CART_UP:
                # One spot above
                if grid[y - 1][x] == VERTICAL:
                    pass
                elif grid[y - 1][x] == LEFT_CORNER:
                    cart.direction = CART_LEFT
                elif grid[y - 1][x] == RIGHT_CORNER:
                    cart.direction = CART_RIGHT
                elif grid[y - 1][x] == INTERSECTION:
                    cart.turn_at_intersection()

                cart.position = [x, y - 1]

            elif cart.direction == CART_DOWN:
                # One spot below
                if grid[y + 1][x] == VERTICAL:
                    pass
                elif grid[y + 1][x] == LEFT_CORNER:
                    cart.direction = CART_RIGHT
                elif grid[y + 1][x] == RIGHT_CORNER:
                    cart.direction = CART_LEFT
                elif grid[y + 1][x] == INTERSECTION:
                    cart.turn_at_intersection()

                cart.position = [x, y + 1]

            elif cart.direction == CART_LEFT:
                # One spot left
                if grid[y][x - 1] == HORIZONTAL:
                    pass
                elif grid[y][x - 1] == LEFT_CORNER:
                    cart.direction = CART_UP
                elif grid[y][x - 1] == RIGHT_CORNER:
                    cart.direction = CART_DOWN
                elif grid[y][x - 1] == INTERSECTION:
                    cart.turn_at_intersection()

                cart.position = [x - 1, y]

            elif cart.direction == CART_RIGHT:
                # One spot right
                if grid[y][x + 1] == HORIZONTAL:
                    pass
                elif grid[y][x + 1] == LEFT_CORNER:
                    cart.direction = CART_DOWN
                elif grid[y][x + 1] == RIGHT_CORNER:
                    cart.direction = CART_UP
                elif grid[y][x + 1] == INTERSECTION:
                    cart.turn_at_intersection()

                cart.position = [x + 1, y]

            new_crashes = find_crashes(grid, carts)
            for crash in new_crashes:
                crashes.append(crash)
                carts = [
                    cart for cart in carts if cart.position not in crashes
                ]

        # we could also look for crashes after the tick (i.e. here),
        # but we'd have to use a more complicated check for carts within 1 unit
        # of each other in case they both moved during the tick (still crashed!)

        ticks += 1
        # print_grid(carts, grid)

    part1 = crashes[0]
    part2 = carts[-1].position

    return part1, part2


if __name__ == '__main__':
    # file_input = './input.sample'
    file_input = './input'
    print(main(file_input))
