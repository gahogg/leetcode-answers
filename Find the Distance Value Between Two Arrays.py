class Solution:
# O(n*m) time, O(1) space
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        num_bad_elems = 0
        for num1 in arr1:
            for num2 in arr2:
                if abs(num1 - num2) <= d:
                    num_bad_elems += 1
                    break
        return len(arr1) - num_bad_elems