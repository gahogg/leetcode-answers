class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        count = 0
        
        for s in S:
            if s in J:
                count += 1
        
        return count