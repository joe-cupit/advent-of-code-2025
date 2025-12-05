def part1(puzzle_input: tuple[list[list[int]], list[int]]):
    id_ranges, ids = puzzle_input
    MIN, MAX = id_ranges[0][0], id_ranges[-1][1]

    fresh_ids = 0
    for id in ids:
        if id < MIN or id > MAX:
            continue

        for i in range(len(id_ranges)):
            if id_ranges[i][0] <= id <= id_ranges[i][1]:
                fresh_ids += 1
                break

    return fresh_ids
