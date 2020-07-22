from collections import Counter


class Solution:
    # O(n) runtime, O(n) space
    def uniqueOccurrences(self, arr):
        num_occurences = Counter(arr)
        unique_occurences = Counter()
        for key in num_occurences:
            unique_occurences[num_occurences[key]] += 1
            if unique_occurences[num_occurences[key]] > 1:
                return False
        return True