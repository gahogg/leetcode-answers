from collections import Counter


class Solution:
    # O(n) time, O(n) space
    def canBeEqual(self, target, arr):
        arr_counter = Counter(arr)
        arr_counter.subtract(Counter(target))
        return all(arr_counter[key] == 0 for key in arr_counter)