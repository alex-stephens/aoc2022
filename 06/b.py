def all_different(string):
    """Returns true if all characters in a string are different."""
    return len(set(string)) == len(string)


def find_start_of_packet(string, window):
    """Finds the start of a packet in a string.

    The packet is defined as a sequence of 4 characters that are all
    different.
    """
    for i in range(window - 1, len(string)):
        if all_different(string[i - window + 1 : i + 1]):
            return i + 1
    return -1


def main():
    filename = "input.txt"
    window = 14

    with open(filename) as f:
        string = f.read()

    print(find_start_of_packet(string, window))


if __name__ == "__main__":
    main()
