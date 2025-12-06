def part2(puzzle_input: list[str]):
    grand_total = 0

    operators = puzzle_input[-1].split()

    problem_index = 0
    curr_problem = ""
    for col_i in range(len(puzzle_input[0])):
        problem_value = "".join([row[col_i] for row in puzzle_input[:-1]])

        # if the column is empty
        if len(problem_value.strip()) == 0:
            grand_total += eval(curr_problem[:-1])
            curr_problem = ""
            problem_index += 1
            continue

        curr_problem += problem_value + operators[problem_index]

    return grand_total
