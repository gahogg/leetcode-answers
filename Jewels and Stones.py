class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        count = 0
        d = {}
        
        for jewel in J:
            d[jewel] = 1
        
        for s in S:
            if s in d:
                count += 1
        
        return count