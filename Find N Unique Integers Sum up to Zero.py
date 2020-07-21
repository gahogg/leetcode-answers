class Solution:
    # O(n) runtime, O(n) space
    def sumZero(self, n):
        mid = n // 2
        if n % 2 == 0:
            return [x for x in range(-mid, mid+1) if x != 0]
        else:
            return [x for x in range(-mid, mid+1)]