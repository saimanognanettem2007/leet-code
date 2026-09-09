class Solution:
    def minimumOperations(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        operations = 0

        for j in range(cols):
            for i in range(1, rows):
                if grid[i][j] <= grid[i - 1][j]:
                    new_value = grid[i - 1][j] + 1
                    operations += new_value - grid[i][j]
                    grid[i][j] = new_value

        return operations
