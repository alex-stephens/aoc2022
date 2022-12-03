import string


def get_priority(c):
    return string.ascii_letters.index(c) + 1


def get_common_letter(s1, s2):
    return list(set(s1).intersection(s2))[0]


def main():
    filename = "input.txt"
    p = 0

    with open(filename) as f:
        for line in f.readlines():
            line = line.strip()
            L = len(line) // 2

            s1, s2 = line[:L], line[L:]

            c = get_common_letter(s1, s2)
            p += get_priority(c)

    print(p)


if __name__ == "__main__":
    main()
