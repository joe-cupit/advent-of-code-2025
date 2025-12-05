def part2(puzzle_input: tuple[list[list[int]], list[int]]):
    id_ranges, _ = puzzle_input

    fresh_ids = 0
    for id_range in id_ranges:
        fresh_ids += id_range[1] - id_range[0] + 1

    return fresh_ids
