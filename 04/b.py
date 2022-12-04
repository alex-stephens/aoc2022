def parse_ranges(line):
    l1, l2 = [a.split("-") for a in line.strip().split(",")]
    v = list(map(int, l1 + l2))
    return [v[:2], v[2:]]


def fully_contained(r1, r2):
    if r1[0] >= r2[0] and r1[1] <= r2[1]:
        return True
    if r2[0] >= r1[0] and r2[1] <= r1[1]:
        return True
    return False


def has_overlap(r1, r2):
    if fully_contained(r1, r2):
        return True
    if r1[0] >= r2[0] and r1[0] <= r2[1]:
        return True
    if r1[1] >= r2[0] and r1[1] <= r2[1]:
        return True
    return False


def main():
    filename = "input.txt"
    ans = 0

    with open(filename) as f:
        for line in f.readlines():
            r1, r2 = parse_ranges(line)
            if has_overlap(r1, r2):
                ans += 1
    print(ans)


if __name__ == "__main__":
    main()
