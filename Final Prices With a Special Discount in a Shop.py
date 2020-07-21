class Solution:
    #O(n) runtime, O(n) space
    def finalPrices(self, prices):
        stk = []
        for i, price in enumerate(prices):
            while stk and prices[stk[-1]] >= price:
                prices[stk.pop()] -= price
            stk.append(i)
        return prices
                
        