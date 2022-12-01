def main():
    filename = "input.txt"

    with open(filename) as f:
        lines = f.readlines()

    current_sum = 0
    elves = []

    for line in lines:
        if line.strip() == "":
            elves.append(current_sum)
            current_sum = 0
            continue
        n = int(line)
        current_sum += n

    print(sum(sorted(elves, reverse=True)[:3]))


if __name__ == "__main__":
    main()
