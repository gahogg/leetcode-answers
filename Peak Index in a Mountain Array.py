class Solution:
    #O(n) runtime, O(1) space
    def peakIndexInMountainArray(self, A):
        max_i = 0
        for i in range(len(A)):
            if A[i] > A[max_i]:
                max_i = i
        return max_i