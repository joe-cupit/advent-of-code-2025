SPLITTER = "^"


def part2(puzzle_input: list[str]):
    beams = dict([(i, 0) for i in range(len(puzzle_input[0]))])
    beams[puzzle_input[0].index("S")] = 1

    for row in puzzle_input[1:]:
        if len(row.replace(".", "")) == 0:
            continue

        for bi in list(beams):
            if row[bi] == SPLITTER:
                if bi - 1 in beams:
                    beams[bi - 1] += beams[bi]
                if bi + 1 in beams:
                    beams[bi + 1] += beams[bi]
                beams[bi] = 0

    return sum(beams.values())
