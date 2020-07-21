from collections import deque


class Solution:
    #  O(n) runtime, O(n) space
    def diStringMatch(self, S):
        N = len(S)
        deque_0_to_N = deque(list(range(N + 1)))
        sol_so_far = []
        for letter in S:
            if letter == "I":
                sol_so_far.append(deque_0_to_N.popleft())
            else:
                sol_so_far.append(deque_0_to_N.pop())
        sol_so_far.append(deque_0_to_N.pop())
        return sol_so_far