from collections import deque


class Solution:
    # O(n) runtime, O(n) space
    def sortArrayByParity(self, A):
        deq_parity_sorted = deque()
        for val in A:
            if val % 2 == 0:
                deq_parity_sorted.appendleft(val)
            else:
                deq_parity_sorted.append(val)
        return list(deq_parity_sorted)