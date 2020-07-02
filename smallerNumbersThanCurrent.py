class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        s = sorted(nums, reverse = True)
        n = len(s)
        m = {}
        prev_elem = s[0]
        
        for i in range(1, len(s)):
            if s[i] != prev_elem:
                m[prev_elem] = n - i
            prev_elem = s[i]
        
        m[s[-1]] = 0
        
        return [m[num] for num in nums]
