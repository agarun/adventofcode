import time
from collections import namedtuple
import re
from string import ascii_uppercase as alphabet


class Node(object):
    def __init__(self, step):
        self.step = step
        self.parents = []
        self.children = []
        self.ordered = False

    def add_child(self, child):
        self.children.append(child)

    def add_parent(self, parent):
        self.parents.append(parent)

    @property
    def ready(self):
        if not self.parents:
            return True
        return all([parent.ordered for parent in self.parents])

    def __repr__(self):
        return '<Node step={step} parents={parents} children={children} ordered={ordered}>'.format(
            step=self.step,
            parents=list(map(lambda n: n.step, self.parents)),
            children=list(map(lambda n: n.step, self.children)),
            ordered=self.ordered)


def find_orphans(nodes):
    return [node for node in nodes.values() if not node.parents]


def build_graph(steps):
    graph = {}

    regexp = re.compile(
        r'Step ([A-Z]{1}) must be finished before step ([A-Z]{1}) can begin.')

    for step in steps:
        parent_step, child_step = regexp.search(step).groups()

        parent_node = graph.get(parent_step)
        child_node = graph.get(child_step)

        if parent_node and child_node:
            pass
        elif parent_node:
            child_node = Node(child_step)
            graph[child_step] = child_node
        elif child_node:
            parent_node = Node(parent_step)
            graph[parent_step] = parent_node
        else:
            parent_node = Node(parent_step)
            graph[parent_step] = parent_node

            child_node = Node(child_step)
            graph[child_step] = child_node

        parent_node.add_child(child_node)
        child_node.add_parent(parent_node)

    return graph


def part1(steps):
    order = ''
    graph = build_graph(steps)
    chain = find_orphans(graph)
    while chain:
        for i, node in enumerate(chain):
            if node.ready:
                current_node = chain.pop(i)
                break

        order += current_node.step
        current_node.ordered = True

        chain = list(set(current_node.children).union(set(chain)))
        chain = sorted(chain, key=lambda node: node.step)

    return order


class Worker(object):
    @staticmethod
    def busy(workers):
        return any([not worker.idle for worker in workers])

    def __init__(self):
        self.idle = True
        self.current_step = None
        self.current_step_end_time = -1

    def finish_step(self):
        self.current_step.ordered = True

        self.idle = True
        self.current_step = None
        self.current_step_end_time = -1


def part2(steps, workers=2, extra_time=0):
    """ Time is in seconds """
    workers = [Worker() for _ in range(workers)]

    steps_to_time = {
        step: alphabet.index(step) + 1 + extra_time
        for step in alphabet
    }

    time = 0

    graph = build_graph(steps)
    chain = find_orphans(graph)
    while chain or Worker.busy(workers):
        for worker in workers:
            if time == worker.current_step_end_time:
                worker.finish_step()

        new_children = []

        for i, node in enumerate(chain):
            if node.ready:
                for worker in workers:
                    if chain and worker.idle:
                        current_node = chain.pop(i)
                        new_children += current_node.children

                        # Found a worker for this step, start step
                        worker.idle = False
                        worker.current_step = current_node
                        worker.current_step_end_time = (
                            time + steps_to_time[current_node.step])
                        break

        chain = list(set(new_children).union(set(chain)))
        chain = sorted(chain, key=lambda node: node.step)

        time += 1

    return time - 1


def main(filename):
    with open(filename) as file_input:
        steps = file_input.read().splitlines()

    part1_solution = part1(steps)
    part2_solution = part2(steps, 2, 0)
    # part2_solution = part2(steps, 5, 60) # Non-sample input

    Solution = namedtuple('Solution', 'part1, part2')
    return Solution(part1=part1_solution, part2=part2_solution)


if __name__ == "__main__":
    start = time.time()
    main('./input')
    print(time.time() - start, 'elapsed')