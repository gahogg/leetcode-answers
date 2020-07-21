class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        mx = 0
        
        for num_candies in candies:
            mx = num_candies if num_candies > mx else mx
        
        lst = []
        
        for num_candies in candies:
            lst.append(num_candies + extraCandies >= mx)
        
        return lst