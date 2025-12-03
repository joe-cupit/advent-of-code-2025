def part2(puzzle_input: list[str]):
    invalids = set()

    for id_range in puzzle_input:
        lower, upper = [int(i) for i in id_range.split("-")]

        length = len(str(lower))
        while length <= len(str(upper)):
            for i in range(1, length // 2 + 1):
                if length % i != 0:
                    continue

                start_digits = int(str(lower)[:i])
                while (n := int(f"{start_digits}" * (length // i))) <= upper:
                    if lower <= n <= upper:
                        invalids.add(n)

                    start_digits += 1

            length += 1
            lower = 10 ** (length - 1)

    return sum(invalids)
