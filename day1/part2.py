def part2(puzzle_input):
    DIRECTIONS = {"L": -1, "R": 1}

    curr_pos = 50
    zeros = 0

    for instr in puzzle_input:
        direction, value = instr[0], int(instr[1:])
        if value == 0:
            continue

        next_pos = curr_pos + (DIRECTIONS[direction] * value)

        if next_pos == 0:
            zeros += 1
        elif next_pos >= 100:
            zeros += next_pos // 100
        elif next_pos < 0:
            zeros += abs(next_pos) // 100 + (curr_pos != 0)

        curr_pos = next_pos % 100

    return zeros
