from numpy import sign

DIRECTION = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}


class Rope:
    def __init__(self, knots):

        # Rope with head at element 0
        self.rope = [[0, 0] for _ in range(knots)]

        self.tail_history = set()
        self.tail_history.add(tuple(self.rope[-1]))

    def move_head(self, dx, dy, distance):
        for _ in range(distance):
            self.rope[0][0] += dx
            self.rope[0][1] += dy

            self.update_tail()

    def update_tail(self):

        # t is the index of the current "tail", t-1 is the head
        for t in range(1, len(self.rope)):
            dx, dy = (
                self.rope[t - 1][0] - self.rope[t][0],
                self.rope[t - 1][1] - self.rope[t][1],
            )

            if abs(dx) > 1 or abs(dy) > 1:
                self.rope[t][0] += 1 * sign(dx)
                self.rope[t][1] += 1 * sign(dy)

        self.tail_history.add(tuple(self.rope[-1]))


def main():
    filename = "input.txt"

    with open(filename) as f:
        data = f.read().splitlines()

    knots = 10
    rope = Rope(knots)

    for move in data:
        dx, dy = DIRECTION[move[0]]
        distance = int(move[1:])

        rope.move_head(dx, dy, distance)

    print(len(rope.tail_history))


if __name__ == "__main__":
    main()
