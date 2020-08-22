class Solution:
# O(n) time, O(1) space
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        arr_len = len(arr)
        consec_odds = 0
        for i in range(arr_len):
            is_odd = (arr[i] % 2) == 1
    
            if is_odd:
                consec_odds += 1
            else:
                consec_odds = 0
                
            if consec_odds == 3:
                return True
            
        return False