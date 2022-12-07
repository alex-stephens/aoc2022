class Move:
    def __init__(self, string):
        parts = string.split()

        self.old = int(parts[3])
        self.new = int(parts[5])
        self.num = int(parts[1])

    def __repr__(self):
        return f"{self.num} from {self.old} to {self.new}"


class Stacks:
    def __init__(self, stack_items):
        self.num_stacks = len(stack_items[0])
        self.stacks = dict()

        for i in range(self.num_stacks):
            self.stacks[i + 1] = ""

        for i, items in enumerate(stack_items[::-1]):
            for j, item in enumerate(items):
                if item != " ":
                    self.stacks[j + 1] += item

    def apply_move(self, m, stable_stack=False):
        """Moves a crate from one stack to another.

        If stable_stack is true, the moving crates maintain the same order.
        """
        # Remove m.num items from m.old
        moving_stack = self.stacks[m.old][-m.num :]
        self.stacks[m.old] = self.stacks[m.old][: -m.num]

        # Add items to m.new
        if not stable_stack:
            moving_stack = moving_stack[::-1]
        self.stacks[m.new] += moving_stack

    def get_top_crates(self):
        ans = ""
        for i in range(1, self.num_stacks + 1):
            ans += self.stacks[i][-1]
        return ans

    def draw(self):
        max_height = max([len(s) for s in self.stacks.values()])

        print()
        for h in range(max_height, 0, -1):
            for i in range(1, self.num_stacks + 1):
                if len(self.stacks[i]) >= h:
                    print(f"[{self.stacks[i][h - 1]}]", end=" ")
                else:
                    print("   ", end=" ")
            print()

        for i in range(1, self.num_stacks + 1):
            print(f" {i} ", end=" ")
        print()


def parse_input(filename):
    with open(filename) as f:
        # Crate stacks
        line = f.readline()
        stack_items = []
        while "[" in line:
            stack_items.append(list(line[1::4]))
            line = f.readline()

        stacks = Stacks(stack_items)

        line = f.readline()
        line = f.readline()

        moves = []
        while line != "":
            moves.append(Move(line))
            line = f.readline().strip()

    return stacks, moves


def main():
    filename = "input.txt"
    stacks, moves = parse_input(filename)

    for m in moves:
        stacks.apply_move(m, stable_stack=False)
        # stacks.draw()

    print(stacks.get_top_crates())


if __name__ == "__main__":
    main()
