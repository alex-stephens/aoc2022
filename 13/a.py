def compare(a, b):
    """Compares the left string (a) to the right string (b).
    Returns 1 if they are in the right order, 0 if equal, -1
    if wrong.
    """

    # print(f"Comparing {a} to {b}...")

    if isinstance(a, int) and isinstance(b, int):
        if a < b:
            return 1
        if a == b:
            return 0
        return -1

    if isinstance(a, list) and isinstance(b, list):
        i = 0
        while i < len(a) and i < len(b):
            c = compare(a[i], b[i])
            if c != 0:
                return c
            i += 1

        if i == len(a) and i == len(b):
            return 0
        if i == len(a):
            return 1
        return -1

    if isinstance(a, list) and isinstance(b, int):
        return compare(a, [b])
    if isinstance(a, int) and isinstance(b, list):
        return compare([a], b)


def split_except_ints(s):
    """Takes a string as input and returns it as a list,
    where each character is an element except consecutive
    integers which are grouped together.
    """
    out = []
    i = 0
    while i < len(s):
        if s[i].isdigit():
            j = i + 1
            while j < len(s) and s[j].isdigit():
                j += 1
            out.append(int(s[i:j]))
            i = j
        else:
            out.append(s[i])
            i += 1
    return out


def parse(data):
    """Parses a list of integers from a string.
    Returns a list of integers.
    """
    out = []
    working_lists = []
    for v in split_except_ints(data[1:-1]):

        if v == "[":
            working_lists.append([])
        elif isinstance(v, int):
            if len(working_lists) == 0:
                out.append(v)
            else:
                working_lists[-1].append(v)
        elif v == "]":
            completed = working_lists.pop()
            if len(working_lists) == 0:
                out.append(completed)
            else:
                working_lists[-1].append(completed)

    return out


def main():
    filename = "input.txt"

    with open(filename) as f:
        lines = f.readlines()

    index = 1
    result = 0
    for i in range(0, len(lines), 3):
        l1 = parse(lines[i].strip())
        l2 = parse(lines[i + 1].strip())

        if compare(l1, l2) == 1:
            result += index

        index += 1

    print(result)


if __name__ == "__main__":
    main()
