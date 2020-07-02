from functools import reduce

class Solution:
    def findNumbers(self, nums):
        return sum(len(str(x)) % 2 == 0 for x in nums)