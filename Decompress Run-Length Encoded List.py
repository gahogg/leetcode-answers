class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        lst = []
        
        for i in range(0, len(nums)-1, 2):
            freq = nums[i]
            val = nums[i+1]
            lst += [val] * freq
        
        return lst