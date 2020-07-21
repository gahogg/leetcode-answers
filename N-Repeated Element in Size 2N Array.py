from collections import Counter


class Solution:
    # O(n) runtime, O(n) space
    def repeatedNTimes(self, A: List[int]) -> int:
        return Counter(A).most_common()[0][0]