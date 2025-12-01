def part1(puzzle_input):
    DIRECTIONS = {"L": -1, "R": 1}

    curr_pos = 50
    zeros = 0

    for instr in puzzle_input:
        direction, value = instr[0], int(instr[1:])
        curr_pos = (curr_pos + DIRECTIONS[direction] * value) % 100

        if curr_pos == 0:
            zeros += 1

    return zeros
