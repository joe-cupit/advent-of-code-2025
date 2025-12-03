def part1(puzzle_input: list[str]):
    invalids = set()

    for id_range in puzzle_input:
        lower, upper = [int(i) for i in id_range.split("-")]

        length = len(str(lower))
        while length <= len(str(upper)):
            if length % 2 != 0:
                length += 1
                lower = 10 ** (length - 1)
                continue

            start_digits = int(str(lower)[: length // 2])
            while int(f"{start_digits}{start_digits}") <= upper:
                if lower <= int(f"{start_digits}{start_digits}") <= upper:
                    invalids.add(int(f"{start_digits}{start_digits}"))

                start_digits += 1

            length += 1
            lower = 10 ** (length - 1)

    return sum(invalids)
