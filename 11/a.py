import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO) # change to DEBUG for more info
logging.basicConfig(style="{", format="[{levelname}]: {message}")


class Game:
    def __init__(self, monkeys, rounds):

        self.rounds = rounds
        self.monkeys = monkeys
        self.current_round = 1

    def play_round(self):
        """Play one round of the game."""

        for monkey in self.monkeys:
            throws = {}  # map items onto targets
            logger.debug(f"Monkey {monkey.num}")
            for i in range(len(monkey.items)):

                val = monkey.inspect(i)

                if val % monkey.test.factor == 0:
                    self.monkeys[monkey.test.target_true].add_item(val)
                    logger.debug(
                        f"    Current worry level is divisible by {monkey.test.factor}"
                    )
                    logger.debug(
                        f"    Item with worry level {val} is thrown to  monkey {monkey.test.target_true}"
                    )
                else:
                    logger.debug(
                        f"    Current worry level is not divisible by {monkey.test.factor}"
                    )
                    logger.debug(
                        f"    Item with worry level {val} is thrown to  monkey {monkey.test.target_false}"
                    )
                    self.monkeys[monkey.test.target_false].add_item(val)

            monkey.items = []

        logger.debug(
            f"After round {self.current_round}, the monkeys are holding items with these worry levels:"
        )
        for m in self.monkeys:
            logger.debug(f"  {m}")
        self.current_round += 1

    def compute_monkey_business(self):

        scores = sorted([m.inspections for m in self.monkeys], reverse=True)
        return scores[0] * scores[1]

    def execute(self):
        """Play the game for the given number of rounds."""
        for _ in range(self.rounds):
            self.play_round()


class Test:
    def __init__(self, factor, target_true, target_false):
        self.factor = factor
        self.target_true = target_true
        self.target_false = target_false


class Monkey:
    def __init__(self, num, items, operation, test):
        self.num = num
        self.items = items
        self.operation = operation
        self.test = test
        self.inspections = 0

    def __repr__(self):
        return f"Monkey {self.num}: {*self.items,}"

    def add_item(self, item):
        self.items.append(item)

    def inspect(self, index):

        old = self.items[index]
        logger.debug(f"  Monkey inspects an item with a worry level of {old}")
        new = eval(self.operation)
        logger.debug(f"    Worry level updates to {new}")

        new //= 3
        logger.debug(
            f"    Monkey gets bored with this item. Worry level is divided by 3 to {new}"
        )

        self.inspections += 1
        return new


def parse_block(lines):
    """Parse a block of input lines and return a Monkey object."""
    num = int(lines[0].strip(":\n").split(" ")[-1])

    tmp = lines[1].split(": ")[1]
    starting_items = list(map(int, tmp.split(", ")))

    op = lines[2].strip().split(": ")[1][6:]
    factor = int(lines[3].split(" ")[-1])

    target_true = int(lines[4].split(" ")[-1])
    target_false = int(lines[5].split(" ")[-1])

    test = Test(factor, target_true, target_false)
    monkey = Monkey(num, starting_items, op, test)

    return monkey


def parse_input(lines):
    """Parse input lines and return a list of Monkeys."""
    LINES_PER_MONKEY = 7
    monkeys = []
    num_monkeys = (len(lines) + 1) // LINES_PER_MONKEY

    for i in range(0, num_monkeys):
        monkey = parse_block(lines[i * LINES_PER_MONKEY : (i + 1) * LINES_PER_MONKEY])
        monkeys.append(monkey)

    return monkeys


def main():
    filename = "input.txt"

    with open(filename) as f:
        lines = f.readlines()

    monkeys = parse_input(lines)
    rounds = 20

    game = Game(monkeys, rounds)
    game.execute()

    print(game.compute_monkey_business())


if __name__ == "__main__":
    main()
