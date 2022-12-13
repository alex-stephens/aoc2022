from numpy import sign

DIRECTION = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}


class Rope:
    def __init__(self):

        self.head = [0, 0]
        self.tail = [0, 0]

        self.tail_history = set()
        self.tail_history.add(tuple(self.tail))

    def move_head(self, dx, dy, distance):
        for _ in range(distance):
            self.head[0] += dx
            self.head[1] += dy

            self.update_tail()

    def update_tail(self):
        head_dx, head_dy = self.head[0] - self.tail[0], self.head[1] - self.tail[1]
        if abs(head_dx) > 1 or abs(head_dy) > 1:
            self.tail[0] += 1 * sign(head_dx)
            self.tail[1] += 1 * sign(head_dy)

        self.tail_history.add(tuple(self.tail))


def main():
    filename = "input.txt"

    with open(filename) as f:
        data = f.read().splitlines()

    rope = Rope()

    for move in data:
        dx, dy = DIRECTION[move[0]]
        distance = int(move[1:])

        rope.move_head(dx, dy, distance)

    print(len(rope.tail_history))


if __name__ == "__main__":
    main()
