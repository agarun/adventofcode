import time
from datetime import datetime
from collections import defaultdict, Counter, namedtuple
import functools
import re


class Guard():
    def __init__(self, guard_id):
        self.id = guard_id
        self.minutes_asleep = []
        self.minute_counter = Counter()

    def add_nap(self, minutes_asleep):
        self.minutes_asleep += minutes_asleep
        self.minute_counter.update(minutes_asleep)

    @property
    def favorite_minute(self):
        if self.minutes_asleep:
            return max(self.minutes_asleep, key=self.minute_counter.get)
        return -1


def minutes_asleep(falls_asleep, wakes_up):
    """ All asleep/awake times are between 00:00 - 00:59
    Minutes asleep are inclusive of the time the events started 
    """
    minute_fell_asleep = int(falls_asleep[15:17])
    minute_woke_up = int(wakes_up[15:17])
    return list(range(minute_fell_asleep, minute_woke_up + 1))


def main(filename):
    with open(filename) as file_input:
        log = file_input.read().splitlines()
        log.sort(
            key=lambda event: datetime.strptime(event[1:17], '%Y-%m-%d %H:%M'))

    guards = {}

    # some defaults
    current_guard = None
    current_minutes_asleep = lambda x: -1

    for line in log:
        if line.endswith('begins shift'):
            g_id_regex = re.compile(r'Guard #(\d+)')
            guard_id = int(g_id_regex.search(line).group(1))

            if guards.get(guard_id):
                current_guard = guards.get(guard_id)
            else:
                current_guard = Guard(guard_id)
                guards[guard_id] = current_guard

        elif line.endswith('falls asleep'):
            current_minutes_asleep = functools.partial(minutes_asleep, line)
        elif line.endswith('wakes up'):
            shift_nap = current_minutes_asleep(line)
            current_guard.add_nap(shift_nap)

    guard_list = sorted(
        guards.values(), key=lambda guard: len(guard.minutes_asleep))
    sleepiest_guard = guard_list[-1]
    part1 = sleepiest_guard.id * sleepiest_guard.favorite_minute
    print(part1)

    # ---

    minutes = defaultdict(list)
    for guard in guards.values():
        minutes[guard.favorite_minute].append(guard)

    # some defaults
    most_frequent_minute = None
    most_frequent_minute_count = 0
    most_frequent_guard = None

    for minute, guards in minutes.items():
        for guard in guards:
            if guard.minute_counter[minute] > most_frequent_minute_count:
                most_frequent_minute = minute
                most_frequent_minute_count = guard.minute_counter[minute]
                most_frequent_guard = guard

    part2 = most_frequent_minute * most_frequent_guard.id
    print(part2)

    Solution = namedtuple('Solution', 'part1, part2')
    return Solution(part1=part1, part2=part2)


if __name__ == "__main__":
    start = time.time()
    main('./input')
    print(time.time() - start, 'elapsed')