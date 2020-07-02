from functools import reduce

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s = str(n)
        if len(s) == 1:
            return 0
        product = reduce(lambda x, y: int(x) * int(y), s)
        summ = reduce(lambda x, y: int(x) + int(y), s)
        return product - summ