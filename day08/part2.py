import math


def straight_distance(point1: tuple[int, int, int], point2: tuple[int, int, int]):
    return math.sqrt(sum([(point1[i] - point2[i]) ** 2 for i in range(len(point1))]))


def part2(puzzle_input: list[tuple[int, int, int]]):

    point_distances = []

    for i1, point1 in enumerate(puzzle_input):
        for j, point2 in enumerate(puzzle_input[i1 + 1 :]):
            point_distances.append((straight_distance(point1, point2), i1, i1 + j + 1))

    point_distances.sort(key=lambda p: p[0])

    circuits: list[set[int]] = []
    for pair in point_distances:
        new_circuit = set([pair[1], pair[2]])
        for circuit in list(circuits):
            if pair[1] in circuit or pair[2] in circuit:
                new_circuit.update(circuit)
                circuits.remove(circuit)

        if len(new_circuit) == len(puzzle_input):
            return puzzle_input[pair[1]][0] * puzzle_input[pair[2]][0]

        circuits.append(new_circuit)

    return 0
