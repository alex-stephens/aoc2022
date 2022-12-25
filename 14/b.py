class Simulation:
    def __init__(self, data):

        self.occ = {}
        self.lim = [1000, -1000, 1000, -1000]  # xmin, xmax, ymin, ymax

        self.sand = 0

        self.source = (500, 0)
        self.update_limits(self.source)

        self.parse_data(data)
        self.add_floor()

    def parse_data(self, data):
        """Populate the occupancy map with the given data."""

        for line in data:
            points = [tuple(map(int, p.split(","))) for p in line.split(" -> ")]

            for i in range(len(points) - 1):
                self.add_line(points[i], points[i + 1])

    def add_line(self, p1, p2):
        delta = [p2[0] - p1[0], p2[1] - p1[1]]
        length = 0
        for i in range(len(delta)):
            if delta[i] == 0:
                continue
            length = abs(delta[i])
            delta[i] = delta[i] // abs(delta[i])

        for inc in range(length + 1):
            p = (p1[0] + inc * delta[0], p1[1] + inc * delta[1])
            self.occ[tuple(p)] = "#"

            # Update the limits xmin, xmax, ymin, ymax
            self.update_limits(p)

    def add_floor(self):
        floor_height = self.lim[3] + 2

        dist_from_centre = abs(self.source[1] - floor_height)

        for x in range(
            self.source[0] - dist_from_centre, self.source[0] + dist_from_centre + 1
        ):
            self.occ[(x, floor_height)] = "#"
            self.update_limits((x, floor_height))

    def update_limits(self, p):
        for i in range(2):
            self.lim[2 * i] = min(self.lim[2 * i], p[i])
            self.lim[2 * i + 1] = max(self.lim[2 * i + 1], p[i])

    def draw(self):
        for y in range(self.lim[3] + 1):
            print(f"{y:3d} ", end="")
            for x in range(self.lim[0], self.lim[1] + 1):
                if (x, y) == self.source:
                    print("+", end="")
                elif (x, y) in self.occ:
                    print(self.occ[(x, y)], end="")
                else:
                    print(".", end="")

            print()
        print()

    def drop_sand(self, source=None):
        """Drop sand from the given source. If no source is given, use the
        default source.
        """
        if source:
            loc = source
        else:
            loc = self.source

        delta = [(0, 1), (-1, 1), (1, 1)]

        while True:
            at_rest = True
            for d in delta:
                nxt_option = (loc[0] + d[0], loc[1] + d[1])
                if nxt_option not in self.occ:
                    at_rest = False
                    break

            if at_rest:
                break

            loc = nxt_option

            # Falling forever
            if loc[1] > self.lim[3]:
                return False, None

            # self.draw()

        self.occ[loc] = "o"

        return True, loc

    def fill(self):

        full = False
        while not full:
            at_rest, loc = self.drop_sand()
            if not at_rest:
                break
            self.sand += 1
            if loc == self.source:
                break


def main():
    filename = "input.txt"
    data = []

    with open(filename) as f:
        for line in f:
            data.append(line.strip())

    sim = Simulation(data)
    sim.fill()
    sim.draw()

    print(sim.sand)


if __name__ == "__main__":
    main()
