def main():
    filename = "input.txt"

    with open(filename) as f:
        lines = f.readlines()

    current_sum, max_sum = 0, 0
    for line in lines:
        if line.strip() == "":
            max_sum = max(max_sum, current_sum)
            current_sum = 0
            continue
        n = int(line)
        current_sum += n

    print(max_sum)


if __name__ == "__main__":
    main()
