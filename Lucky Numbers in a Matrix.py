class Solution:
    # O(m*n) runtime, O(m*n) space
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        min_in_row_mat = Solution._get_minimum_in_row_mat(matrix)
        max_in_col_mat = Solution._get_maximum_in_col_mat(matrix)
        return Solution._get_lucky_numbers(min_in_row_mat, max_in_col_mat, matrix)
    
    
    @staticmethod
    def _get_minimum_in_row_mat(matrix):
        m, n = len(matrix), len(matrix[0])
        is_minimum_in_row_mat = [[0] * n for i in range(m)]
        
        for i in range(m):
            min_j = 0
            for j in range(n):
                if matrix[i][j] < matrix[i][min_j]:
                    min_j = j
            is_minimum_in_row_mat[i][min_j] = 1
        return is_minimum_in_row_mat
    
    
    @staticmethod
    def _get_maximum_in_col_mat(matrix):
        m, n = len(matrix), len(matrix[0])
        is_maximum_in_col_mat = [[0] * n for i in range(m)]
        
        for i in range(n):
            max_j = 0
            for j in range(m):
                if matrix[j][i] > matrix[max_j][i]:
                    max_j = j
            is_maximum_in_col_mat[max_j][i] = 1
        return is_maximum_in_col_mat
    
    
    @staticmethod
    def _get_lucky_numbers(min_in_row_mat, max_in_col_mat, matrix):
        m, n = len(matrix), len(matrix[0])
        lucky_numbers = []
        print(min_in_row_mat)
        print(max_in_col_mat)
        for i in range(m):
            for j in range(n):
                if min_in_row_mat[i][j] and max_in_col_mat[i][j]:
                    lucky_numbers.append(matrix[i][j])
        return lucky_numbers