class Solution:
    # O(m*n) runtime, O(n) space
    def relativeSortArray(self, arr1, arr2):
        swap_pos = 0
        for arr2_elem in arr2:
            for i in range(swap_pos, len(arr1)):
                if arr1[i] == arr2_elem:
                    temp = arr1[swap_pos]
                    arr1[swap_pos] = arr1[i]
                    arr1[i] = temp
                    swap_pos += 1
        next_sorted_list = sorted(arr1[swap_pos:])
        for i in range(swap_pos, len(arr1)):
            arr1[i] = next_sorted_list[i-swap_pos]
        return arr1