class Solution:
    def balancedStringSplit(self, s: str) -> int:
        stk = []
        count = 0
        
        for letter in s:
            if not stk:
                stk.insert(0, letter)
            elif stk[0] == letter:
                stk.insert(0, letter)
            else:
                stk.pop()
                if not stk:
                    count += 1
        
        return count