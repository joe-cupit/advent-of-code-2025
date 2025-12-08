SPLITTER = "^"


def part1(puzzle_input: list[str]):
    beams = set([puzzle_input[0].index("S")])

    times_split = 0
    for row in puzzle_input[1:]:
        if len(row.replace(".", "")) == 0:
            continue

        for bi in list(beams):
            if row[bi] == SPLITTER:
                beams.remove(bi)
                if bi - 1 >= 0:
                    beams.add(bi - 1)
                if bi + 1 < len(row):
                    beams.add(bi + 1)

                times_split += 1

    return times_split
