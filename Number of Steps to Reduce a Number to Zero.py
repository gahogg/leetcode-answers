class Solution:
    def numberOfSteps (self, num: int) -> int:
        if num == 0:
            return 0
        elif num % 2 == 0:
            num /= 2
        else:
            num -= 1
        return 1 + self.numberOfSteps(num)