from math import prod


class Grid:
    def __init__(self, grid):
        self.grid = grid

        self.rows = len(grid)
        self.cols = len(grid[0])

    def check_visible(self, i, j):
        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        h = self.grid[i][j]

        for d in dirs:
            x = i + d[0]
            y = j + d[1]
            visible = True

            while 0 <= x < self.rows and 0 <= y < self.cols:
                if self.grid[x][y] >= h:
                    visible = False
                    break

                x += d[0]
                y += d[1]

            if visible:
                return True
        return False

    def count_visible(self):
        count = 0
        for i in range(self.rows):
            for j in range(self.cols):
                if self.check_visible(i, j):
                    count += 1
        return count

    def get_scenic_score(self, i, j):
        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        h = self.grid[i][j]
        scores = [0] * 4

        for k, d in enumerate(dirs):
            x = i + d[0]
            y = j + d[1]

            while 0 <= x < self.rows and 0 <= y < self.cols:
                scores[k] += 1
                if self.grid[x][y] >= h:
                    break

                x += d[0]
                y += d[1]

        return prod(scores)

    def get_max_scenic_score(self):
        max_score = 0
        for i in range(self.rows):
            for j in range(self.cols):
                score = self.get_scenic_score(i, j)
                max_score = max(score, max_score)
        return max_score


def main():
    filename = "input.txt"

    data = []
    with open(filename) as f:
        for line in f:
            data.append(list(map(int, list(line.strip()))))

    grid = Grid(data)
    print(grid.get_max_scenic_score())


if __name__ == "__main__":
    main()
