class Solution:
    def arrayPairSum(self, nums):
        sorted_nums = sorted(nums)
        return sum(sorted_nums[i] for i in range(len(nums)) if i % 2 == 0)