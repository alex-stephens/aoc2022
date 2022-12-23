class HeightMap:
    def __init__(self, lines):
        self.width = len(lines[0].strip())
        self.height = len(lines)

        self.start = None
        self.end = None
        self.grid = self.parse_input(lines)

    def parse_input(self, lines):
        grid = [[-1 for _ in range(self.width)] for _ in range(self.height)]

        for i, line in enumerate(lines):
            for j, c in enumerate(line.strip()):
                if c == "S":
                    height = 1
                    self.start = (i, j)
                elif c == "E":
                    height = 26
                    self.end = (i, j)
                else:
                    height = ord(c) - ord("a") + 1
                grid[i][j] = height
        return grid

    def draw(self):
        for row in self.grid:
            for n in row:
                print(f"{n:-2d}", end=" ")
            print()

    def bfs(self):
        """Run a BFS from the start node to the end node.

        Return the path from the start node to the end node.
        """
        queue = [self.start]
        visited = set()
        parent = {}

        it = 0
        while len(queue) > 0:
            it += 1
            node = queue.pop(0)
            if node in visited:
                continue
            if node == self.end:
                break
            visited.add(node)

            for neighbor in self.get_neighbors(node):
                if neighbor in visited:
                    continue
                parent[neighbor] = node
                queue.append(neighbor)

        path = []
        node = self.end
        while node != self.start:
            path.append(node)
            node = parent[node]
        path.append(self.start)
        path.reverse()
        return path

    def get_neighbors(self, node):
        """Get the neighbors of a node."""
        neighbors = []
        for direction in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            dx, dy = direction

            x, y = node
            x += dx
            y += dy

            # out of range
            if x < 0 or x >= self.height or y < 0 or y >= self.width:
                continue

            # height increase too large
            if self.grid[x][y] - self.grid[node[0]][node[1]] > 1:
                continue

            neighbors.append((x, y))
        return neighbors


def main():
    filename = "input.txt"

    with open(filename) as f:
        lines = f.readlines()

    hmap = HeightMap(lines)
    # hmap.draw()

    path = hmap.bfs()
    steps = len(path) - 1

    print(steps)


if __name__ == "__main__":
    main()
