def part1(puzzle_input: list[str]):
    grand_total = 0

    puzzle_input_split = [row.split() for row in puzzle_input]

    for col_i in range(len(puzzle_input_split[0])):
        problem = puzzle_input_split[-1][col_i].join(
            [row[col_i] for row in puzzle_input_split[:-1]]
        )

        grand_total += eval(problem)

    return grand_total
