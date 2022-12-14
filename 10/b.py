class Instruction:
    def __init__(self, string):
        data = string.split(" ")

        self.op = data[0]
        self.arg = None
        self.duration = None

        if len(data) > 1:
            self.arg = int(data[1])

        if self.op == "addx":
            self.duration = 2
        elif self.op == "noop":
            self.duration = 1

    def __repr__(self):
        return f"Instruction(op={self.op}, arg={self.arg}, duration={self.duration})"


class CRT:
    def __init__(self, width, positions):
        self.width = width
        self.positions = positions

    def draw(self):
        for i, p in enumerate(self.positions[1:]):
            horizontal_pos = i % self.width

            if abs(horizontal_pos - p) <= 1:
                print("#", end="")
            else:
                print(".", end="")

            if (i + 1) % self.width == 0:
                print()


class Circuit:
    def __init__(self, initial_value=1, key_cycles=[]):
        self.x = initial_value
        self.cycle = 1
        self.instructions = {}  # map cycles to list of instructions

        self.key_cycles = key_cycles
        self.score = 0

        # Track the value at each cycle (starting from 1 - dummy value at 0)
        self.x_history = [0]

    def apply_instruction(self, instr):
        if instr.op == "addx":
            self.x += instr.arg
        elif instr.op == "noop":
            pass

    def run_instruction(self, instr):
        remaining_cycles = instr.duration

        for _ in range(remaining_cycles):
            self.run_cycle()

        # Run the instruction
        self.apply_instruction(instr)

    def run_cycle(self):

        # Add to score
        if self.cycle in self.key_cycles:
            self.score += self.x * self.cycle

        self.x_history.append(self.x)
        self.cycle += 1


def main():
    filename = "input.txt"
    key_cycles = [20, 60, 100, 140, 180, 220]

    instructions = []
    with open(filename) as f:
        for line in f:
            instructions.append(Instruction(line.strip()))

    circuit = Circuit(initial_value=1, key_cycles=key_cycles)

    for inst in instructions:
        circuit.run_instruction(inst)

    crt = CRT(40, circuit.x_history)
    crt.draw()


if __name__ == "__main__":
    main()
