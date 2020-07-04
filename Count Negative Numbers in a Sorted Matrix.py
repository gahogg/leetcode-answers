class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        negative_count = 0

        for i, row in enumerate(grid):
            if row[0] < 0:
                negative_count += (m - i) * n
                break
            else:
                for j, cell in enumerate(row):
                    if cell < 0:
                        negative_count += (n - j)
                        break

        return negative_count
