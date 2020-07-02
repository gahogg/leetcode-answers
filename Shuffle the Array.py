class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        n = len(nums) // 2
        lst = []
        
        for i in range(n):
            lst += [nums[i], nums[i+n]]
        
        return lst