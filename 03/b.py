import string


def get_priority(c):
    return string.ascii_letters.index(c) + 1


def get_common_letter(strings):
    return list(set(strings[0]).intersection(*strings[1:]))[0]


def main():
    filename = "input.txt"
    p = 0
    groups = []

    with open(filename) as f:
        for i, line in enumerate(f.readlines()):
            g = i // 3
            if len(groups) < g + 1:
                groups.append([])

            groups[g].append(line.strip())

    for group in groups:
        c = get_common_letter(group)
        p += get_priority(c)

    print(p)


if __name__ == "__main__":
    main()
