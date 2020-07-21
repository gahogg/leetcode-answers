class Solution:
    # O(n) runtime, O(n) space
    def generateTheString(self, n):
        return "".join(['a' for i in range(n-1)] + ['b']) if n % 2 == 0 else "".join(['a' for i in range(n)])