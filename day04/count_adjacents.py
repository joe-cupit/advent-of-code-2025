def count_adjacents(grid: list[str], match, loc: tuple[int, int]):
    adj = 0

    adjacents = [
        (loc[0] - 1, loc[1] - 1),
        (loc[0] - 1, loc[1]),
        (loc[0] - 1, loc[1] + 1),
        (loc[0], loc[1] - 1),
        (loc[0], loc[1] + 1),
        (loc[0] + 1, loc[1] - 1),
        (loc[0] + 1, loc[1]),
        (loc[0] + 1, loc[1] + 1),
    ]

    for adj_loc in adjacents:
        if (
            adj_loc[0] < 0
            or adj_loc[0] >= len(grid)
            or adj_loc[1] < 0
            or adj_loc[1] >= len(grid[0])
        ):
            continue

        if grid[adj_loc[0]][adj_loc[1]] == match:
            adj += 1

    return adj
