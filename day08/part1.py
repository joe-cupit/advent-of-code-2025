import math


def straight_distance(point1: tuple[int, int, int], point2: tuple[int, int, int]):
    return math.sqrt(sum([(point1[i] - point2[i]) ** 2 for i in range(len(point1))]))


def part1(puzzle_input: list[tuple[int, int, int]], connections: int = 1000):

    closest_points = []
    biggest_small = 9999999999999

    for i1, point1 in enumerate(puzzle_input):
        for j, point2 in enumerate(puzzle_input[i1 + 1 :]):

            dist = straight_distance(point1, point2)
            if dist < biggest_small:
                if len(closest_points) == connections:
                    closest_points = closest_points[:-1]
                closest_points.append((dist, i1, i1 + j + 1))
                closest_points.sort()
                biggest_small = closest_points[-1][0]

    circuits: list[set[int]] = []
    for pair in closest_points:
        new_circuit = set([pair[1], pair[2]])
        for circuit in list(circuits):
            if pair[1] in circuit or pair[2] in circuit:
                new_circuit.update(circuit)
                circuits.remove(circuit)

        circuits.append(new_circuit)

    big_three = sorted(circuits, key=lambda c: len(c), reverse=True)[:3]

    out = 1
    for circuit in big_three:
        out *= len(circuit)

    return out
