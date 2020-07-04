class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        mat = [[0] * m for i in range(n)]

        for (r, c) in indices:
            mat[r] = list(map(lambda x: x + 1, mat[r]))

            for row in mat:
                row[c] += 1

        odd_count = 0

        for row in mat:
            odd_count += sum(cell % 2 == 1 for cell in row)

        return odd_count
