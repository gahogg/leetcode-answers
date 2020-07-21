
class Solution:
    # O(m * n) time, O(1) space
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for row in A:
            i = 0
            j = len(A[0]) - 1
            while i <= j:
                if i == j:
                    row[i] = int(not row[i])
                else:
                    temp = row[i]
                    row[i] = int(not row[j])
                    row[j] = int(not temp)
                i += 1
                j -= 1
                    
        return A
                    