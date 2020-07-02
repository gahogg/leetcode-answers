class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = [start + i*2 for i in range(n)]
        val = nums.pop(0)
        while(nums):
            val = val ^ nums.pop(0)
        return val