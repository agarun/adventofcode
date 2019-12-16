def orbit_map_from_file():
    with open("./input") as orbit_map_from_file:
        return orbit_map_from_file.read().splitlines()


class Node:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent

    def num_indirect_orbits(self):
        parent = self.parent
        if parent and parent.parent:
            return 1 + parent.num_indirect_orbits()
        else:
            return 0


def create_tree(orbit_map):
    nodes = {}
    orbits = orbit_map.split("\n") if orbit_map else orbit_map_from_file()

    for orbit in orbits:
        parent, child = orbit.split(")")
        if not nodes.get(parent):
            nodes[parent] = Node(parent, None)

        if not nodes.get(child):
            nodes[child] = Node(child, nodes[parent])
        else:
            nodes[child].parent = nodes[parent]

    return nodes


def part1(orbit_map=None):
    nodes = create_tree(orbit_map)

    num_indirect_orbits = 0
    for node in nodes.values():
        num_indirect_orbits += node.num_indirect_orbits()

    return (
        len(nodes.keys()) - 1 + num_indirect_orbits
    )  # or len(orbits) + num_indirect_orbits


def get_tree_path(tree, start):
    path = []
    current = tree[start]
    while current.parent:
        path.append(current.parent)
        current = current.parent
    return list(reversed(path))


def part2(orbit_map=None, start="YOU", end="SAN"):
    nodes = create_tree(orbit_map)
    path_from_start = get_tree_path(nodes, start)
    path_from_end = get_tree_path(nodes, end)

    for node in reversed(path_from_start):
        if node in path_from_end:
            transfers_for_start = len(path_from_start) - 1 - path_from_start.index(node)
            transfers_for_end = len(path_from_end) - 1 - path_from_end.index(node)
            return transfers_for_start + transfers_for_end

