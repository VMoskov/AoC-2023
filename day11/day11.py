from itertools import combinations


def part1():
    space = open("day11_input.txt", 'r').read().splitlines()
    galaxies, empty_rows, empty_cols = extract_data(space)
    combs = list(combinations(galaxies, 2))

    distances = []
    for pair in combs:
        distances.append(find_distances(pair, empty_rows, empty_cols, 2))
    print(f"Part1: {sum(distances)}")


def part2():
    space = open("day11_input.txt", 'r').read().splitlines()
    galaxies, empty_rows, empty_cols = extract_data(space)
    combs = list(combinations(galaxies, 2))

    distances = []
    for pair in combs:
        distances.append(find_distances(pair, empty_rows, empty_cols, 1000000))
    print(f"Part2: {sum(distances)}")


def extract_data(space):
    galaxies = []
    empty_rows, empty_cols = [i for i in range(len(space))], [i for i in range(len(space[0]))]
    for i, line in enumerate(space):
        for j, char in enumerate(line):
            if char == "#":
                galaxies.append((i, j))
                if i in empty_rows:
                    empty_rows.remove(i)
                if j in empty_cols:
                    empty_cols.remove(j)
    return galaxies, empty_rows, empty_cols


def find_distances(pair, empty_rows, empty_cols, expansion_factor):
    multiplication_factor = expansion_factor - 1

    raw_distance = abs(pair[1][0] - pair[0][0]) + abs(pair[1][1] - pair[0][1])
    empty_rows_between = [i for i in range(*sorted([pair[0][0], pair[1][0]])) if i in empty_rows]
    empty_cols_between = [i for i in range(*sorted([pair[0][1], pair[1][1]])) if i in empty_cols]

    true_distance = raw_distance + multiplication_factor * (len(empty_rows_between) + len(empty_cols_between))
    return true_distance


if __name__ == "__main__":
    part1()
    part2()
