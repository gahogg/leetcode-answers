class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        cur_max = -1
        i = len(arr) - 1

        while i >= 0:
            elem = arr[i]
            arr[i] = cur_max

            if elem > cur_max:
                cur_max = elem

            i -= 1

        return arr
