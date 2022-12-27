from parse import parse


class Sensor:
    def __init__(self, x, y, nearest_beacon):
        self.x = x
        self.y = y
        self.nearest_beacon = nearest_beacon

        self.range = abs(x - nearest_beacon.x) + abs(y - nearest_beacon.y)

    def is_covering_location(self, x, y):
        return abs(x - self.x) + abs(y - self.y) <= self.range

    def __repr__(self):
        return f"Sensor at ({self.x}, {self.y}), nearest beacon {self.nearest_beacon}"


class Beacon:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Beacon({self.x}, {self.y})"


class Grid:
    def __init__(self, data):

        self.sensors = []
        self.beacons = []

        self.parse_data(data)

    def add_sensor(self, sensor):
        self.sensors.append(sensor)

    def add_beacon(self, beacon):
        self.beacons.append(beacon)

    def parse_data(self, data):

        for line in data:
            values = parse(
                "Sensor at x={0}, y={1}: closest beacon is at x={2}, y={3}", line
            )
            values = list(map(int, values))
            sx, sy, bx, by = values

            beacon = Beacon(bx, by)
            sensor = Sensor(sx, sy, beacon)

            self.add_beacon(beacon)
            self.add_sensor(sensor)

    def has_beacon(self, x, y):
        for beacon in self.beacons:
            if beacon.x == x and beacon.y == y:
                return True
        return False

    def check_row_coverage(self, y):
        covered = 0

        max_range = max([sensor.range for sensor in self.sensors])
        xmin = min([sensor.x for sensor in self.sensors]) - max_range
        xmax = max([sensor.x for sensor in self.sensors]) + max_range

        for x in range(xmin, xmax + 1):
            if self.has_beacon(x, y):
                continue
            for sensor in self.sensors:
                if sensor.is_covering_location(x, y):
                    covered += 1
                    break

        return covered


def main():
    filename = "input.txt"
    data = []

    target_row = 2000000

    with open(filename) as f:
        for line in f:
            data.append(line.strip())

    grid = Grid(data)

    print(grid.check_row_coverage(target_row))


if __name__ == "__main__":
    main()
