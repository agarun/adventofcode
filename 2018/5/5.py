import re

alphabet = 'abcdefghijklmnopqrstuvwxyz'


def react(polymer, idx):
    return polymer[:idx] + polymer[idx + 2:]


def part1(polymer):
    unstable = True
    while unstable:
        unstable = False

        for i in range(1, len(polymer)):
            if i < len(polymer) and abs(ord(polymer[i]) -
                                        ord(polymer[i - 1])) == 32:
                unstable = True
                polymer = react(polymer, i - 1)

    return polymer


def part2(polymer):
    return min((
        len(part1(re.sub(letter, '', polymer, flags=re.IGNORECASE)))
        for letter in alphabet
    ))


with open('./input') as file_input:
    polymer = file_input.read().strip()
    print(len(part1(polymer)))
    print(part2(polymer))
