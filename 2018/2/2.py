from collections import defaultdict, Counter
from functools import reduce
from itertools import combinations

# 1
with open('./input') as file:
    appearance_to_counts = defaultdict(int)

    ids = file.readlines()
    for id in ids:
        letter_to_counts = defaultdict(int)
        for letter in id:
            letter_to_counts[letter] += 1

        appearances = letter_to_counts.values()
        appearances = set(appearances)

        for appearance in appearances:
            appearance_to_counts[appearance] += 1
    # or...
    # counts = [Counter(id) for id in ids]

    appearance_to_counts.pop(1)
    checksum = reduce(
        lambda x, y: x * y, 
        appearance_to_counts.values(), 
        1)

    print(checksum)

# 2
with open('./input') as file:
    ids = file.read().splitlines()

    # TODO: zip
    id_combos = combinations(ids, 2)
    for combo in id_combos:
        first, second = combo

        differences = 0
        for i in range(len(first)):
            if first[i] != second[i]:
                differences += 1

        if differences == 1:
            common = ''
            for j, str in enumerate(first):
                if first[j] == second[j]:
                    common += str

            print(common)
            break
