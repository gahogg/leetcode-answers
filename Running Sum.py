class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        lst = []
        prev = 0
        
        for num in nums:
            lst.append(num + prev)
            prev = lst[-1]
        
        return lst